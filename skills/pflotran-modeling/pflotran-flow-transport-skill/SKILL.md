---
name: pflotran-flow-transport-skill
description: Select PFLOTRAN flow and transport modes, initial and boundary conditions, source/sink terms, timestep controls, and breakthrough-curve design for saturated, variably saturated, advective, dispersive, and diffusion-dominated systems.
---

# PFLOTRAN Flow And Transport Skill

## Purpose

Design PFLOTRAN flow and transport configuration without fabricating boundary conditions or calibration.

## When To Use

Use for saturated groundwater flow, variably saturated flow, advection-dispersion, diffusion-dominated transport, source/sink terms, and breakthrough-curve simulations.

## Required Inputs

Flow regime, hydraulic head/pressure/saturation data, recharge/seepage rates, boundary faces, initial conditions, dispersivity, diffusion, simulation time, timestep controls, and observation points.

## Internal Workflow

1. Select saturated or variably saturated flow.
2. Define flow and transport initial conditions.
3. Define boundary condition types and data needs.
4. Specify timestep/output cadence and stability checks.
5. Link observation points to output-analysis skill.

## Output Contract

Return mode selection, boundary/initial condition table, source/sink plan, timestep plan, breakthrough-curve design, and missing inputs.

## Handoff Rules

Pass blocks to input-deck skill and validation targets to calibration-validation skill.

## Limitations

Do not invent hydraulic gradients, recharge, dispersivity, diffusion coefficients, or source fluxes.
