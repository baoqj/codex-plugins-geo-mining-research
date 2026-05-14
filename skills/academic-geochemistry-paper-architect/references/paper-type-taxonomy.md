# Geochemistry Paper Type Taxonomy

Classify the paper before writing. State primary, secondary, and tertiary paper types when the topic is mixed.

## Data Paper / Database Paper

Trigger terms: database, compilation, dataset, repository, schema, data structure, CSV, SQL, metadata, FAIR, public data.

Core question: How is a reusable geochemical dataset constructed, standardized, quality-controlled, and made useful?

Typical sections: Introduction; existing databases; data sources; database structure; processing and QA/QC; data statistics; computed properties; data/code availability; limitations; conclusions.

Required data: sample identifiers, coordinates, lithology/sample medium, analytes, units, analytical methods, detection limits, source citation, version, license, quality flags.

Figures/tables: database schema, sample distribution map, age histogram, element-count histogram, lithology/sample-medium breakdown, source table, field dictionary, QA/QC workflow.

## Regional Geochemical Characterization Paper

Trigger terms: regional geochemistry, background values, spatial pattern, lithology control, soil, sediment, lake water, whole-rock, regional survey.

Core question: What geochemical patterns exist in the region, and what geological controls explain them?

Typical sections: Introduction; geological setting; sampling and methods; QA/QC; major/trace elements; spatial patterns; associations/anomalies; geological controls; implications; conclusions.

Figures/tables: study/sampling map, anomaly maps, correlation matrix, PCA, clustering, boxplots by lithology, REE patterns, spider diagrams, threshold table.

## Mineral Exploration Geochemistry Paper

Trigger terms: mineral exploration, anomaly, pathfinder, target, prospectivity, claim, mineral occurrence, U-Th-K, GIS overlay, weights of evidence.

Core question: Which geochemical signals are consistent with mineral-system processes, and how should targets be ranked without overstating economic significance?

Typical sections: Introduction; geological/mineral-system framework; data/methods; anomaly definition; multi-element associations; spatial integration; target ranking; uncertainty and disclosure boundaries; conclusions.

Figures/tables: anomaly maps, pathfinder association plots, PCA/factor-loading plots, prospectivity maps, target ranking table, evidence-layer workflow.

## Petrogenesis Paper

Trigger terms: petrogenesis, magma source, fractionation, crustal assimilation, tectonic setting, granitoid, basalt, Harker, TAS, REE, spider.

Core question: What processes explain the origin and evolution of the rocks?

Typical sections: Introduction; geological setting; petrography; analytical methods; major/trace geochemistry; isotopic/age constraints; petrogenetic modeling; tectonic implications; conclusions.

Figures/tables: TAS/QAPF, Harker diagrams, REE patterns, primitive mantle normalized spider diagrams, discrimination diagrams, isotope evolution diagrams, age distributions.

## Isotope Geochemistry Paper

Trigger terms: Sr, Nd, Pb, Hf, O, C, S, zircon, crustal growth, mantle source, isotope evolution, Archean, provenance.

Core question: What isotopic evidence constrains source, age, mixing, crustal evolution, or fluid origin?

Figures/tables: isotope ratio plots, epsilon-time diagrams, concordia/age plots, mixing models, source comparison tables.

## Hydrogeochemistry Paper

Trigger terms: groundwater, pH, Eh, alkalinity, HCO3, charge balance, Piper, Gibbs, PHREEQC, speciation, saturation index.

Core question: What chemical controls govern groundwater composition, solute mobility, and mineral saturation?

Typical sections: hydrogeological setting; water sampling and QA/QC; major ions; trace/radionuclide chemistry; speciation/saturation; controlling processes; uncertainty; conclusions.

Figures/tables: Piper, Stiff, Gibbs, Eh-pH, saturation-index plot, speciation fraction plot, reaction-path diagram, breakthrough curve, charge-balance table.

## Environmental Geochemistry Paper

Trigger terms: contamination, acid mine drainage, tailings, seepage, baseline, risk, metal mobility, remediation, ecological or human exposure.

Core question: Which geochemical processes control contaminant release, transport, attenuation, or baseline variability?

Figures/tables: concentration maps, pH/Eh diagrams, metal-sulfate plots, adsorption/precipitation conceptual models, exceedance tables with regulatory context when appropriate.

## Reactive Transport Modelling Paper

Trigger terms: reactive transport, PHREEQC transport, PhreeqcRM, PFLOTRAN, OpenGeoSys, THMC, breakthrough, boundary condition, kinetic reaction.

Core question: How do flow, transport, and reactions jointly explain observed or hypothesized geochemical evolution?

Typical sections: conceptual model; governing equations; parameterization; boundary/initial conditions; numerical implementation; verification/calibration; results; sensitivity; limitations.

Figures/tables: conceptual model, domain/grid, reaction network, breakthrough curves, spatial concentration fields, saturation-index evolution, sensitivity plots, parameter table.

## Experimental Geochemistry Paper

Trigger terms: experiment, batch, column, reactor, kinetics, temperature, pressure, sorption, dissolution, precipitation.

Core question: Which controlled experiment constrains reaction rates, partitioning, or mechanisms?

Figures/tables: experimental setup, time-series plots, rate fits, mass balance, microscopy/mineral evidence, parameter estimation table.

## Radiolysis / Nuclear Geochemistry Paper

Trigger terms: radiolysis, G-value, dose rate, LET, radicals, hydrated electron, H2, H2O2, radionuclide, nuclear waste, bentonite, copper canister.

Core question: How does radiation chemistry alter redox state, gas generation, radionuclide mobility, or engineered/natural barrier performance?

Figures/tables: radiolysis reaction network, G-value comparison, pore-size effect, dose-rate effect, radical lifetime, redox/speciation evolution, nuclear-safety boundary table.

## Geochemical Modelling and Machine Learning Paper

Trigger terms: machine learning, classifier, random forest, neural network, prediction, feature importance, clustering, prospectivity score, surrogate model.

Core question: Can a transparent model explain or predict geochemical patterns without overfitting or hiding geological meaning?

Figures/tables: feature engineering workflow, train/test split, cross-validation, feature importance, ROC/AUC if classification is valid, confusion matrix, uncertainty/transferability table.

## Review / Perspective Paper

Trigger terms: review, progress, future directions, synthesis, conceptual framework, perspective, literature.

Core question: What is known, what is uncertain, and what framework or research agenda resolves the field's next problems?

Do not present a review as a new-data paper. Separate evidence synthesis from speculative perspective.

## Technical Note / Methods Paper

Trigger terms: method, workflow, protocol, benchmark, tool, reproducible pipeline, validation, comparison.

Core question: What method or workflow is introduced, benchmarked, and made reproducible?

Figures/tables: workflow diagram, benchmark datasets, validation table, comparison against existing methods, failure-mode table.
