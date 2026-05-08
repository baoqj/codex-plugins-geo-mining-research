#!/usr/bin/env python3
"""Validate the GeoMine Research Codex plugin package."""

from __future__ import annotations

import json
import sys
from pathlib import Path
import tomllib


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SKILLS = [
    "geomine-research-router-skill",
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
    ".mcp.json",
    "MCP_SETUP.md",
    "references/data-sources-canada.md",
    "references/evidence-grading.md",
    "references/entity-schema.md",
    "references/evidence-matrix-template.md",
    "references/deposit-model-cheatsheet.md",
    "references/ni43-101-cim-boundary.md",
    "references/output-contracts.md",
    "references/mcp-roadmap.md",
    "references/adapter-mcp-design.md",
    "references/runnable-mcp-server-build-guide.md",
    "scripts/geomine/evidence_schema.py",
    "scripts/geomine/data_sources.py",
    "scripts/geomine/aoi.py",
    "scripts/geomine/geochem.py",
    "scripts/geomine/occurrences.py",
    "scripts/geomine/reports.py",
    "scripts/geomine/tools.py",
    "scripts/geomine_mcp_server.py",
    "scripts/run_mcp_sample_cases.py",
    "scripts/geomine/adapters/__init__.py",
    "scripts/geomine/adapters/base.py",
    "scripts/geomine/adapters/ckan.py",
    "scripts/geomine/adapters/arcgis.py",
    "scripts/geomine/adapters/source_registry.py",
    "tests/test_mcp_tools.py",
    "tests/test_mcp_server_import.py",
    "README.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "pyproject.toml",
]
EXPECTED_MCP_TOOLS = [
    "normalize_aoi",
    "search_canada_geodata",
    "search_cdogs_surveys",
    "search_bc_minfile",
    "search_ontario_omi",
    "search_saskatchewan_mineral_data",
    "fetch_dataset_metadata",
    "summarize_dataset_provenance",
    "query_claim_neighbors",
    "calculate_infrastructure_distance",
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
    if manifest.get("version") != "0.2.0":
        errors.append("manifest version must be 0.2.0")
    if manifest.get("skills") != "./skills/":
        errors.append("manifest skills must be ./skills/")
    if manifest.get("mcpServers") != "./.mcp.json":
        errors.append("manifest mcpServers must be ./.mcp.json")
    if manifest.get("interface", {}).get("displayName") != "GeoMine Research":
        errors.append("interface.displayName must be GeoMine Research")

    mcp_path = ROOT / ".mcp.json"
    if mcp_path.exists():
        try:
            mcp_config = json.loads(mcp_path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001 - validation should report context.
            errors.append(f"Cannot read .mcp.json: {exc}")
        else:
            geomine = mcp_config.get("geomine")
            if not isinstance(geomine, dict):
                errors.append(".mcp.json must define a geomine server")
            else:
                if geomine.get("command") != "uv":
                    errors.append(".mcp.json geomine.command must be uv")
                if "--no-project" not in geomine.get("args", []):
                    errors.append(".mcp.json geomine.args must include --no-project")
                if geomine.get("enabled") is not True:
                    errors.append(".mcp.json geomine.enabled must be true")
                if geomine.get("required") is not False:
                    errors.append(".mcp.json geomine.required must be false")
                enabled_tools = geomine.get("enabled_tools")
                if enabled_tools != EXPECTED_MCP_TOOLS:
                    errors.append(".mcp.json enabled_tools must match expected GeoMine MCP tools")

    for rel_path in REQUIRED_FILES:
        if not (ROOT / rel_path).exists():
            errors.append(f"missing required file: {rel_path}")

    pyproject_path = ROOT / "pyproject.toml"
    if pyproject_path.exists():
        try:
            pyproject = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as exc:
            errors.append(f"invalid pyproject.toml: {exc}")
        else:
            project = pyproject.get("project", {})
            dependencies = set(project.get("dependencies", []))
            if project.get("version") != "0.2.0":
                errors.append("pyproject version must be 0.2.0")
            if "mcp[cli]>=1.2.0" not in dependencies:
                errors.append("pyproject dependencies must include mcp[cli]>=1.2.0")
            if "httpx>=0.28.0" not in dependencies:
                errors.append("pyproject dependencies must include httpx>=0.28.0")
            scripts = project.get("scripts", {})
            if scripts.get("geomine-mcp") != "geomine_mcp_server:main":
                errors.append("pyproject must expose geomine-mcp = geomine_mcp_server:main")

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
