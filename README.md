# GeoMine Research

GeoMine Research is a Codex plugin for Canada-first geoscience and mining research workflows. It routes broad questions into focused skills, normalizes AOIs and CRS assumptions, recommends public geodata sources, structures geochemical and mineral occurrence evidence, checks deposit-model fit, and assembles evidence-backed Markdown outputs.

## MVP Scope

- Skill-only Codex plugin.
- GIS and AOI normalization.
- Canada-first geodata discovery.
- Geochemical survey interpretation support.
- Mineral occurrence normalization.
- Deposit model checklists.
- NI 43-101 and CIM terminology risk flagging.
- Markdown research synthesis.

## Non-Goals

- No live data adapters in v0.1.
- No MCP server declaration in v0.1.
- No commercial database access.
- No legal advice, investment advice, QP opinion, feasibility conclusion, resource validation, reserve estimate, or permitting decision.
- No production prospectivity modeling.

## Directory Structure

```text
.codex-plugin/plugin.json
skills/
references/
scripts/geomine/
scripts/geomine/adapters/
tests/
examples/
README.md
AGENTS.md
CHANGELOG.md
pyproject.toml
```

## Local Codex Installation

This plugin is located at:

```text
/Users/aibao/Documents/Project/MiningReg/openminer/plugins/Code/geo-mining-research
```

For Codex local plugin testing, register this folder in a local marketplace or copy/symlink it into the marketplace plugin path used by your Codex installation. The manifest is `.codex-plugin/plugin.json`, and the plugin name is `geo-mining-research`.

If using a repository-local marketplace rooted at `openminer/plugins/Code`, the plugin source path is:

```json
{
  "name": "geo-mining-research",
  "source": {
    "source": "local",
    "path": "./geo-mining-research"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Research"
}
```

## Sample Prompts

- Use GeoMine Research to screen a BC AOI for porphyry Cu-Mo-Au potential.
- Use GeoMine Research to evaluate an Ontario claim block for LCT pegmatite potential.
- Use GeoMine Research to review this technical disclosure draft for NI 43-101 terminology and evidence-gap risks.

## Development Commands

```bash
python3 scripts/validate_plugin.py
PYTHONPATH=scripts uv run --no-project --with pytest python -m pytest
```

## Safety Boundary

This output is for research assistance only. It is not legal advice, investment advice, a Qualified Person opinion, a feasibility study, a reserve estimate, or a permitting decision. All material technical disclosure should be reviewed by a Qualified Person and, where relevant, legal and regulatory counsel.

## Roadmap

- v0.2: MCP roadmap, adapter/MCP design, and deterministic adapter URL builders/parsers for Open Canada, BC Data Catalogue, and ArcGIS REST.
- v0.2.1: CDoGS, OGSEarth, and EarthChem fixture parsers, still without default live network tests.
- v0.3: lightweight prospectivity modeling helpers with spatial cross-validation guidance.
- v0.4: deeper NI 43-101 review workflows and technical-report evidence extraction.

## MCP Roadmap

See [references/mcp-roadmap.md](references/mcp-roadmap.md) and [references/adapter-mcp-design.md](references/adapter-mcp-design.md). The plugin still does not declare `.mcp.json`; that should be added only after a working MCP server and contract tests exist.
