# GeoMine Research Project Organization Plan

## Purpose

This document organizes the current GeoMine Research plugin state after several capability expansions. The goal is to preserve useful work, make boundaries explicit, reduce startup risk, and provide a practical roadmap for unfinished features.

## Current Project State

GeoMine Research now contains:

- 43 skill entrypoints under `skills/`;
- base GeoMine research skills;
- academic geochemistry paper architecture and paper-writing skills;
- figure package and visualization skills;
- PHREEQC, THMC, and PFLOTRAN modeling skill families;
- optional MCP servers and disabled MCP example configs;
- deterministic helper scripts;
- 15 repository-level test files plus MCP server package tests;
- examples for AOI, geochemistry, MCP, visualization, paper writing, PHREEQC, THMC, and PFLOTRAN workflows.

This is no longer only an MVP. It is a multi-family research plugin with a default-off runtime policy.

## Consolidation Rules

### Keep

Keep files that are one of:

- referenced by `scripts/validate_plugin.py`;
- covered by tests;
- part of a skill family;
- a disabled MCP example config;
- a source/reference/template used by a skill;
- a user-facing documentation file;
- a clear roadmap artifact.

### Move Into `docs/`

Use `docs/` for human-facing explanations:

- project overview;
- user manual;
- architecture guide;
- cleanup plan;
- public portal documentation source.

Keep low-level MCP setup files at root if they are operational runbooks:

- `MCP_SETUP.md`
- `MCP_TROUBLESHOOTING.md`
- `THMC_MCP_INTEGRATION_GUIDE.md`
- `THMC_MODELING_GUIDE.md`

### Keep Under `references/`

Use `references/` for material that skills load or route to:

- evidence rules;
- entity schema;
- MCP roadmap;
- adapter design;
- data-source references;
- disabled MCP templates.

### Keep Under `skills/`

Use `skills/` only for Codex skill instructions and direct skill resources:

- `SKILL.md`;
- `references/`;
- `templates/`;
- `scripts/`;
- `examples/`;
- `schemas/`.

### Keep Under `mcp/`

Use `mcp/` for standalone MCP packages. Do not mix MCP package source into top-level scripts unless it is the legacy/simple `geomine` server.

## Cleanup Completed In This Pass

- Added project documentation under `docs/`.
- Added English and Chinese README entrypoints.
- Documented the multi-skill architecture, MCP default-off model, usage examples, and capability boundaries.
- Removed obvious local system artifacts such as `.DS_Store` and transient PHREEQC log output from the working tree.
- Preserved existing untracked skill families and MCP files because they are part of current plugin capability and validation coverage.

## Unfinished Or Partially Complete Areas

### 1. Live Data Adapters

Current status:

- The plugin has deterministic source planners and adapter scaffolds.
- Live network retrieval is not enabled by default.
- Several adapters are still planned rather than production data connectors.

Plan:

1. Keep source planners stable.
2. Add fixture-backed parsers for each source.
3. Add live adapters only behind explicit environment flags.
4. Preserve source version, license, CRS, scale, query, and retrieval date.
5. Never silently fall back from failed live retrieval to invented data.

### 2. MCP Publishing and Installation

Current status:

- MCP example configs exist and are disabled.
- Local MCP development commands are documented.
- Root `.mcp.json` remains absent by design.

Plan:

1. Keep default-off policy.
2. Add install scripts only when path handling is robust.
3. Add a marketplace packaging guide when Codex plugin publishing requirements are final.
4. Add a versioned release checklist.

### 3. THMC / PHREEQC / PFLOTRAN Execution Boundary

Current status:

- PHREEQC skill supports input design and local file scripts.
- THMC and PFLOTRAN MCP tools focus on planning, mock records, and run manifests.
- Mock run results are not scientific validation.

Plan:

1. Keep Core Mode functional without MCP.
2. Separate draft input generation from execution.
3. Add live execution only through explicit adapters and run records.
4. Require validation datasets before making calibration or safety claims.

### 4. Visualization Output

Current status:

- Visualization skill can generate conceptual React/Vite/Three.js scenes.
- SceneSpec examples exist.

Plan:

1. Add more domain examples: tailings, DGR, fracture flow, hydrogeochemistry, exploration targeting.
2. Add screenshot/build verification to generated visualization packages.
3. Keep conceptual geometry labelled unless CRS, scale, and authoritative coordinates are provided.

### 5. Figure Quality

Current status:

- Academic Figure Package skill provides rules and scaffolds.
- Data charts need strict labels, units, legends, source notes, and captions.

Plan:

1. Enforce the minimum data-chart text contract in figure specs.
2. Improve plotting scaffolds for line, bar, scatter, uncertainty, source notes, and annotations.
3. Add tests that inspect scaffold quality.

### 6. Documentation Publication

Current status:

- Markdown docs are under `docs/`.
- Portal route `/geomine/docs` should render an HTML/e-book page.

Plan:

1. Keep Markdown docs as source-of-truth for GitHub.
2. Render a curated HTML reading experience in the OpenMine portal.
3. Add links from `/geomine`.
4. Verify production after Cloudflare Pages deploy.

## Suggested Roadmap

### v0.2.1 Documentation and Packaging

- Finish docs and README bilingual pass.
- Keep plugin validation green.
- Publish GitHub repository.
- Publish portal docs page.

### v0.2.2 Figure and Visualization Hardening

- Improve data-chart scaffolds.
- Add visual QA tests for generated web visualizations.
- Add more figure package examples.

### v0.3 Bounded Live Source Adapters

- Add fixture-backed CDoGS, OGSEarth, Saskatchewan, BC, and Open Canada parsers.
- Add optional live retrieval behind explicit flags.
- Add provenance snapshots.

### v0.4 Modeling Execution Records

- Add stronger PHREEQC local execution integration if available.
- Add run-record schemas for real solver outputs.
- Keep mock/live distinction explicit.

### v0.5 Public Marketplace Readiness

- Add package signing/release checklist.
- Add install/uninstall docs.
- Add security review notes.
- Add versioned examples and release notes.

## Definition Of Done For Future Changes

A GeoMine Research change is done only when:

- `python3 scripts/validate_plugin.py` passes;
- repository tests pass;
- new skills include focused `SKILL.md` frontmatter;
- new MCP tools preserve `mode`, `provenance`, `warnings`, and `errors`;
- docs or README are updated when behavior changes;
- no local cache, `.DS_Store`, generated logs, secrets, or transient build output are committed;
- outputs keep disclosure, legal, investment, QP, and scientific-validation boundaries.
