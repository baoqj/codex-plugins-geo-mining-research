# Figure Package: Regional Geochemical Anomaly Interpretation for Uranium or Lithium Exploration

## 1. Figure Strategy

- Paper section: data, methods, results, interpretation.
- Research purpose: show how sample distribution, anomaly thresholds, pathfinder associations, and target ranking support cautious exploration interpretation.
- Main visual argument: anomalies are evidence requiring QA/QC and geologic context, not discovery claims.
- Target audience: exploration geochemistry and mineral systems researchers.
- Target journal or format: academic paper or technical report.
- Discipline profile: applied geochemistry, GIS, mineral exploration.

## 2. Figure Inventory

| Figure | Type | Paper Section | Main Message | Required Data | Output Format |
|---|---|---|---|---|---|
| Figure 1 | Sampling location map | Data | Sampling design and geology constrain interpretation | sample locations, CRS, geology, source | PDF/SVG |
| Figure 2 | Single-element anomaly map | Results | U or Li anomalies require documented thresholds | element values, unit, threshold, QA/QC | PDF/SVG |
| Figure 3 | Pathfinder heatmap | Results | Multi-element patterns are stronger than isolated highs | standardized element matrix | PDF/SVG |
| Figure 4 | Target ranking evidence matrix | Discussion | Ranking is evidence-weighted and limited | evidence lanes, confidence | PDF/SVG |

## 3. Figure Specifications

### Figure 1. Sampling location and geological background

#### Intent

GIS / map figure and sampling location map.

#### Scientific Content

- Entities: samples, lithologic units, structures, AOI, survey boundary.
- Processes: sampling design and spatial coverage.
- Relationships: sample density and geology affect anomaly interpretation.
- Data layers: sample points, geology, structures, AOI, survey boundary.
- Variables: sample medium, unit, coordinates, CRS.
- Uncertainties: coordinate precision and sample medium compatibility.
- Caveats: map does not establish mineralization.

#### Visual Grammar

Circles = sampling sites; gray polygons = geology; solid lines = mapped structures; dotted lines = inferred structures; orange outlines = anomaly context. Use labels and symbols, not color alone.

#### Layout Plan

Single map panel with CRS, scale bar, north arrow, legend, source note, and sample medium / QA/QC note.

#### Toolchain

Primary tool: QGIS or GeoPandas. Secondary tool: Inkscape. Export formats: PDF/SVG and PNG preview.

#### Drawing Prompt

Create a publication map showing sampling locations over geological background with CRS, scale bar, north arrow, legend, source, sample medium, unit note, detection limit note, and QA/QC limitation.

#### Script / Rendering Plan

Use QGIS layout checklist. Verify sample medium, units, analytical method, detection limits, and QA/QC status before final export.

#### Caption Draft

**Figure 1. Sampling location and geological background.** The map shows sample distribution relative to geologic units and structures. Final rendering must include CRS, scale bar, north arrow, legend, source, sample medium, units, detection limits, and QA/QC limitations.

#### Publication Checklist

- [ ] CRS, scale bar, north arrow, legend, and source included.
- [ ] Sample medium, unit, detection limit, and QA/QC limitation included.
- [ ] No discovery or economic claim.

### Figure 2. Single-element anomaly map

#### Intent

Geochemical-anomaly figure and GIS / map figure.

#### Scientific Content

- Entities: sample locations, anomaly zones, element values, geology.
- Processes: thresholding and spatial interpolation if justified.
- Relationships: element anomaly must be interpreted with sample medium and geology.
- Data layers: sample points, element concentration, geology, AOI.
- Variables: U or Li concentration, unit, sample medium, detection limit, threshold.
- Uncertainties: censored data, analytical error, interpolation uncertainty.
- Caveats: anomaly does not equal mineralization.

#### Visual Grammar

Orange = anomaly class; gray = geology; circles = samples; hatching = interpolation uncertainty; labels show threshold method.

#### Layout Plan

Single map panel or two panels: (a) point values, (b) threshold class map. Include CRS, scale bar, north arrow, legend, source, units, sample medium, detection limits, and QA/QC limitation.

#### Toolchain

Primary tool: Python Matplotlib/GeoPandas or QGIS. Secondary tool: Inkscape. Export formats: PDF/SVG.

#### Drawing Prompt

Create an academic geochemical anomaly map for a single element with sample points, anomaly classes, threshold method, units, sample medium, detection limits, QA/QC caveat, CRS, scale bar, north arrow, legend, and source.

#### Script / Rendering Plan

Use verified data and robust thresholds. Do not interpolate unless spacing and geology justify it.

#### Caption Draft

**Figure 2. Single-element anomaly map.** The figure shows element concentrations and anomaly classes for the specified sample medium. Units, detection limits, threshold method, QA/QC limitation, CRS, scale bar, north arrow, legend, and source must be shown. The anomaly pattern is not a discovery claim.

#### Publication Checklist

