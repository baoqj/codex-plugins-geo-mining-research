# Academic Figure Package Skill

This skill plans publication-style academic figure packages for GeoMine Research and general research writing. It creates figure inventory, figure specifications, visual grammar, layout plans, drawing prompts, script plans, captions, validation checklists, and JSON manifests.

Use it for paper figures, GIS maps, geochemical anomaly maps, groundwater/radionuclide conceptual models, mining exploration figures, workflow diagrams, technical-report figures, and graphical abstracts.

It integrates with GeoMine Research by consuming router outputs, evidence matrices, geodata plans, geochemical interpretations, academic paper plans, and visualization SceneSpec concepts. It does not require MCP, live web access, or GUI software.

Example input:

```text
Create a complete Figure Package for a paper on U-Ra-Rn-Po-Pb radionuclide migration in uranium mining area groundwater.
```

Example output:

```text
Figure inventory, each figure spec, visual grammar, drawing prompt, script plan, caption, publication checklist, and JSON manifest.
```

Validation scripts:

```bash
python skills/figure-generation/academic-figure-package-skill/scripts/validate_figure_package.py skills/figure-generation/academic-figure-package-skill/examples/uranium-groundwater-figure-package.md
python skills/figure-generation/academic-figure-package-skill/scripts/build_figure_manifest.py input.md --output manifest.json
```

Current limits:

- It does not create final accepted journal artwork automatically.
- AI-generated images are treated as editable sketches.
- Final GIS, mining, legal, QP, investment, and data interpretations require expert review.
