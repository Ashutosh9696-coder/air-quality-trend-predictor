# Air Quality Trend Predictor

A beginner-friendly machine learning project that predicts the next hour's PM2.5 concentration using historical air-quality and weather data.

## Project Overview

This project uses the Beijing Multi-Site Air Quality dataset from the UCI Machine Learning Repository. It focuses on the Aotizhongxin monitoring station and forecasts PM2.5 concentration one hour ahead.

The project compares two machine learning models against a simple persistence baseline.

## Models Compared

1. **Persistence Baseline:** Uses the current hour's PM2.5 concentration as the prediction for the next hour.
2. **Linear Regression:** Learns a linear relationship between weather conditions, current PM2.5, and next-hour PM2.5.
3. **Random Forest Regression:** Learns nonlinear relationships using an ensemble of decision trees.

## Dataset

* **Source:** UCI Machine Learning Repository
* **Dataset:** Beijing Multi-Site Air Quality
* **Station:** Aotizhongxin
* **Target:** Next-hour PM2.5 concentration
* **Unit:** Micrograms per cubic metre (µg/m³)

The Python script downloads the dataset automatically when it runs.

## Evaluation Results

Results from the current experiment:

| Approach                 | Mean Absolute Error (µg/m³) |
| ------------------------ | --------------------------: |
| Persistence Baseline     |                       10.36 |
| Linear Regression        |                       10.48 |
| Random Forest Regression |                       10.61 |

Lower MAE indicates better predictive accuracy.

In this experiment, the persistence baseline performed better than both machine learning models. This demonstrates why a model should be compared against a simple baseline rather than evaluated in isolation.

## Technologies Used

* Python
* pandas
* scikit-learn
* Matplotlib
* Requests

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Ashutosh9696-coder/air-quality-trend-predictor.git
cd air-quality-trend-predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the predictor

```bash
python air_quality_predictor.py
```

The script downloads the dataset, prepares the data, trains the models, prints evaluation metrics, and saves a graph to `results/actual_vs_predicted.png`.

## Limitations

* The experiment uses one monitoring station.
* The selected features and model settings may not capture all factors affecting PM2.5.
* Results from one chronological test split may not generalize to other locations or periods.
* The persistence baseline outperformed both machine learning models in the current experiment.

## Future Improvements

* Experiment with additional time-based and lagged features.
* Tune model parameters using training data only.
* Evaluate performance at multiple monitoring stations.
* Investigate whether alternative models can outperform the baseline.

## Author

Ashutosh Shukla
