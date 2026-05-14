---
name: pflotran-output-analysis-skill
description: Plan PFLOTRAN output and observation analysis for breakthrough curves, spatial concentration/pH/temperature/mineral/porosity fields, mass balance, result summaries, and paper-ready figures.
---

# PFLOTRAN Output Analysis Skill

## Purpose

Design how PFLOTRAN outputs should be parsed, checked, summarized, and turned into scientific interpretation and figures.

## When To Use

Use when observation points, breakthrough curves, spatial field plots, mass balance, mineral volume, or porosity/permeability evolution outputs are needed.

## Required Inputs

Observation locations, output variables, output cadence, expected PFLOTRAN files, executed output if available, figure targets, and validation data.

## Internal Workflow

1. Define observation points and variables.
2. Specify breakthrough-curve and spatial-field outputs.
3. Design mass-balance and convergence checks.
4. Summarize executed observations only when real files are supplied.
5. Hand figure needs to Academic Figure Package when requested.

## Output Contract

Return observation design, output manifest, parsing plan, summary statistics plan, figure/table plan, and interpretation boundaries.

## Handoff Rules

Pass output design to input-deck, calibration-validation, figure package, and paper-synthesis skills.

## Limitations

Do not fabricate outputs, convergence, or breakthrough curves.
