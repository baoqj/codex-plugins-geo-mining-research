#!/usr/bin/env python3
"""Validate the GeoMine Research Codex plugin MVP."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SKILLS = [
    "research-router-skill",
    "aoi-crs-normalizer-skill",
    "geodata-discovery-skill",
    "geochemical-survey-skill",
    "mineral-occurrence-skill",
    "deposit-model-skill",
    "ni43-101-disclosure-check-skill",
    "report-synthesis-skill",
]
REQUIRED_FILES = [
    ".codex-plugin/plugin.json",
    "references/data-sources-canada.md",
    "references/evidence-grading.md",
    "references/deposit-model-cheatsheet.md",
    "references/ni43-101-cim-boundary.md",
    "references/output-contracts.md",
    "scripts/geomine/evidence_schema.py",
    "scripts/geomine/data_sources.py",
    "scripts/geomine/aoi.py",
    "scripts/geomine/geochem.py",
    "scripts/geomine/occurrences.py",
    "scripts/geomine/reports.py",
    "README.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "pyproject.toml",
]


def _failures() -> list[str]:
    errors: list[str] = []
    manifest_path = ROOT / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - validation should report context.
        return [f"Cannot read manifest: {exc}"]

    if manifest.get("name") != "geo-mining-research":
        errors.append("manifest name must be geo-mining-research")
    if manifest.get("version") != "0.1.0":
        errors.append("manifest version must be 0.1.0")
    if manifest.get("skills") != "./skills/":
        errors.append("manifest skills must be ./skills/")
    if "mcpServers" in manifest:
        errors.append("v0.1 must not declare mcpServers")
    if manifest.get("interface", {}).get("displayName") != "GeoMine Research":
        errors.append("interface.displayName must be GeoMine Research")

    for rel_path in REQUIRED_FILES:
        if not (ROOT / rel_path).exists():
            errors.append(f"missing required file: {rel_path}")

    for skill_name in REQUIRED_SKILLS:
        skill_path = ROOT / "skills" / skill_name / "SKILL.md"
        if not skill_path.exists():
            errors.append(f"missing skill: {skill_name}")
            continue
        text = skill_path.read_text(encoding="utf-8")
        frontmatter = _frontmatter(text)
        if frontmatter is None:
            errors.append(f"{skill_name} missing YAML frontmatter")
            continue
        if frontmatter.get("name") != skill_name:
            errors.append(f"{skill_name} frontmatter name mismatch")
        if not frontmatter.get("description"):
            errors.append(f"{skill_name} missing description")
    return errors


def _frontmatter(text: str) -> dict[str, str] | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return data
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"').strip("'")
    return None


def main() -> int:
    errors = _failures()
    if errors:
        print("GeoMine Research plugin validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("GeoMine Research plugin validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
