---
name: pflotran-grid-material-skill
description: Design PFLOTRAN grid, region, and material-property plans for tailings, aquifers, fractured rock, reaction barriers, thermal domains, and field-scale reactive transport scenarios.
---

# PFLOTRAN Grid And Material Skill

## Purpose

Specify model discretization, regions, and material properties in a PFLOTRAN-ready way.

## When To Use

Use when a PFLOTRAN package needs domain dimensions, structured grid first, material regions, porosity/permeability fields, or refinement logic.

## Required Inputs

Domain extent, dimension, coordinate system, hydrostratigraphy, region definitions, mesh/grid constraints, porosity, permeability, tortuosity, thermal properties, and known parameter fields.

## Internal Workflow

1. Prefer a structured grid unless the problem requires unstructured assets.
2. Define material regions such as tailings, vadose zone, aquifer, fracture zone, host rock, barrier, source zone, and receptor zone.
3. Assign material-property placeholders and provenance.
4. Note refinement around sources, fronts, boundaries, fractures, and observation points.

## Output Contract

Return grid plan, region plan, material property table, porosity/permeability assumptions, refinement notes, and missing parameter fields.

## Handoff Rules

Pass grid/material outputs to flow/transport, input-deck, run-management, and output-analysis skills.

## Limitations

Do not invent porosity/permeability fields, mineral volume fractions, or mesh quality.
