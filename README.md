# Air Quality Trend Predictor 🌫️

A machine learning project that predicts PM2.5 air pollution levels one hour ahead using historical pollution readings and weather measurements.

## 🎯 Objective

The objective of this project is to explore whether machine learning models can predict short-term changes in air pollution using historical air quality data.

## 📊 Dataset

**Dataset:** Beijing Multi-Site Air Quality Data

**Source:** UCI Machine Learning Repository

**Station used:** Aotizhongxin

**Period:** March 2013 – February 2017

The dataset contains hourly air pollution readings and weather measurements.

### Features Used

* PM2.5 readings from the previous three hours
* Temperature (TEMP)
* Atmospheric pressure (PRES)
* Dew point (DEWP)
* Rainfall (RAIN)
* Wind speed (WSPM)

**Target:** PM2.5 concentration one hour into the future.

## ⚙️ Methodology

1. Download and load the dataset.
2. Convert date and time columns into timestamps.
3. Sort observations chronologically.
4. Create lag features from previous PM2.5 readings.
5. Remove observations with missing required historical readings or targets.
6. Keep consecutive hourly observations.
7. Split the data chronologically into training and testing sets.
8. Train regression models and evaluate their predictions using Mean Absolute Error (MAE).
9. Visualize actual and predicted PM2.5 values.

## 🤖 Models Evaluated

Three approaches were evaluated:

* **Persistence Baseline:** Uses the latest PM2.5 reading as the prediction for the next hour.
* **Linear Regression:** Models the relationship between historical pollution readings, weather measurements, and future PM2.5.
* **Random Forest Regressor:** Uses an ensemble of decision trees to model potentially nonlinear relationships.

## 📈 Experimental Results

The standalone Python script produced the following results:

| Approach             | MAE (µg/m³) |
| -------------------- | ----------: |
| Persistence Baseline |       10.36 |
| Linear Regression    |       10.48 |
| Random Forest        |       10.61 |

**Interpretation:** The persistence baseline achieved the lowest MAE among the three approaches in this experiment. Both machine learning models performed slightly worse than simply using the latest PM2.5 reading.

This result highlights the importance of comparing machine learning models against simple baselines rather than assuming that a more complex model will perform better.

*Note: These results are from the standalone Python script. The notebook experiment has not yet been verified to produce identical results.*

## 📉 Visualization

The project generates a graph comparing actual PM2.5 measurements with model predictions.

Output file:

`results/actual_vs_predicted.png`

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* Scikit-learn
* Requests

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Ashutosh9696-coder/air-quality-trend-predictor.git
cd air-quality-trend-predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the project

```bash
python air_quality_predictor.py
```

The script downloads the dataset, trains the models, prints evaluation metrics, and generates the prediction graph.

An internet connection is required to download the dataset.

## ⚠️ Limitations

* The project uses data from a single monitoring station.
* Prediction accuracy may vary with changing pollution patterns and weather conditions.
* The persistence baseline outperformed both machine learning models in the reported experiment.
* The current results do not establish how well the model generalizes to other stations or cities.
* The notebook and standalone script still need to be checked for consistency.

## 🔮 Future Improvements

* Compare additional regression models.
* Investigate feature engineering and model parameters.
* Evaluate performance across different monitoring stations.
* Explore longer prediction horizons.
* Investigate why the machine learning models do not outperform the persistence baseline.

## 👨‍💻 Author

Ashutosh Shukla

GitHub: [Ashutosh9696-coder](https://github.com/Ashutosh9696-coder)
