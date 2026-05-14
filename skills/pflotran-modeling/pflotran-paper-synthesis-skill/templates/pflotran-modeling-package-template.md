# PFLOTRAN Modeling Package

## 1. Research Objective

## 2. Scenario Classification

## 3. Why PFLOTRAN Is Appropriate

## 4. Relationship to THMC / PHREEQC / GeoMine Workflow

## 5. Conceptual Model

## 6. Process Mode Selection

## 7. Model Domain and Grid

## 8. Regions and Material Properties

## 9. Initial Conditions

## 10. Boundary Conditions

## 11. Flow and Transport Configuration

## 12. Chemistry Configuration

## 13. Thermal-Hydrologic-Chemical Coupling, if applicable

## 14. Geomechanics Scope, if applicable

## 15. Generated PFLOTRAN Input Deck Skeleton

```pflotran
# Insert draft input deck skeleton here.
```

## 16. Database and Reaction Network Requirements

## 17. Run Command and Execution Plan

## 18. Output / Observation Design

## 19. Calibration and Validation Plan

## 20. Sensitivity and Uncertainty Plan

## 21. Expected Figures and Tables

## 22. Paper-ready Methods Draft

## 23. Paper-ready Results Interpretation Plan

## 24. Limitations and Assumptions

## 25. Future MCP / Remote Compute Extension

Future tools should remain optional and default-off unless explicitly installed:

- `validate_input_deck`
- `run_pflotran_local`
- `submit_pflotran_remote`
- `get_run_status`
- `fetch_run_logs`
- `fetch_pflotran_outputs`
- `query_mesh_from_postgis`
- `fetch_parameter_field_from_r2`
- `save_model_version`
- `save_run_record`
- `parse_observation_output`
- `generate_result_summary`

## 26. Machine-readable Model Manifest

```json
{
  "package_type": "PFLOTRAN Modeling Package",
  "version": "0.1",
  "research_objective": "",
  "scenario": "",
  "solver_family": "PFLOTRAN",
  "relationship_to_thmc": "solver-specific implementation of selected THMC/THC process model",
  "process_modes": {
    "flow": "",
    "transport": "",
    "reactive_transport": true,
    "thermal": false,
    "geomechanics": false
  },
  "domain": {
    "dimension": "1D/2D/3D",
    "grid_type": "structured/unstructured",
    "extent": [],
    "regions": []
  },
  "materials": [],
  "initial_conditions": [],
  "boundary_conditions": [],
  "chemistry": {
    "database": "",
    "primary_species": [],
    "secondary_species": [],
    "minerals": [],
    "kinetic_reactions": [],
    "sorption": [],
    "ion_exchange": [],
    "notes": []
  },
  "execution": {
    "input_file": "model.in",
    "database_file": "",
    "run_command": "pflotran -pflotranin model.in",
    "mpi_processes": null,
    "status": "draft_not_executed"
  },
  "outputs": {
    "observation_points": [],
    "variables": [],
    "figure_plan": []
  },
  "limitations": [],
  "missing_data": []
}
```
