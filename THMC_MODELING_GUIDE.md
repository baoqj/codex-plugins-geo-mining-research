# GeoMine THMC Modeling Guide

## Core Idea

THMC Modeling converts a groundwater or reactive-transport research problem into a reproducible modeling package. The package should describe the conceptual model, active T/H/M/C processes, governing equations, reaction network, data requirements, solver route, validation plan, uncertainty plan, figures, model spec, and run records.

## Mode Selection

- Core Mode: skills-only, no MCP required.
- MCP-Enhanced Mode: use `geomine_thmc` for structured data, PHREEQC drafts/mock jobs, OGS/PFLOTRAN job lifecycle, model versions, and run records.
- DGR Data Acquisition Mode: use `geomine_thmc_data` for field-data campaign design, borehole records, T/H/M/C measurements, data-gap validation, calibration datasets, and DGR data packages.

## Minimum Package

1. Research objective.
2. Scenario classification and coupling level.
3. MCP status table, if applicable.
4. Conceptual THMC model.
5. Coupling matrix.
6. Domain, mesh, and parameter fields.
7. Governing equations.
8. Boundary and initial conditions.
9. Reaction network.
10. Solver recommendation.
11. DGR field-data acquisition and data-gap matrix, if repository or现场实测数据 is relevant.
12. PHREEQC and remote-compute plan, if applicable.
13. Calibration, validation, sensitivity, uncertainty.
14. Model version, DGR data package, run records, warnings.
15. Machine-readable JSON model spec.

## Scientific Boundary

The workflow produces research and model-design artifacts. It is not a validated simulation, engineering certification, environmental compliance decision, NI 43-101 technical conclusion, or investment recommendation.
