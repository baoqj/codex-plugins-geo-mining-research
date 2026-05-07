# Real Data Adapter And MCP Design

This document defines the engineering boundary for real GeoMine Research data access. The adapter layer comes first. MCP activation comes after adapters are stable enough to expose to Codex.

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

The v0.2 pre-activation implementation already includes `scripts/geomine/tools.py` and `scripts/geomine_mcp_server.py`. They remain unbundled until `.mcp.json` activation is tested.

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

- `search_geodata_sources` -> CKAN adapters and source registry.
- `fetch_geochem_metadata` -> CDoGS and USGS geochemical adapters.
- `search_mineral_occurrences` -> BC MINFILE, OMI, and USGS ArcGIS adapters.
- `resolve_aoi` -> local AOI normalizer.
- `retrieve_assessment_reports` -> future provincial report adapters.

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

## MCP Activation Checklist

Before adding `.mcp.json`:

1. Implement at least one complete adapter with live integration tests.
2. Implement `scripts/geomine_mcp_server.py`.
3. Add fixture and contract tests for every exposed tool.
4. Update `.codex-plugin/plugin.json` with `"mcpServers": "./.mcp.json"`.
5. Update README with install, run, and network-disable instructions.
6. Confirm `python3 scripts/validate_plugin.py` and `python3 -m pytest` pass.
