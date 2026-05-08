---
name: research-router-skill
description: Route broad GIS, geochemistry, mineral exploration, mine development, and Canadian disclosure research tasks to the smallest useful skill set.
---

# Research Router Skill

## Purpose

Use this as the default entrypoint for broad or ambiguous GeoMine Research tasks. Interpret the user question, normalize geoscience and mining entities, choose the smallest useful set of skills, and require final synthesis with evidence, uncertainty, and limitations.

## Inputs To Identify

- Research question and intended output format.
- AOI, coordinates, polygon, claim block, property name, NTS sheet, province or territory.
- Input CRS, analysis CRS, output CRS, buffer assumptions, and coordinate precision.
- Commodity, deposit model, project stage, project or property name.
- Jurisdiction, including federal, provincial or territorial, Indigenous, and municipal context when relevant.
- Evidence lanes: GIS, geology, structure, geochemistry, geophysics, remote sensing, mineral occurrences, technical reports, development context, NI 43-101 or CIM disclosure.
- Source provenance needs: source name, date, version, scale or resolution, CRS, license, QA/QC status, and uncertainty.

## Procedure

1. Restate the interpreted research question in one sentence.
2. Normalize the main entities before analysis: AOI, CRS, jurisdiction, commodity, deposit model, project name, data source, and evidence type.
3. Classify the task into lanes:
   - AOI / GIS / CRS
   - Geology and structure
   - Geochemistry and QA/QC
   - Mineral occurrences
   - Deposit model fit
   - Development context
   - NI 43-101 / CIM disclosure boundary
   - Report synthesis
4. Select the smallest useful skill set:
   - AOI screening: `aoi-crs-normalizer-skill`, `geodata-discovery-skill`, `mineral-occurrence-skill`, `deposit-model-skill`, `report-synthesis-skill`.
   - Geochemical interpretation: `geochemical-survey-skill`, `deposit-model-skill`, `report-synthesis-skill`.
   - Mineral occurrence review: `mineral-occurrence-skill`, `deposit-model-skill`, `report-synthesis-skill`.
   - Disclosure or technical-report wording review: `ni43-101-disclosure-check-skill`, `report-synthesis-skill`.
5. Recommend subagents only when the user explicitly asks for subagents or the task has independent evidence lanes that can be analyzed separately.
6. If live data has not actually been queried, say that the output is a source plan or evidence framework, not a live data retrieval result.
7. Hand final assembly to `report-synthesis-skill` or use its output contract.

## MCP Usage

When the user asks for live, external, or authoritative geoscience data, use the `geomine` MCP server when available.

Use MCP tools for:

- AOI normalization: `normalize_aoi`.
- Canadian public geodata discovery: `search_canada_geodata`.
- CDoGS geochemical survey lookup: `search_cdogs_surveys`.
- BC MINFILE occurrence lookup: `search_bc_minfile`.
- Ontario OMI / OGSEarth lookup: `search_ontario_omi`.
- Saskatchewan public mineral data lookup: `search_saskatchewan_mineral_data`.
- Dataset metadata and provenance: `fetch_dataset_metadata`, `summarize_dataset_provenance`.
- Claim-neighbor scans: `query_claim_neighbors`.
- Infrastructure distance planning: `calculate_infrastructure_distance`.

MCP tools provide data access and deterministic operations. This skill remains responsible for geological interpretation, evidence grading, conflict handling, caveats, and synthesis.

If the `geomine` MCP server is unavailable, report the missing MCP dependency and continue only with repository-local references or user-provided files.

## Output Contract

Return Markdown with:

- Interpreted research question.
- Normalized entities.
- Selected skill set and reason for each skill.
- Evidence by lane.
- Key findings with confidence.
- Conflicts and limitations.
- Recommended next analyses or work program.
- Source list and data provenance table.
- Compliance boundary note where the task touches Canadian technical disclosure, project economics, resources, reserves, permitting, or Indigenous consultation.

## Evidence And Provenance Rules

- Prefer government geological survey data, peer-reviewed papers, signed technical reports, and QP-supported materials for major findings.
- Preserve source name, release date, dataset version, CRS, scale or resolution, license, sample medium, analytical method, detection limits, and QA/QC status when known.
- Mark inferred or model-derived findings as hypotheses.
- Separate data-source recommendations from fetched evidence.
- State unknowns directly instead of filling gaps with plausible assumptions.

## Guardrails And Limitations

- Do not provide legal advice, investment advice, a Qualified Person opinion, a feasibility conclusion, a reserve estimate, or a permitting decision.
- Do not convert historical resources into current mineral resources.
- Do not claim a target has economic value from geochemical or spatial evidence alone.
- Do not say live data was fetched unless an actual tool or script retrieved it in the current run.
- Do not overuse skills. Route to the minimum set needed for the question.
