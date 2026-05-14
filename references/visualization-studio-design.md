# GeoMine Visualization Studio Design

## Source Pattern Reviewed

`cell-architecture-studio` is a React 19, TypeScript, Vite, Three.js, React Three Fiber, and Drei application. The useful transferable patterns are:

- a 3D canvas as the default primary experience;
- selectable specimens with metadata panels;
- mesh/focus modes;
- GLB support with procedural fallback geometry;
- object-level highlighting;
- responsive desktop and mobile layouts;
- Playwright screenshot verification with canvas pixel metrics;
- clear asset provenance.

GeoMine should reuse the interaction pattern, not the biological domain model. Geoscience equivalents:

| Cell Studio Concept | GeoMine Equivalent |
|---|---|
| Cell specimen | AOI, deposit model, project, or geologic scenario |
| Organelle | lithology, fault, vein, ore lens, drillhole, sample cluster |
| Mesh mode | full geologic scene |
| Focus mode | highlight selected evidence lane |
| Cross section | geologic cross-section or cutaway view |
| GLB model | future terrain, drillhole, mine, or geological model asset |
| Procedural fallback | generated strata, tubes, blocks, spheres, linework |
| Organelles panel | evidence/layer panel |
| Microscope modes | map/cross-section/evolution modes |
| Verification | screenshot and nonblank canvas checks |

## SceneSpec Schema

Use this JSON shape as the stable interchange format between GeoMine research output and generated visualization apps:

```json
{
  "title": "Athabasca Uranium Concept Model",
  "subtitle": "Conceptual basin-margin unconformity scene",
  "status": "conceptual",
  "crs": "not authoritative",
  "verticalExaggeration": 1.4,
  "camera": {
    "position": [4.5, 3.2, 5.5],
    "target": [0, -0.4, 0]
  },
  "layers": [
    {
      "id": "sandstone",
      "name": "Athabasca sandstone",
      "color": "#d8a657",
      "depth": 0.35,
      "thickness": 0.5,
      "note": "Conceptual cover sequence"
    }
  ],
  "structures": [
    {
      "id": "fault-corridor",
      "name": "Reactivated basement fault",
      "color": "#ef4444",
      "points": [[-2.0, -1.2, -0.8], [-0.8, -0.4, -0.1], [1.8, 0.45, 0.7]],
      "note": "Conceptual fluid pathway"
    }
  ],
  "oreBodies": [
    {
      "id": "uranium-lens",
      "name": "Uranium lens",
      "color": "#facc15",
      "position": [0.2, -0.28, 0.05],
      "scale": [0.75, 0.11, 0.28],
      "note": "Illustrative mineralized zone, not a resource"
    }
  ],
  "drillholes": [
    {
      "id": "ddh-01",
      "name": "DDH-01",
      "color": "#111827",
      "from": [-1.4, 1.2, -0.7],
      "to": [-0.2, -1.1, 0.1],
      "note": "Example drill trace only"
    }
  ],
  "gisPoints": [
    {
      "id": "sample-cluster",
      "name": "Geochemical sample cluster",
      "color": "#38bdf8",
      "position": [1.2, 0.1, -0.7],
      "note": "Represents source-planning evidence, not live retrieval"
    }
  ],
  "timeline": [
    {
      "id": "basement",
      "label": "Basement architecture",
      "description": "Structural preparation creates pathways"
    }
  ],
  "provenance": [
    {
      "label": "NRCan CDoGS",
      "url": "https://geochem.nrcan.gc.ca/cdogs/content/main/home_en.htm",
      "retrievalStatus": "planned",
      "limitations": "No live survey retrieval in current demo"
    }
  ]
}
```

## Scene Types

### Stratigraphic Cross-Section

Use horizontal layer blocks plus faults, veins, drillholes, and sample points. This is the safest default because it is easy to label as conceptual when exact geometry is not available.

### GIS Evidence Scene

Use a shallow terrain plane, point markers, route/infrastructure lines, and layer chips. Require CRS and source status before implying distance or overlap.

### Mineralization Model

Use tubes for faults/fluid pathways, ellipsoids for ore lenses, and colored points for geochemical anomalies. Always mark it as interpretive unless based on a verified model.

### Geologic Evolution Animation

Use timeline events to progressively reveal basement, cover, structure, fluid flow, mineralization, erosion, and modern sampling. Do not animate unsupported certainty.

## Required Caveats

- Conceptual geometry is not authoritative.
- Visual proximity does not imply economic mineralization.
- Mineralized shapes are not resources or reserves.
- Distance and volume require real geometry, CRS, and spatial analysis.
- Data source status must remain visible: planned, parsed, unsupported, or verified.

## Verification Pattern

Generated projects should include `scripts/verify.mjs` that:

1. launches the Vite app in a browser;
2. waits for a canvas;
3. captures desktop and mobile screenshots;
4. computes simple pixel metrics to detect blank renders;
5. outputs JSON with screenshot paths and visual metrics.
