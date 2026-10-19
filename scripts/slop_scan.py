#!/usr/bin/env python3
"""Scan prose for the mechanical AI-writing patterns defined in SKILL.md.

The scanner covers only the checks a machine can make without judgment:
banned words (pattern 8), misused dashes (15), bold-label lists (17),
English-style title case headings (18), decorated headings (19), mixed
quote styles (20), and unnecessary hyphenated English jargon (28). The
rhetorical patterns stay with the model. The word lists are parsed from
SKILL.md so they never drift from the skill.

Dialogue dashes at the start of a line ("— Não vou, disse ela.") are a
legitimate Portuguese convention and are never flagged.

Usage:
  python3 scripts/slop_scan.py FILE           scan a file
  python3 scripts/slop_scan.py -              scan stdin
  python3 scripts/slop_scan.py FILE --strict  exit 1 on any finding

The exit status is 0 even with findings, unless --strict is given, so an
agent can read the report without treating it as a command failure.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Words that do not count toward the title-case heuristic.
STOPWORDS = {
    "a", "an", "the", "and", "or", "of", "to", "in", "for", "on", "with",
    "at", "by", "from", "as", "is", "are", "was", "be", "it", "its", "not",
    "but", "vs", "into", "that", "this",
    "de", "da", "do", "das", "dos", "e", "o", "os", "as", "em", "no", "na",
    "nos", "nas", "para", "por", "com", "um", "uma", "que", "ao", "aos",
}

EM_DASH = "\u2014"
EN_DASH = "\u2013"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
BOLD_ITEM_RE = re.compile(r"^\s*[-*+]\s+\*\*([^*\n]+)\*\*")
DECORATION_RE = re.compile(
    "[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F\u2190-\u21FF]"
)
TABLE_RULE_RE = re.compile(r"^\s*\|[\s:|-]+\|?\s*$")
DOUBLE_HYPHEN_RE = re.compile(r"(?<!-)--(?!-)")


@dataclass
class Finding:
    line: int
    pattern: int
    kind: str
    detail: str


def blank(match: re.Match[str]) -> str:
    return " " * len(match.group(0))


def mask_code(text: str) -> str:
    """Blank out code so line numbers survive and code is never flagged."""
    text = re.sub(r"```.*?```", blank, text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]*`", blank, text)
    return text


def skill_text() -> str:
    return (ROOT / "SKILL.md").read_text(encoding="utf-8")


def banned_words() -> list[str]:
    for anchor in ("Banidas de cara:", "Banned outright:"):
        for line in skill_text().splitlines():
            if line.startswith(anchor):
                body = line[len(anchor):]
                body = re.sub(r"\([^)]*\)", "", body)
                for mark in ('"', "\u201c", "\u201d"):
                    body = body.replace(mark, "")
                words = [w.strip(" .") for w in body.split(",")]
                return [w for w in words if w]
    raise SystemExit("Could not find the banned word list in SKILL.md")


def anglicisms() -> list[str]:
    """Hyphenated English jargon watched by pattern 28 in SKILL.md."""
    section = re.search(r"(?s)#### 28\..*?(?=#### 29\.|\Z)", skill_text())
    if section is None:
        raise SystemExit("Could not find pattern 28 in SKILL.md")
    match = re.search(r"\*\*Palavras vigiadas:\*\*(.*)", section.group(0))
    if match is None:
        raise SystemExit("Could not find the watch list of pattern 28")
    words = [w.strip(" .") for w in match.group(1).split(",")]
    return [w for w in words if w]


def variants(word: str) -> set[str]:
    out = {word, word + "s", word + "es", word + "d", word + "ed", word + "ing"}
    if word.endswith("y"):
        out |= {word[:-1] + "ies", word[:-1] + "ied"}
    if word.endswith("o"):
        out |= {word[:-1] + "a", word[:-1] + "os", word[:-1] + "as"}
    return out


def term_pattern(term: str) -> str:
    forms = []
    for form in sorted(variants(term), key=len, reverse=True):
        forms.append(r"\s+".join(re.escape(part) for part in form.split()))
    return r"\b(?:" + "|".join(forms) + r")\b"


def compile_terms(words: list[str]) -> re.Pattern[str]:
    return re.compile("|".join(term_pattern(w) for w in words), re.IGNORECASE)


BANNED_RE = compile_terms(banned_words())
ANGLICISM_RE = compile_terms(anglicisms())


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
    masked = mask_code(text)
    lines = masked.splitlines()
    findings: list[Finding] = []

    straight = sum(line.count('"') for line in lines)
    curly = sum(line.count("\u201c") + line.count("\u201d") for line in lines)

    for lineno, line in enumerate(lines, 1):
        for match in BANNED_RE.finditer(line):
            findings.append(Finding(lineno, 8, "banned", f'"{match.group(0)}"'))

        # A line-initial em dash marks dialogue speech and is never flagged.
        if not line.lstrip().startswith(EM_DASH):
            for char, name in ((EM_DASH, "em dash"), (EN_DASH, "en dash")):
                if char in line:
                    count = line.count(char)
                    findings.append(
                        Finding(lineno, 15, "dash", f"{name} x{count}")
                    )

            if DOUBLE_HYPHEN_RE.search(line) and not TABLE_RULE_RE.match(line):
                findings.append(
                    Finding(lineno, 15, "dash", "double hyphen used as a dash")
                )

        bold_item = BOLD_ITEM_RE.match(line)
        if bold_item:
            label = bold_item.group(1)
            rest = line[bold_item.end():]
            if label.endswith(":") or rest.lstrip().startswith(":"):
                findings.append(
                    Finding(lineno, 17, "bold_label", f'"{label.strip(":").strip()}"')
                )

        heading = HEADING_RE.match(line)
        if heading:
            title = heading.group(2)
            if DECORATION_RE.search(title):
                findings.append(
                    Finding(lineno, 19, "decoration", "decorated heading")
                )
            if is_title_case(title):
                findings.append(Finding(lineno, 18, "title_case", f'"{title}"'))

        for match in ANGLICISM_RE.finditer(line):
            findings.append(
                Finding(
                    lineno,
                    28,
                    "anglicism",
                    f'"{match.group(0)}" (use um equivalente natural se houver)',
                )
            )

    if straight and curly:
        findings.append(
            Finding(
                1,
                20,
                "mixed_quotes",
                f"{straight} straight and {curly} curly double quotes",
            )
        )

    findings.sort(key=lambda f: (f.line, f.pattern))
    return findings


def format_findings(findings: list[Finding]) -> str:
    return "\n".join(
        f"line {f.line}: [pattern {f.pattern}] {f.kind}: {f.detail}"
        for f in findings
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan prose for the mechanical AI-writing patterns."
    )
    parser.add_argument("path", help="file to scan, or - for stdin")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit 1 when findings exist (for clean-text CI checks)",
    )
    args = parser.parse_args()

    if args.path == "-":
        text = sys.stdin.read()
    else:
        text = Path(args.path).read_text(encoding="utf-8")

    findings = scan_text(text)
    if findings:
        print(format_findings(findings))
        print(f"{len(findings)} finding(s)")
    else:
        print("no findings")
    return 1 if args.strict and findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
