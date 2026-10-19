#!/usr/bin/env python3
"""Check that Humanize AI Slop and Humanize BR have not drifted apart.

The two skills are translations of each other with the same structure.
This check compares the files they share byte for byte, and compares the
structure of the rest: version, pattern numbers, catalog categories, the
sections of SKILL.md and eval.md with their numbered items and bold
labels, and the eval prompts with their assertion counts. This file is
the same in both repositories.

Usage:
  python3 scripts/check-sync.py [PATH_TO_OTHER_REPO]

Without a path, it looks for the other repository next to this one.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAMES = ("humanize-ai-slop", "humanize-br")
SHARED = (
    "scripts/slop_scan.py",
    "scripts/check-sync.py",
    "evals/run_evals.py",
    "evals/run_agent_evals.py",
)


def read(repo: Path, name: str) -> str:
    return (repo / name).read_text(encoding="utf-8")


def skill_name(repo: Path) -> str:
    match = re.search(r"(?m)^name:\s*(\S+)", read(repo, "SKILL.md"))
    if match is None:
        raise SystemExit(f"No skill name in {repo / 'SKILL.md'}")
    return match.group(1)


def sections(text: str) -> list[tuple[int, int]]:
    """Numbered items and line-start bold labels of each ## section."""
    parts = re.split(r"(?m)^## ", text)[1:]
    return [
        (
            len(re.findall(r"(?m)^\d+\. ", part)),
            len(re.findall(r"(?m)^(?:- )?\*\*[^*\n]+\*\*", part)),
        )
        for part in parts
    ]


def structure(repo: Path) -> dict[str, object]:
    skill = read(repo, "SKILL.md")
    catalog = read(repo, "references/patterns.md")
    evals = json.loads(read(repo, "evals/evals.json"))["evals"]
    return {
        "version": re.search(r'(?m)^\s+version:\s*"([^"]+)"', skill).group(1),
        "patterns": re.findall(r"(?m)^### (\d+)\. ", catalog),
        "categories": len(re.findall(r"(?m)^## ", catalog)),
        "SKILL.md sections": sections(skill),
        "eval.md sections": sections(read(repo, "eval.md")),
        "evals.json": [(e["id"], len(e["assertions"])) for e in evals],
    }


def main() -> int:
    own = skill_name(ROOT)
    if own not in NAMES:
        raise SystemExit(f"Unknown skill: {own}")
    other_name = NAMES[1 - NAMES.index(own)]
    other = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / other_name
    if not (other / "SKILL.md").is_file() or skill_name(other) != other_name:
        raise SystemExit(f"Could not find {other_name} at {other}")

    problems = []
    for name in SHARED:
        if (ROOT / name).read_bytes() != (other / name).read_bytes():
            problems.append(f"{name} differs; copy the newer version to both repos")

    mine, theirs = structure(ROOT), structure(other)
    for key in mine:
        if mine[key] != theirs[key]:
            problems.append(f"{key}: {own} has {mine[key]}, {other_name} has {theirs[key]}")

    if problems:
        print(f"{own} and {other_name} have drifted:")
        for problem in problems:
            print(f"  {problem}")
        return 1
    print(f"{own} and {other_name} are in sync")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
