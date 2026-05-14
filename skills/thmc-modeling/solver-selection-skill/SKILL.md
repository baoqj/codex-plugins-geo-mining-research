---
name: solver-selection-skill
description: Recommend solver and software routes for THMC Modeling Packages by comparing PHREEQC, Python + PHREEQC/PhreeqcRM, COMSOL + PHREEQC, OpenGeoSys + PHREEQC, PFLOTRAN, CrunchFlow/MIN3P, and PINN or PyTorch surrogate approaches.
---

# Solver Selection Skill

## Purpose

Choose a software route based on coupling level, geometry, reaction complexity, reproducibility, HPC needs, licensing constraints, user skill level, and future OpenMine cloud integration.

## Routes To Compare

- PHREEQC alone.
- Python + PHREEQC / PhreeqcRM.
- COMSOL + PHREEQC.
- OpenGeoSys + PHREEQC.
- PFLOTRAN.
- CrunchFlow / MIN3P.
- PINN / PyTorch surrogate.
- GeoMine MCP-Enhanced route: `geomine_thmc` for project data, PHREEQC drafts/mock runs, OGS/PFLOTRAN job lifecycle, model versions, and run records.

Read `references/solver-route-comparison.md` and route-specific notes when needed.

## Output Contract

Return:

- Recommended route.
- Fallback route.
- Not recommended routes and reasons.
- Implementation complexity.
- Required files.
- Required MCP tools, if using MCP-Enhanced Mode.
- Model-version and run-record strategy.
- Reproducibility and licensing notes.
- Next steps.
