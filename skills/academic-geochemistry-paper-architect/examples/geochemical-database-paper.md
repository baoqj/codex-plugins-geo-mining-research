# Example: Regional Geochemical Database Paper Architecture

## Input Topic

Build a reusable regional database combining whole-rock geochemistry, sample metadata, GIS context, and source provenance for Canadian mineral systems research.

## Paper Type Classification

- Primary type: Data Paper / Database Paper
- Secondary type: Regional Geochemical Characterization Paper
- Tertiary type: Technical Note / Methods Paper

## Research Questions

- How can multi-source geochemical data be standardized into a reproducible and reusable schema?
- Which metadata and QA/QC flags are required to prevent misleading regional interpretation?
- What research questions can the database support, and what questions remain unsupported?

## Hypotheses

- A source-versioned schema with explicit QA/QC flags improves reuse and reduces ambiguity across public datasets.

## Required Data

- Sample identifiers, coordinates, CRS, sample medium, lithology, analytes, units, analytical methods, detection limits, source, version, license.

## Methods

- Source inventory.
- Schema design and data dictionary.
- Unit and analyte normalization.
- QA/QC flag design.
- Summary statistics and data availability statement.

## Figure Plan

- Database schema diagram.
- Source and sample distribution map.
- Element coverage histogram.
- QA/QC workflow diagram.

## Downstream Skills

- `geodata-discovery-skill`
- `academic-figure-package-skill`
- `academic-paper-research-writer`
