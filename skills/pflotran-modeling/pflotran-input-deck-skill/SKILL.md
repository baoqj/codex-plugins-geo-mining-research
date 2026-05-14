---
name: pflotran-input-deck-skill
description: Generate PFLOTRAN input deck skeletons by assembling SIMULATION, SUBSURFACE, GRID, REGION, MATERIAL_PROPERTY, FLOW_CONDITION, TRANSPORT_CONDITION, CHEMISTRY, and OUTPUT blocks with explicit placeholders.
---

# PFLOTRAN Input Deck Skill

## Purpose

Build a draft PFLOTRAN `.in` input deck skeleton from the PFLOTRAN Modeling Package components.

## When To Use

Use after conceptual model, grid/material, flow/transport, and chemistry planning. Use the templates in `templates/` and keep placeholders when values are missing.

## Required Inputs

Process mode, grid plan, regions, materials, initial/boundary conditions, chemistry plan, output plan, run mode, and missing-data list.

## Internal Workflow

1. Select base template: subsurface flow, reactive transport, THC, chemistry, output, or full skeleton.
2. Assemble `SIMULATION`, `SUBSURFACE`, `GRID`, `REGION`, `MATERIAL_PROPERTY`, `FLOW_CONDITION`, `TRANSPORT_CONDITION`, `CHEMISTRY`, and `OUTPUT` blocks.
3. List every placeholder in a missing-data table.
4. Validate basic structure with run-management validation script or MCP planner if available.

## Output Contract

Return input deck skeleton, placeholder inventory, required database/files, warnings, and validation status.

## Handoff Rules

Pass generated deck to run-management for commands/manifests and to paper-synthesis for package assembly.

## Limitations

The skeleton is not a validated executable model. Do not claim it ran unless PFLOTRAN execution evidence exists.
