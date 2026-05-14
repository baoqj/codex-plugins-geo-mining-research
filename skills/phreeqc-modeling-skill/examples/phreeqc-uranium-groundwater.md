# Example: Uranium Groundwater Speciation And Saturation Screening

## Research Objective

Design a PHREEQC model to screen uranium-bearing groundwater for aqueous uranium speciation and saturation indices of carbonate, sulfate, Fe oxyhydroxide, and uranium phases.

## Model Type Classification

- `speciation`
- `saturation_index`
- Optional later extension: `surface_complexation` if measured Fe-oxide surface area/site density and compatible constants are supplied.

## Input Data Audit

Measured chemistry is required for pH, temperature, alkalinity, Ca, Mg, Na, K, Cl, sulfate, uranium, and redox handling. If pe/Eh is missing, keep `<pe_value>` and interpret uranium valence/speciation as redox-sensitive.

## Database Recommendation

Start by checking `llnl.dat` for uranium species and target minerals. Compare against `phreeqc.dat` for major-ion controls. Do not merge missing uranium reactions without documented thermodynamic sources.

## PHREEQC Keyword Plan

- `SOLUTION`: measured groundwater chemistry.
- `SELECTED_OUTPUT`: pH, pe, totals, saturation indices, molalities for uranium species.
- `EQUILIBRIUM_PHASES`: only for scenario tests with explicit phase amounts.

## Generated Input Fragment

```phreeqc
TITLE Uranium groundwater screening
SOLUTION 1 <sample_id>
  temp <temperature_C>
  units mg/L
  pH <pH_value>
  pe <pe_value>
  Alkalinity <alkalinity_value> as CaCO3
  Ca <Ca_value>
  Mg <Mg_value>
  Na <Na_value>
  K <K_value>
  Cl <Cl_value>
  S(6) <SO4_value> as SO4
  U <U_value>

SELECTED_OUTPUT 1
  -file uranium_groundwater.sel
  -reset false
  -pH true
  -pe true
  -temperature true
  -alkalinity true
  -ionic_strength true
  -charge_balance true
  -totals U Ca Mg Na K Cl S(6)
  -saturation_indices Calcite Gypsum Ferrihydrite Uraninite Schoepite

END
```

## Interpretation Plan

Interpret speciation and saturation indices as screening calculations only. Discuss database coverage, redox uncertainty, carbonate complexation sensitivity, and lack of adsorption/transport constraints.
