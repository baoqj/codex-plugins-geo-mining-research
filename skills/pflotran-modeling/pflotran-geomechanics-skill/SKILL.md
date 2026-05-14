---
name: pflotran-geomechanics-skill
description: Define the safe scope and limitations of geomechanics in PFLOTRAN-oriented models, including porosity/permeability feedback, Biot coupling notes, and when to route to OpenGeoSys or COMSOL for stronger THM/THMC mechanics.
---

# PFLOTRAN Geomechanics Scope Skill

## Purpose

Clarify what PFLOTRAN can and cannot represent for geomechanical feedback in the requested modeling workflow.

## When To Use

Use when the problem mentions deformation, stress, fracture aperture, Biot coupling, compaction, thermal expansion, damage, swelling, or porosity/permeability feedback.

## Required Inputs

Mechanical process, deformation scale, porosity/permeability feedback needs, stress/strain data, thermal expansion data, fracture properties, and solver alternatives.

## Internal Workflow

1. Separate chemical porosity/permeability feedback from full geomechanics.
2. Identify whether PFLOTRAN is adequate or whether OGS/COMSOL comparison is needed.
3. Document missing mechanical parameters and validation requirements.

## Output Contract

Return geomechanics scope note, supported feedbacks, excluded mechanics, solver-comparison trigger, and limitations.

## Handoff Rules

Hand full nonlinear mechanics to THMC solver-selection. Pass simple porosity/permeability feedback to grid/material and chemistry skills.

## Limitations

Do not overstate PFLOTRAN geomechanics capability or claim coupled mechanics without solver evidence.
