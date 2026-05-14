# PFLOTRAN Modeling Skill Family

PFLOTRAN Modeling is an independent GeoMine Research skill family for designing PFLOTRAN-based subsurface flow, transport, reactive transport, and thermal-hydrologic-chemical modeling packages.

Version `0.1` is skills-only. It does not execute PFLOTRAN and does not require MCP. It generates conceptual models, grid/material plans, input deck skeletons, run manifests, output-analysis plans, calibration/validation plans, paper-writing guidance, and future MCP extension specifications.

Relationship to other GeoMine skills:

- THMC Modeling defines the scientific coupling framework and solver-selection logic.
- PHREEQC Modeling prototypes aqueous chemistry, saturation indices, batch reactions, and reaction networks.
- PFLOTRAN Modeling implements solver-specific spatial reactive-transport package design after PFLOTRAN is justified.
- Academic Figure Package can turn PFLOTRAN output designs into publication figures.

Do not use PFLOTRAN for single-sample speciation or saturation-index-only work; route those to PHREEQC. Do not treat PFLOTRAN as a validated model without real input data, executed solver output, calibration, and professional review.

Future MCP extension may expose `geomine_pflotran` tools for input validation, local/remote run orchestration, PostGIS/R2 mesh and field access, output parsing, model-version storage, and run-record storage. MCP examples must remain disabled by default until explicitly installed.
