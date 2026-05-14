---
name: thmc-report-synthesis-skill
description: Synthesize THMC skill-family outputs into a complete THMC Modeling Package with objective, scenario classification, conceptual model, coupling matrix, equations, reaction network, solver route, implementation plan, calibration and validation plan, uncertainty plan, figure plan, limitations, and JSON model spec.
---

# THMC Report Synthesis Skill

## Purpose

Assemble all THMC family outputs into the standard THMC Modeling Package. Use `templates/thmc-modeling-package-template.md` and validate the JSON model spec against `templates/thmc-model-spec-schema.json` when possible.

For THMC 2.0 MCP-Enhanced output, also use `../templates/thmc-modeling-package-2.0-template.md`, `../templates/thmc-model-spec.schema.json`, and `../templates/thmc-run-record.schema.json` when available.

## Required Sections

1. Research Objective
2. Scenario Classification
3. Conceptual THMC Model
4. THMC Coupling Matrix
5. Model Domain and Geometry
6. Primary Variables
7. Governing Equations
8. Boundary and Initial Conditions
9. Geochemical Reaction Network
10. Parameters and Data Requirements
11. DGR Field Data Acquisition and Data-Gap Matrix, when repository or现场实测数据 is relevant
12. Solver / Software Recommendation
13. PHREEQC Coupling Plan, when chemical is active
14. OGS / PFLOTRAN Remote-Run Plan, when remote compute is relevant
15. Model Version and Run Records, when MCP outputs or job specs are created
16. Implementation Plan
17. Calibration and Validation Plan
18. Sensitivity and Uncertainty Plan
19. Expected Outputs
20. Publication Figure Plan
21. Limitations and Assumptions
22. Machine-readable JSON Model Spec

## Caveats To Include

- Conceptual or planning output, not a validated numerical simulation.
- Not engineering certification.
- Not environmental legal advice.
- Not a substitute for laboratory or field calibration.
- Professional review required before regulatory or investment use.

## Output Contract

Return the full Markdown package plus a machine-readable JSON model spec. If the user asks for paper figures, delegate to `thmc-paper-figure-skill` or `academic-figure-package-skill`.

Preserve MCP provenance exactly: tool name, `mode`, query, result summary, asset ids, warnings, and errors. Do not turn a mock or cached MCP output into a live-data claim.

For `geomine_thmc_data` outputs, include campaign id, borehole ids, record ids, QA/QC flags, coverage matrix, calibration dataset asset ids, and data package ids. Separate measured, planned, mock, inferred, and missing records.
