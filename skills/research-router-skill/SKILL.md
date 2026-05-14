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
- Academic-output needs: literature review, hypotheses, theoretical framework, governing equations, equation registry, peer-review check, or publication-style paper.
- Geochemistry paper-architecture needs: geochemistry manuscript, hydrogeochemistry paper, exploration geochemistry article, isotope/petrogenesis paper, environmental geochemistry paper, radiolysis/nuclear geochemistry paper, geochemical database paper, methods paper, or a request to classify the paper type before writing.
- THMC modeling needs: groundwater chemistry, reactive transport, water-rock reactions, radionuclide migration, acid mine drainage, tailings seepage, thermal gradient, fracture flow, porosity-permeability feedback, PHREEQC, OpenGeoSys, PFLOTRAN, COMSOL, or PINN surrogate.
- PHREEQC modeling needs: speciation, saturation index, PHREEQC input, selected output, database selection, inverse modeling, surface complexation, ion exchange, gas phase, batch reaction, or PhreeqcRM coupling plan.
- PFLOTRAN modeling needs: PFLOTRAN input deck, field-scale reactive transport, 2D/3D groundwater simulation, long-term spatial geochemical prediction, THC simulation, HPC subsurface simulation, spatial output fields, or breakthrough curves.
- Deliverable needs: Markdown report, academic paper, academic figure package, figure captions, figure design prompts, PDF export, math rendering, chemistry notation, units, Chinese typography, or visualization.
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
   - Academic paper framing, mechanism, equations, and peer-review checks
   - Geochemistry academic paper architecture, including paper-type classification, hypotheses, data/method requirements, figure/table design, and section-level writing controls
   - Academic figure package planning, visual grammar, captions, and publication checks
   - THMC groundwater chemistry modeling and reactive-transport package generation
   - Paper or report PDF export with math/chemistry/unit rendering
   - Report synthesis
4. Select the smallest useful skill set:
   - AOI screening: `aoi-crs-normalizer-skill`, `geodata-discovery-skill`, `mineral-occurrence-skill`, `deposit-model-skill`, `report-synthesis-skill`.
   - Geochemical interpretation: `geochemical-survey-skill`, `deposit-model-skill`, `report-synthesis-skill`.
   - Mineral occurrence review: `mineral-occurrence-skill`, `deposit-model-skill`, `report-synthesis-skill`.
   - Disclosure or technical-report wording review: `ni43-101-disclosure-check-skill`, `report-synthesis-skill`.
   - Geochemistry academic paper architecture: `academic-geochemistry-paper-architect`, then relevant domain/modeling/figure skills, then `academic-paper-research-writer`.
   - Academic paper or literature-grounded mechanism study: if geochemistry-specific, start with `academic-geochemistry-paper-architect`; otherwise use `academic-paper-research-writer`, relevant domain skills, then `report-synthesis-skill`.
   - Academic figure package, manuscript figures, figure captions, or visual abstract: `academic-figure-package-skill`, relevant domain skills, then `report-synthesis-skill` if a written report is also needed.
   - Standalone PHREEQC, groundwater chemistry tables, speciation, saturation indices, inverse modeling, selected output, or PhreeqcRM plan: `phreeqc-modeling-skill`, then `report-synthesis-skill` if broader GeoMine synthesis is needed.
   - Standalone PFLOTRAN, field-scale reactive transport, 2D/3D groundwater simulation, long-term spatial geochemical prediction, THC simulation, or input deck generation: `pflotran-router-skill`, relevant `pflotran-modeling` family skills, then `pflotran-paper-synthesis-skill`.
   - THMC groundwater chemistry, reactive transport, radionuclide migration, acid mine drainage, tailings seepage, geothermal, bentonite buffer, or porosity-permeability feedback modeling: `thmc-groundwater-router-skill`, relevant THMC family skills, then `thmc-report-synthesis-skill`.
   - Paper/report PDF or formula-heavy deliverable: write Markdown first, then `geomine-paper-pdf-export-skill`.
   - Academic paper PDF: `academic-paper-research-writer`, `report-synthesis-skill`, then `geomine-paper-pdf-export-skill`.
