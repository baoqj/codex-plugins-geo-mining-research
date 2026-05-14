# GeoMine Research

**Language:** English | [中文](README.zh-CN.md)

GeoMine Research is a Codex plugin package for academic geoscience, geochemistry, mining research, and Canada-first mineral-information workflows. It combines focused Codex skills, deterministic helper scripts, optional MCP servers, source/provenance references, tests, and examples.

The project is intentionally conservative: it helps organize evidence, design research workflows, draft academic papers, build model packages, and generate visual/PDF outputs, but it does not present itself as a live exploration database, a Qualified Person opinion, a legal opinion, an investment recommendation, or a validated numerical simulator.

## What It Does

GeoMine Research supports:

- AOI normalization, CRS planning, and Canada-first geodata discovery.
- Geochemical survey interpretation and QA/QC-aware evidence synthesis.
- Mineral occurrence normalization and deposit-model reasoning.
- NI 43-101 / CIM terminology risk review.
- Academic paper architecture, paper drafting, equation/evidence registries, peer-review checks, and math-aware PDF export.
- Academic figure package planning for maps, geochemical plots, conceptual mechanisms, figure captions, and reproducible scaffolds.
- 3D / web visualization studio output using React, Vite, and Three.js.
- PHREEQC Modeling Packages for groundwater chemistry, speciation, saturation indices, water-rock reaction, inverse modeling plans, and paper methods text.
- THMC Modeling Skill Family for thermo-hydro-mechanical-chemical groundwater and reactive-transport research planning.
- PFLOTRAN Modeling Skill Family for solver-specific PFLOTRAN input-deck, grid/material, chemistry, run, output, calibration, and paper-synthesis planning.
- Optional local MCP servers for deterministic data/tool contracts, mock-backed THMC records, DGR field-data acquisition, and PFLOTRAN planning artifacts.

## Safety-First Startup Behavior

By default:

- `.codex-plugin/plugin.json` does **not** auto-register local skills.
- `.codex-plugin/plugin.json` does **not** auto-register MCP servers.
- The plugin root does **not** ship a default `.mcp.json`.
- MCP examples under `references/*.mcp.example.json` are disabled and optional.

This prevents Codex startup failures when local Python, `uv`, MCP dependencies, or environment-specific paths are not ready. Skills and MCP servers remain available as source templates and can be explicitly installed or enabled.

## Architecture

```text
geo-mining-research/
  .codex-plugin/
    plugin.json
  docs/
    README.md
    GeoMine_Research_User_Manual.md
    GeoMine_Research_User_Manual.zh-CN.md
    PROJECT_ORGANIZATION_PLAN.md
  skills/
    geomine-research-router-skill/
    research-router-skill/
    academic-geochemistry-paper-architect/
    academic-paper-research-writer/
    figure-generation/academic-figure-package-skill/
    geomine-paper-pdf-export-skill/
    geomine-visualization-studio-skill/
    phreeqc-modeling-skill/
    thmc-modeling/
    pflotran-modeling/
    ...base GIS, geochemistry, occurrence, deposit, disclosure, synthesis skills
  scripts/
    geomine_mcp_server.py
    geomine/
    run_mcp_sample_cases.py
    validate_plugin.py
  mcp/
    geomine-thmc-server/
  references/
    *.md
    *.mcp.example.json
  examples/
  tests/
```

The core workflow is router-driven:

1. Interpret the user request and normalize entities.
2. Classify the research type and evidence lanes.
3. Select the smallest useful skill set.
4. Use optional MCP only when explicitly available.
5. Preserve provenance, uncertainty, limitations, and caveats.
6. Produce Markdown, modeling packages, figure packages, visualization output, or PDF deliverables.

## Skill Families

| Area | Key skills | Purpose |
|---|---|---|
| Routing | `geomine-research-router-skill`, `research-router-skill` | Normalize entities, classify tasks, select skills/MCP tools, and structure final synthesis. |
| Base GeoMine | `aoi-crs-normalizer-skill`, `geodata-discovery-skill`, `geochemical-survey-skill`, `mineral-occurrence-skill`, `deposit-model-skill`, `ni43-101-disclosure-check-skill`, `report-synthesis-skill` | AOI, GIS, geochemistry, occurrence, deposit-model, disclosure, and report foundations. |
| Academic writing | `academic-geochemistry-paper-architect`, `academic-paper-research-writer`, `geomine-paper-pdf-export-skill` | Architecture-first geochemistry papers, publication-style drafting, equations, evidence matrices, and PDF export. |
| Figures and visuals | `academic-figure-package-skill`, `geomine-visualization-studio-skill` | Figure packages, captions, GIS/geochemistry figures, React/Vite/Three.js conceptual scenes. |
| PHREEQC | `phreeqc-modeling-skill` | Groundwater chemistry modeling packages and local PHREEQC file scaffolding. |
| THMC | `skills/thmc-modeling/` | Coupling-level selection, conceptual models, governing equations, reaction networks, solver routes, validation, uncertainty, and THMC reports. |
| PFLOTRAN | `skills/pflotran-modeling/` | Independent PFLOTRAN Modeling Package, input decks, grid/material plans, chemistry, run manifests, output analysis, and paper synthesis. |

