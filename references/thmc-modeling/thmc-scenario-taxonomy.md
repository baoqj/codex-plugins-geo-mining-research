# THMC Scenario Taxonomy

| Scenario | Dominant processes | Typical active fields | Key reactions | Required data | Typical solvers | Expected outputs |
|---|---|---|---|---|---|---|
| acid_mine_drainage | seepage, oxidation, acidity, metals | H/C, often T | pyrite oxidation, carbonate neutralization, Fe/Al hydroxides | flow, oxygen, sulfide minerals, pH, sulfate, metals | PHREEQC, PFLOTRAN, OGS-PHREEQC | pH, sulfate, metals, neutralization |
| radionuclide_transport | decay, sorption, reactive transport | H/C, often T | decay chain, sorption, carbonate complexation | radionuclides, pH, Eh, minerals, sorption | PHREEQC, OGS-PHREEQC, PFLOTRAN | concentrations, dose proxies |
| uranium_mine_groundwater | fractured flow, redox, carbonate control | H/C or THC | U(VI)/U(IV), Ra/Rn/Pb/Po, adsorption | fractures, water chemistry, mineralogy | PHREEQC, OGS-PHREEQC | plume, speciation, risk indicators |
| tailings_seepage | leachate generation and migration | HC/THC/HMC | sulfate, metals, secondary minerals | tailings chemistry, seepage, seasonal T | PHREEQC, PFLOTRAN | seepage chemistry |
| nuclear_waste_repository | heat, diffusion, sorption, barriers | THMC | cation exchange, radionuclide sorption, mineral alteration | thermal, bentonite, porewater, mechanics | OGS-PHREEQC, COMSOL, PFLOTRAN | long-term evolution |
| bentonite_buffer_evolution | swelling, heat, groundwater intrusion | THMC | cation exchange, mineral transformation | swelling, porewater, heat, diffusion | OGS-PHREEQC, COMSOL | buffer evolution |
| geothermal_fluid_rock_interaction | high-T flow and scaling | THMC | silica, carbonate scaling, metal mobility | T, flow, chemistry, fractures | PFLOTRAN, COMSOL, PHREEQC | scaling, injectivity |
| co2_storage_reactive_transport | acidification, mineral trapping | THC/HMC | carbonate reactions, dissolution/precipitation | pressure, CO2, brine, minerals | PFLOTRAN, OGS | trapping, pH, porosity |
| fractured_rock_contaminant_transport | fracture flow and matrix diffusion | HC/HMC | sorption, diffusion, decay if relevant | fracture network, tracer, chemistry | OGS, PFLOTRAN | breakthrough |
| mining_heat_pollution | heat plume in groundwater | TH/THC | optional temperature-dependent chemistry | heat source, flow, T profile | COMSOL, OGS | temperature field |
| groundwater_metal_mobility | metals and redox transport | HC/THC | complexation, sorption, redox | chemistry, minerals, flow | PHREEQC, PFLOTRAN | metal mobility |
| long_term_environmental_risk | scenario prediction | HC/THC/THMC | scenario-specific | monitoring, parameters, uncertainty | route-specific | risk indicators |
| reactive_transport_benchmark | method verification | H/HC/THC | benchmark-specific | benchmark data | Python, PHREEQC, OGS | verification metrics |
| custom_thmc_model | user-defined | user-defined | user-defined | user-defined | route-specific | modeling package |

