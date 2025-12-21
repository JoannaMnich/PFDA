




## Project
Historical weather data were obtained from the Met Éireann website.
As the data are provided separately for individual stations, an automated data collection process was implemented using Python to download, clean, and merge multiple datasets into a single unified dataset suitable for analysis.
The analysis focuses on the period from 2005 onwards, as this is the earliest year for which consistent and complete monthly wind data are available across the selected meteorological stations. This ensures data comparability and reduces the impact of missing values.
Ten meteorological stations were selected to ensure balanced geographical coverage across Ireland, including northern, southern, eastern, and western regions, as well as coastal and inland locations.
This selection reduces location bias and allows meaningful comparison of wind speed patterns across different climatic regions.

Selected meteorological stations by region

North: Malin Head

South: Roches Point, SherkinIsland, Valentia Observatory

East: Dublin Airport, Phoenix Park, Casement Aerodrome

West: Belmullet

Central (inland): Mullingar, Claremorris

## Project structure

- `project.ipynb` – data acquisition, cleaning, aggregation, and analysis
- `data/raw/` – raw hourly wind data downloaded from Met Éireann
- `data/processed/` – cleaned and aggregated monthly wind datasets

## Cleaning

Some stations have missing data for certain months or years. Missing months are either removed or represented as NaN to maintain consistent time indices across all stations.