# Canada-First Geoscience Data Sources

GeoMine Research v0.1 is a source-planning and evidence-synthesis plugin. It may recommend these sources, but it must not claim live retrieval unless a real tool or script fetches data during the current run.

## NRCan CDoGS

- Jurisdiction: Canada.
- Data type: regional geochemical surveys, sample locations, survey metadata.
- Likely formats: CSV, GIS exports, database records.
- Use case: regional geochemical screening, sample-media review, background values, anomaly planning.
- Provenance notes: preserve survey id, sample medium, analytical method, detection limits, release date, and license.
- Limitations: survey coverage, sample medium, analytical methods, and detection limits vary.

## Geo.ca

- Jurisdiction: Canada.
- Data type: federal and open-government geospatial catalog records.
- Likely formats: catalog metadata, WMS, WFS, KML, CSV, Shapefile, GeoPackage links.
- Use case: data discovery, metadata review, license lookup, linked-source discovery.
- Provenance notes: preserve catalog title, publisher, last updated date, access URL, license, and linked source.
- Limitations: catalog discovery is not data retrieval.

## BC MINFILE

- Jurisdiction: British Columbia.
- Data type: mineral occurrences, commodities, deposit types, status, historic notes.
- Likely formats: database records, GIS, CSV.
- Use case: nearby occurrence review, deposit-model context, commodity history.
- Provenance notes: preserve MINFILE id, record date, location confidence, commodities, and source notes.
- Limitations: historic resource or production language must be treated cautiously.

## BC Geological Survey Data Portals

- Jurisdiction: British Columbia.
- Data type: geology, geochemistry, geophysics, geochronology, publications.
- Likely formats: ArcGIS REST, CSV, Shapefile, GeoPackage, PDF.
- Use case: bedrock geology, structural context, geochemical and geophysical screening.
- Provenance notes: preserve map id, product id, scale, release year, CRS, and license.
- Limitations: compilation scale and vintage may not support target-scale conclusions.

## Ontario OGSEarth And Ontario Mineral Inventory

- Jurisdiction: Ontario.
- Data type: KML/KMZ GIS layers, bedrock geology, surficial geology, geochemistry, geophysics, drillholes, OMI occurrences.
- Likely formats: KML, KMZ, Shapefile, ArcGIS REST, CSV.
- Use case: Ontario claim screening, LCT pegmatite context, occurrence review.
- Provenance notes: preserve OGS layer name, OMI id, update date, CRS, and metadata URL.
- Limitations: KML layers may require conversion; records can mix historic and current interpretations.

## Provincial And Territorial Geological Surveys

- Jurisdiction: Canadian provinces and territories.
- Data type: geology, assessment reports, geochemistry, geophysics, tenure, open files.
- Likely formats: PDF, GIS, CSV, ArcGIS REST, map services.
- Use case: jurisdiction-specific data discovery and assessment-report planning.
- Provenance notes: preserve agency, publication id, report id, scale, and license.
- Limitations: access patterns and metadata quality vary by jurisdiction.

## USGS Mineral Data

- Jurisdiction: United States and global extension.
- Data type: mineral occurrences, geology, geochemistry, geophysics.
- Likely formats: REST, CSV, GIS, database exports.
- Use case: cross-border comparison and global extension.
- Provenance notes: preserve USGS dataset, query date, version, and coordinate reference details.
- Limitations: use as an extension source for Canadian AOIs, not a replacement for Canadian government data.

## EarthChem

- Jurisdiction: global extension.
- Data type: rock geochemistry, petrology, sample-level records.
- Likely formats: portal export, CSV, database records.
- Use case: regional geochemical background and petrogenetic comparisons.
- Provenance notes: preserve repository, sample id, method, citation, and download date.
- Limitations: coverage and analytical comparability vary by contributing database.
