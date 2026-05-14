---
name: hydro-transport-skill
description: Design the hydrological flow and solute transport component of a THMC groundwater model, including saturated or unsaturated flow, fracture flow, advection, dispersion, diffusion, matrix diffusion, retardation, and hydraulic calibration targets.
---

# Hydro Transport Skill

## Purpose

Design the H component and its transport implications for THMC models.

## Workflow

1. Choose flow representation: saturated, variably saturated, dual continuum, discrete fracture network, or equivalent porous medium.
2. Choose transport representation: conservative, reactive, dual-porosity, matrix diffusion, or fracture-dominated.
3. Define advection, dispersion, molecular diffusion, retardation, and source/sink terms.
4. Define hydrological boundary and initial conditions.
5. List hydraulic parameter requirements.
6. Identify observation and calibration targets.

## Output Contract

Return:

- Flow model choice.
- Transport model choice.
- Required hydraulic parameters.
- Boundary and initial conditions.
- Observation/calibration targets.
- Common pitfalls and data gaps.

