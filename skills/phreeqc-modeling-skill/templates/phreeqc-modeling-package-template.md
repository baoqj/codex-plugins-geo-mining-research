# PHREEQC Modeling Package

## 1. Research Objective

- Question:
- Study system:
- Intended use:
- Output status: draft model / executed model / interpretation plan

## 2. Model Type Classification

- Selected model type(s):
- Why this type is sufficient:
- Excluded model types and reason:

## 3. Input Data Audit

| Data class | Provided fields | Missing fields | Effect on interpretation |
| --- | --- | --- | --- |
| Water chemistry |  |  |  |
| Field parameters |  |  |  |
| Lithology/mineralogy |  |  |  |
| Surfaces/exchange sites |  |  |  |
| Kinetics |  |  |  |
| Transport/boundaries |  |  |  |

Measured data:

- 

Assumptions/placeholders:

- 

## 4. Database Recommendation

- Recommended database:
- Reason:
- Missing species/phases/constants:
- Alternative database:

## 5. PHREEQC Keyword Plan

| Keyword | Included? | Data source | Rationale | Limitation |
| --- | --- | --- | --- | --- |
| `SOLUTION` | yes |  |  |  |
| `SELECTED_OUTPUT` | yes |  |  |  |
| `EQUILIBRIUM_PHASES` |  |  |  |  |
| `KINETICS` / `RATES` |  |  |  |  |
| `SURFACE` |  |  |  |  |
| `EXCHANGE` |  |  |  |  |
| `GAS_PHASE` |  |  |  |  |
| `TRANSPORT` |  |  |  |  |
| `INVERSE_MODELING` |  |  |  |  |

## 6. Generated Input

```phreeqc
TITLE <model_title>

# Insert generated PHREEQC input here.

END
```

## 7. Run Instructions

```bash
phreeqc input.phr output.out database.dat
```

- PHREEQC executable:
- Database path:
- Input file:
- Output file:
- Selected output file:
- Run manifest:

## 8. Selected Output Design

| Output group | Variables/minerals/species | Purpose |
| --- | --- | --- |
| Core water state | pH, pe, temperature, ionic strength, charge balance |  |
| Totals |  |  |
| Saturation indices |  |  |
| Molalities/activities |  |  |
| Custom `USER_PUNCH` |  |  |

## 9. Interpretation Plan

- Speciation interpretation:
- Saturation-index interpretation:
- Reaction-path interpretation:
- Transport/inverse-model interpretation:
- Figures/tables:
- Checks against observations:

## 10. Paper Methods Draft

Use this paragraph as a starting point and replace placeholders before publication:

> PHREEQC calculations were designed to evaluate <research_objective>. Input waters were derived from <data_source> and screened for units, field parameters, and charge-balance constraints. The model used <database_name> because <database_reason>. The PHREEQC input included <keyword_list>. Selected outputs included <selected_output_list>. Missing data were retained as explicit placeholders and the resulting calculations should be interpreted as <draft_or_executed_status>.

## 11. Limitations And Uncertainty

- Missing measured concentrations:
- Missing kinetic/surface/exchange constants:
- Database coverage limits:
- Redox assumptions:
- Mineral amount uncertainty:
- Boundary-condition uncertainty:
- Calibration status:

## 12. Future MCP Extension

Potential MCP tools:

- `run_phreeqc`
- `validate_phreeqc_input`
- `parse_phreeqc_output`
- `save_model_version`
- `query_water_samples`
- `query_mineralogy`
