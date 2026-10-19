#!/usr/bin/env python3
"""Self-checks for the scanner, the grader, and the packaged fixtures.

Run without arguments in CI. Use --grade to check a rewrite produced by
the skill or by an agent run:

    python3 evals/run_evals.py --grade evals/fixtures/sao-paulo.md out.md
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
sys.path.insert(0, str(REPO / "scripts"))
import slop_scan  # noqa: E402

FIXTURES = ROOT / "fixtures"
GOLDEN = ROOT / "golden"

# Minimum scanner findings each fixture must produce, by kind. A value of
# None marks a negative control: a text the scanner must not flag.
FIXTURE_MINIMUMS = {
    "sao-paulo.md": {"banned": 1, "dash": 1, "bold_label": 3},
    "museu.md": {
        "banned": 2,
        "dash": 1,
        "title_case": 1,
        "mixed_quotes": 1,
        "anglicism": 1,
    },
    "resposta.md": None,
}

GOLDEN_CHECKS = {
    "sao-paulo-after.md": {
        "input": "sao-paulo.md",
        "summary_heading": "O que mudou",
        "keep": [
            "São Paulo",
            "Liberdade",
            "Mooca",
            "Bixiga",
            "Mercadão",
            "Vila Madalena",
            "mortadela",
            "kaiseki",
            "pastel",
        ],
    },
}


def scan(path: Path) -> list[slop_scan.Finding]:
    return slop_scan.scan_text(path.read_text(encoding="utf-8"))


def count_kinds(findings: list[slop_scan.Finding]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for finding in findings:
        counts[finding.kind] = counts.get(finding.kind, 0) + 1
    return counts


def numbers(text: str) -> set[str]:
    return {
        n.replace(",", "").replace(".", "")
        for n in re.findall(r"\d+(?:[.,]\d+)*", text)
    }


def grade(
    input_text: str, output_text: str, keep: list[str] | None = None
) -> list[str]:
    """Check a rewrite: mechanically clean and fact preserving."""
    problems: list[str] = []
    findings = slop_scan.scan_text(output_text)
    if findings:
        problems.append("scanner findings in the rewrite:")
        problems.extend(
            "  " + line for line in slop_scan.format_findings(findings).splitlines()
        )
    missing = numbers(input_text) - numbers(output_text)
    if missing:
        problems.append(
            f"numbers from the draft missing in the rewrite: {sorted(missing)}"
        )
    for term in keep or []:
        if term.lower() not in output_text.lower():
            problems.append(f'expected fact missing in the rewrite: "{term}"')
    return problems


def run_checks() -> int:
    failures = 0

    for name, minimums in FIXTURE_MINIMUMS.items():
        path = FIXTURES / name
        findings = scan(path)
        if minimums is None:
            if findings:
                failures += 1
                print(f"FAIL {name}: scanner flagged a clean control text")
                print("  " + slop_scan.format_findings(findings).replace("\n", "\n  "))
            else:
                print(f"pass {name}: negative control clean")
            continue
        counts = count_kinds(findings)
        for kind, wanted in minimums.items():
            got = counts.get(kind, 0)
            if got < wanted:
                failures += 1
                print(f"FAIL {name}: expected >= {wanted} {kind}, got {got}")
            else:
                print(f"pass {name}: {kind} x{got} (>= {wanted})")

    for name, spec in GOLDEN_CHECKS.items():
        text = (GOLDEN / name).read_text(encoding="utf-8")
        findings = slop_scan.scan_text(text)
        if findings:
            failures += 1
            print(f"FAIL {name}: golden rewrite is not clean")
            print("  " + slop_scan.format_findings(findings).replace("\n", "\n  "))
        else:
            print(f"pass {name}: clean under the scanner")

        heading = spec["summary_heading"]
        if heading.lower() not in text.lower():
            failures += 1
            print(f'FAIL {name}: missing "{heading}" section')
        else:
            print(f'pass {name}: has a "{heading}" section')

        source = (FIXTURES / spec["input"]).read_text(encoding="utf-8")
        problems = grade(source, text, spec["keep"])
        if problems:
            failures += 1
            print(f"FAIL {name}: grader problems")
            for problem in problems:
                print(f"  {problem}")
        else:
            print(f"pass {name}: grader (facts preserved, mechanically clean)")

    evals = json.loads((ROOT / "evals.json").read_text(encoding="utf-8"))
    if len(evals.get("evals", [])) < 3:
        failures += 1
        print("FAIL evals.json: fewer than 3 eval prompts")
    else:
        print(f"pass evals.json: {len(evals['evals'])} eval prompts")

    if failures:
        print(f"{failures} check(s) failed")
        return 1
    print("all checks passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run scanner, grader, and fixture self-checks."
    )
    parser.add_argument("--grade", nargs=2, metavar=("INPUT", "OUTPUT"))
    parser.add_argument(
        "--keep",
        default="",
        help="comma-separated facts that must survive the rewrite",
    )
    args = parser.parse_args()

    if args.grade:
        input_text = Path(args.grade[0]).read_text(encoding="utf-8")
        output_text = Path(args.grade[1]).read_text(encoding="utf-8")
        keep = [k.strip() for k in args.keep.split(",") if k.strip()]
        problems = grade(input_text, output_text, keep)
        if problems:
            print("rewrite has problems:")
            for problem in problems:
                print(f"  {problem}")
            return 1
        print("rewrite passes: mechanically clean, facts preserved")
        return 0

    return run_checks()


if __name__ == "__main__":
    raise SystemExit(main())
