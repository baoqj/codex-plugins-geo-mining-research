---
name: geomine-research-router-skill
description: Coordinate GeoMine research-router workflows by normalizing entities, planning evidence lanes, selecting skills and MCP tools, optionally using subagents, and synthesizing evidence-backed outputs.
---

# GeoMine Research Router Skill

## Primary Responsibility

Act as the coordinator for GeoMine Research. Understand the user's research question, normalize all domain entities, classify the research type, choose the smallest sufficient set of skills and MCP tools, optionally split independent evidence lanes into subagents, reconcile evidence, and produce a structured research output with caveats and provenance.

## Normalize Before Retrieval

Always normalize:

- AOI, coordinates, NTS sheet, claim block, and CRS.
- Commodity and pathfinder elements.
- Deposit model.
- Jurisdiction, including Canadian province or territory.
- Claim / tenure identifiers.
- Company, project, and comparable asset names.
- Dataset, source, license, CRS, scale, and update date.
- Technical report type, QP status, report date, and disclosure context.
- Evidence grade and confidence.

## Research Types

Classify the task into one or more types:

- `aoi_screening`
- `claim_due_diligence`
- `commodity_potential_review`
- `deposit_model_assessment`
- `geochemical_anomaly_interpretation`
- `geophysical_interpretation`
- `mineral_occurrence_context`
- `prospectivity_modeling`
- `technical_report_review`
- `ni43_101_disclosure_check`
- `mine_development_due_diligence`
- `permitting_risk_scoping`
- `environmental_baseline_review`
- `company_neighbor_intelligence`
- `work_program_design`
- `investment_memo_generation`
- `dataset_discovery`
- `literature_review`
- `academic_paper_generation`
- `geochemistry_paper_architecture`
- `figure_package_generation`
- `thmc_modeling`
- `phreeqc_modeling`
- `pflotran_modeling`
- `visualization_generation`
- `paper_pdf_export`

## Evidence Lane Planning

Plan only the lanes needed for the question:

- AOI / CRS / GIS.
- Geology and structural context.
- Geochemistry and QA/QC.
- Geophysics and remote sensing.
- Mineral occurrences and deposit model fit.
- Claims, tenure, infrastructure, and neighbor context.
- Development, environmental, and permitting context.
- Canadian NI 43-101 / CIM terminology and disclosure boundary.
- Company, technical report, and literature intelligence.
- Academic paper framing, hypotheses, mechanism, equations, evidence matrix, and peer-review checks.
- Geochemistry paper architecture: paper-type classification, scientific question, hypothesis design, data/method/QA/QC plan, figure/table architecture, citation discipline, and uncertainty controls.
- Academic figure package planning, paper diagrams, captions, visual grammar, and publication checks.
- THMC groundwater chemistry and reactive-transport modeling, including T/H/M/C process detection, coupling-level selection, reaction networks, solver route, validation, uncertainty, and Modeling Package synthesis.
- PHREEQC modeling, including groundwater chemistry data audit, database selection, keyword planning, input generation, selected-output design, run manifest, and paper methods/results guidance.
- PFLOTRAN modeling, including field-scale reactive transport, 2D/3D groundwater simulation, long-term spatial geochemical prediction, THC modeling, input deck skeletons, run manifests, output/observation plans, and solver-specific Modeling Package synthesis.
- 3D visualization, geologic evolution, GIS scene, and presentation-page output.
- Paper/report PDF export with math, physics, chemistry notation, units, and Chinese typography.

## MCP Usage

Use the `geomine` MCP server for data access and deterministic operations. MCP tools provide source discovery, normalization, and provenance; skills provide interpretation and synthesis.

Available MCP tools:

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

If the `geomine` MCP server is unavailable, say that MCP data tools are unavailable and continue only with repository-local references or user-provided files. Do not invent dataset availability, coordinates, sample counts, assay values, map scales, update dates, claim status, or infrastructure distances.

## Visualization Output

When the user asks for a 3D scene, animation, GIS demo page, geologic evolution page, or visual presentation, route to `geomine-visualization-studio-skill`. Treat generated geometry as conceptual unless authoritative coordinates, CRS, scale, and source provenance are supplied. The visualization skill can generate a standalone Vite/React/Three.js project from a GeoMine SceneSpec and should run build/browser verification when feasible.

## Academic Paper Output

When the user asks for a paper, academic paper, journal article, publication-ready draft, 投稿, 论文, 学术论文, literature-grounded mechanism paper, governing equations, hypotheses, theoretical framework, or peer-review-ready output, route to `academic-paper-research-writer`. Use domain skills and MCP evidence lanes before final writing. The academic-paper skill must produce a paper plan, evidence matrix, equation registry when equations are used, limitations, references or citation placeholders, and a peer-review check. Do not fabricate DOI values, datasets, experiments, sample counts, assay values, or model results.

For geochemistry-specific papers, first route to `academic-geochemistry-paper-architect`. This includes whole-rock, soil, sediment, groundwater, isotope, petrogenesis, environmental, nuclear/radiolysis, mineral exploration, geochemical database, geochemical modeling, review, perspective, and methods papers. The architect must classify the paper type, choose the writing mode, define research questions/hypotheses, plan data/method/QA/QC needs, design figures/tables, and set citation, uncertainty, and conclusion-boundary rules before drafting begins.

