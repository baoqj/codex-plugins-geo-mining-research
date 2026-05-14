# Groundwater Chemistry Data Schema

Use this schema to audit tables before generating `SOLUTION` blocks.

## Recommended Columns

| Column | Required | Notes |
| --- | --- | --- |
| `sample_id` | yes | Unique sample identifier |
| `location_id` | recommended | Borehole, well, spring, seep, or station |
| `sample_date` | recommended | ISO date if available |
| `depth_m` | optional | Required for depth-dependent interpretation |
| `temperature_c` | recommended | PHREEQC `temp` |
| `pH` | recommended | Mark field/lab pH |
| `pe` or `Eh_mV` | optional | Redox handling must be explicit |
| `units` | recommended | `mg/L`, `mmol/kgw`, or other PHREEQC-compatible basis |
| `alkalinity` | recommended | Specify basis, such as as CaCO3 or as HCO3 |
| `density_kg_L` | optional | Needed for some concentration conversions |
| `charge_balance_percent` | optional | QA/QC indicator |
| `Ca`, `Mg`, `Na`, `K`, `Cl`, `S(6)` or `SO4`, `C(4)` or `HCO3` | recommended | Major ions |
| `Fe`, `Fe(2)`, `Fe(3)`, `Al`, `Mn`, trace metals | optional | Needed for AMD or metals work |
| `U`, `Ra`, `Rn`, `Pb`, `Po`, radionuclides | optional | Needed for radionuclide systems |
| `detection_limit_*` | optional | Important for censored data |
| `qa_qc_flag` | optional | Field/lab quality indicator |

## Missing Data Handling

Use placeholders in generated input and list the missing field. Examples:

- `<pH_field_or_lab>`
- `<temperature_C>`
- `<alkalinity_value_and_basis>`
- `<Eh_mV_or_pe>`
- `<U_concentration_and_units>`

Do not estimate missing concentrations unless the user explicitly provides a defensible conversion rule.
