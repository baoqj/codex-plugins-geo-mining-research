---
name: reactive-transport-implementation-skill
description: Convert conceptual THMC groundwater models into solver-agnostic implementation plans, model input manifests, mesh/discretization requirements, parameter files, chemistry database needs, solver-specific file structures, and reproducibility checklists without executing solvers.
---

# Reactive Transport Implementation Skill

## Purpose

Transform conceptual model outputs into an implementation plan. Do not execute numerical solvers in v0.1.

## Supported Plans

- PHREEQC prototype.
- Python + PHREEQC parameter scan.
- COMSOL-PHREEQC setup plan.
- OpenGeoSys-PHREEQC project plan.
- PFLOTRAN input structure plan.
- PINN surrogate plan.

## Output Contract

Return:

- Implementation phases.
- Model input manifest.
- Mesh or discretization requirements.
- Parameter files and table structure.
- Chemistry database requirements.
- Solver-specific file structure.
- Reproducibility checklist.

