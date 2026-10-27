import io
import zipfile
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import requests
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

DATA_URL = (
"https://archive.ics.uci.edu/ml/"
"machine-learning-databases/00501/"
"PRSA2017_Data_20130301-20170228.zip"
)

STATION_FILE = (
"PRSA_Data_"
"Aotizhongxin_20130301-20170228.csv"
)

FEATURES = ["PM2.5", "TEMP", "PRES", "DEWP", "RAIN", "WSPM"]

def load_data():
"""Download and load the Aotizhongxin station data."""
print("Downloading dataset...")

```
response = requests.get(DATA_URL, timeout=120)
response.raise_for_status()

with zipfile.ZipFile(io.BytesIO(response.content)) as archive:
    matches = [
        name for name in archive.namelist()
        if name.endswith(STATION_FILE)
    ]

    if not matches:
        raise FileNotFoundError(
            f"Could not find {STATION_FILE} in the downloaded archive."
        )

    with archive.open(matches[0]) as file:
        df = pd.read_csv(file)

print("Dataset loaded:", df.shape)
return df
```

def prepare_data(df):
"""Create chronological one-hour-ahead forecasting observations."""
data = df.copy()

```
data["datetime"] = pd.to_datetime(
    data[["year", "month", "day", "hour"]]
)

data = data.sort_values("datetime").set_index("datetime")

# Target is PM2.5 in the next row.
data["target"] = data["PM2.5"].shift(-1)

# Keep only pairs exactly one hour apart.
next_time = pd.Series(data.index, index=data.index).shift(-1)

hourly = data[
    next_time - data.index == pd.Timedelta(hours=1)
].copy()

# Drop rows with missing inputs or target; do not interpolate.
model_data = hourly[FEATURES + ["target"]].dropna()

if len(model_data) < 10:
    raise ValueError("Not enough valid observations to train the model.")

split = int(len(model_data) * 0.8)

train = model_data.iloc[:split]
test = model_data.iloc[split:]

return train, test
```

def main():
df = load_data()
train, test = prepare_data(df)

```
X_train = train[FEATURES]
y_train = train["target"]

X_test = test[FEATURES]
y_test = test["target"]

# Train Linear Regression.
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

model_mae = mean_absolute_error(y_test, predictions)

# Persistence baseline: next hour equals current hour.
baseline_predictions = X_test["PM2.5"].to_numpy()
baseline_mae = mean_absolute_error(y_test, baseline_predictions)

print("\nEVALUATION RESULTS")
print("------------------")
print("Training samples:", len(train))
print("Testing samples:", len(test))
print("Forecast horizon: 1 hour")
print(f"Persistence baseline MAE: {baseline_mae:.2f} µg/m³")
print(f"Linear Regression MAE: {model_mae:.2f} µg/m³")

if model_mae < baseline_mae:
    print("Linear Regression performed better on this test set.")
else:
    print("The persistence baseline performed as well as or better.")

# Save an actual-versus-predicted plot.
output_dir = Path("results")
output_dir.mkdir(exist_ok=True)

n = min(200, len(test))

plt.figure(figsize=(12, 5))
plt.plot(y_test.iloc[:n].values, label="Actual PM2.5")
plt.plot(predictions[:n], label="Predicted PM2.5")
plt.title("One-Hour-Ahead PM2.5 Prediction")
plt.xlabel("Test observations")
plt.ylabel("PM2.5 (µg/m³)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plot_path = output_dir / "actual_vs_predicted.png"
plt.savefig(plot_path, dpi=150)
plt.close()

print("\nSaved graph to:", plot_path)
```

if **name** == "**main**":
main()
