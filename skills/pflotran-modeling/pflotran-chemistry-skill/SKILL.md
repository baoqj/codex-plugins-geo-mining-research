---
name: pflotran-chemistry-skill
description: Design PFLOTRAN chemistry configurations from PHREEQC prototypes, groundwater chemistry, mineralogy, and reaction-network concepts, including species, minerals, kinetics, sorption, ion exchange, AMD, uranium, and tailings patterns.
---

# PFLOTRAN Chemistry Skill

## Purpose

Translate groundwater chemistry and reaction-network ideas into a PFLOTRAN chemistry configuration plan.

## When To Use

Use for reactive transport, uranium/radionuclide mobility, acid mine drainage, tailings seepage, mineral dissolution/precipitation, sorption, ion exchange, or chemistry database planning.

## Required Inputs

Water chemistry, thermodynamic database candidate, primary/secondary species, minerals, kinetic reactions, sorption/exchange data, PHREEQC reaction prototype if available, and missing constants.

## Internal Workflow

1. Import PHREEQC prototype concepts when available.
2. Identify primary species, secondary species, minerals, gases, sorption/exchange reactions, and kinetic reactions.
3. Select database requirements and missing thermodynamic data.
4. Map scenario patterns for uranium, AMD, tailings, geothermal, or DGR chemistry.
5. Keep unknown constants as placeholders.

## Output Contract

Return chemistry block plan, database requirements, species/mineral list, reaction table, sorption/exchange table, missing constants, and interpretation limits.

## Handoff Rules

Pass chemistry plan to input-deck, output-analysis, calibration-validation, and paper-synthesis skills. Use PHREEQC skill for speciation/saturation-only work.

## Limitations

Do not invent thermodynamic constants, kinetic rates, mineral amounts, surface constants, or ion-exchange capacities.
