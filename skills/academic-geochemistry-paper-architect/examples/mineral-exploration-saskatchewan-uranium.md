# Example: Saskatchewan Uranium Exploration Geochemistry Paper Architecture

## Input Topic

Use Saskatchewan public geochemistry, geophysics, geology, and mineral occurrence data to identify potential uranium exploration targets around the Athabasca Basin margin.

## Paper Type Classification

- Primary type: Mineral Exploration Geochemistry Paper
- Secondary type: Regional Geochemical Characterization Paper
- Tertiary type: Geochemical Modelling and Machine Learning Paper

## Research Questions

- Which pathfinder-element associations are spatially consistent with uranium mineral-system processes?
- How do geochemical anomalies relate to structure, lithology, basin margin context, and known occurrences?
- Can target ranking be framed as a transparent evidence score without implying resource or economic value?

## Hypotheses

- Multi-element U-Th-K and alteration-related anomalies aligned with favorable structures provide stronger exploration evidence than isolated single-element highs.
- Prospectivity ranking is sensitive to data coverage, threshold method, and source scale.

## Required Data

- Sample coordinates, medium, U and pathfinder elements, detection limits, QA/QC status.
- Geology, structures, geophysics, mineral occurrences, claim/AOI context, source dates and scales.

## Methods

- Unit normalization and QA/QC.
- Robust anomaly thresholds and multi-element association analysis.
- GIS overlay with geology, structure, and occurrence layers.
- Disclosure-boundary review to avoid economic or resource claims.

## Figure Plan

- Study area geological map.
- U and pathfinder anomaly maps.
- Correlation matrix or PCA biplot.
- Multi-layer prospectivity map.
- Target ranking table with uncertainty flags.

## Downstream Skills

- `geochemical-survey-skill`
- `deposit-model-skill`
- `ni43-101-disclosure-check-skill`
- `academic-figure-package-skill`
