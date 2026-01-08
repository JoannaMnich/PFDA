# Project
Historical weather data were obtained from the Met Éireann website.
As the data are provided separately for individual stations, an automated data collection process was implemented using Python to download, clean, and merge multiple datasets into a single unified dataset suitable for analysis.
The analysis focuses on the period from 2005 onwards, as this is the earliest year for which consistent and complete monthly wind data are available across the selected meteorological stations. This ensures data comparability and reduces the impact of missing values.
Ten meteorological stations were selected to ensure balanced geographical coverage across Ireland, including northern, southern, eastern, and western regions, as well as coastal and inland locations.
This selection reduces location bias and allows meaningful comparison of wind speed patterns across different climatic regions.

Selected meteorological stations by region

North: Malin Head

South: Roches Point, SherkinIsland, 

East: Dublin Airport, Casement Aerodrome

West: Belmullet, Valentia Observatory

Central (inland): Mullingar, Claremorris, Mt Dillon

## Project structure

- `project.ipynb` – data acquisition, cleaning, aggregation, and analysis
- `data/raw/` – raw hourly wind data downloaded from Met Éireann
- `data/processed/` – cleaned and aggregated monthly wind datasets

## Cleaning
Some stations have missing data for certain months or years. Missing months are either removed or represented as NaN to maintain consistent time indices across all stations.

Although some station files are clean enough to be parsed directly, others contain inconsistent formatting.
Therefore, numeric type normalization was applied uniformly across all datasets.
Column names were normalised to lowercase and stripped of whitespace before type conversion to ensure consistency across stations
Due to non-standard metadata headers in Met Éireann station files, column names were explicitly defined during import to ensure consistent parsing across stations.

## Data Cleaning Pipeline for Weather Station CSV Files
This script provides a reusable data-cleaning pipeline for multiple Irish weather stations.
It avoids code duplication by using a single function that can be applied to all stations.

The cleaning pipeline automatically detects the row containing the column headers (year, month, wdsp), loads the CSV data while skipping metadata rows, normalizes column names, converts relevant columns to numeric values, filters data to the period 2005–2025, removes rows with missing wind speed values, keeps only the relevant columns, saves a cleaned CSV file for each station.

## Understanding  Data
A cleaned dataset has: year,month,wdsp,station
wdsp = mean wind speed for that month 
station = location

###    For wind power estimation, we need to consider:
Mean wind speed → baseline power potential.
Operational range of wind turbines → usually turbines only operate between a cut-in and cut-out speed.
Variability → min, max, or standard deviation of wind speeds.

## Analysing data
To analyse mean wind speed, I create a master DataFrame by merging all processed station files and adding a station column. This will give one tidy dataset for analysis.

### Analyse mean wind speed from merged station script
This table shows the average wind speed at each station over the 20-year period. Higher values indicate stronger potential for wind energy. Wind farms typically operate best within a specific wind range, so both mean and range (min/max) are important for assessing usable power.
This table shows the mean, minimum, and maximum wind speeds at each station. Wind farms have operational limits; therefore knowing the extremes helps estimate how often turbines will operate at full capacity.

### Monthly average wind speed plot for each station
The monthly wind speed values represent the mean of all observations for a given month across approximately 20 years, providing a long-term seasonal wind pattern for each station.

### Annual wind speed trends 2005-2025
Annual mean wind speeds were calculated for each weather station using cleaned observational data from 2005 to 2025. Any aggregated master rows were removed to ensure only individual station data were included.
For each station, a linear regression was applied to the annual mean wind speed values to quantify long-term trends. The slope of the regression line indicates whether wind speeds are increasing or decreasing over time.
The results are visualised as time series plots for each station, showing annual mean values alongside the corresponding regression slope. This allows for comparison of trends between stations and provides insight into long-term changes in wind behaviour.

### Machine Learning Approach: Linear Regression (Scikit-learn)
The linear regression model achieved an RMSE of approximately 2.5, indicating
a moderate prediction error. The negative R² value suggests that annual mean
wind speed is not strongly explained by a simple linear relationship with time,
which is expected for climatic data influenced by multiple factors.
- Suggested Model Improvement:
A potential improvement to the regression model would be to use monthly data
instead of annual averages. Wind speed is known to exhibit strong seasonal
patterns, and aggregating the data to yearly means may remove important
variability. Using monthly observations would allow the model to capture both
long-term trends and seasonal effects, potentially improving predictive
performance and model interpretability.

