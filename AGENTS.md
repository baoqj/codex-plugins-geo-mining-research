# GeoMine Research Contributor Rules

- Do not fabricate data, citations, source ids, distances, sample counts, map layers, or live retrieval results.
- Do not claim live data retrieval unless a real tool or script fetched data during the current run.
- Do not provide legal advice, investment advice, Qualified Person opinions, feasibility conclusions, resource validation, reserve estimates, or permitting decisions.
- Do not convert historical resources into current mineral resources.
- Preserve CRS, data date, source id, scale or resolution, sample medium, analytical method, detection limits, QA/QC status, license, and uncertainty whenever known.
- Keep each skill focused on one job.
- Use `academic-paper-research-writer` for formal papers, journal articles, publication-ready drafts, hypotheses, theoretical frameworks, governing equations, and peer-review-style outputs.
- For academic-paper outputs, do not invent references, DOI values, datasets, experiments, sample counts, model results, assay values, or feasibility conclusions. Use citation placeholders and `requires further evidence` where needed.
- Use `academic-figure-package-skill` for manuscript figures, scientific diagrams, GIS maps, geochemical anomaly figures, visual abstracts, figure captions, drawing prompts, and publication figure packages. It plans and validates figure production; it does not promise final accepted artwork.
- Use `thmc-groundwater-router-skill` for THMC, groundwater chemistry modeling, reactive transport, radionuclide migration, acid mine drainage, tailings seepage, geothermal water-rock interaction, bentonite buffer evolution, and porosity-permeability feedback tasks. Keep v0.1 as skills-only planning; do not claim solver execution.
- Prefer deterministic scripts for schema validation, geochemical scoring, occurrence normalization, and report assembly.
- Keep the plugin manifest free of default MCP or skill auto-registration unless explicit installation behavior is requested and tested.
- Run `python scripts/validate_plugin.py` and `python -m pytest` before summarizing completion.
