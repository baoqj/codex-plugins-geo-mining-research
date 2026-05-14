---
name: mechanical-damage-permeability-skill
description: Design the mechanical component and permeability feedback of THMC models, including stress, strain, displacement, effective stress, fracture aperture evolution, porosity/permeability updates, swelling, compaction, damage, mineral clogging, and conditions for excluding mechanics.
---

# Mechanical Damage Permeability Skill

## Purpose

Decide whether M is required and, if so, define the mechanical model and feedbacks to H and C.

## Workflow

1. Identify stress, deformation, swelling, compaction, subsidence, or fracture aperture needs.
2. Choose a mechanical model: excluded, effective stress only, elastic deformation, poromechanics, swelling, damage, or fracture-aperture evolution.
3. Define permeability and porosity update options.
4. Link mineral precipitation/dissolution to clogging or opening only when supported.
5. List mechanical parameters and measurements.

## Output Contract

Return:

- Mechanical model choice.
- Permeability evolution law options.
- Porosity update options.
- Required mechanical parameters.
- Coupling terms.
- Reason to include or exclude M.
- Limitations.

