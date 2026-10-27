# Air Quality Trend Predictor

## Technical Report

### 1. Project Overview

This project investigates whether machine learning can predict PM2.5 concentrations one hour ahead using historical air-quality measurements and weather data.

The initial implementation uses Linear Regression and compares its predictions with a persistence baseline.

### 2. Dataset

The project uses the Beijing Multi-Site Air Quality dataset from the UCI Machine Learning Repository.

The experiment focuses on the Aotizhongxin monitoring station. The original station dataset contains 35,064 hourly records and 18 columns.

Relevant variables include:

* PM2.5: fine particulate matter concentration
* TEMP: temperature
* PRES: atmospheric pressure
* DEWP: dew point
* RAIN: rainfall
* WSPM: wind speed

### 3. Data Preparation

The year, month, day, and hour columns are combined to construct timestamps. Observations are sorted chronologically.

The target is the PM2.5 measurement at the next timestamp. Only pairs exactly one hour apart are retained. Rows containing missing values in the selected input features or target are removed.

The remaining observations are split chronologically: the first 80% are used for training and the final 20% for testing.

### 4. Methodology

#### Linear Regression

Linear Regression is trained using the current hour's PM2.5, temperature, atmospheric pressure, dew point, rainfall, and wind speed to estimate PM2.5 one hour later.

#### Persistence Baseline

The persistence baseline predicts that the next hour's PM2.5 concentration will equal the current hour's concentration.

This baseline is important because pollution levels often change gradually. A more complex model should be compared with this simple alternative.

### 5. Evaluation Metric

Mean Absolute Error (MAE) is used to measure prediction error.

MAE is the average absolute difference between predicted and observed PM2.5 concentrations. Lower values indicate smaller average absolute errors on the evaluated dataset.

### 6. Experimental Results

The initial Colab experiment produced the following results:

| Model                | MAE (µg/m³) |
| -------------------- | ----------: |
| Persistence baseline |       10.36 |
| Linear Regression    |       10.48 |

The persistence baseline performed slightly better than Linear Regression. The difference between the two MAE values was 0.12 µg/m³.

These results do not demonstrate that Linear Regression improves on the persistence baseline for this experiment.

The standalone Python script has been prepared to reproduce the experiment, but its execution results must be checked separately before claiming that the notebook and script produce identical results.

### 7. Visualization

The notebook generates a plot comparing actual PM2.5 measurements with Linear Regression predictions over a portion of the test period.

The predictions follow some of the observed trends but do not perfectly capture every peak or sudden change.

### 8. Limitations

1. Only one monitoring station is used in the current experiment.
2. Linear Regression may not capture nonlinear relationships in pollution and weather measurements.
3. Missing observations are removed, reducing the amount of usable data.
4. The model has been evaluated on one chronological holdout period.
5. The persistence baseline slightly outperforms Linear Regression.
6. Further testing is needed to assess performance across different stations and time periods.
7. The current experiment does not establish that the model is suitable for operational air-quality warnings or public-health decisions.

### 9. Future Improvements

Possible extensions include:

* Adding lagged PM2.5 measurements.
* Comparing additional regression models.
* Evaluating performance across multiple stations.
* Examining errors during high-pollution periods.
* Comparing results across different chronological test periods.

Any improvements should be evaluated using the same test period and appropriate safeguards against information leakage.

### 10. Conclusion

This project implements an initial one-hour-ahead PM2.5 forecasting experiment using Linear Regression.

The experiment demonstrates how to prepare chronological observations, train a regression model, evaluate predictions using MAE, and compare the model with a simple baseline.

The persistence baseline achieved a slightly lower MAE than Linear Regression. This finding highlights the importance of evaluating machine-learning models against simple alternatives rather than assuming that a more complex model will perform better.
