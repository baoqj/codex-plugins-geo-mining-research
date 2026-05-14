# Electric-Field Coupling and Radiolytic Source Terms in Saturated Porous Media

## Abstract

This example illustrates how GeoMine Research should frame a publication-style paper on radiolysis and electrolysis in saturated porous media. The draft focuses on a bounded mechanistic question: how confinement, mineral surfaces, pore-scale transport, and electric fields may alter radical survival, hydrogen generation, and redox gradients compared with bulk water. The paper does not claim demonstrated industrial hydrogen production. It presents a hypothesis-driven framework, identifies measurable variables, and lists the experimental and modeling evidence required before any feasibility statement.

## Keywords

Porous media; radiolysis; electrolysis; groundwater; hydrogen; reactive transport; G-value; mineral surface catalysis.

## Introduction

Radiolysis of water produces hydrated electrons, hydroxyl radicals, hydrogen atoms, molecular hydrogen, hydrogen peroxide, and associated ionic species. In bulk water these yields are commonly described through G-values, but porous media introduce mineral surfaces, restricted diffusion, local electric fields, heterogeneous dose deposition, and pore-scale residence times. These features may change radical recombination and product migration.

This paper treats porous radiolysis as a coupled radiation-chemistry, electrochemical, and transport problem. The central objective is to formalize the governing variables and evidence requirements for evaluating whether an applied electric field can modify product distributions in water-filled pores.

## Research Questions and Hypotheses

RQ1: How do pore size, mineral surface area, and pore-water chemistry modify the effective radiolytic source terms relative to bulk water?

RQ2: Under what boundary conditions can an applied electric field separate charged radiolytic products before recombination?

RQ3: Which measurements are required to distinguish enhanced hydrogen generation from redistribution of pre-existing products?

H1: Confined pore networks alter effective G-values through surface scavenging, radical adsorption, and diffusion-limited recombination.

H2: Electric-field effects are only meaningful when charge migration timescales are shorter than recombination and surface quenching timescales.

H3: Industrial hydrogen production is hypothesis only unless supported by energy balance, radiation source accounting, gas recovery efficiency, safety analysis, and regulatory assessment.

## Literature Review

The literature review should compare bulk-water radiolysis, mineral-surface radiation chemistry, porous reactive transport, electrolysis in confined media, and nuclear-waste groundwater contexts. Each source must be verified before inclusion. Example placeholders:

- Source to verify: review literature on water radiolysis product yields and G-values.
- Source to verify: studies of oxide and clay mineral surface effects on radical scavenging and hydrogen generation.
- Source to verify: reactive transport models for redox species in saturated porous media.
- Source to verify: radiation safety and hydrogen management guidance for nuclear facilities.

## Theoretical Framework

Water radiolysis is represented as a source term coupled to transport and reaction:

```math
\mathrm{H_2O}
\xrightarrow{\mathrm{ionizing\ radiation}}
e_{aq}^{-} + \mathrm{\cdot OH} + \mathrm{H\cdot}
+ \mathrm{H_3O^{+}} + \mathrm{OH^{-}}
+ \mathrm{H_2} + \mathrm{H_2O_2}
```

For species `i`, the volumetric radiolytic production term is:

```math
S_i^{rad} = \rho_w \dot{D}_w G_i
```

where `rho_w` is pore-water density, `dot{D}_w` is pore-water absorbed dose rate, and `G_i` is the radiolytic yield of species `i` after unit conversion. In this notation `rho_w` uses `w` as a subscript, `dot{D}_w` denotes the time derivative or rate-like dose term for water, and `m^{-3}` denotes inverse cubic meters.

A minimal reactive transport balance is:

```math
\frac{\partial C_i}{\partial t}
+ \nabla \cdot \left(-D_i^{eff}\nabla C_i + z_i u_i F C_i \nabla \phi\right)
= S_i^{rad} + R_i(C, pH, E_h, A_s)
```

## Methods / Model Formulation

The proposed method uses three linked analyses:

1. Bulk-water baseline: compile verified G-values and recombination rates under comparable temperature, pH, ionic strength, and dose-rate conditions.
2. Porous-media correction: represent mineral surface area, tortuosity, pore-size distribution, and adsorption/scavenging terms.
3. Field-coupled transport: test whether electric migration and diffusion can change product separation before recombination.

No numerical result should be reported unless the input values, units, and source provenance are recorded.

## Mechanistic Analysis

Bulk water and porous media differ in at least five mechanisms: surface quenching, catalytic hydrogen recombination, restricted radical diffusion, heterogeneous dose deposition near mineral grains, and pore-scale redox stratification. The strongest claim permitted without experiment is that porous media can plausibly alter effective product distributions. Quantitative enhancement remains requires further evidence.