### Monthly Seasonal Wind Pattern and Variability per Station
This block calculates the average wind speed per month for each station over the 20-year period.
It also computes the standard deviation per month to show the variability of wind speeds.
The results can help identify seasonal patterns and assess the stability of wind resources, which is important for wind energy planning.
If the standard deviation is small and the annual trend is stable → future years will likely be similar
If the standard deviation is large or the trend is variable → risk must be considered in wind energy planning

## Power output next week (forecast)
A 7-day wind speed forecast was estimated for four representative stations in Ireland (Dublin Airport, Malin Head, Roches Point, and Belmullet). The forecast is based on historical monthly average wind speeds for the current month. Predicted wind speeds are converted into estimated power output using a simple linear relation P=k×V, where k is a constant representing turbine size and efficiency. This provides a short-term projection of wind conditions and potential energy generation.

Wind speed and estimated power output are plotted on separate axes due to their different scales. While wind speed varies moderately over the week, the estimated power output shows larger fluctuations due to its cubic dependence on wind speed.

## Trend Analysis for a wind speeds in the next 10 years
he 10-year wind speed forecast is based on annual mean wind speed values.
Monthly forecasting was considered; however, the annual aggregation process removes the monthly variable, making seasonal modelling impossible at this stage.
A monthly forecast would require the use of non-aggregated monthly data and would allow the model to capture seasonal variability in wind patterns.
A linear regression model was trained separately for each weather station using annual mean wind speed data.
The model was then used to forecast wind speed trends for the period 2026–2035.
Annual aggregation was selected to analyse long-term trends, while seasonal variability is discussed as a potential extension using monthly data.
Most stations show stable trends, while a few indicate a slight increase/decrease

## Future work
What anything else I can think of?

1. This study is based on annual mean wind speed data, which allows long-term trend analysis but does not capture seasonal variability. Additionally, the use of a simple linear regression model may not fully reflect complex or non-linear wind patterns.
Future work could involve using monthly data to model seasonality and applying more advanced machine learning techniques to improve forecasting accuracy.

2. Develop a script to automate report generation for new data, making it easier to update analyses without manual work.

## Other Weather Metrics Worth Analyzing
While this project focuses on wind speed for evaluating wind energy potential, it is also valuable to consider other weather variables that could influence wind patterns and, consequently, wind power production. Metrics such as temperature, rainfall, or atmospheric pressure may have correlations with wind speed.

Analyzing these relationships can help identify conditions under which wind speed is higher or lower, and improve predictions of energy output for wind farms. For example, computing correlations between wind speed and temperature or precipitation could reveal seasonal or meteorological patterns that affect turbine performance. Understanding these interactions allows for more accurate forecasting and planning for wind energy generation.

# Conclusion 

The results show that wind conditions are consistent and reliable across the analysed stations. Wind energy potential depends mainly on repeating seasonal patterns, not on individual years.

Similar wind speeds observed in the same months over a 20-year period indicate a stable wind resource. Low variability suggests low risk for long-term wind energy production, making these locations suitable for wind farm development.
North station such as  Malin Head exhibit higher mean wind speeds compared to inland locations, reflecting Ireland’s maritime climate. The lower mean wind speed is in Mullingar.
Wind speeds peak during winter months (December–February) and are lowest during summer, consistent with increased Atlantic storm activity in winter.

# Use of Resources

This project used a range of official Python libraries and publicly available data sources to support data cleaning, analysis, visualization, and forecasting. Each library was applied in specific sections of the project as follows:

- Pandas – used in all notebooks (project.ipynb, assignment*.ipynb) and scripts (merge_stations.py) for loading CSV files, cleaning data, filtering by station, aggregating annual and monthly statistics, and preparing datasets for analysis.

- NumPy – used for numerical operations, array handling, and supporting calculations in statistical analyses and forecasting.

- Matplotlib – used for visualizing trends and patterns, including annual wind speed trends, monthly averages, and comparative plots between stations.

- SciPy (scipy.stats.linregress) – applied in the Annual Wind Speed Trends (2005–2025) section to calculate regression slopes, quantify long-term trends, and display linear trends per station.

- Scikit-learn – used in the Trend Analysis for Wind Speeds in the Next 10 Years section to train linear regression models and forecast future wind speeds for each station.

- Jupyter Notebook – provided the interactive environment for combining code, outputs, visualizations, and written analysis, supporting reproducible workflows.

- Met Éireann Public Datasets – source of historical wind speed data for Irish weather stations, processed and merged for analysis in this project.
