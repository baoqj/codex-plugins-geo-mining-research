# Figure Package: Mining Project Study Area, Claims, Neighboring Companies, Infrastructure, and Geological Context

## 1. Figure Strategy

- Paper section: project context and data provenance.
- Research purpose: communicate where a project sits relative to claims, neighbors, infrastructure, and geology.
- Main visual argument: project context requires spatial provenance and disclosure caveats, not promotional overstatement.
- Target audience: technical report readers, exploration researchers, internal due diligence teams.
- Target journal or format: technical memo or paper figure package.
- Discipline profile: GIS, mineral exploration, mining disclosure.

## 2. Figure Inventory

| Figure | Type | Paper Section | Main Message | Required Data | Output Format |
|---|---|---|---|---|---|
| Figure 1 | Claim location map | Project context | AOI and claim setting require source and date | claims, AOI, CRS, source | PDF/SVG |
| Figure 2 | Neighbor and infrastructure map | Context | Access and neighboring activity are contextual only | roads, power, towns, neighbors, source | PDF/SVG |
| Figure 3 | Geological setting map | Geology | Host geology and structures frame hypotheses | geology, structures, source | PDF/SVG |
| Figure 4 | Disclosure caveat figure | Technical report | Separate verified evidence from inferred context | evidence and caveat matrix | PDF/SVG |

## 3. Figure Specifications

### Figure 1. Study area and claim location map

#### Intent

Study-area figure, GIS / map figure, and technical-report figure.

#### Scientific Content

- Entities: AOI, claim blocks, administrative boundaries, nearby projects.
- Processes: tenure context review.
- Relationships: claims define spatial context but do not prove rights or economic value.
- Data layers: claim polygons, AOI, basemap, jurisdiction boundary.
- Variables: claim id, status date, tenure source, CRS.
- Uncertainties: claim status can change and must be dated.
- Caveats: not a legal tenure opinion.

#### Visual Grammar

AOI = bold black outline; claims = transparent fills; neighboring claims = muted gray; inferred boundaries = dotted. Include direct labels and a clear legend.

#### Layout Plan

Map with regional inset. Required: CRS, scale bar, north arrow, legend, source, status date, and spatial precision note.

#### Toolchain

Primary tool: QGIS or GeoPandas. Secondary tool: Inkscape. Export formats: PDF/SVG and PNG.

#### Drawing Prompt

Create a claim location map with AOI, claims, neighbors, CRS, scale bar, north arrow, legend, source, status date, and legal-tenure caveat.

#### Script / Rendering Plan

Use QGIS layout plan. Verify claim status and source date before final rendering.

#### Caption Draft

**Figure 1. Study area and claim location map.** The map shows AOI and claim context using dated source data. CRS, scale bar, north arrow, legend, source, and spatial precision must be included. The figure is not a legal tenure opinion.

#### Publication Checklist

- [ ] CRS, scale bar, north arrow, legend, and source included.
- [ ] Claim status date shown.
- [ ] Legal/QP caveat included.

### Figure 2. Neighboring companies and infrastructure context

#### Intent

GIS / map figure and company-intelligence context figure.

#### Scientific Content

- Entities: neighboring projects, roads, power, rail, towns, processing facilities if verified.
- Processes: access and regional activity context.
- Relationships: proximity is contextual and not evidence of mineralization.
- Data layers: infrastructure, neighbors, AOI, claims, basemap.
- Variables: distance, source date, CRS.
- Uncertainties: distance estimates and source currency.
- Caveats: not investment advice.

#### Visual Grammar

Roads = gray lines; power = blue line; neighboring projects = triangles; AOI = black outline; labels include source and date.

#### Layout Plan

Single map panel with CRS, scale bar, north arrow, legend, source, and distance-method note.

#### Toolchain

Primary tool: QGIS/GeoPandas. Export formats: PDF/SVG.

#### Drawing Prompt

Create a regional infrastructure and neighboring-company map with CRS, scale bar, north arrow, legend, source, and explicit caveat that proximity is contextual only.

#### Script / Rendering Plan

Calculate distances only from verified geometry. Otherwise mark distance as not calculated.

#### Caption Draft

**Figure 2. Neighboring companies and infrastructure context.** The map summarizes infrastructure and neighboring project context. CRS, scale bar, north arrow, legend, source, and distance method must be documented. Proximity does not imply mineralization, feasibility, or investment value.

#### Publication Checklist

