#!/usr/bin/env python3
"""Scan prose for the machine-checkable AI-writing patterns of the skill.

Findings come in two severities. A `fix` finding is a mechanical pattern
the skill always removes: banned words (pattern 8), misused dashes (15),
bold-label lists (17), title case headings (18), emoji in headings and
list items (19), mixed quote styles (20), and stacked hyphenated pairs
or hyphenated English jargon (28). A `watch` finding is a phrase or shape
that is often, but not always, slop: binary contrasts (10), emoji in body
text (19), watched phrases from the catalog (patterns 5, 21, 22, 25, 27,
29, 30, 35, 36, 37, and 41), and horizontal rules (40). The model confirms
or dismisses each `watch` finding by reading the context.

The same file ships in Humanize AI Slop (English) and Humanize BR
(Brazilian Portuguese). It picks the language from SKILL.md and parses its
word lists from SKILL.md and references/patterns.md, so it never drifts
from the skill.

Code, YAML metadata, link targets, and URLs are never scanned. Text inside
quotation marks is skipped by the word checks, because the skill does not
rewrite watched phrases that are quoted rather than used. A line-initial
em dash marks dialogue and is never flagged.

Usage:
  python3 scripts/slop_scan.py FILE           scan a file
  python3 scripts/slop_scan.py -              scan stdin
  python3 scripts/slop_scan.py FILE --json    print findings as JSON
  python3 scripts/slop_scan.py FILE --strict  exit 1 on any fix finding

The exit status is 0 even with findings, unless --strict is given, so an
agent can read the report without treating it as a command failure.
"""
from __future__ import annotations

import argparse
import itertools
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")
CATALOG = (ROOT / "references" / "patterns.md").read_text(encoding="utf-8")

LANG = "pt" if "Banidas de cara:" in SKILL else "en"

CONFIG = {
    "en": {
        "banned_anchor": "Banned outright:",
        "filler_anchor": "Often-empty phrases:",
        "watch_label": r"(?:Phrases|Words) to watch",
        "hyphen_stack": True,
        "anglicisms": False,
        "contrast": re.compile(
            r"\b(?:is not|isn't|are not|aren't|was not|wasn't)\s"
            r"[^.;:!?\n]{1,60}?[,;.]\s+(?:it's|it is|they're|they are|this is)\b"
            r"|\bnot (?:just|only|merely)\s[^.;:!?\n]{1,60}?[,;.]?\s+but\b"
            r"|(?:^|[.!?]\s+)Not [^.!?\n]{1,40}\.\s+Not ",
            re.IGNORECASE,
        ),
    },
    "pt": {
        "banned_anchor": "Banidas de cara:",
        "filler_anchor": "Frases costumeiramente vazias:",
        "watch_label": r"(?:Frases|Palavras) vigiadas",
        "hyphen_stack": False,
        "anglicisms": True,
        "contrast": re.compile(
            r"\bnão (?:é|são|foi|era|está)\s[^.;:!?\n]{1,60}?[,;.]\s+(?:é|são|foi|era)\b"
            r"|\bnão (?:só|apenas|somente)\s[^.;:!?\n]{1,60}?[,;.]?\s+mas\b"
            r"|(?:^|[.!?]\s+)Não [^.!?\n]{1,40}\.\s+Não ",
            re.IGNORECASE,
        ),
    },
}[LANG]

# Catalog patterns whose watch lists the scanner matches as `watch`.
WATCH_PATTERNS = (5, 21, 22, 27, 29, 30, 35, 36, 37, 41)

# Words that do not count toward the title-case heuristic.
STOPWORDS = {
    "a", "an", "the", "and", "or", "of", "to", "in", "for", "on", "with",
    "at", "by", "from", "as", "is", "are", "was", "be", "it", "its", "not",
    "but", "vs", "into", "that", "this",
    "de", "da", "do", "das", "dos", "e", "o", "os", "em", "no", "na",
    "nos", "nas", "para", "por", "com", "um", "uma", "que", "ao", "aos",
}

