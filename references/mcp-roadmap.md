# GeoMine Research MCP Roadmap

This roadmap moves GeoMine Research from a skill-only v0.1 plugin to a v0.2 plugin with real data adapters and a later MCP server. Do not add `.mcp.json` or `mcpServers` to `.codex-plugin/plugin.json` until at least one MCP server is implemented, tested, and documented.

## Current State

- v0.1 packages skills, references, examples, validation, and deterministic helper scripts.
- v0.1 does not perform live retrieval.
- v0.1 does not declare MCP servers.
- v0.2 should introduce adapter modules that can build real requests, parse real responses, and preserve provenance.
- v0.2 may still defer MCP server activation until the adapter layer is stable.

## Official Codex Constraints

- Codex plugins use `.codex-plugin/plugin.json` as the required manifest.
- Plugin paths such as `skills`, `mcpServers`, and apps are relative to the plugin root.
- `.mcp.json` belongs at the plugin root, not inside `.codex-plugin/`.
- MCP servers can be local stdio processes or streamable HTTP servers.
- MCP configuration should be introduced only when the server can be started and tested.

## v0.2 Candidate Tools

### `search_geodata_sources`

- Purpose: search Canada-first geodata catalogues for AOI-relevant source records.
- Candidate adapters: Open Canada CKAN, BC Data Catalogue CKAN, Geo.ca/Open Maps records.
- Inputs: query, jurisdiction, data type, rows, optional AOI bounding box.
- Output schema: source name, catalogue id, title, description, formats, license, URL, provider, date, confidence, retrieval status.
- Cache key: normalized query, jurisdiction, data type, rows, source adapter version.
- Test strategy: fixture-based CKAN payloads and no network calls in unit tests.

### `fetch_geochem_metadata`

- Purpose: retrieve or parse geochemical survey metadata before analytical interpretation.
- Candidate adapters: NRCan CDoGS, USGS National Geochemical Database, provincial geochemical catalogues.
- Inputs: survey id or catalogue record URL, optional element list, jurisdiction.
- Output schema: survey id, medium, methods, elements, detection-limit notes, file links, KML or WMS links, provenance.
- Cache key: source id or source URL plus adapter version.
- Test strategy: saved HTML/JSON/CSV fixtures; live integration tests remain opt-in.

### `search_mineral_occurrences`

- Purpose: find mineral occurrence records around a confirmed AOI or by commodity/model query.
- Candidate adapters: BC MINFILE through DataBC tables, Ontario Mineral Inventory KML/GeologyOntario records, USGS MRData/USMIN as extension source.
- Inputs: jurisdiction, commodity, deposit model, AOI geometry or bbox, rows, source preference.
- Output schema: occurrence id, source, name, coordinates, CRS, commodity, status, deposit model, location confidence, source URL, update date.
- Cache key: jurisdiction, source, normalized AOI/bbox, commodity, model, rows.
- Test strategy: fixture-based CKAN, KML, GeoJSON, and ArcGIS REST FeatureSet payloads.

### `resolve_aoi`

- Purpose: normalize supplied AOI geometry and explicitly detect what is unresolved.
- Candidate adapters: none in early v0.2; use local normalization plus optional future geocoder.
- Inputs: name, province or territory, country, CRS, coordinates, bbox, polygon, NTS sheet.
- Output schema: normalized AOI, warnings, assumptions, source geometry status, analysis CRS recommendation.
- Test strategy: deterministic unit tests.

### `retrieve_assessment_reports`

- Purpose: plan or retrieve public assessment-report metadata and source documents.
- Candidate adapters: BC ARIS and Property File, Ontario Assessment File Database, provincial report systems.
- Inputs: jurisdiction, report id, project/property name, NTS, commodity, AOI.
- Output schema: report id, title, author, year, source, file URL, data package URL, confidentiality or access notes.
- Cache key: jurisdiction, report id or query fields.
- Test strategy: fixture-based metadata pages; file downloads remain opt-in.

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

When adapter tests are stable, introduce:

```text
.mcp.json
scripts/geomine_mcp_server.py
scripts/geomine/adapters/
tests/test_mcp_contract.py
```

Proposed server name:

```text
geomine-research
```

Proposed tools:

- `search_geodata_sources`
- `fetch_geochem_metadata`
- `search_mineral_occurrences`
- `resolve_aoi`
- `retrieve_assessment_reports`

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

## Test Gates Before Adding `.mcp.json`

- Unit tests for URL building and parsing pass without network.
- Fixture tests cover CKAN, ArcGIS REST FeatureSet, GeoJSON, KML, CSV, and HTML metadata where relevant.
- Optional integration tests are gated by `GEOMINE_RUN_LIVE_TESTS=1`.
- Live tests use small bounded queries and record source URLs.
- Validation script checks `.mcp.json` only after it is intentionally introduced.
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
