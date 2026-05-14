---
name: geodata-discovery-skill
description: Recommend Canada-first public GIS, geology, geochemistry, geophysics, mineral occurrence, and report data sources without fabricating live retrieval.
---

# Geodata Discovery Skill

## Purpose

Map a normalized AOI and research question to relevant public geoscience and mining data sources. This skill recommends source candidates and retrieval steps; it does not claim live data retrieval unless a real tool is used.

## Inputs To Identify

- Jurisdiction: Canada, province, territory, or extension country.
- AOI and CRS status.
- Data types needed: geology, structure, geochemistry, geophysics, remote sensing, mineral occurrences, drilling, assessment reports, technical reports, tenure, environmental baseline.
- Commodity and deposit model.
- Required output format: source list, data checklist, GIS retrieval plan, provenance table.

## Procedure

1. Use `references/data-sources-canada.md` as the source catalog.
2. Prefer federal and provincial or territorial government data before secondary sources.
3. For Canada-wide geochemistry, include NRCan CDoGS where relevant.
4. For source discovery and metadata, include Geo.ca where relevant.
5. For British Columbia mineral occurrences, include BC MINFILE.
6. For Ontario GIS and occurrences, include OGSEarth and Ontario Mineral Inventory.
7. Add USGS and EarthChem only as extension sources or for cross-border comparison.
8. If helpful, use `scripts/geomine/data_sources.py` for static source filtering.
9. If the user asks for study-area maps, geological setting maps, sampling maps, claim maps, GIS figures, captions, or figure packages, route to `academic-figure-package-skill` after required CRS, source, scale, license, and spatial-precision metadata are identified.

## Output Contract

Return a Markdown source plan with:

- Source name.
- Jurisdiction.
- Relevant data type.
- Likely formats.
- Use case.
- Provenance and license notes.
- Known limitations.
- Recommended next retrieval step.
- Whether the source was actually queried in this run.
- Recommended map figures when the user is preparing a paper or report.

## Evidence And Provenance Rules

- Distinguish between catalog discovery, metadata review, and downloaded data.
- Preserve source URL, dataset title, release date, version, license, CRS, and scale or resolution when known.
- Prefer source-specific ids, such as MINFILE id, OMI id, map id, survey id, or report id.
- Mark unqueried sources as recommendations only.

## Guardrails And Limitations

- Do not fabricate API responses, map layers, sample counts, occurrence distances, or report contents.
- Do not treat a data catalog entry as evidence that the dataset supports a target.
- Do not rely on commercial or key-protected data sources in the MVP.
- Do not omit licensing and provenance caveats when recommending data.
