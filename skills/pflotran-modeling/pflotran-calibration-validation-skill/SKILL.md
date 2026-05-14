---
name: pflotran-calibration-validation-skill
description: Design PFLOTRAN calibration, validation, benchmark, sensitivity, and uncertainty plans for hydraulic heads, flow rates, temperature, pH, ions, metals, breakthrough curves, minerals, and porosity/permeability evolution.
---

# PFLOTRAN Calibration And Validation Skill

## Purpose

Define what data and metrics are needed before a PFLOTRAN model can support scientific claims.

## When To Use

Use for calibration targets, validation datasets, benchmark selection, uncertainty/sensitivity design, or model credibility assessment.

## Required Inputs

Observed hydraulic heads, flow rates, concentrations, temperatures, mineral observations, porosity/permeability evidence, monitoring locations, time series, and parameter priors.

## Internal Workflow

1. Separate calibration and validation datasets.
2. Define metrics for heads, flow, temperature, pH, major ions, trace metals, breakthrough curves, mineral zones, and porosity/permeability.
3. Select benchmark checks and sensitivity parameters.
4. Identify missing observations that block validation.

## Output Contract

Return calibration table, validation table, benchmark plan, sensitivity/uncertainty plan, acceptance criteria, and residual risks.

## Handoff Rules

Pass credibility conclusions to paper-synthesis. Route missing field data to DGR/THMC data acquisition when relevant.

## Limitations

Do not invent calibration results or imply model validation without independent observations.
