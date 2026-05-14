---
name: governing-equations-skill
description: Select and explain governing equations, variables, parameters, coupling terms, assumptions, and boundary-condition needs for H, HC, THC, HM, THM, or THMC groundwater reactive transport models.
---

# Governing Equations Skill

## Purpose

Select the smallest defensible equation set for the chosen coupling level. Do not overcomplicate an HC problem by forcing full THMC equations.

## Equation Families

Read `references/thmc-equation-library.md` and `references/variable-parameter-glossary.md` as needed.

Include only active fields:

- Groundwater flow and Darcy law.
- Advection-dispersion-reaction transport.
- Heat transport.
- Mechanical equilibrium and effective stress.
- Chemical reaction source/sink terms.
- Porosity/permeability update terms when feedback is active.
- Temperature-dependent reaction and transport terms when thermal coupling is active.

## Output Contract

Return:

- Coupling level and active equation set.
- Equation table.
- Primary variables.
- Parameters and units.
- Coupling terms.
- Assumptions.
- Boundary-condition requirements.
- Notes on excluded equations.