- [ ] Unit, sample medium, detection limit, threshold method, and QA/QC limitation visible.
- [ ] CRS, scale bar, north arrow, legend, and source included.
- [ ] Interpolation caveat included if used.

### Figure 3. Multi-element pathfinder association heatmap

#### Intent

Data-visualization figure and geochemical-anomaly figure.

#### Scientific Content

- Entities: samples or zones, U/Li pathfinder elements, anomaly classes.
- Processes: normalization, robust scoring, association analysis.
- Relationships: multi-element association supports but does not prove target potential.
- Data layers: standardized geochemical table.
- Variables: element concentration, unit, robust score, sample medium, detection limit.
- Uncertainties: compositional effects, censored values, QA/QC limitations.
- Caveats: pathfinder association is hypothesis only until geological validation.

#### Visual Grammar

Sequential palette for standardized scores; labels and clustering lines; hatching or icons for censored data. Avoid red/green-only encoding.

#### Layout Plan

Single heatmap with rows as zones/samples and columns as elements. Include a side legend for sample medium, unit treatment, detection limit handling, and QA/QC limitation.

#### Toolchain

Primary tool: Python Matplotlib or R ggplot2. Secondary tool: Inkscape. Export formats: PDF/SVG and PNG.

#### Drawing Prompt

Create a multi-element pathfinder heatmap with standardized geochemical scores, labels, units note, sample medium, detection limit treatment, QA/QC limitation, and deposit-model caveat.

#### Script / Rendering Plan

Use a reproducible script that logs transformation, censoring, and threshold parameters.

#### Caption Draft

**Figure 3. Multi-element pathfinder association heatmap.** The heatmap summarizes standardized element associations for the selected sample medium. Units, detection limit handling, and QA/QC limitations must be documented. Associations are interpreted as exploration hypotheses, not mineralization proof.

#### Publication Checklist

- [ ] Unit, sample medium, detection limit handling, and QA/QC limitation included.
- [ ] Color accessibility checked.
- [ ] Transformation and threshold method documented.

### Figure 4. Target ranking evidence matrix

#### Intent

Evidence-synthesis figure for discussion.

#### Scientific Content

- Entities: target zones, evidence lanes, confidence grades.
- Processes: evidence weighting and uncertainty disclosure.
- Relationships: target ranking combines geochemistry, geology, and data quality.
- Data layers: geochemistry, geology, occurrences, QA/QC, source provenance.
- Variables: evidence grade, confidence, required follow-up.
- Uncertainties: missing field validation and incomplete QA/QC.
- Caveats: target rank is not an investment or discovery statement.

#### Visual Grammar

Matrix with labels plus color; hatching for missing evidence; icons for geochemistry, geology, and source quality.

#### Layout Plan

Single evidence matrix panel.

#### Toolchain

Primary tool: Python Matplotlib or spreadsheet-to-SVG workflow. Export formats: PDF/SVG.

#### Drawing Prompt

Create an evidence matrix ranking target zones by evidence lane, confidence, limitations, and follow-up requirements.

#### Script / Rendering Plan

Render from a CSV evidence matrix and preserve source/provenance columns.

#### Caption Draft

**Figure 4. Target ranking evidence matrix.** The matrix summarizes geochemical, geological, and data-quality evidence for follow-up planning. It is not investment advice, not a Qualified Person opinion, and not a resource or reserve statement.

#### Publication Checklist

- [ ] Evidence grades and caveats visible.
- [ ] QP and investment boundaries stated.
- [ ] Follow-up needs listed.

## 4. Cross-Figure Visual Consistency

Use orange for geochemical anomaly, gray for geology, blue for water or contextual flow, circles for samples, triangles for occurrences, and hatching for uncertain or interpolated zones.

## 5. Data and Provenance Requirements

Record source, CRS, scale bar, north arrow, legend, sample medium, units, analytical method, detection limits, QA/QC limitations, threshold method, survey date, and license.

## 6. Caveats

This package is for research planning only. It is not legal advice, not investment advice, not a Qualified Person opinion, not a feasibility study, not a resource estimate, and not a reserve estimate.

## 7. Machine-Readable JSON Summary

```json
{
  "figure_package": {
    "title": "Regional Geochemical Anomaly Interpretation",
    "paper_title": "Regional geochemical anomaly interpretation for uranium or lithium exploration",
    "discipline": "exploration geochemistry",
    "target_journal": "academic journal",
    "created_for": "GeoMine Research",
    "figures": [
      {"figure_id": "Figure 1", "title": "Sampling location and geological background", "figure_type": "GIS / map figure"},
      {"figure_id": "Figure 2", "title": "Single-element anomaly map", "figure_type": "geochemical-anomaly figure"},
      {"figure_id": "Figure 3", "title": "Multi-element pathfinder association heatmap", "figure_type": "data-visualization figure"},
      {"figure_id": "Figure 4", "title": "Target ranking evidence matrix", "figure_type": "evidence-synthesis figure"}
    ]
  }
}
```
