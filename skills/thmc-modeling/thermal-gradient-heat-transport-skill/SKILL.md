---
name: thermal-gradient-heat-transport-skill
description: Design the thermal component of THMC groundwater chemistry models, including conduction, advective heat transport, geothermal gradient, waste heat, temperature-dependent fluid properties, reaction rates, equilibrium constants, diffusion, and thermal-mechanical coupling.
---

# Thermal Gradient Heat Transport Skill

## Purpose

Handle thermal processes and their coupling to H, M, and C.

## Workflow

1. Decide whether thermal coupling is required or optional.
2. Define conduction, advective heat transport, heat sources, and thermal boundary conditions.
3. Identify temperature effects on viscosity, density, diffusion, equilibrium constants, and reaction rates.
4. Identify thermal expansion or thermal stress if mechanics is active.
5. State assumptions and excluded thermal processes.

## Output Contract

Return:

- Thermal model choice.
- Thermal boundary and initial conditions.
- Required thermal parameters.
- Coupling effects on H, M, and C.
- Assumptions and limitations.

