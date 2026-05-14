---
name: geomine-visualization-studio-skill
description: Generate provenance-aware 3D geology, GIS, mineralization, vein, drillhole, and geologic-evolution demo pages for GeoMine Research using React, Vite, Three.js, and React Three Fiber.
---

# GeoMine Visualization Studio Skill

## Purpose

Use this skill when a GeoMine Research task asks for a 3D visualization, animated geology demo, GIS scene, vein/mineralization model, geologic evolution storyboard, or browser-based presentation page.

The skill adapts the `cell-architecture-studio` pattern to geoscience: a polished React/Vite interface, a Three.js canvas as the primary experience, selectable domain objects, focus modes, procedural fallback geometry, metadata panels, and screenshot/pixel verification.

## Inputs To Identify

- AOI, CRS, scale, and whether coordinates are real, approximate, or conceptual.
- Scene type: stratigraphy, mineralization, drillholes, GIS points, faults, veins, basin model, infrastructure, or geologic evolution.
- Commodity and deposit model.
- Evidence items with provenance, source URL, license, CRS, scale/resolution, update date, and limitations.
- Required output: static 3D scene, animated sequence, report-embedded page, or standalone Vite project.
- Whether the result is conceptual/interpretive or based on verified spatial data.

## Workflow

1. Normalize the research context using the GeoMine router and AOI/CRS rules.
2. Decide whether a 3D output is warranted. Use static Markdown tables when the user only needs a source list.
3. Read `references/visualization-studio-design.md` for the scene schema and design patterns when building or modifying a visualization.
4. Convert GeoMine evidence into a `SceneSpec`:
   - layers for stratigraphy and lithology;
   - structures for faults, shear zones, folds, and fluid pathways;
   - ore bodies or veins for mineralization;
   - drillholes and intercepts;
   - GIS points for samples, occurrences, infrastructure, and source locations;
   - timeline events for geologic evolution.
5. Generate a standalone Vite/React/Three.js project with:

```bash
python3 skills/geomine-visualization-studio-skill/scripts/create_geomine_visualization.py \
  --output /tmp/geomine-visualization-demo
```

6. If the user supplied scene data:

```bash
python3 skills/geomine-visualization-studio-skill/scripts/create_geomine_visualization.py \
  --scene-data examples/visualization-uranium-basin-scene.json \
  --output /tmp/geomine-visualization-demo
```

7. When feasible, run:

```bash
cd /tmp/geomine-visualization-demo
npm install
npm run build
npm run verify
```

8. If browser verification is not possible, report the unverified state and give the exact commands to run.

## Output Rules

- Mark conceptual scenes as conceptual. Do not imply coordinates, distances, or geometries are authoritative unless verified.
- Attach provenance and limitations to every visual layer or claim.
- Keep the 3D scene as the primary surface; do not bury it inside decorative cards.
- Include camera controls, focus mode, layer toggles, and a metadata/evidence panel.
- For animations, show the timeline event labels and what evidence supports each step.
- Do not present prospectivity, resource, reserve, mineability, or economics as a visual conclusion.

## Quality Gates

- Generated project contains `package.json`, `src/App.tsx`, `src/scene-data.ts`, and `scripts/verify.mjs`.
- Scene renders nonblank canvas at desktop and mobile viewport sizes.
- Text labels do not overlap controls.
- Evidence/provenance panel shows data source status and caveats.
- Any real GIS layer must preserve CRS, scale/resolution, source URL, license, and retrieval status.
