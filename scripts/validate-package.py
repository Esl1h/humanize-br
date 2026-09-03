#!/usr/bin/env python3
"""Check Humanize BR's package files without external dependencies."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL_PATH = ROOT / "SKILL.md"
SKILL = SKILL_PATH.read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")
AGENTS = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
EVAL = (ROOT / "eval.md").read_text(encoding="utf-8")
CLAUDE_PLUGIN = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
CODEX_PLUGIN = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))

PATTERN_COUNT = 38


def require_match(match: re.Match[str] | None, message: str) -> re.Match[str]:
    if match is None:
        raise SystemExit(message)
    return match


yaml_metadata = require_match(
    re.match(r"\A---\n(.*?)\n---\n", SKILL, re.DOTALL),
    "SKILL.md must begin with YAML metadata",
).group(1)

for unsupported_field in ("compatibility:", "allowed-tools:"):
    if re.search(rf"(?m)^{re.escape(unsupported_field)}", yaml_metadata):
        raise SystemExit(f"Remove unsupported YAML field: {unsupported_field[:-1]}")

skill_version = require_match(
    re.search(r'(?m)^\s+version:\s*["\']([^"\']+)["\']\s*$', yaml_metadata),
    "Add metadata.version to SKILL.md",
).group(1)
readme_version = require_match(
    re.search(r"(?m)^- \*\*([0-9]+\.[0-9]+\.[0-9]+)\*\*", README),
    "Add a version entry to README.md",
).group(1)

package_versions = {
    skill_version,
    readme_version,
    str(CLAUDE_PLUGIN.get("version", "")),
    str(CODEX_PLUGIN.get("version", "")),
}
if len(package_versions) != 1:
    raise SystemExit(
        f"Use one package version in all files: {sorted(package_versions)}"
    )

skill_files = {path.relative_to(ROOT) for path in ROOT.rglob("SKILL.md")}
if SKILL_PATH.is_symlink() or skill_files != {Path("SKILL.md")}:
    raise SystemExit("Keep one regular SKILL.md at the repo root")
if CLAUDE_PLUGIN.get("skills") != ["./"]:
    raise SystemExit("Point the Claude plugin skill loader at the repo root")
if CODEX_PLUGIN.get("skills") != "./":
    raise SystemExit("Point the Codex plugin skill loader at the repo root")

plain_language_rules = (
    "## Estilo de escrita",
    "Vá direto ao ponto principal.",
    "Use palavras comuns e voz ativa.",
    "Mantenha frases e parágrafos curtos.",
    "Preserve o sentido técnico completo.",
)
missing_plain_language_rules = [
    rule for rule in plain_language_rules if rule not in AGENTS
]
if missing_plain_language_rules:
    raise SystemExit(
        "Add the missing plain-language rules to AGENTS.md: "
        + ", ".join(missing_plain_language_rules)
    )

pattern_numbers = [
    int(number)
    for number in re.findall(r"(?m)^#### ([0-9]+)\. ", SKILL)
]
if pattern_numbers != list(range(1, PATTERN_COUNT + 1)):
    raise SystemExit(
        f"Number SKILL.md patterns from 1 through {PATTERN_COUNT}: {pattern_numbers}"
    )

readme_numbers = {
    int(number) for number in re.findall(r"(?m)^\| ([0-9]+) \|", README)
}
if readme_numbers != set(range(1, PATTERN_COUNT + 1)):
    raise SystemExit(f"List patterns 1 through {PATTERN_COUNT} in the README table")

eval_sections = ("## Princípios de edição", "## Palavras e expressões vigiadas", "## Os 38 padrões", "## Leitura final")
missing_eval_sections = [section for section in eval_sections if section not in EVAL]
if missing_eval_sections:
    raise SystemExit("Add the missing sections to eval.md: " + ", ".join(missing_eval_sections))

if len(SKILL.splitlines()) > 900:
    raise SystemExit("Keep SKILL.md at 900 lines or fewer")

print(f"Humanize BR package v{skill_version} is valid")
