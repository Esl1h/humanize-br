#!/usr/bin/env python3
"""Run the prompts in evals/evals.json through an agent and judge the answers.

The agent and the judge are shell commands that read a prompt on stdin
and print the answer on stdout, so any CLI works. The agent must have the
skill installed. Examples:

    python3 evals/run_agent_evals.py --agent "claude -p"
    python3 evals/run_agent_evals.py --agent "claude -p" --judge "claude -p"
    python3 evals/run_agent_evals.py --agent "codex exec -" --only 1 3

Each answer is saved to evals/out/<id>.md. An eval with a "grade" entry
also runs the mechanical grader from run_evals.py on the answer. With
--judge, each assertion is checked by the judge command, which must reply
with JSON. This file is the same in Humanize AI Slop and Humanize BR.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
sys.path.insert(0, str(ROOT))
import run_evals  # noqa: E402

PLACEHOLDER_RE = re.compile(r"\[(?:paste|cole) (evals/[^\]\s]+)\]")

JUDGE_PROMPT = """You grade the answer of a writing assistant against a list of assertions.

The user's request:
<request>
{request}
</request>

The assistant's answer:
<answer>
{answer}
</answer>

Assertions:
{assertions}

Reply with JSON only, in this shape:
{{"results": [{{"assertion": 1, "pass": true, "reason": "one short sentence"}}]}}
"""


def build_prompt(template: str) -> str:
    def paste(match: re.Match[str]) -> str:
        text = (REPO / match.group(1)).read_text(encoding="utf-8").strip()
        return f"\n\n{text}\n\n"

    return PLACEHOLDER_RE.sub(paste, template).strip() + "\n"


def run(command: str, prompt: str, timeout: int) -> str:
    result = subprocess.run(
        command,
        shell=True,
        input=prompt,
        capture_output=True,
        text=True,
        timeout=timeout,
        cwd=REPO,
    )
    if result.returncode != 0:
        raise RuntimeError(f"`{command}` exited {result.returncode}: {result.stderr.strip()[:500]}")
    return result.stdout


def parse_judgement(reply: str, count: int) -> list[dict]:
    match = re.search(r"\{.*\}", reply, re.DOTALL)
    if match is None:
        raise ValueError("the judge did not reply with JSON")
    results = json.loads(match.group(0)).get("results", [])
    if len(results) != count:
        raise ValueError(f"the judge returned {len(results)} results for {count} assertions")
    return results


def run_eval(item: dict, args: argparse.Namespace) -> int:
    failures = 0
    request = build_prompt(item["prompt"])
    answer = run(args.agent, request, args.timeout)
    out = args.out / f"{item['id']}.md"
    out.write_text(answer, encoding="utf-8")
    print(f"eval {item['id']}: answer saved to {out}")

    if "grade" in item:
        source = (REPO / item["grade"]["input"]).read_text(encoding="utf-8")
        problems = run_evals.grade(source, answer, item["grade"].get("keep"))
        if problems:
            failures += 1
            print("  FAIL grader")
            for problem in problems:
                print(f"    {problem}")
        else:
            print("  pass grader (facts preserved, no fix findings)")

    if args.judge:
        assertions = item.get("assertions", [])
        listed = "\n".join(f"{n}. {a}" for n, a in enumerate(assertions, 1))
        prompt = JUDGE_PROMPT.format(request=request, answer=answer, assertions=listed)
        try:
            results = parse_judgement(run(args.judge, prompt, args.timeout), len(assertions))
        except (ValueError, json.JSONDecodeError) as error:
            print(f"  FAIL judge: {error}")
            return failures + 1
        for assertion, result in zip(assertions, results):
            status = "pass" if result.get("pass") is True else "FAIL"
            if status == "FAIL":
                failures += 1
            print(f"  {status} {assertion}: {result.get('reason', '')}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Run evals.json through an agent.")
    parser.add_argument("--agent", required=True, help="command that answers a prompt on stdin")
    parser.add_argument("--judge", help="command that grades assertions and replies with JSON")
    parser.add_argument("--only", nargs="+", type=int, metavar="ID", help="run only these eval ids")
    parser.add_argument("--out", type=Path, default=ROOT / "out", help="where to save the answers")
    parser.add_argument("--timeout", type=int, default=600, help="seconds per command")
    args = parser.parse_args()
    args.out = args.out.resolve()
    args.out.mkdir(parents=True, exist_ok=True)

    evals = json.loads((ROOT / "evals.json").read_text(encoding="utf-8"))["evals"]
    failures = 0
    for item in evals:
        if args.only and item["id"] not in args.only:
            continue
        try:
            failures += run_eval(item, args)
        except (RuntimeError, subprocess.TimeoutExpired) as error:
            failures += 1
            print(f"eval {item['id']}: FAIL {error}")

    print(f"{failures} failure(s)" if failures else "all agent evals passed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