EM_DASH = "\u2014"
EN_DASH = "\u2013"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
LIST_ITEM_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
BOLD_ITEM_RE = re.compile(r"^\s*[-*+]\s+\*\*([^*\n]+)\*\*")
DECORATION_RE = re.compile(
    "[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F\u2190-\u21FF\u25A0-\u25FF]"
)
TABLE_RULE_RE = re.compile(r"^\s*\|[\s:|-]+\|?\s*$")
HORIZONTAL_RULE_RE = re.compile(r"^ {0,3}(?:(?:-[ \t]*){3,}|(?:\*[ \t]*){3,}|(?:_[ \t]*){3,})$")
DOUBLE_HYPHEN_RE = re.compile(r"(?<!-)--(?!-)")
# Letters only, three or more on each side: skips e-mail, GPT-4, and dates.
HYPHEN_PAIR_RE = re.compile(r"(?<![\w-])[^\W\d_]{3,}-[^\W\d_]{3,}(?![\w-])")
QUOTED_RE = re.compile(r'"[^"\n]{1,200}"|\u201C[^\u201D\n]{1,200}\u201D|\u00AB[^\u00BB\n]{1,200}\u00BB')


@dataclass
class Finding:
    line: int
    pattern: int
    severity: str
    kind: str
    detail: str


def blank(match: re.Match[str]) -> str:
    """Replace a match with spaces, keeping newlines so line numbers survive."""
    return re.sub(r"[^\n]", " ", match.group(0))


