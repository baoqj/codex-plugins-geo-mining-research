---
name: pflotran-paper-synthesis-skill
description: Assemble a PFLOTRAN Modeling Package with methods draft, results interpretation plan, limitations, expected figures/tables, and machine-readable model manifest for paper-ready GeoMine outputs.
---

# PFLOTRAN Paper Synthesis Skill

## Purpose

Assemble all PFLOTRAN sub-skill outputs into a publication-ready modeling package.

## When To Use

Use at the end of a PFLOTRAN workflow, especially when the user asks for a report, paper, modeling package, methods section, results plan, or manifest.

## Required Inputs

Router decision, conceptual model, grid/material plan, flow/transport plan, chemistry plan, THC/geomechanics scope if relevant, input deck skeleton, run manifest, output plan, calibration/validation plan, and limitations.

## Internal Workflow

1. Fill `templates/pflotran-modeling-package-template.md`.
2. Draft methods, results interpretation, and limitations.
3. Produce machine-readable manifest from the schema.
4. Preserve missing data and placeholders.
5. State whether the model is draft, executed, calibrated, or validated.

## Output Contract

Return the 26-section PFLOTRAN Modeling Package, methods draft, results interpretation plan, limitations, and JSON manifest.

## Handoff Rules

Use `geomine-paper-pdf-export-skill` after Markdown when PDF is requested. Use Academic Figure Package for final figures.

## Limitations

Do not claim validated results, safety, compliance, or engineering readiness without executed model output and validation evidence.
