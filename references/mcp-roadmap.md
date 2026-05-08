# GeoMine Research MCP Roadmap

This roadmap moves GeoMine Research from a skill-only v0.1 plugin to a v0.2 plugin with a tested local MCP server, deterministic evidence tools, and a path toward future bounded live adapters.

## Current State

- v0.1 packaged skills, references, examples, validation, and deterministic helper scripts.
- v0.2 declares plugin-root `.mcp.json` through `.codex-plugin/plugin.json`.
- v0.2 exposes a local stdio MCP server named `geomine`.
- v0.2 includes adapter modules, pure MCP tool functions, server wrappers, and contract tests.
- v0.2 still disables live network retrieval by default; unsupported live paths return explicit `unsupported` status instead of fabricated data.

## Official Codex Constraints

- Codex plugins use `.codex-plugin/plugin.json` as the required manifest.
- Plugin paths such as `skills`, `mcpServers`, and apps are relative to the plugin root.
- `.mcp.json` belongs at the plugin root, not inside `.codex-plugin/`.
- MCP servers can be local stdio processes or streamable HTTP servers.
- MCP configuration should be introduced only when the server can be started and tested.

## v0.2 Exposed MCP Tools

### `normalize_aoi`

- Purpose: normalize supplied AOI text or geometry and explicitly detect what remains unresolved.
- Inputs: AOI string or object, default CRS.
- Output schema: normalized AOI fields, assumptions, warnings, provenance, and next steps.
- Test strategy: deterministic unit tests and MCP stdio sample call.

### `search_canada_geodata`

- Purpose: plan Canada-first geodata catalogue discovery for a query, province, and commodity.
- Candidate adapters: Open Canada CKAN, BC Data Catalogue CKAN, Geo.ca/Open Maps records.
- Output schema: planned source records, request metadata, provenance, warnings, and next steps.
- Test strategy: fixture-safe tool contract tests and no default network calls.

### `search_cdogs_surveys`

- Purpose: plan NRCan CDoGS geochemical survey discovery before analytical interpretation.
- Candidate adapters: future CDoGS metadata and spreadsheet/KML parsers.
- Output schema: source notes, expected metadata fields, limitations, provenance, warnings, and next steps.
- Test strategy: deterministic current output; future saved HTML/CSV/KML fixtures.

### `search_bc_minfile`

- Purpose: plan BC MINFILE occurrence lookup for an AOI and commodity.
- Candidate adapters: BC Data Catalogue and MINFILE table-resource parser.
- Test strategy: deterministic current output; future CKAN/table fixtures.

### `search_ontario_omi`

- Purpose: plan Ontario Mineral Inventory / OGSEarth occurrence lookup.
- Candidate adapters: OGSEarth KML registry and OMI metadata parser.
- Test strategy: deterministic current output; future KML fixtures.

### `search_saskatchewan_mineral_data`

- Purpose: plan Saskatchewan public mineral-data lookup for AOI, NTS, or commodity context.
- Candidate adapters: future Saskatchewan public registry and map-service wrappers.
- Test strategy: deterministic current output; future source-specific fixtures.

### `fetch_dataset_metadata`

- Purpose: fetch local registry metadata for a known dataset id.
- Output schema: local metadata record, missing provenance fields, warnings, and next steps.
- Test strategy: deterministic local registry tests.

### `summarize_dataset_provenance`

- Purpose: normalize a supplied dataset/provenance block without claiming source verification.
- Output schema: provenance summary, missing fields, warnings, and next steps.
- Test strategy: deterministic object contract tests.

### `query_claim_neighbors`

- Purpose: plan a claim-neighbor scan without fabricating tenure results.
- Candidate adapters: future provincial tenure APIs or downloaded public tenure layers.
- Test strategy: deterministic current output; future bounded integration tests behind flags.

### `calculate_infrastructure_distance`

- Purpose: plan infrastructure-distance calculation and report required missing inputs.
- Candidate adapters: future authoritative roads, rail, power, port, and processing-facility layers.
- Test strategy: deterministic current output; future spatial fixtures.

## Data Source Roadmap

### NRCan CDoGS

- Access pattern: public website, survey metadata pages, spreadsheet/KML links, WMS index layer, reduced MS Access downloads.
- Authentication: none identified for public metadata and downloads.
- v0.2 adapter: metadata discovery and file-link extraction only.
- v0.3 adapter: spreadsheet parser for standardized survey files.
- Provenance: preserve survey id, publication, medium, analysis history, data file URL, KML URL, and date retrieved.

### Geo.ca / Open Maps / Open Canada

- Access pattern: geospatial catalogue and Open Canada CKAN-style API.
- Authentication: none for public catalogue search.
- v0.2 adapter: CKAN package search and resource parsing.
- v0.3 adapter: linked WMS/WFS/ArcGIS/GeoJSON resource probing with explicit format support.
- Provenance: preserve package id, resource id, organization, license, formats, metadata URL, and date retrieved.

### BC MINFILE / BC Data Catalogue