## Figure Package integration

Use `academic-figure-package-skill` when:

- The user asks for paper figures, academic diagrams, scientific illustrations, visual abstracts, figure plans, or publication-ready figure packages.
- The user provides a paper abstract, report outline, research proposal, or GeoMine evidence synthesis and asks how to visualize it.
- The output should include study area maps, geochemical anomaly maps, conceptual migration diagrams, GIS figures, workflow diagrams, or multi-panel journal figures.
- The user asks for a manuscript-ready figure list, figure captions, or figure design prompts.

Do not use the figure skill for simple factual Q&A unless the user asks for visualization.

## THMC Modeling Integration

Use `skills/thmc-modeling/thmc-groundwater-router-skill` when the user asks about THMC, thermo-hydro-mechanical-chemical modeling, groundwater chemistry model, reactive transport, water-rock reaction, radionuclide migration, uranium series migration, U-Ra-Rn-Po-Pb, acid mine drainage, tailings seepage, bentonite buffer, nuclear waste repository, geothermal groundwater, heat pollution, porosity-permeability evolution, fracture aperture, stress-dependent permeability, PHREEQC, COMSOL, OpenGeoSys, PFLOTRAN, PhreeqcRM, or PINN surrogate modeling.

When triggered:

1. Classify the THMC scenario.
2. Identify active T/H/M/C processes.
3. Select coupling level `H`, `HC`, `THC`, `HM`, `THM`, or `THMC`.
4. Delegate to `thmc-groundwater-router-skill`.
5. Request a complete THMC Modeling Package.
6. If the user also asks for paper figures, use `thmc-paper-figure-skill` or `academic-figure-package-skill`.

Do not require MCP. If MCP is unavailable, continue in skills-only Core Mode.

## PHREEQC Modeling Integration

Use `phreeqc-modeling-skill` directly when the user asks specifically for PHREEQC, speciation, saturation indices, PHREEQC input files, selected output parsing, inverse modeling, groundwater chemistry modeling, water-rock reaction, acid mine drainage geochemical calculations, uranium/radionuclide aqueous speciation, tailings seepage chemistry, or a PhreeqcRM coupling plan.

If the request also includes THMC coupling, transport solvers, repository mechanics, heat, stress, or flow-field feedback, call `thmc-groundwater-router-skill` first and let it route to `phreeqc-modeling-skill` as a downstream chemistry modeler.

PHREEQC tasks must not invent measured concentrations, kinetic constants, surface complexation constants, thermodynamic data, mineral amounts, calibration results, or field boundary conditions.

## PFLOTRAN Modeling Integration

Route to `skills/pflotran-modeling/pflotran-router-skill` when the user asks for PFLOTRAN, field-scale reactive transport, 2D/3D groundwater simulation, long-term spatial geochemical prediction, THC modeling, high-performance subsurface simulation, mineral reactions that alter porosity/permeability, spatial concentration/pH/mineral/porosity fields, breakthrough curves, or PFLOTRAN input deck generation.

If the user only asks for aqueous speciation, saturation indices, or batch reaction for water samples, route to `phreeqc-modeling-skill` instead.

If the user asks for conceptual thermal-hydrological-mechanical-chemical coupling without choosing a solver, route to `thmc-groundwater-router-skill` first, then recommend PFLOTRAN only if solver selection justifies it.

PFLOTRAN Modeling is independent and not a child skill under THMC Modeling. It may receive THMC conceptual outputs and PHREEQC reaction prototypes, then produce a solver-specific PFLOTRAN Modeling Package.

## Paper PDF Output

When the user asks for a paper, research report, Markdown-to-PDF export, formula rendering, or publication-style PDF, route to `geomine-paper-pdf-export-skill` after Markdown synthesis. For academic papers, run `academic-paper-research-writer` first, then export the finished Markdown to PDF. Keep the Markdown source, then export a PDF that normalizes fenced math, inline math, formula-like code spans, and common scientific variables/units such as `rho_w`, `dot{D}_w`, `S_i^{rad}`, and `mol m^{-3} s^{-1}`.

## Subagent Policy

Recommend subagents only when evidence lanes are independent. Good parallel lanes include geology, geochemistry, occurrences/deposit model, claim/infrastructure, company/report intelligence, and compliance. Do not use subagents for a single source lookup or a tightly dependent chain where one result determines the next input.

## Output Contract

Return:

1. Executive Summary.
2. Normalized Entities.
3. Research Type and Evidence Lanes.
4. Evidence Matrix.
5. Key Findings by Lane.
6. Conflicting Evidence.
7. Data Gaps.
8. Confidence and Evidence Strength.
9. Recommended Next Work Program.
10. Compliance and Disclosure Caveats.
11. Sources and Provenance.
12. Machine-readable JSON Summary.

## Guardrails

- This is not legal advice, investment advice, a Qualified Person opinion, a feasibility study, a reserve estimate, or a permitting decision.
- Do not convert historical resources to current resources.
- Do not infer economic mineralization from geochemical or occurrence proximity alone.
- Preserve source provenance and uncertainty for every material claim.
