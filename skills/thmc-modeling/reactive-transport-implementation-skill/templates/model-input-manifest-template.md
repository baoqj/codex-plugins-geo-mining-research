# Model Input Manifest

| File / dataset | Type | Required for | Source | Status | Notes |
|---|---|---|---|---|---|
| geometry | domain | mesh | user / GIS / section | required |  |
| hydraulic_parameters.csv | parameters | flow | field / literature | required |  |
| chemistry_database.dat | database | reactions | thermodynamic database | required |  |
| initial_solution.csv | chemistry | initial conditions | lab / field | required |  |
| boundary_conditions.md | model config | all fields | conceptual model | required |  |
| calibration_targets.csv | observations | calibration | monitoring | recommended |  |

