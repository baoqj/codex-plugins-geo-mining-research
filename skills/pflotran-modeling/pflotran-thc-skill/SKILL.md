---
name: pflotran-thc-skill
description: Design PFLOTRAN thermal-hydrologic-chemical coupling plans for geothermal groundwater, mine heat pollution, nuclear waste heat, deep fractured rock chemistry, and temperature-dependent reactions.
---

# PFLOTRAN THC Skill

## Purpose

Specify when and how temperature should be coupled to flow, transport, and chemistry in a PFLOTRAN Modeling Package.

## When To Use

Use for geothermal gradients, mine heat pollution, nuclear waste heat, deep fractured groundwater, thermal boundary conditions, and temperature-dependent mineral precipitation/dissolution.

## Required Inputs

Heat source, thermal boundary conditions, thermal conductivity/heat capacity, initial temperature field, flow/transport setup, temperature-sensitive reactions, and time horizon.

## Internal Workflow

1. Decide whether H, HC, TH, or THC is required.
2. Define heat sources and thermal boundaries.
3. Specify temperature-dependent chemistry assumptions and missing data.
4. Identify expected thermal, hydraulic, and chemical outputs.

## Output Contract

Return THC justification, heat-source plan, thermal boundaries, temperature-dependent chemistry plan, output variables, and uncertainty notes.

## Handoff Rules

Pass thermal blocks to input-deck and figure/output requirements to output-analysis.

## Limitations

Do not invent heat fluxes, thermal properties, or temperature-rate laws.
