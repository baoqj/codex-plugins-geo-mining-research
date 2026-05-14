# Example: Tailings Seepage Mixing And Attenuation Hypothesis

## Research Objective

Design a PHREEQC model to compare tailings porewater, background groundwater, and a seepage-mixing scenario for pH buffering, sulfate transport, and metal attenuation hypotheses.

## Model Type Classification

- `speciation`
- `saturation_index`
- `batch_reaction`
- Optional: `inverse_modeling` if measured upgradient and downgradient waters plus candidate phases are available.
- Optional: `one_dimensional_transport` if hydraulic boundary conditions and plume geometry are provided.

## Input Data Audit

Require separate measured end-member waters, units, pH, temperature, alkalinity, major ions, sulfate, Fe/Al/Mn, metals, and mixing proportions. If mixing proportions are unknown, mark them as scenario placeholders.

## Database Recommendation

Use `wateq4f.dat` or `llnl.dat` for natural-water and metal speciation screening. Use `minteq.dat` only if surface complexation is explicitly modeled with documented constants.

## PHREEQC Keyword Plan

- `SOLUTION 1`: tailings porewater.
- `SOLUTION 2`: background groundwater.
- `MIX`: scenario mixing proportion.
- `SELECTED_OUTPUT`: water state, metals, sulfate, saturation indices.
- `INVERSE_MODELING`: optional when measured initial/final waters exist.

## Generated Input Fragment

```phreeqc
TITLE Tailings seepage mixing draft
SOLUTION 1 Tailings_porewater
  temp <tailings_temperature_C>
  units mg/L
  pH <tailings_pH>
  pe <tailings_pe>
  Alkalinity <tailings_alkalinity> as CaCO3
  S(6) <tailings_SO4> as SO4
  Fe <tailings_Fe>
  Al <tailings_Al>
  Mn <tailings_Mn>

SOLUTION 2 Background_groundwater
  temp <background_temperature_C>
  units mg/L
  pH <background_pH>
  pe <background_pe>
  Alkalinity <background_alkalinity> as CaCO3
  S(6) <background_SO4> as SO4

MIX 10 Seepage_scenario
  1 <tailings_fraction>
  2 <background_fraction>
SAVE solution 10

SELECTED_OUTPUT 1
  -file tailings_seepage.sel
  -reset false
  -pH true
  -pe true
  -alkalinity true
  -ionic_strength true
  -charge_balance true
  -totals S(6) Fe Al Mn Ca Mg Na K Cl
  -saturation_indices Calcite Dolomite Gypsum Ferrihydrite Goethite Jarosite

END
```

## Interpretation Plan

Treat attenuation as a hypothesis until field seepage flux, mineral abundance, adsorption capacity, and downgradient monitoring data are available.
