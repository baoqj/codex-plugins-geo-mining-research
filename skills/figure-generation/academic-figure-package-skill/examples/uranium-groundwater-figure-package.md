# Figure Package: U-Ra-Rn-Po-Pb Radionuclide Migration in Uranium Mining Area Groundwater

## 1. Figure Strategy

- Paper section: introduction, methods, mechanism, evidence synthesis.
- Research purpose: explain how uranium-series radionuclides may migrate through groundwater systems around a uranium mining area.
- Main visual argument: migration risk must be interpreted through hydrogeology, decay-chain behavior, redox and sorption controls, and measured evidence.
- Target audience: hydrogeochemistry, environmental geoscience, mining environmental review.
- Target journal or format: academic journal article.
- Discipline profile: groundwater geochemistry, radionuclide transport, mining environmental science.

## 2. Figure Inventory

| Figure | Type | Paper Section | Main Message | Required Data | Output Format |
|---|---|---|---|---|---|
| Figure 1 | Study-area map | Introduction | Locate the mine area, hydrogeologic setting, monitoring wells, and flow context | AOI, CRS, geology, wells, hydrology, source metadata | PDF/SVG + PNG |
| Figure 2 | Decay-chain mechanism diagram | Background | Distinguish decay relationships from transport controls | Decay-chain reference, chemistry notes | SVG/PDF |
| Figure 3 | Conceptual cross-section | Mechanism | Link groundwater flow, redox zones, sorption, and migration pathways | Stratigraphy, water table, flow direction, conceptual sources | SVG/PDF |
| Figure 4 | Evidence matrix | Discussion | Separate measured evidence from inferred migration mechanisms | Evidence table, confidence, limitations | PDF/SVG |

## 3. Figure Specifications

### Figure 1. Study area and hydrogeological setting

#### Intent

Study-area figure and GIS / map figure for the introduction.

#### Scientific Content

- Entities: uranium mining area, groundwater wells, surface water, hydrostratigraphic units, bedrock, AOI.
- Processes: groundwater flow, recharge, discharge, potential contaminant migration.
- Relationships: monitoring wells relate to flow paths and hydrogeologic units.
- Data layers: AOI boundary, geology, hydrology, wells, claims or mine footprint if supplied.
- Variables: hydraulic gradient, well depth, water table, radionuclide concentrations if verified.
- Uncertainties: well-screen depth, spatial precision, dated geologic layers.
- Caveats: map is not a regulatory site assessment.

#### Visual Grammar

Blue arrows = groundwater flow; red dashed arrows = potential radionuclide migration; gray polygons = bedrock units; circles = monitoring wells; dotted lines = inferred boundaries. Include color-accessible labels and line styles.

#### Layout Plan

Single map panel with inset regional locator. Required cartographic elements: CRS, scale bar, north arrow, legend, source note, AOI extent, and spatial precision note.

#### Toolchain

Primary tool: QGIS or GeoPandas. Secondary tools: Inkscape for label cleanup. Export formats: PDF/SVG and PNG preview.

#### Drawing Prompt

Create an academic study-area map showing a uranium mining AOI, monitoring wells, hydrogeologic units, groundwater flow arrows, and an inset regional locator. Include CRS, scale bar, north arrow, legend, data source note, and spatial precision caveat.

#### Script / Rendering Plan

Use `scaffold_qgis_layout_plan.py` with CRS and verified layer names. Do not draw final well locations without verified coordinates.

#### Caption Draft

**Figure 1. Study area and hydrogeological setting.** The map locates the uranium mining area, hydrogeologic units, monitoring wells, and interpreted groundwater flow context. Data sources, CRS, scale bar, north arrow, legend, and spatial precision must be included in the final map. Conceptual flow arrows require verification from hydraulic-head data.

#### Publication Checklist

- [ ] CRS, scale bar, north arrow, legend, and source note included.
- [ ] Spatial precision and layer dates recorded.
- [ ] Conceptual arrows labeled as interpreted.
- [ ] Not a regulatory or Qualified Person opinion.

### Figure 2. Decay-chain and radionuclide behavior diagram

#### Intent

Conceptual-mechanism figure for background and mechanism sections.

#### Scientific Content

- Entities: U, Ra, Rn, Po, Pb species.
- Processes: radioactive decay, aqueous transport, sorption, gas-phase radon migration, precipitation.
- Relationships: decay-chain sequence does not equal identical mobility.
- Data layers: verified decay-chain reference and hydrogeochemical behavior notes.
- Variables: half-life, solubility, sorption tendency, redox sensitivity.
- Uncertainties: site chemistry and speciation not supplied.
- Caveats: conceptual behavior summary, not dose assessment.

#### Visual Grammar

Horizontal decay-chain backbone with colored process tags. Purple = radiological signal, blue = aqueous transport, gray = sorbed/solid phase, dashed red = mobile risk pathway.

#### Layout Plan

Single vector panel with decay sequence on top and behavior classes below.

#### Toolchain

Primary tool: Mermaid or SVG. Secondary tools: Inkscape/Figma. Export formats: SVG/PDF.

#### Drawing Prompt

Create a clean vector diagram of the U-Ra-Rn-Po-Pb decay chain with mobility annotations for aqueous transport, sorption, gas transport, and precipitation. Mark conceptual content as conceptual.

#### Script / Rendering Plan

Use `generate_mermaid_from_spec.py --mode mechanism --nodes "Uranium source,Radium mobility,Radon gas pathway,Polonium/Lead products,Measurement evidence"`.

#### Caption Draft

**Figure 2. Decay-chain and radionuclide behavior diagram.** The figure distinguishes uranium-series decay relationships from groundwater transport behavior. Colors and arrows identify conceptual aqueous, sorbed, gas, and decay processes. Final values require verified decay data and site-specific hydrogeochemistry.

