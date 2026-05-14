---
name: calibration-validation-skill
description: Design calibration and validation plans for THMC groundwater chemistry models, including hydraulic, thermal, chemical, radionuclide, mineralogical, porosity/permeability, breakthrough, benchmark, metric, and model rejection criteria.
---

# Calibration Validation Skill

## Purpose

Define how a THMC model will be calibrated, validated, benchmarked, and rejected if it fails evidence constraints.

## Calibration Targets

Potential targets include hydraulic head, flow rate, temperature, pH, Eh, EC/TDS, major ions, trace metals, isotope or radionuclide concentrations, saturation indices, mineralogical changes, porosity/permeability changes, and breakthrough curves.

## Output Contract

Return:

- Calibration target table.
- DGR field-data source table, when `dgr-field-data-acquisition-skill` or `geomine_thmc_data` MCP outputs are available.
- Validation dataset requirements.
- Data-gap matrix separating measured, mock, planned, inferred, and missing evidence.
- Benchmark suggestions.
- Error metrics.
- Model rejection criteria.
- Professional caution notes.

## MCP Integration

For DGR or field-data-heavy tasks, request the `dgr-field-data-acquisition-skill` output before finalizing calibration targets. Use `validate_dgr_thmc_dataset` results to determine whether calibration can proceed, and use `build_dgr_calibration_dataset` or `save_dgr_data_package` ids only as dataset package references, not as proof of model validity.
