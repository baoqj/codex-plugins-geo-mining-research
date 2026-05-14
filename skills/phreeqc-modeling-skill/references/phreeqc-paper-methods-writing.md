# PHREEQC Paper Methods Writing

Use precise language that separates model construction from executed results.

## Methods Structure

1. Study objective and modeled process.
2. Sample/data provenance, units, QA/QC, and preprocessing.
3. PHREEQC version, database, and activity model.
4. Keyword structure and rationale.
5. Boundary/initial conditions and assumptions.
6. Selected output variables.
7. Scenario, sensitivity, or inverse-model constraints.
8. Reproducibility statement with file names, checksums, and run command.

## Results Structure

- Report only executed model outputs.
- Label saturation indices, speciation fractions, reaction extents, inverse-model mass transfers, and transport breakthrough curves as calculated values.
- Connect each interpretation to the specific selected-output column or PHREEQC output section.

## Required Caveats

- Thermodynamic database coverage constrains interpretation.
- Redox disequilibrium may not be captured by a single pe/Eh value.
- Kinetic constants, surface complexation constants, exchange capacities, and mineral amounts must be measured or sourced.
- Inverse models are non-unique.
- Transport outputs require defensible boundary conditions and calibration.