## MCP Servers

GeoMine includes optional local MCP implementations:

| Server | Purpose | Default |
|---|---|---|
| `geomine` | AOI normalization, Canadian source discovery planning, provenance summaries, claim-neighbor planning, infrastructure-distance planning. | Disabled |
| `geomine_thmc` | Mock-backed THMC project/AOI/water-chemistry/lithology/mineralogy records, PHREEQC draft/mock runs, OGS/PFLOTRAN job records, model versions, run records. | Disabled |
| `geomine_thmc_data` | DGR field-data acquisition records, boreholes, sensors, water samples, rock core measurements, packer tests, stress, validation, data packages. | Disabled |
| `geomine_pflotran` | PFLOTRAN planning artifacts: input deck skeletons, validation, run manifests, observation parsing, result summaries, model packages. | Disabled |

Mock outputs demonstrate workflow shape only. They are not validated field data, solver results, safety assessments, or regulatory evidence.

## Installation Notes

For local Codex plugin testing, place or symlink this folder under a local plugin marketplace, for example:

```text
~/.codex/plugins/geo-mining-research
```

Then point your Codex marketplace configuration to the plugin root and install it from the Codex plugin UI or CLI. Keep MCP disabled unless you explicitly want local MCP testing.

For direct local MCP debugging:

```bash
codex mcp add geomine \
  --env PYTHONPATH=/Users/aibao/Documents/Project/MiningReg/openminer/plugins/Code/geo-mining-research/scripts \
  -- \
  uv \
  --directory /Users/aibao/Documents/Project/MiningReg/openminer/plugins/Code/geo-mining-research \
  run \
  --no-project \
  --with \
  "mcp[cli]" \
  --with \
  httpx \
  python \
  scripts/geomine_mcp_server.py
```

For THMC/DGR/PFLOTRAN MCP development, see:

- [MCP_SETUP.md](MCP_SETUP.md)
- [THMC_MCP_INTEGRATION_GUIDE.md](THMC_MCP_INTEGRATION_GUIDE.md)
- [MCP_TROUBLESHOOTING.md](MCP_TROUBLESHOOTING.md)

## Example Prompts

```text
Use GeoMine Research to screen a Saskatchewan AOI for uranium potential using geology, geochemistry, mineral occurrences, and disclosure-safe caveats.
```

```text
Use GeoMine Research to design a geochemistry academic paper on uranium migration in fractured Canadian Shield groundwater using PHREEQC speciation and saturation indices.
```

```text
Use GeoMine Research THMC Modeling to build a THMC Modeling Package for tailings seepage, sulfide oxidation, shallow groundwater transport, and pH buffering.
```

```text
Use GeoMine Research to generate an Academic Figure Package for a uranium groundwater paper, including study-area map, Piper diagram, Eh-pH diagram, speciation plot, conceptual migration cross-section, captions, and publication checklist.
```

```text
Use GeoMine Research to generate a 3D conceptual uranium basin-margin visualization page with stratigraphy, faults, drillholes, geochemical evidence lanes, provenance, and caveats.
```

## Development Commands

```bash
python3 scripts/validate_plugin.py
PYTHONPATH=scripts uv run --no-project --with pytest --with "mcp[cli]>=1.2.0" --with "httpx>=0.28.0" python -m pytest
PYTHONPATH=scripts python3 scripts/run_mcp_sample_cases.py ../../report
python3 tests/validate_thmc_skill_family.py
python3 tests/validate_thmc_mcp_config.py
python3 scripts/test_thmc_mcp_tools.py
python3 scripts/test_thmc_data_mcp_tools.py
python3 scripts/test_pflotran_mcp_tools.py
uv --directory mcp/geomine-thmc-server run --with pytest python -m pytest
```

## Documentation

See:

- [docs/README.md](docs/README.md)
- [docs/GeoMine_Research_User_Manual.md](docs/GeoMine_Research_User_Manual.md)
- [docs/PROJECT_ORGANIZATION_PLAN.md](docs/PROJECT_ORGANIZATION_PLAN.md)