## Equation Registry

| Equation ID | Equation | Variables | Units | Assumptions | Boundary Conditions |
| --- | --- | --- | --- | --- | --- |
| EQ-1 | `S_i^{rad} = rho_w dot{D}_w G_i` | `S_i^{rad}` source term; `rho_w` water density; `dot{D}_w` dose rate; `G_i` yield | `mol m^{-3} s^{-1}` after conversion | Homogeneous absorbed dose within representative pore volume | Saturated pore water, known porosity, known dose-rate field |
| EQ-2 | Reactive transport balance | `C_i`, `D_i^{eff}`, `z_i`, `u_i`, `F`, `phi`, `R_i` | concentration, diffusion, charge, mobility, potential, reaction rate | Continuum approximation at representative elementary volume | No-flux or specified concentration boundaries; defined electric potential |

## Evidence Matrix

| Claim | Evidence Type | Current Support | Confidence | Additional Evidence Needed | Limitations |
| --- | --- | --- | --- | --- | --- |
| Porous media can alter effective radiolytic yields | Literature and mechanism | Source verification required | Medium | Controlled pore-size experiments; mineral-specific surfaces | Mineralogy and water chemistry are confounding variables |
| Electric fields may reduce recombination for charged products | Equation and inference | Timescale analysis required | Low | Field-strength experiments; radical lifetime measurements | Neutral radicals and surface reactions may dominate |
| Industrial hydrogen production is not established | Boundary analysis | Energy and safety constraints unresolved | High | Energy balance; gas recovery; radiation source accounting | Not a feasibility conclusion |

## Discussion

The proposed framework reframes the problem from "does radiation make hydrogen" to "under which coupled transport, reaction, and surface conditions can product separation or survival change measurably." This is more defensible because it separates mechanism from feasibility. A publishable study would require controlled samples, known dose-rate fields, verified chemistry, gas measurements, and a model that can reproduce negative controls.

## Industrial and Environmental Implications

Any industrial hydrogen claim must define input radiation source, absorbed dose, electrical work, gas capture efficiency, radiolytic product hazards, explosion controls, and regulatory setting. In nuclear-waste or underground facilities, the same mechanisms may matter more for redox alteration, corrosion, gas pressure, and radionuclide migration than for hydrogen production.

## Safety and Regulatory Boundary

This example is not a design for radiation use, hydrogen production, nuclear-facility operation, or environmental compliance. Radiation handling, hydrogen accumulation, and nuclear-site work require qualified safety, engineering, and regulatory review.

## Limitations

- The draft does not include verified G-values, rate constants, dose fields, or mineral-specific experiments.
- The electric-field mechanism is hypothesis only until timescale and measurement evidence are provided.
- Continuum transport equations may fail in nanopores or highly heterogeneous media.
- Feasibility cannot be inferred from chemical plausibility.

## Conclusion

Porous media can plausibly modify radiolytic source terms and radical survival relative to bulk water, but the magnitude and direction of the effect depend on mineralogy, pore geometry, water chemistry, dose rate, and field strength. The correct academic posture is a bounded mechanistic hypothesis with explicit equations and evidence needs, not a feasibility claim.

## Future Work

- Build a verified literature table for bulk-water and mineral-surface radiolysis.
- Design controlled experiments comparing bulk water, inert porous media, and reactive minerals.
- Couple dose-rate fields with reactive transport and gas measurements.
- Test electric-field effects under safety-reviewed laboratory conditions.

## References

- Reference placeholder: verified review on water radiolysis product yields and G-values.
- Reference placeholder: verified experimental paper on mineral-surface radiation chemistry.
- Reference placeholder: verified reactive transport reference for charged species in porous media.
- Reference placeholder: verified radiation safety and hydrogen management guidance.

## Appendix: Symbols and Units

| Symbol | Definition | Unit |
| --- | --- | --- |
| `rho_w` | Pore-water density | `kg m^{-3}` |
| `dot{D}_w` | Absorbed dose rate in pore water | `Gy s^{-1}` |
| `G_i` | Radiolytic yield of species `i` | converted to `mol J^{-1}` |
| `S_i^{rad}` | Radiolytic source term for species `i` | `mol m^{-3} s^{-1}` |
| `C_i` | Concentration of species `i` | `mol m^{-3}` |

## Peer Review Checklist

- Research questions and hypotheses are explicit.
- Bulk water and porous media are compared.
- Equations define variables, units, assumptions, and boundary conditions.
- Unsupported feasibility claims are excluded.
- References are placeholders until verified.
