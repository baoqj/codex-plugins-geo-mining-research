---
name: aoi-crs-normalizer-skill
description: Normalize AOIs, coordinates, CRS assumptions, province or territory context, NTS sheets, and precision warnings for mining research.
---

# AOI CRS Normalizer Skill

## Purpose

Convert an area of interest into a structured research object without pretending to resolve boundaries, geocode names, or reproject coordinates unless a real tool has done so.

## Inputs To Identify

- AOI name, property name, claim block, project name, or target area.
- Coordinates, point, polygon, bounding box, shapefile path, GeoJSON, KML, or NTS sheet.
- Province or territory, country, and nearby administrative area.
- Input CRS and expected output CRS.
- Requested buffer, analysis scale, and coordinate precision.
- Source of the AOI geometry and date of the geometry.

## Procedure

1. Preserve the original AOI expression before normalization.
2. Identify whether the AOI is geometry-based, name-based, tenure-based, or map-sheet-based.
3. Record input CRS. If missing, warn that distance, area, and buffer calculations are unsafe.
4. Recommend an analysis CRS only at a planning level. For Canadian regional work, prefer a suitable projected CRS after confirming location.
5. Record province or territory. If a Canadian AOI lacks this field, flag it as a missing jurisdiction.
6. Record precision and scale limits, such as approximate point, bounding box, hand-drawn polygon, or claim name only.
7. If a local script is useful, call `scripts/geomine/aoi.py` to normalize simple dictionaries.

## Output Contract

Return:

- Original AOI input.
- Normalized AOI name.
- Country and province or territory.
- Geometry type and coordinates if supplied.
- Input CRS, analysis CRS recommendation, and output CRS.
- NTS sheet if supplied.
- Assumptions.
- Warnings.
- Next retrieval step for authoritative geometry.

## Evidence And Provenance Rules

- Keep the geometry source and date when known.
- Do not silently assume EPSG:4326. If coordinates appear to be longitude and latitude, state that it is an unverified assumption.
- Do not calculate area, buffer distance, or proximity unless CRS and geometry are confirmed.
- Separate tenure boundaries from exploration AOIs when both appear.

## Guardrails And Limitations

- Do not geocode a property name from memory.
- Do not infer claim boundaries from a company name or project name alone.
- Do not use approximate AOIs for precise land tenure, permitting, or Indigenous consultation conclusions.
- Do not treat a point occurrence as a property boundary.