def mask_unscanned(text: str) -> str:
    """Blank out metadata, code, link targets, and URLs."""
    text = re.sub(r"\A---\n.*?\n---\n", blank, text, flags=re.DOTALL)
    text = re.sub(r"```.*?```", blank, text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]*`", blank, text)
    text = re.sub(r"\]\([^)\s]*(?:\s+\"[^\"]*\")?\)", lambda m: "]" + blank(m)[1:], text)
    text = re.sub(r"<https?://[^>\s]+>|https?://\S+", blank, text)
    return text


def mask_quotes(line: str) -> str:
    return QUOTED_RE.sub(blank, line.replace("\u2019", "'"))


def split_list(body: str) -> list[str]:
    body = re.sub(r"\([^)]*\)", "", body)
    for mark in ('"', "\u201C", "\u201D"):
        body = body.replace(mark, "")
    words = []
    for item in body.split(","):
        for word in item.split("/") if " " not in item.strip() else [item]:
            word = word.strip(" .")
            if word:
                words.append(word)
    return words


def anchored_list(anchor: str) -> list[str]:
    for line in SKILL.splitlines():
        if line.startswith(anchor):
            return split_list(line[len(anchor):])
    raise SystemExit(f"Could not find the list {anchor!r} in SKILL.md")


def pattern_section(number: int) -> str:
    match = re.search(rf"(?s)^### {number}\..*?(?=^### |\Z)", CATALOG, re.MULTILINE)
    if match is None:
        raise SystemExit(f"Could not find pattern {number} in references/patterns.md")
    return match.group(0)


def watch_line(number: int) -> str:
    match = re.search(rf"\*\*{CONFIG['watch_label']}:\*\*(.*)", pattern_section(number))
    return match.group(1) if match else ""


def watch_phrases(number: int) -> list[str]:
    """Literal phrases from a pattern's watch list, slash alternatives expanded.

    Entries with placeholders ([date], X, Y) and single words are skipped:
    a lone "Look" or "overall" is too common to report.
    """
    phrases = []
    raw = re.sub(r"\([^)]*\)", "", watch_line(number))
    for entry in raw.split(","):
        entry = entry.replace("...", " ").replace("\u2026", " ")
        entry = entry.strip(" .?!:\"\u201C\u201D")
        if not entry or "[" in entry or re.search(r"\b[XYZ]\b", entry):
            continue
        tokens = entry.split()
        if not 2 <= len(tokens) <= 6:
            continue
        options = [token.strip("?!:").split("/") for token in tokens]
        for combo in itertools.product(*options):
            phrases.append(" ".join(combo).replace("\u2019", "'"))
    return phrases


def inflections(word: str) -> set[str]:
    out = {word}
    if LANG == "en":
        out |= {word + "s", word + "es", word + "d", word + "ed", word + "ing"}
        if word.endswith("y"):
            out |= {word[:-1] + "ies", word[:-1] + "ied"}
        if word.endswith("e"):
            out |= {word[:-1] + "ing"}
        return out
    if len(word) > 4 and word[-2:] in ("ar", "er", "ir"):
        stem, vowel = word[:-2], word[-2]
        if vowel == "a":
            endings = ("a", "am", "ou", "aram", "ando", "ado", "ada", "ados", "adas", "ará", "arão", "amos")
        else:
            participle = "ido"
            endings = ("e", "em", "eu" if vowel == "e" else "iu", vowel + "ram",
                       vowel + "ndo", participle, "ida", "idos", "idas")
        out |= {stem + ending for ending in endings}
    elif word.endswith("o"):
        out |= {word[:-1] + "a", word + "s", word[:-1] + "as"}
    elif word.endswith("or"):
        out |= {word + "a", word + "es", word + "as"}
    elif word.endswith("l"):
        out |= {word[:-1] + "is"}
    elif word[-1:] in ("a", "e"):
        out |= {word + "s"}
    return out


def term_pattern(term: str, inflect: bool) -> str:
    parts = term.split()
    # English inflects the head noun at the end; Portuguese, the verb or noun at the start.
    index = -1 if LANG == "en" else 0
    heads = inflections(parts[index]) if inflect else {parts[index]}
    forms = []
    for head in sorted(heads, key=len, reverse=True):
        words = list(parts)
        words[index] = head
        forms.append(r"\s+".join(re.escape(word) for word in words))
    return r"(?<!\w)(?:" + "|".join(forms) + r")(?!\w)"


def compile_terms(terms: list[str], inflect: bool) -> re.Pattern[str] | None:
    if not terms:
        return None
    return re.compile("|".join(term_pattern(t, inflect) for t in terms), re.IGNORECASE)


BANNED_RE = compile_terms(anchored_list(CONFIG["banned_anchor"]), inflect=True)
ANGLICISM_RE = (
    compile_terms(split_list(watch_line(28)), inflect=False) if CONFIG["anglicisms"] else None
)
WATCH_RES = [(25, compile_terms(anchored_list(CONFIG["filler_anchor"]), inflect=False))]
WATCH_RES += [(n, compile_terms(watch_phrases(n), inflect=False)) for n in WATCH_PATTERNS]


def is_title_case(title: str) -> bool:
    """True when nearly every content word in the heading is capitalized."""
    words = re.findall(r"[\w'\u00C0-\u024F]+", title)
    content = [
        w
        for i, w in enumerate(words)
        if i > 0 and len(w) >= 3 and w.lower() not in STOPWORDS and not w.isupper()
    ]
    if len(content) < 3:
        return False
    return all(w[0].isupper() for w in content)


def scan_text(text: str) -> list[Finding]:
    lines = mask_unscanned(text).splitlines()
    findings: list[Finding] = []

    def add(line: int, pattern: int, severity: str, kind: str, detail: str) -> None:
        findings.append(Finding(line, pattern, severity, kind, detail))

    straight_lines = [i for i, line in enumerate(lines, 1) if '"' in line]
    curly_lines = [i for i, line in enumerate(lines, 1) if "\u201C" in line or "\u201D" in line]

    for lineno, line in enumerate(lines, 1):
        words = mask_quotes(line)

        for match in BANNED_RE.finditer(words):
            add(lineno, 8, "fix", "banned", f'"{match.group(0)}"')
        if ANGLICISM_RE:
            for match in ANGLICISM_RE.finditer(words):
                add(lineno, 28, "fix", "anglicism", f'"{match.group(0)}" (use um equivalente natural se houver)')

        if not line.lstrip().startswith(EM_DASH):
            for char, name in ((EM_DASH, "em dash"), (EN_DASH, "en dash")):
                if char in line:
                    add(lineno, 15, "fix", "dash", f"{name} x{line.count(char)}")
            if DOUBLE_HYPHEN_RE.search(line) and not TABLE_RULE_RE.match(line):
                add(lineno, 15, "fix", "dash", "double hyphen used as a dash")

        bold_item = BOLD_ITEM_RE.match(line)
        if bold_item:
            label = bold_item.group(1)
            rest = line[bold_item.end():]
            if label.endswith(":") or rest.lstrip().startswith(":"):
                add(lineno, 17, "fix", "bold_label", f'"{label.strip(":").strip()}"')

        heading = HEADING_RE.match(line)
        if heading:
            title = heading.group(2)
            if DECORATION_RE.search(title):
                add(lineno, 19, "fix", "decoration", "emoji or symbol in a heading")
            if is_title_case(title):
                add(lineno, 18, "fix", "title_case", f'"{title}"')
        elif LIST_ITEM_RE.match(line) and DECORATION_RE.search(line):
            add(lineno, 19, "fix", "decoration", "emoji or symbol in a list item")
        elif DECORATION_RE.search(line):
            add(lineno, 19, "watch", "emoji", "emoji or symbol in body text")

        if HORIZONTAL_RULE_RE.match(line):
            add(lineno, 40, "watch", "rule", "horizontal rule between sections")

        if CONFIG["hyphen_stack"]:
            for sentence in re.split(r"(?<=[.!?])\s+", words):
                pairs = HYPHEN_PAIR_RE.findall(sentence)
                if len(pairs) >= 3:
                    add(lineno, 28, "fix", "hyphen_stack", " ".join(pairs))

        for match in CONFIG["contrast"].finditer(words):
            add(lineno, 10, "watch", "contrast", f'"{match.group(0).strip(" .!?")}"')

        for pattern, regex in WATCH_RES:
            if regex:
                for match in regex.finditer(words):
                    add(lineno, pattern, "watch", "phrase", f'"{match.group(0)}"')

    if straight_lines and curly_lines:
        minority = min(straight_lines, curly_lines, key=len)
        add(
            minority[0],
            20,
            "fix",
            "mixed_quotes",
            f"straight quotes on {len(straight_lines)} line(s), curly on "
            f"{len(curly_lines)}; first minority quote here",
        )

    findings.sort(key=lambda f: (f.line, f.pattern))
    return findings


def fixes(findings: list[Finding]) -> list[Finding]:
    return [f for f in findings if f.severity == "fix"]


def format_findings(findings: list[Finding]) -> str:
    return "\n".join(
        f"line {f.line}: [pattern {f.pattern}] {f.severity} {f.kind}: {f.detail}"
        for f in findings
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan prose for the machine-checkable AI-writing patterns."
    )
    parser.add_argument("path", help="file to scan, or - for stdin")
    parser.add_argument("--json", action="store_true", help="print findings as JSON")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit 1 when fix findings exist (for clean-text CI checks)",
    )
    args = parser.parse_args()

    if args.path == "-":
        text = sys.stdin.read()
    else:
        text = Path(args.path).read_text(encoding="utf-8")

    findings = scan_text(text)
    fix_count = len(fixes(findings))
    if args.json:
        print(json.dumps([asdict(f) for f in findings], ensure_ascii=False, indent=2))
    elif findings:
        print(format_findings(findings))
        print(f"{fix_count} fix, {len(findings) - fix_count} watch")
    else:
        print("no findings")
    return 1 if args.strict and fix_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
