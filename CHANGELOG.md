# Changelog

## Unreleased

- Activated plugin MCP configuration with `.mcp.json` and manifest `mcpServers`.
- Added ten GeoMine MCP tool wrappers matching the improved architecture and setup guide.
- Added `geomine-research-router-skill`, MCP setup documentation, entity schema, evidence matrix template, and deterministic MCP sample runner.
- Implemented the first runnable v0.2 MCP server entrypoint and pure tool layer, then activated it in the plugin manifest after automated smoke tests.
- Updated the helper package to `0.2.0` with `mcp[cli]` and `httpx` dependencies plus a `geomine-mcp` script.
- Added v0.2 MCP roadmap and adapter/MCP design references.
- Added deterministic adapter skeletons for CKAN package search and ArcGIS REST FeatureSet parsing.
- Added adapter source registry and fixture-only adapter tests.
- Added a runnable MCP server build guide with implementation order, local Codex config, Inspector testing, and plugin bundling steps.

## 0.1.0

- Created GeoMine Research Codex plugin MVP.
- Added eight focused skills for routing, AOI/CRS normalization, geodata discovery, geochemistry, mineral occurrences, deposit models, NI 43-101 risk checking, and report synthesis.
- Added Canada-first references, deterministic helper scripts, tests, examples, and validation.