- Access pattern: MINFILE website, daily MINFILE/pc download, and DataBC tables in SHP, XLS, CSV, KML, and WMS.
- Authentication: none identified for public downloads.
- v0.2 adapter: BC Data Catalogue search and MINFILE table-resource selection.
- v0.3 adapter: occurrence table download and normalization.
- Provenance: preserve MINFILE number, table source, update date, location confidence, and source URL.

### Ontario OGSEarth / OMI

- Access pattern: OGSEarth KML bookmarks and GeologyOntario record pages.
- Authentication: none identified for public KML records.
- v0.2 adapter: KML link catalog and OMI metadata extraction.
- v0.3 adapter: KML parsing into normalized occurrence records.
- Provenance: preserve OMI id, KML URL, source layer, update date, and record URL.

### USGS MRData / National Geochemical Database

- Access pattern: MRData web portal, OGC WMS/WFS/WMTS, APIs, and ArcGIS REST services.
- Authentication: none identified for public MRData services.
- v0.2 adapter: ArcGIS REST and WFS query builders plus FeatureSet parsing.
- v0.3 adapter: media-specific geochemical query wrappers.
- Provenance: preserve service URL, layer id, query parameters, spatial reference, and USGS public-domain status when present.

### EarthChem

- Access pattern: EarthChem Portal and EarthChem Library search.
- Authentication: public search appears available; some workflows may require portal-specific interaction or downloads.
- v0.2 adapter: source planner and manual-retrieval record model only.
- v0.3 adapter: implement API or export parsing only after a supported public interface is confirmed.
- Provenance: preserve repository, dataset id, IGSN when available, data type, release date, and citation.

## MCP Server Shape

The v0.2 implementation includes a plugin-root `.mcp.json`, the server entrypoint, deterministic tools, and adapter scaffolding:

```text
.mcp.json
scripts/geomine_mcp_server.py
scripts/geomine/tools.py
scripts/geomine/adapters/
tests/test_mcp_tools.py
tests/test_mcp_server_import.py
```

Server name:

```text
geomine
```

Enabled tools:

- `normalize_aoi`
- `search_canada_geodata`
- `search_cdogs_surveys`
- `search_bc_minfile`
- `search_ontario_omi`
- `search_saskatchewan_mineral_data`
- `fetch_dataset_metadata`
- `summarize_dataset_provenance`
- `query_claim_neighbors`
- `calculate_infrastructure_distance`

Each MCP tool should return:

- `data`: normalized structured result.
- `provenance`: source URL, adapter name, retrieval time, query parameters, cache status.
- `warnings`: limitations, partial results, unsupported source features.
- `next_steps`: recommended follow-up retrieval or validation.

## Cache And Provenance

- Cache raw responses separately from normalized records.
- Store cache entries under a user-specified cache directory, not inside the plugin by default.
- Cache key must include adapter name, adapter version, endpoint, normalized parameters, and response format.
- Each normalized record must retain a pointer to the raw source or cache id.
- Never collapse multiple sources into one record without preserving source lineage.

## Activation And Test Gates

- `.mcp.json` is present at the plugin root and referenced by `"mcpServers": "./.mcp.json"`.
- Validation checks plugin manifest, MCP config, required files, and enabled tool names.
- Unit tests for URL building and parsing pass without network.
- Fixture tests cover CKAN, ArcGIS REST FeatureSet, GeoJSON, KML, CSV, and HTML metadata where relevant.
- Optional integration tests are gated by `GEOMINE_RUN_LIVE_TESTS=1`.
- Live tests use small bounded queries and record source URLs.
- MCP stdio smoke tests confirm the server starts, exposes exactly ten tools, and can call sample tools.
- README documents how to run the MCP server and how to disable network access.

## Source Notes Reviewed

- OpenAI Codex plugin docs: `https://developers.openai.com/codex/plugins/build`
- OpenAI Codex MCP docs: `https://developers.openai.com/codex/mcp`
- NRCan CDoGS: `https://geochem.nrcan.gc.ca/cdogs/content/main/home_en.htm`
- NRCan GEO.ca overview: `https://natural-resources.canada.ca/science-and-data/data-and-analysis/geoca/25757`
- BC MINFILE Mineral Inventory: `https://www2.gov.bc.ca/gov/content/industry/mineral-exploration-mining/british-columbia-geological-survey/mineralinventory`
- BC Geological Survey Digital Geoscience Data: `https://www2.gov.bc.ca/gov/content/industry/mineral-exploration-mining/british-columbia-geological-survey/publications/digital-geoscience-data`
- Ontario OGSEarth: `https://www.geologyontario.mndm.gov.on.ca/ogsearth.html`
- USGS MRData: `https://www.usgs.gov/centers/geology-energy-and-minerals-science-center/science/mineral-resource-online-data-catalog`
- USGS National Geochemical Database: `https://www.usgs.gov/centers/gggsc/science/national-geochemical-database`
- EarthChem Library search: `https://ecl.earthchem.org/search.php`
