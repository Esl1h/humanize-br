#!/usr/bin/env python3
"""Self-checks for the scanner, the grader, and the packaged fixtures.

Run without arguments in CI. The expected findings for each fixture and
the facts each golden rewrite must keep live in evals/checks.json, so this
file is the same in Humanize AI Slop and Humanize BR. Use --grade to check
a rewrite produced by the skill or by an agent run:

    python3 evals/run_evals.py --grade evals/fixtures/INPUT.md out.md
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
CHECKS = json.loads((ROOT / "checks.json").read_text(encoding="utf-8"))


def scan(path: Path) -> list[slop_scan.Finding]:
    return slop_scan.scan_text(path.read_text(encoding="utf-8"))


def count_kinds(findings: list[slop_scan.Finding]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for finding in findings:
        counts[finding.kind] = counts.get(finding.kind, 0) + 1
    return counts


def normalize_number(token: str) -> str:
    """Drop thousands separators but keep decimals, so 1.5 and 15 differ.

    A separator followed by exactly three digits is a thousands separator
    in both English (1,000) and Portuguese (1.000); any other separator is
    a decimal mark.
    """
    parts = re.split(r"[.,]", token)
    head, rest = parts[0], parts[1:]
    while rest and len(rest[0]) == 3:
        head += rest.pop(0)
    return head + ("." + "".join(rest) if rest else "")


def numbers(text: str) -> set[str]:
    return {normalize_number(n) for n in re.findall(r"\d+(?:[.,]\d+)*", text)}


def indent(text: str) -> str:
    return "  " + text.replace("\n", "\n  ")


def grade(
    input_text: str, output_text: str, keep: list[str] | None = None
) -> list[str]:
    """Check a rewrite: free of fix findings and fact preserving."""
    problems: list[str] = []
    fix_findings = slop_scan.fixes(slop_scan.scan_text(output_text))
    if fix_findings:
        problems.append("scanner fix findings in the rewrite:")
        problems.append(indent(slop_scan.format_findings(fix_findings)))
    missing = numbers(input_text) - numbers(output_text)
    if missing:
        problems.append(
            f"numbers from the draft missing in the rewrite: {sorted(missing)}"
        )
    for term in keep or []:
        if term.lower() not in output_text.lower():
            problems.append(f'expected fact missing in the rewrite: "{term}"')
    return problems


def check_fixture(name: str, spec: dict) -> int:
    findings = scan(FIXTURES / name)
    failures = 0
    if spec.get("control"):
        fix_findings = slop_scan.fixes(findings)
        watch_count = len(findings) - len(fix_findings)
        if fix_findings:
            failures += 1
            print(f"FAIL {name}: scanner flagged a clean control text")
            print(indent(slop_scan.format_findings(fix_findings)))
        else:
            print(f"pass {name}: negative control has no fix findings")
        max_watch = spec.get("max_watch")
        if max_watch is not None and watch_count > max_watch:
            failures += 1
            print(f"FAIL {name}: expected <= {max_watch} watch findings, got {watch_count}")
            print(indent(slop_scan.format_findings(findings)))
    counts = count_kinds(findings)
    for kind, wanted in spec.get("min", {}).items():
        got = counts.get(kind, 0)
        if got < wanted:
            failures += 1
            print(f"FAIL {name}: expected >= {wanted} {kind}, got {got}")
        else:
            print(f"pass {name}: {kind} x{got} (>= {wanted})")
    return failures


def check_golden(name: str, spec: dict) -> int:
    text = (GOLDEN / name).read_text(encoding="utf-8")
    failures = 0

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
        print(f"pass {name}: grader (facts preserved, no fix findings)")
    return failures


def run_checks() -> int:
    failures = 0
    for name, spec in CHECKS["fixtures"].items():
        failures += check_fixture(name, spec)
    for name, spec in CHECKS["golden"].items():
        failures += check_golden(name, spec)

    evals = json.loads((ROOT / "evals.json").read_text(encoding="utf-8"))
    if len(evals.get("evals", [])) < 3:
        failures += 1
        print("FAIL evals.json: fewer than 3 eval prompts")
    else:
        print(f"pass evals.json: {len(evals['evals'])} eval prompts")
    for item in evals.get("evals", []):
        for file in item.get("files", []):
            if not (REPO / file).is_file():
                failures += 1
                print(f"FAIL evals.json: eval {item['id']} names a missing file: {file}")

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
        print("rewrite passes: no fix findings, facts preserved")
        return 0

    return run_checks()


if __name__ == "__main__":
    raise SystemExit(main())