- [ ] Source and distance method included.
- [ ] Not investment advice caveat included.
- [ ] No unsupported access or feasibility claim.

### Figure 3. Geological setting map

#### Intent

GIS / map figure and geological context figure.

#### Scientific Content

- Entities: lithologic units, faults, structures, occurrences, AOI.
- Processes: geological setting and deposit-model context.
- Relationships: geology frames hypotheses but needs field verification.
- Data layers: geology, structure, occurrences, AOI.
- Variables: map scale, source, CRS.
- Uncertainties: map scale and generalized contacts.
- Caveats: not a resource or reserve statement.

#### Visual Grammar

Lithologies = muted colors; faults = solid/dashed lines depending on confidence; occurrences = triangles; AOI = black outline.

#### Layout Plan

Map panel with CRS, scale bar, north arrow, legend, source, map scale, and resolution note.

#### Toolchain

Primary tool: QGIS. Secondary tool: Inkscape. Export formats: PDF/SVG.

#### Drawing Prompt

Create a geological setting map with AOI, lithology, structures, occurrences, CRS, scale bar, north arrow, legend, source, scale, and uncertainty caveat.

#### Script / Rendering Plan

Use official geology layers where available and preserve map scale/resolution.

#### Caption Draft

**Figure 3. Geological setting map.** The figure places the project in regional geological context. CRS, scale bar, north arrow, legend, source, map scale, and generalized-contact caveats must be included.

#### Publication Checklist

- [ ] Map source, CRS, scale bar, north arrow, and legend included.
- [ ] Structure confidence encoded by line style.
- [ ] Resource/reserve caveat included.

### Figure 4. Technical disclosure evidence and caveat matrix

#### Intent

NI 43-101 technical disclosure review figure and evidence-synthesis figure.

#### Scientific Content

- Entities: claims, occurrences, geochemistry, infrastructure, reports, QP review needs.
- Processes: disclosure-risk screening.
- Relationships: each claim needs source, evidence grade, and caveat.
- Data layers: source table and evidence matrix.
- Variables: evidence grade, review status, limitation.
- Uncertainties: absent evidence versus evidence not provided.
- Caveats: not legal advice or Qualified Person opinion.

#### Visual Grammar

Rows = evidence categories; columns = source, confidence, limitation, required review. Use labels and icons, not red/green-only status.

#### Layout Plan

Single matrix panel for report discussion.

#### Toolchain

Primary tool: table-to-SVG via Python or spreadsheet. Export formats: PDF/SVG.

#### Drawing Prompt

Create a technical disclosure caveat matrix separating verified evidence, inferred context, missing evidence, and required professional review.

#### Script / Rendering Plan

Render from a structured evidence CSV. Preserve source id and review status.

#### Caption Draft

**Figure 4. Technical disclosure evidence and caveat matrix.** The matrix separates verified evidence, inferred context, missing evidence, and required professional review. It is not legal advice, not investment advice, and not a Qualified Person opinion.

#### Publication Checklist

- [ ] QP/legal/investment caveats included.
- [ ] Sources and limitations included.
- [ ] No compliance conclusion stated.

## 4. Cross-Figure Visual Consistency

Use black AOI outlines, gray infrastructure, triangles for mineral occurrences, muted geology colors, dashed lines for inferred features, and explicit caveat labels.

## 5. Data and Provenance Requirements

Required metadata: CRS, scale bar, north arrow, legend, source, claim status date, geology source scale, infrastructure source, distance method, and professional review caveats.

## 6. Caveats

This package is not legal advice, not investment advice, not a Qualified Person opinion, not a feasibility study, not a resource estimate, not a reserve estimate, and not a permitting decision.

## 7. Machine-Readable JSON Summary

```json
{
  "figure_package": {
    "title": "Mining Project Study Area Map Package",
    "paper_title": "Mining project spatial context and disclosure caveats",
    "discipline": "mining GIS",
    "target_journal": "technical memo",
    "created_for": "GeoMine Research",
    "figures": [
      {"figure_id": "Figure 1", "title": "Study area and claim location map", "figure_type": "GIS / map figure"},
      {"figure_id": "Figure 2", "title": "Neighboring companies and infrastructure context", "figure_type": "GIS / map figure"},
      {"figure_id": "Figure 3", "title": "Geological setting map", "figure_type": "GIS / map figure"},
      {"figure_id": "Figure 4", "title": "Technical disclosure evidence and caveat matrix", "figure_type": "technical-report figure"}
    ]
  }
}
```