5. Recommend subagents only when the user explicitly asks for subagents or the task has independent evidence lanes that can be analyzed separately.
6. If live data has not actually been queried, say that the output is a source plan or evidence framework, not a live data retrieval result.
7. Hand final assembly to `report-synthesis-skill` or use its output contract.
8. If the user requests a formal academic paper, or the task clearly asks for hypotheses, mechanisms, equations, literature positioning, peer-review-style output, or publication-ready form, do not stop at a generic research brief. Produce the academic-paper structure required by `academic-paper-research-writer`.
9. If the user requests PDF, paper output, report PDF, formula rendering, or Markdown-to-PDF export, keep the Markdown as source of truth and run `geomine-paper-pdf-export-skill` after the Markdown is complete.

## Figure Package integration

Use `academic-figure-package-skill` when the user asks for paper figures, scientific diagrams, visual abstracts, figure plans, manuscript-ready captions, drawing prompts, study-area maps, geochemical anomaly maps, conceptual migration diagrams, GIS figures, workflow diagrams, or multi-panel journal figures. Do not use it for simple factual Q&A unless visualization is requested.

## Geochemistry Paper Architecture Integration

Use `academic-geochemistry-paper-architect` before final drafting when the user asks for a geochemistry, hydrogeochemistry, isotope geochemistry, petrogenesis, environmental geochemistry, nuclear/radiolysis geochemistry, mineral exploration geochemistry, geochemical database, geochemical modeling, review, perspective, or methods paper.

The architect must classify the paper type, define scientific questions and hypotheses, plan data/method/QA/QC needs, design figures and tables, define citation and uncertainty controls, and then route to `academic-paper-research-writer` for drafting. If the paper requires PHREEQC, THMC, PFLOTRAN, GIS, or figure work, call the relevant skill before or alongside drafting.

## THMC Modeling Integration

Use `thmc-groundwater-router-skill` for groundwater chemistry models, reactive transport, THMC, THC, HMC, radionuclide migration, uranium-series migration, U-Ra-Rn-Po-Pb, acid mine drainage, tailings seepage, bentonite buffer, nuclear waste repository, geothermal groundwater, heat pollution, porosity/permeability evolution, fracture aperture, stress-dependent permeability, PHREEQC, COMSOL, OpenGeoSys, PFLOTRAN, PhreeqcRM, or PINN surrogate tasks. Request a complete THMC Modeling Package and continue in skills-only Core Mode when MCP is unavailable.

## PHREEQC Modeling Integration

Use `phreeqc-modeling-skill` directly for standalone PHREEQC tasks, groundwater chemistry tables, speciation, saturation indices, water-rock reactions, mineral equilibrium, inverse modeling, surface complexation, ion exchange, gas phase, one-dimensional PHREEQC transport, PHREEQC selected output, or paper-ready PHREEQC methods text.

If PHREEQC is only one part of a coupled THMC problem, route first to `thmc-groundwater-router-skill` and require the PHREEQC Modeling Package as a nested chemistry-modeling output.

## PFLOTRAN Modeling Integration

Use the independent `pflotran-modeling` family for PFLOTRAN-specific solver implementation packages: field-scale reactive transport, 2D/3D flow and chemistry, long-term spatial prediction, THC simulation, HPC-oriented simulation, spatial fields, breakthrough curves, and input deck skeletons.

Do not route single-sample speciation, saturation-index-only, or batch-reaction-only questions to PFLOTRAN; use `phreeqc-modeling-skill`.

If PFLOTRAN is selected after THMC solver comparison, hand off from THMC to `pflotran-router-skill` and preserve PFLOTRAN as an independent family.

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
