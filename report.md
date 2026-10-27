# Air Quality Trend Predictor

## Technical Report

**Author:** Ashutosh Shukla
**Project:** Singularity Research Lab — AI Division
**Domain:** Machine Learning and Air Quality Prediction

---

## 1. Abstract

This project explores the use of machine learning to predict PM2.5 air pollution levels one hour ahead using historical pollution readings and weather measurements. The Beijing Multi-Site Air Quality dataset was used, with observations from the Aotizhongxin monitoring station.

A persistence baseline, Linear Regression, and Random Forest Regressor were evaluated using Mean Absolute Error (MAE). In the standalone Python experiment, the persistence baseline achieved the lowest error, demonstrating that a simple prediction method can sometimes outperform more complex machine learning models.

## 2. Objective

The primary objective was to build a model that predicts the next hour's PM2.5 concentration using previous pollution measurements and weather features.

The project also aimed to:

* Process and prepare historical air quality data.
* Visualize pollution trends over time.
* Train and evaluate regression models.
* Compare machine learning predictions with a simple baseline.

## 3. Dataset Description

**Dataset:** Beijing Multi-Site Air Quality Data
**Source:** UCI Machine Learning Repository
**Monitoring station:** Aotizhongxin
**Period:** March 2013 to February 2017
**Original station dataset:** 35,064 hourly records and 18 columns.

The dataset contains air pollutant measurements and meteorological information.

### Selected Features

* PM2.5 readings from the previous three hours.
* Temperature (TEMP).
* Atmospheric pressure (PRES).
* Dew point (DEWP).
* Rainfall (RAIN).
* Wind speed (WSPM).

**Target variable:** PM2.5 concentration one hour into the future.

## 4. Methodology

### 4.1 Data Preprocessing

The dataset was loaded and its date and time components were combined into timestamps. The observations were sorted chronologically.

Lag features were created using the previous one, two, and three hours of PM2.5 readings. The target variable was created by shifting PM2.5 forward by one hour.

Observations were retained only when the next recorded timestamp was exactly one hour later. Rows missing the required lag features or target were removed.

### 4.2 Train-Test Split

The standalone Python script divides the valid observations chronologically, using the first 80% for training and the remaining 20% for testing.

This approach preserves the time order of the observations and avoids randomly mixing earlier and later records.

### 4.3 Models

**Persistence Baseline:** Uses the latest available PM2.5 reading as the prediction for the following hour.

**Linear Regression:** Learns a linear relationship between the selected pollution and weather features and the target PM2.5 value.

**Random Forest Regressor:** Uses an ensemble of decision trees to model relationships between the input features and future PM2.5 concentration.

### 4.4 Evaluation Metric

Mean Absolute Error (MAE) was used to evaluate the predictions.

MAE measures the average absolute difference between predicted and actual values. A lower MAE indicates better predictive performance.

## 5. Experimental Results

The standalone Python script completed successfully and produced the following results:

| Approach                | MAE (µg/m³) |
| ----------------------- | ----------: |
| Persistence Baseline    |       10.36 |
| Linear Regression       |       10.48 |
| Random Forest Regressor |       10.61 |

The persistence baseline achieved the lowest MAE of 10.36 µg/m³. Linear Regression produced an MAE of 10.48 µg/m³, while Random Forest produced an MAE of 10.61 µg/m³.

These results indicate that neither machine learning model outperformed the persistence baseline in this experiment.

The difference between the baseline and Linear Regression was small. This suggests that, for this test set and prediction horizon, using the most recent pollution reading was already a competitive approach.

**Result scope:** These numerical results are from the standalone Python script. The notebook experiment has produced different metrics and has not yet been reconciled with the script. The reported values should therefore not be interpreted as verified results from both implementations.

## 6. Visualization

The project generates a graph comparing actual PM2.5 measurements with the predictions from the regression models.

The graph helps visually assess how closely the predictions follow changes in actual pollution levels.

The standalone script saves its graph to:

`results/actual_vs_predicted.png`

A historical PM2.5 trend visualization was also created during notebook experimentation.

## 7. Limitations

1. The experiment uses data from one monitoring station, so the results may not generalize to other locations.
2. Air pollution can change rapidly due to weather, traffic, and other factors that are not fully represented by the selected features.
3. The persistence baseline outperformed both regression models in the reported experiment.
4. The notebook and standalone Python script have not yet been verified to produce identical results.
5. Further testing is needed before drawing conclusions about performance on other stations or longer prediction horizons.

## 8. Future Improvements

Possible improvements include:

* Investigating additional features and feature-engineering techniques.
* Tuning model parameters and comparing other regression algorithms.
* Evaluating the models on data from multiple monitoring stations.
* Testing different prediction horizons.
* Investigating why the regression models did not outperform the baseline.
* Ensuring that the notebook and Python script use identical preprocessing, features, and evaluation procedures.

## 9. Conclusion

This project demonstrates a basic machine learning workflow for one-hour-ahead PM2.5 prediction, including data preparation, feature engineering, chronological evaluation, regression modelling, and visualization.

In the standalone Python experiment, the persistence baseline achieved the lowest MAE of 10.36 µg/m³, outperforming Linear Regression and Random Forest on the selected test set.

The experiment highlights an important lesson: complex models should be compared with simple baselines, and their performance should be evaluated using measured results rather than assumptions.

Further work is required to reconcile the notebook and standalone script before treating their results as fully reproducible.

## 10. Repository

**GitHub Repository:**
https://github.com/Ashutosh9696-coder/air-quality-trend-predictor
