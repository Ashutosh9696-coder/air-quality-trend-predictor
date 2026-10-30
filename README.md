## Model Evaluation and Results

The model was evaluated using a **chronological 80:20 train-test split** to preserve the time-based order of observations and avoid using future data during training.

The experiment used 28,048 training samples and 7,012 testing samples.

### Performance Comparison

Two approaches were evaluated:

1. **Persistence Baseline:** Uses the most recent PM2.5 reading as the prediction for the next hour.
2. **Linear Regression:** Uses historical PM2.5 readings (three lag features) along with meteorological measurements to predict the next PM2.5 concentration.

The evaluation was performed using Mean Absolute Error (MAE).

| Model                | MAE (µg/m³) |
| -------------------- | ----------: |
| Persistence Baseline |       16.77 |
| Linear Regression    |       16.83 |

### Key Findings

* The Persistence Baseline achieved an MAE of **16.77 µg/m³**.
* Linear Regression achieved an MAE of **16.83 µg/m³**.
* The baseline performed slightly better, with a difference of just **0.06 µg/m³**.
* Adding historical and weather-related features did not produce an improvement over the simple baseline in this experiment.

### Actual vs Predicted

The project generates a visualization comparing actual PM2.5 concentrations with Linear Regression predictions on the test dataset.

This helps assess how closely the model follows changes in pollution levels over time.

### Interpretation

An important observation from this experiment is that a machine learning model does not necessarily outperform a simple forecasting baseline.

Although Linear Regression was implemented using historical pollution and weather features, it did not achieve a lower MAE than the persistence approach. This provides a useful starting point for future improvements, such as feature engineering, alternative regression models, and further evaluation across monitoring stations.