The OpenMine portal documentation page is intended to be published at:

```text
https://openmine.vip/geomine/docs
```

## Improvement and Iteration History

### 0.1.0 - MVP Skill-Only Plugin

- Created the initial GeoMine Research Codex plugin.
- Added focused skills for routing, AOI/CRS normalization, geodata discovery, geochemical survey interpretation, mineral occurrence normalization, deposit-model review, NI 43-101/CIM risk flagging, and report synthesis.
- Added Canada-first references, entity schema, evidence matrix templates, examples, deterministic helper scripts, and validation tests.
- Established the core guardrail: no legal advice, investment advice, Qualified Person opinion, feasibility conclusion, resource validation, reserve estimate, or permitting decision.

### 0.2.0 - Deferred MCP Architecture

- Added a local `geomine` MCP server entrypoint and pure tool layer.
- Added ten deterministic MCP tool wrappers for AOI normalization, public-source discovery planning, provenance summaries, claim-neighbor planning, and infrastructure-distance planning.
- Moved MCP activation to disabled example templates under `references/`.
- Removed default plugin `skills` and `mcpServers` manifest entries to keep Codex startup safe.
- Added adapter/MCP design notes, source registries, CKAN/ArcGIS parser scaffolds, MCP sample runner, and smoke tests.

### 0.2.x - Academic Research and Publication Workflow

- Added `academic-paper-research-writer` for journal-style papers, hypotheses, evidence matrices, equation registries, citation discipline, and peer-review checks.
- Added `geomine-paper-pdf-export-skill` for formula-safe Markdown-to-PDF export with math, physics, chemistry notation, and scientific units.
- Added `academic-geochemistry-paper-architect` to classify geochemistry paper types before drafting and to enforce architecture, data, method, figure, citation, uncertainty, and conclusion-boundary rules.
- Added `academic-figure-package-skill` for manuscript figure packages, captions, drawing prompts, script scaffolds, and publication checklists.

### 0.2.x - Visualization Studio

- Added `geomine-visualization-studio-skill`.
- Added GeoMine SceneSpec examples for uranium basin and research workflow visualization.
- Added a React/Vite/Three.js generation workflow for conceptual geologic, GIS, mineralization, vein, drillhole, and geologic-evolution scenes.

### 0.2.x - THMC Skill Family

- Added a focused THMC Modeling Skill Family covering scenario routing, conceptual models, governing equations, hydro-transport, reaction networks, thermal transport, mechanical-damage/permeability, solver selection, validation, uncertainty, figures, and synthesis.
- Added THMC Modeling Package 2.0 templates and schema files.
- Added optional `geomine_thmc` MCP tools for mock project context, water chemistry, lithology/mineralogy, mesh/parameter fields, PHREEQC draft/mock jobs, OGS/PFLOTRAN job lifecycle, model versions, and run records.

### 0.2.x - DGR Field Data and PFLOTRAN Planning

- Added `dgr-field-data-acquisition-skill` and `geomine_thmc_data` MCP tools for DGR campaign/borehole/sensor/water/rock/packer/stress data records, validation, calibration datasets, and data packages.
- Added independent `pflotran-modeling` skill family and optional `geomine_pflotran` planning MCP tools.
- Added PFLOTRAN input deck, grid/material, chemistry, THC, geomechanics, run-management, output-analysis, calibration/validation, and paper-synthesis skills.

### 0.2.x - PHREEQC Modeling

- Added `phreeqc-modeling-skill` as an independent skill family for groundwater chemistry modeling.
- Added references, templates, examples, and local scripts for water chemistry validation, solution block generation, selected output generation, selected output parsing, and run manifest construction.

### Current Cleanup and Documentation Pass

- Consolidated the project-level documentation under `docs/`.
- Added English and Chinese README entry points.
- Documented the plugin architecture, operation model, current capability boundaries, unfinished work, and practical usage examples.
- Added an OpenMine portal docs route target at `/geomine/docs`.

## Current Boundaries and Open Work

- Live source adapters remain conservative and bounded. Many current tools are source planners, fixture parsers, or mock-backed workflow validators.
- PHREEQC, THMC, and PFLOTRAN MCP layers currently emphasize package generation, draft inputs, mock runs, run records, and planning. Scientific validation still requires real data, solver execution, calibration, and domain review.
- Marketplace publishing beyond local Codex installation still requires final packaging policy, versioning, and user-facing security review.
- Public technical disclosure outputs must be reviewed by a Qualified Person and legal/regulatory counsel where relevant.

## License

Proprietary. See `.codex-plugin/plugin.json` for plugin metadata.
