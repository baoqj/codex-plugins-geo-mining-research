# Changelog

## Unreleased

- Added bilingual project README files with a complete improvement and iteration history.
- Added `docs/` with a full GeoMine Research user manual, Chinese manual, documentation index, and project organization plan.
- Added `academic-geochemistry-paper-architect` for architecture-first geochemistry paper design and router/writer integration.
- Disabled default plugin auto-registration of local skills and MCP servers to avoid startup errors from incomplete local installations.
- Added `geomine-visualization-studio-skill`, a React/Vite/Three.js visualization generator, a SceneSpec reference, and a uranium basin sample scene.
- Added `geomine-paper-pdf-export-skill`, a Markdown-to-PDF exporter that normalizes fenced math, formula-like inline code, bare scientific variables, physical units, and chemistry notation before Pandoc/MathML/Chrome PDF rendering.
- Added `academic-paper-research-writer`, a publication-style academic paper skill with research framing, literature synthesis, mechanism prompts, equation registry, evidence matrix, citation discipline, examples, and tests.
- Added `academic-figure-package-skill`, a publication figure-planning skill with references, templates, validation/scaffold scripts, four example Figure Packages, and GeoMine router/synthesis integration.
- Added `thmc-modeling`, a skills-only THMC groundwater chemistry and reactive-transport skill family with 13 focused skills, modeling package templates, scenario references, JSON model spec schema, validation script, and router integration.
- Moved the root MCP config into `references/geomine.mcp.example.json` as a disabled future-install template.
- Kept MCP implementation available without declaring `.mcp.json` or manifest `mcpServers` by default.
- Added ten GeoMine MCP tool wrappers matching the improved architecture and setup guide.
- Added `geomine-research-router-skill`, MCP setup documentation, entity schema, evidence matrix template, and deterministic MCP sample runner.
- Implemented the first runnable v0.2 MCP server entrypoint and pure tool layer while keeping activation manual.
- Updated the helper package to `0.2.0` with `mcp[cli]` and `httpx` dependencies plus a `geomine-mcp` script.
- Added v0.2 MCP roadmap and adapter/MCP design references.
- Added deterministic adapter skeletons for CKAN package search and ArcGIS REST FeatureSet parsing.
- Added adapter source registry and fixture-only adapter tests.
- Added a runnable MCP server build guide with implementation order, local Codex config, Inspector testing, and plugin bundling steps.

## 0.1.0

- Created GeoMine Research Codex plugin MVP.
- Added eight focused skills for routing, AOI/CRS normalization, geodata discovery, geochemistry, mineral occurrences, deposit models, NI 43-101 risk checking, and report synthesis.
- Added Canada-first references, deterministic helper scripts, tests, examples, and validation.
