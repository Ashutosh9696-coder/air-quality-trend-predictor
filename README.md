# Air Quality Trend Predictor

A machine learning project that predicts future PM2.5 concentrations using historical air pollution readings and meteorological data.

The project explores how previous pollution levels and weather conditions can be used to understand and forecast air quality trends.

## Project Objective

The main objective is to develop a model that predicts the next hourly PM2.5 concentration using historical air quality measurements.

The project also compares the machine learning model against a simple persistence baseline to evaluate whether the model provides an actual improvement.

## Dataset

**Dataset:** Beijing Multi-Site Air Quality Data
**Source:** UCI Machine Learning Repository
**Selected monitoring station:** Aotizhongxin

The dataset contains hourly measurements of air pollutants and weather conditions.

### Features Used

**Historical pollution features:**

* PM2.5_lag1
* PM2.5_lag2
* PM2.5_lag3

**Meteorological features:**

* Temperature (TEMP)
* Atmospheric Pressure (PRES)
* Dew Point (DEWP)
* Rainfall (RAIN)
* Wind Speed (WSPM)

**Target:** Next-hour PM2.5 concentration.

## Methodology

The project follows these main steps:

1. Download and load the air quality dataset.
2. Convert date and time information into a datetime format.
3. Sort observations chronologically.
4. Handle missing numerical readings using forward filling.
5. Create lag features from previous PM2.5 readings.
6. Combine historical pollution readings with weather measurements.
7. Remove incomplete observations and non-consecutive hourly records.
8. Split the data chronologically into training and testing sets.
9. Train a Linear Regression model.
10. Compare its performance against a persistence baseline.

## Models Evaluated

### 1. Persistence Baseline

Uses the most recent available PM2.5 reading to predict the next hourly concentration.

### 2. Linear Regression

Uses three previous PM2.5 readings and meteorological measurements to predict the next-hour PM2.5 concentration.

## Model Evaluation and Results

The experiment used a chronological 80:20 train-test split.

| Dataset  | Number of Samples |
| -------- | ----------------: |
| Training |            28,048 |
| Testing  |             7,012 |

Performance was evaluated using Mean Absolute Error (MAE).

| Model                | MAE (µg/m³) |
| -------------------- | ----------: |
| Persistence Baseline |       16.77 |
| Linear Regression    |       16.83 |

### Key Findings

* The persistence baseline achieved an MAE of 16.77 µg/m³.
* Linear Regression achieved an MAE of 16.83 µg/m³.
* The persistence baseline performed slightly better, with an MAE difference of 0.06 µg/m³.
* The additional historical and weather features did not improve prediction accuracy in this experiment.

### Interpretation

The results demonstrate that a machine learning model does not necessarily outperform a simple forecasting baseline.

Although Linear Regression incorporated historical pollution readings and weather measurements, it did not achieve better accuracy than the persistence approach.

This finding highlights the importance of baseline comparisons when evaluating machine learning models.

## Visualization

The project generates an Actual vs Predicted visualization to compare Linear Regression predictions with actual PM2.5 concentrations in the test dataset.

The graph helps examine how closely the model follows pollution trends over time.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Requests
* Jupyter Notebook
* Google Colab

## Project Structure

```text
air-quality-trend-predictor/
│
├── air_quality_predictor.py
├── Air_Quality_Trend_Predictor.ipynb
├── README.md
├── report.md
├── requirements.txt
├── actual_vs_predicted.png
└── .gitignore
```

## Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/Ashutosh9696-coder/air-quality-trend-predictor.git
```

### 2. Navigate to the project directory

```bash
cd air-quality-trend-predictor
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python air_quality_predictor.py
```

The script downloads the dataset, performs preprocessing, trains the model, evaluates its performance, and generates the visualization.

## Limitations

* The experiment uses data from a single monitoring station.
* Linear Regression may not capture complex nonlinear relationships.
* Missing readings and sudden environmental changes can affect predictions.
* Results are specific to the selected dataset and testing period.

## Future Improvements

Potential improvements include:

* Experimenting with more advanced regression algorithms.
* Exploring additional features and feature engineering techniques.
* Evaluating performance across multiple monitoring stations.
* Improving prediction accuracy through further experimentation.

## Author

**Ashutosh Shukla**

GitHub: [Ashutosh9696-coder](https://github.com/Ashutosh9696-coder)