#### Publication Checklist

- [ ] Decay-chain source verified.
- [ ] Conceptual mobility labels separated from measured data.
- [ ] Safety and regulatory caveat included.

### Figure 3. Groundwater flow and migration conceptual cross-section

#### Intent

Conceptual-mechanism figure and hydrogeologic cross-section.

#### Scientific Content

- Entities: recharge area, mine-related source term, aquifer, aquitard, fractures, wells, discharge zone.
- Processes: advection, dispersion, diffusion, sorption, redox reaction, decay.
- Relationships: transport pathways depend on hydraulic gradient and geochemical retardation.
- Data layers: stratigraphy, water table, flow direction, monitoring wells.
- Variables: hydraulic head, concentration, retardation, redox state.
- Uncertainties: geometry and hydraulic properties are conceptual unless verified.
- Caveats: not a site-specific risk assessment.

#### Visual Grammar

Blue arrows = groundwater flow; red dashed arrows = radionuclide migration; dotted lines = inferred fracture zones; gray = bedrock; green = low-permeability layer; circles = monitoring wells.

#### Layout Plan

Two-panel figure: (a) hydrogeologic cross-section, (b) process inset showing sorption and decay along a flow path.

#### Toolchain

Primary tool: SVG/Figma/Inkscape. Secondary tool: GeoMine Visualization Studio if a 3D conceptual page is requested. Export formats: SVG/PDF.

#### Drawing Prompt

Draw a two-panel academic cross-section showing groundwater flow and radionuclide migration from a uranium source area through fractured bedrock and monitoring wells. Clearly label conceptual geometry, flow paths, sorption zones, and redox zones.

#### Script / Rendering Plan

Draft as SVG; if made interactive, convert evidence lanes to a GeoMine SceneSpec and label all geometry as conceptual.

#### Caption Draft

**Figure 3. Groundwater flow and migration conceptual cross-section.** Panel (a) shows a conceptual hydrogeologic section with groundwater flow and potential radionuclide migration pathways. Panel (b) summarizes key attenuation and transformation processes. Geometry and pathways are conceptual unless supported by verified site data.

#### Publication Checklist

- [ ] Conceptual geometry marked clearly.
- [ ] Flow direction and migration arrows are visually distinct.
- [ ] Caveat states not a site-specific risk or compliance assessment.

### Figure 4. Dose contribution evidence matrix

#### Intent

Evidence-synthesis figure for discussion.

#### Scientific Content

- Entities: radionuclide groups, sampling media, evidence sources, confidence grades.
- Processes: measurement, attribution, uncertainty review.
- Relationships: dose contribution claims must trace to measured or modeled evidence.
- Data layers: literature, monitoring data, model outputs if supplied.
- Variables: activity concentration, dose coefficient, exposure pathway.
- Uncertainties: missing sample media, method, and detection limits.
- Caveats: not a radiological safety determination.

#### Visual Grammar

Matrix cells encode evidence strength with color plus labels; hatching indicates missing evidence; icons mark measured, modeled, or inferred claims.

#### Layout Plan

Single matrix panel with rows as radionuclides and columns as evidence type, exposure pathway, confidence, and limitation.

#### Toolchain

Primary tool: Python Matplotlib or R ggplot2. Secondary tool: Inkscape. Export formats: PDF/SVG.

#### Drawing Prompt

Create an evidence matrix that separates measured, modeled, and inferred dose contribution evidence for uranium-series radionuclides, with explicit confidence and limitation labels.

#### Script / Rendering Plan

Use `scaffold_matplotlib_figure.py` as a starting point and replace placeholder values with verified data.

#### Caption Draft

**Figure 4. Dose contribution evidence matrix.** The matrix separates measured, modeled, and inferred evidence for radionuclide dose contribution hypotheses. Cells encode confidence using labels and accessible color. The figure is not a radiological safety determination.

#### Publication Checklist

- [ ] Evidence source and method are cited.
- [ ] Confidence and limitation labels are visible.
- [ ] No unsupported dose or safety conclusion.

## 4. Cross-Figure Visual Consistency

Use blue for groundwater flow, red dashed arrows for migration pathways, purple for radiological signal, gray for bedrock, dotted boundaries for inferred features, and direct labels for color-accessibility.

## 5. Data and Provenance Requirements

Record CRS, scale bar, north arrow, legend, source, well coordinates, layer dates, radionuclide measurement methods, units, detection limits, QA/QC status where relevant, and whether each element is measured or conceptual.

## 6. Caveats

This package is for research figure planning only. It is not legal advice, not investment advice, not a Qualified Person opinion, not a radiological safety assessment, not a feasibility study, and not a permitting decision.

## 7. Machine-Readable JSON Summary

```json
{
  "figure_package": {
    "title": "U-Ra-Rn-Po-Pb Radionuclide Migration in Uranium Mining Area Groundwater",
    "paper_title": "Uranium-series radionuclide migration in mining-area groundwater",
    "discipline": "hydrogeochemistry",
    "target_journal": "academic journal",
    "created_for": "GeoMine Research",
    "figures": [
      {"figure_id": "Figure 1", "title": "Study area and hydrogeological setting", "figure_type": "GIS / map figure"},
      {"figure_id": "Figure 2", "title": "Decay-chain and radionuclide behavior diagram", "figure_type": "conceptual-mechanism figure"},
      {"figure_id": "Figure 3", "title": "Groundwater flow and migration conceptual cross-section", "figure_type": "conceptual cross-section"},
      {"figure_id": "Figure 4", "title": "Dose contribution evidence matrix", "figure_type": "evidence-synthesis figure"}
    ]
  }
}
```
