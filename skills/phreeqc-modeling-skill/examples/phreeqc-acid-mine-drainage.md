# Example: Acid Mine Drainage Neutralization Scenario

## Research Objective

Design a PHREEQC workflow to evaluate acid mine drainage chemistry, metal mobility, and a controlled carbonate neutralization scenario.

## Model Type Classification

- `speciation`
- `saturation_index`
- `batch_reaction`
- Optional: `kinetic_reactions` only if sourced sulfide oxidation and neutralization rate laws are provided.

## Input Data Audit

Required measured fields include pH, temperature, sulfate, Fe, Al, Mn, Ca, Mg, Na, K, Cl, acidity/alkalinity, and trace metals. Missing oxygen flux, sulfide abundance, or kinetic constants prevents kinetic interpretation.

## Database Recommendation

Use `wateq4f.dat`, `minteq.dat`, or `llnl.dat` after checking Fe, Al, sulfate, and target metal species. Use `minteq.dat` if adsorption constants and surface model are central.

## PHREEQC Keyword Plan

- `SOLUTION`: acid drainage sample.
- `SELECTED_OUTPUT`: pH, acidity-related totals, metals, saturation indices.
- `REACTION`: scenario-based calcite or alkalinity addition.
- `EQUILIBRIUM_PHASES`: optional mineral controls if phase amounts are known or explicitly scenario placeholders.

## Generated Input Fragment

```phreeqc
TITLE Acid mine drainage neutralization draft
SOLUTION 1 <amd_sample_id>
  temp <temperature_C>
  units mg/L
  pH <pH_value>
  pe <pe_value>
  S(6) <SO4_value> as SO4
  Fe <Fe_value>
  Al <Al_value>
  Mn <Mn_value>
  Ca <Ca_value>
  Mg <Mg_value>
  Na <Na_value>
  K <K_value>
  Cl <Cl_value>

REACTION 1
  Calcite 1.0
  <calcite_addition_moles>

SELECTED_OUTPUT 1
  -file acid_mine_drainage.sel
  -reset false
  -pH true
  -pe true
  -ionic_strength true
  -charge_balance true
  -totals S(6) Fe Al Mn Ca Mg Na K Cl
  -saturation_indices Calcite Gypsum Ferrihydrite Goethite Schwertmannite Jarosite

END
```

## Interpretation Plan

Treat neutralization as a scenario, not a field prediction, unless flow, mineral abundance, reaction time, and calibration data exist.
