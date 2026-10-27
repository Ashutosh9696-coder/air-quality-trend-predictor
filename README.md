# Air Quality Trend Predictor

A beginner-friendly machine learning project that investigates one-hour-ahead PM2.5 forecasting using historical air-quality and weather measurements.

## Project Overview

This project uses Linear Regression to estimate PM2.5 concentration one hour into the future. Its performance is compared with a persistence baseline, which assumes that the next hour's PM2.5 concentration will equal the current hour's value.

The experiment uses data from the Aotizhongxin monitoring station in the Beijing Multi-Site Air Quality dataset.

## Features

* Downloads the dataset from the UCI Machine Learning Repository.
* Prepares chronological hourly observations.
* Uses a chronological training/testing split.
* Trains a Linear Regression model.
* Evaluates predictions using Mean Absolute Error (MAE).
* Compares the model with a persistence baseline.
* Generates an actual-versus-predicted graph.

## Repository Structure

```text
air-quality-trend-predictor/
├── Air_Quality_Trend_Predictor.ipynb
├── air_quality_predictor.py
├── requirements.txt
├── README.md
└── report.md
```

## Requirements

* Python 3.10 or newer
* Internet access to download the dataset
* The libraries listed in `requirements.txt`

## How to Run

Clone or download this repository.

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Python implementation:

```bash
python air_quality_predictor.py
```

The script downloads the dataset, trains the model, prints evaluation metrics, and saves a graph to `results/actual_vs_predicted.png`.

## Initial Experimental Results

The initial Google Colab experiment produced:

| Model                | MAE (µg/m³) |
| -------------------- | ----------: |
| Persistence baseline |       10.36 |
| Linear Regression    |       10.48 |

The persistence baseline performed slightly better than Linear Regression in this experiment.

These are results from the initial notebook run. The standalone script must be executed separately to verify reproducibility.

## Evaluation

MAE measures the average absolute difference between predicted and observed PM2.5 concentrations. Lower values indicate smaller average errors on the evaluated test set.

## Limitations

* The experiment uses one monitoring station.
* Linear Regression may not capture nonlinear patterns.
* Missing observations are removed.
* Results are based on one chronological holdout period.
* The model did not outperform the persistence baseline in the initial experiment.
* The model is a learning prototype, not a validated public-health forecasting system.

## Future Improvements

* Add lagged pollution measurements.
* Compare alternative forecasting models.
* Evaluate performance across additional stations.
* Investigate errors during high-pollution periods.
* Test robustness across different time periods.

## Dataset

Beijing Multi-Site Air Quality dataset, available from the UCI Machine Learning Repository.

## Technical Report

See [`report.md`](report.md) for the methodology, results, limitations, and conclusions.

