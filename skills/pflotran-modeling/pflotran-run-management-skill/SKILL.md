---
name: pflotran-run-management-skill
description: Generate PFLOTRAN local and MPI run commands, run manifests, expected output inventories, log-check instructions, and reproducibility records without requiring PFLOTRAN installation or claiming execution.
---

# PFLOTRAN Run Management Skill

## Purpose

Prepare reproducible run instructions and manifests for a draft PFLOTRAN input deck.

## When To Use

Use after an input deck skeleton exists or when the user asks for run commands, MPI command, manifest, output paths, or log checks.

## Required Inputs

Input deck path, model name, database file, output directory, MPI process count, expected outputs, solver version if known, and execution status.

## Internal Workflow

1. Validate deck structure locally without executing PFLOTRAN.
2. Generate local command: `pflotran -pflotranin model.in`.
3. Generate MPI command when requested: `mpirun -np N pflotran -pflotranin model.in`.
4. Build run manifest and expected output list.

## Output Contract

Return run commands, manifest JSON, validation warnings, expected outputs, and log-check checklist.

## Handoff Rules

Pass manifest to paper-synthesis and output-analysis. If MCP is available in future, hand run records to MCP storage tools.

## Limitations

Run commands are not execution evidence. Do not claim convergence or results without actual solver output.
