---
name: pflotran-conceptual-model-skill
description: Convert a GeoMine research question into a PFLOTRAN-ready conceptual model with source-pathway-receptor logic, active/excluded processes, regions, boundaries, observation points, and assumptions.
---

# PFLOTRAN Conceptual Model Skill

## Purpose

Translate a research problem into the conceptual structure needed before PFLOTRAN input design.

## When To Use

Use after PFLOTRAN routing, before grid/material, flow/transport, chemistry, or input deck generation.

## Required Inputs

Scenario, domain scale, source terms, receptors, hydrostratigraphy, flow regime, reactions, time horizon, observation goals, and known data gaps.

## Internal Workflow

1. Define source, pathway, receptor, domain, and time horizon.
2. Identify active flow, transport, reaction, thermal, and optional geomechanical processes.
3. Define model regions, reaction zones, boundary faces, initial condition zones, and observation points.
4. Mark excluded processes and why they are excluded.
5. Preserve placeholders for unknown field parameters.

## Output Contract

Return conceptual narrative, process map, source-pathway-receptor table, region list, observation list, assumptions, excluded processes, and missing inputs.

## Handoff Rules

Pass regions and active processes to grid/material, flow/transport, chemistry, THC, and input-deck skills.

## Limitations

Do not invent field parameters, boundary conditions, or calibrated process importance.
