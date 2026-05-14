# Data, Methods, QA/QC, and Reproducibility Rules

## Data Sources

Acceptable geochemistry data sources include user-provided files, public paper supplementary data, EarthChem, GEOROC, PetDB, USGS/GSC and provincial surveys, assessment reports, groundwater monitoring reports, PHREEQC inputs/outputs, GIS files, CSV/Excel, PostGIS, D1, and R2.

Do not claim a source was queried unless it was actually queried in the current run.

## Standardization

Normalize:

- sample identifiers and aliases;
- coordinates and CRS;
- units and analyte names;
- oxide notation and element notation;
- sample medium and lithology;
- age units and uncertainty;
- analytical method and detection limits;
- citation, license, version, and QA/QC flags.

## QA/QC Checks

Require the relevant checks:

- major-element total and LOI;
- detection limits and censored values;
- duplicates, standards, blanks, and reference materials;
- charge balance error for groundwater;
- missing coordinates, ages, lithology, or methods;
- unit consistency and impossible values;
- outlier policy and whether outliers are analytical, geological, or unknown.

## Transformations

Use only transformations justified by data type:

- LOI-free normalization;
- trace-element normalization;
- chondrite or primitive-mantle normalization;
- log or centered log-ratio transformation for compositional data;
- age binning;
- spatial joins;
- feature engineering for models.

Record constants, reference compositions, software, package versions, and scripts.

## Reproducibility Minimum

Every architecture must specify:

- raw data source and version;
- processing script or planned script;
- unit conversion and normalization rules;
- software and version;
- model database when using PHREEQC or thermodynamic calculations;
- output files and data/code availability plan.
