# Real Data Adapter And MCP Design

This document defines the engineering boundary for real GeoMine Research data access. v0.2 exposes deterministic MCP tools through the local `geomine` stdio server; future live adapters must still be added behind explicit network flags and fixture-backed tests.

## Design Principles

- Adapter outputs must be structured, provenance-preserving, and testable without network access.
- Network access is opt-in. Unit tests must use fixtures.
- Every adapter must distinguish `planned`, `queried`, `downloaded`, `parsed`, and `unsupported` states.
- Unsupported or unconfirmed public APIs should be represented as roadmap items, not fake live adapters.
- The MCP server should be a thin tool wrapper over the adapter layer, not a second implementation.

## Package Layout

```text
scripts/geomine/adapters/
  __init__.py
  base.py
  ckan.py
  arcgis.py
  source_registry.py
```

Future files:

```text
scripts/geomine/adapters/cdogs.py
scripts/geomine/adapters/bc_minfile.py
scripts/geomine/adapters/ogsearth.py
scripts/geomine/adapters/earthchem.py
```

The v0.2 implementation includes `scripts/geomine/tools.py`, `scripts/geomine_mcp_server.py`, and plugin-root `.mcp.json`. The exposed tools currently return deterministic planning/provenance records unless a bounded live adapter is implemented.

## Shared Adapter Contract

Each adapter should expose:

- `name`
- `version`
- deterministic request builders
- fixture-safe response parsers
- `source_note()` for limitations and provenance rules

Each result should include source, title, record id, URL, formats, license, jurisdiction, data type, retrieval status, query parameters, warnings, and resources.

## Adapter Classes

### `OpenCanadaCkanAdapter`

- Scope: Open Canada / Open Maps / Geo.ca-style catalogue discovery through CKAN search.
- Endpoint: `https://open.canada.ca/data/api/3/action/package_search`
- Core methods: `build_package_search_url(...)`, `parse_package_search(...)`.
- Known limitation: catalogue results may point to downstream WMS, WFS, ArcGIS REST, ZIP, CSV, or HTML resources that need separate adapters.

### `BcDataCatalogueAdapter`

- Scope: BC Data Catalogue search for MINFILE and BCGS resources.
- Endpoint: `https://catalogue.data.gov.bc.ca/api/3/action/package_search`
- Core methods: `build_package_search_url(...)`, `parse_package_search(...)`.
- Known limitation: BC catalogue records need resource selection and download handling before occurrence normalization.

### `ArcGisFeatureServiceAdapter`

- Scope: ArcGIS REST FeatureServer or MapServer query builders and FeatureSet parsing.
- Candidate use: USGS MRData, government map services, and future provincial endpoints.
- Core methods: `build_query_url(...)`, `parse_feature_set(...)`.
- Known limitation: service-specific layer ids and fields must be configured per source.

### Future `CdogsAdapter`

- Scope: NRCan CDoGS metadata, spreadsheet links, KML links, and WMS index layer.
- Early design: parse known survey metadata pages and table links.
- Do not parse analytical spreadsheets until sample-medium, units, and detection-limit handling are implemented.

### Future `OgsEarthAdapter`

- Scope: Ontario OGSEarth KML link discovery and OMI record extraction.
- Early design: maintain a KML link registry and parse KML features from fixtures.
- Do not claim live OMI search until endpoint and throttling behavior are verified.

### Future `EarthChemAdapter`

- Scope: EarthChem source planning and export parsing.
- Early design: represent manual search/export workflows with provenance.
- Do not automate broad EarthChem search until a supported public API or export workflow is confirmed.

## MCP Tool Mapping

- `normalize_aoi` -> local AOI normalizer.
- `search_canada_geodata` -> source registry plus future Open Canada / Geo.ca / BC Data Catalogue CKAN adapters.
- `search_cdogs_surveys` -> future CDoGS metadata and geochemical survey parsers.
- `search_bc_minfile` -> future BC Data Catalogue and MINFILE occurrence parser.
- `search_ontario_omi` -> future OGSEarth KML and OMI metadata parser.
- `search_saskatchewan_mineral_data` -> future Saskatchewan public mineral data adapters.
- `fetch_dataset_metadata` -> local source registry.
- `summarize_dataset_provenance` -> provenance-normalization helper.
- `query_claim_neighbors` -> future provincial tenure adapters.
- `calculate_infrastructure_distance` -> future infrastructure layer adapters and spatial calculators.

## Error Model

Adapters should return warnings rather than throwing for source-level gaps:

- unsupported format
- missing CRS
- missing license
- missing geometry
- API result partial or paginated
- downstream resource not yet parsed

Throw exceptions only for programmer errors such as invalid input types or malformed required configuration.

## Network Policy

The adapter package may include URL builders and parsers now. A future live client must:

- require explicit `allow_network=True`
- set a clear user agent
- enforce timeouts
- bound result counts
- cache raw responses
- expose source URLs and retrieval timestamps
- keep live integration tests behind `GEOMINE_RUN_LIVE_TESTS=1`

## MCP Activation Status

Completed in v0.2:

1. Implemented `scripts/geomine_mcp_server.py`.
2. Added pure tool wrappers and contract tests for every exposed MCP tool.
3. Added plugin-root `.mcp.json` and updated `.codex-plugin/plugin.json` with `"mcpServers": "./.mcp.json"`.
4. Updated README and `MCP_SETUP.md` with install, run, and network-disable instructions.
5. Confirmed `python3 scripts/validate_plugin.py`, MCP JSON parsing, pytest, and stdio smoke tests pass.

Future live-adapter activation still requires:

1. Fixture-backed parsers for each source-specific adapter.
2. Opt-in live integration tests behind `GEOMINE_RUN_LIVE_TESTS=1`.
3. Bounded HTTP clients with cache, timeout, user-agent, source URL, and retrieval timestamp.
4. Clear unsupported states where a source has no confirmed stable public API.
