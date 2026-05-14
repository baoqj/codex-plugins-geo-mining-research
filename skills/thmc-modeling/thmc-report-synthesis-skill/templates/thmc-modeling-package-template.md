# THMC Groundwater Chemistry Modeling Package

## 1. Research Objective

State the scientific objective and applied context.

## 2. Scenario Classification

- Scenario type:
- Coupling level:
- Active processes:
- Spatial scale:
- Time scale:
- Modeling purpose:

## 3. Conceptual THMC Model

Describe the geological/hydrogeological/chemical system.

Include:
- model domain
- geological units
- groundwater pathways
- heat sources or thermal gradients
- mechanical features
- reaction zones
- observation points

## 4. THMC Coupling Matrix

| From / To | Thermal | Hydrological | Mechanical | Chemical |
|---|---|---|---|---|
| Thermal | - | | | |
| Hydrological | | - | | |
| Mechanical | | | - | |
| Chemical | | | | - |

## 5. Model Domain and Geometry

- 1D column / 2D cross-section / 3D domain / fractured network
- Representative elementary volume or discrete fracture network
- Boundary geometry
- Mesh or discretization concept

## 6. Primary Variables

| Field | Primary variables | Meaning | Unit |
|---|---|---|---|
| Thermal | T | Temperature | K or deg C |
| Hydrological | p, h, q, S_w | Pressure/head/flux/saturation | mixed |
| Mechanical | u, sigma, epsilon | Displacement/stress/strain | mixed |
| Chemical | C_i, SI, mineral volume | Species, saturation index, minerals | mixed |

## 7. Governing Equations

### 7.1 Flow Equation

### 7.2 Solute / Reactive Transport Equation

### 7.3 Heat Transport Equation

### 7.4 Mechanical Equilibrium Equation

### 7.5 Chemical Reaction Terms

## 8. Boundary and Initial Conditions

| Category | Boundary / initial condition | Required data | Notes |
|---|---|---|---|
| Thermal | | | |
| Hydrological | | | |
| Mechanical | | | |
| Chemical | | | |

## 9. Geochemical Reaction Network

### 9.1 Aqueous Species

### 9.2 Minerals

### 9.3 Gas Phase, if any

### 9.4 Surface Complexation / Sorption

### 9.5 Ion Exchange

### 9.6 Redox Reactions

### 9.7 Kinetic Reactions

### 9.8 Radioactive Decay Chain, if relevant

## 10. Parameters and Data Requirements

| Parameter | Symbol | Field | Unit | Source / required measurement | Priority |
|---|---|---|---|---|---|

## 11. Solver / Software Recommendation

Compare:
- PHREEQC alone
- Python + PHREEQC / PhreeqcRM
- COMSOL + PHREEQC
- OpenGeoSys + PHREEQC
- PFLOTRAN
- CrunchFlow / MIN3P, optional
- PINN / PyTorch surrogate

## 12. Implementation Plan

- Prototype level
- Numerical model level
- Calibration level
- Publication / reporting level

## 13. Calibration and Validation Plan

- Calibration targets
- Validation datasets
- Benchmark cases
- Goodness-of-fit metrics
- Model rejection criteria

## 14. Sensitivity and Uncertainty Plan

- Key uncertain parameters
- Sensitivity design
- Scenario uncertainty
- Parameter uncertainty
- Structural uncertainty

## 15. Expected Outputs

- concentration fields
- pH / Eh / saturation index
- mineral volume change
- porosity / permeability evolution
- temperature field
- hydraulic head / flow velocity
- stress / deformation, if active
- risk indicators

## 16. Publication Figure Plan

- Figure 1: Conceptual THMC model
- Figure 2: Coupling matrix
- Figure 3: Model domain and boundary conditions
- Figure 4: Reaction network
- Figure 5: Calibration / validation plots
- Figure 6: Spatial-temporal simulation outputs
- Figure 7: Sensitivity and uncertainty results

## 17. Limitations and Assumptions

Include assumptions, excluded processes, data gaps, scale limitations, parameter uncertainty, and professional-review caveats.

## 18. Machine-readable JSON Model Spec

```json
{}
```

