# Air Quality Trend Predictor

## Project Report

### 1. Objective

The objective of this project is to predict future PM2.5 concentrations using historical air quality readings and weather measurements. The project uses machine learning to study pollution trends and evaluate prediction accuracy.

### 2. Dataset

**Dataset:** Beijing Multi-Site Air Quality Data
**Source:** UCI Machine Learning Repository
**Station selected:** Aotizhongxin

The dataset contains hourly air quality measurements and meteorological information, including:

* PM2.5 concentration
* Temperature (TEMP)
* Atmospheric pressure (PRES)
* Dew point (DEWP)
* Rainfall (RAIN)
* Wind speed (WSPM)

### 3. Data Preprocessing

The following preprocessing steps were performed:

* Converted date and time information into a datetime format.
* Sorted observations chronologically.
* Handled missing numerical readings using forward filling.
* Created three lag features using previous PM2.5 readings:

  * PM2.5_lag1
  * PM2.5_lag2
  * PM2.5_lag3
* Used weather measurements as additional input features.
* Removed rows with missing required values and observations where consecutive hourly readings were unavailable.

### 4. Model and Methodology

Linear Regression was used to predict future PM2.5 concentrations.

The input features included the previous three PM2.5 readings and weather measurements.

A persistence baseline was also implemented for comparison. It predicts the next PM2.5 value using the most recent available PM2.5 reading.

The dataset was divided chronologically into:

* 80% training data
* 20% testing data

This approach ensures that future observations are not used to train the model.

### 5. Experimental Results

The experiment produced the following results:

| Metric                   |      Result |
| ------------------------ | ----------: |
| Training samples         |      28,048 |
| Testing samples          |       7,012 |
| Persistence Baseline MAE | 16.77 µg/m³ |
| Linear Regression MAE    | 16.83 µg/m³ |

**Observation:**

The persistence baseline performed slightly better than Linear Regression in this experiment. The difference in MAE was 0.06 µg/m³.

This suggests that the Linear Regression model did not improve upon simply using the most recent PM2.5 reading as the prediction.

### 6. Visualization

An Actual vs Predicted graph was generated to compare the model's predictions with the actual PM2.5 concentrations in the test dataset.

The visualization helps identify how closely the model follows the actual pollution trend.

### 7. Limitations

* The experiment uses data from one monitoring station.
* Linear Regression may not capture complex patterns in air pollution.
* Missing sensor readings and sudden changes in weather can affect prediction accuracy.
* The results are based on the selected dataset and test period and may not generalize to other locations.

### 8. Conclusion

This project demonstrates a basic machine learning approach to predicting PM2.5 concentrations using historical pollution readings and weather data.

Although Linear Regression was implemented successfully, it did not outperform the persistence baseline in the experiment. This highlights the importance of comparing machine learning models against simple baseline methods rather than assuming that a more complex model will always perform better.

### 9. Tools and Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Jupyter Notebook / Google Colab
