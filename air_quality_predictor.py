
import io
import zipfile
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import requests

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

DATA_URL = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/"
    "00501/PRSA2017_Data_20130301-20170228.zip"
)

STATION_FILE = "PRSA_Data_Aotizhongxin_20130301-20170228.csv"

FEATURES = [
    "PM2.5_lag1",
    "PM2.5_lag2",
    "PM2.5_lag3",
    "TEMP",
    "PRES",
    "DEWP",
    "RAIN",
    "WSPM",
]


def load_data():
    print("Downloading dataset...")

    response = requests.get(DATA_URL, timeout=120)
    response.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(response.content)) as archive:
        matches = [
            name for name in archive.namelist()
            if name.endswith(STATION_FILE)
        ]

        if not matches:
            raise FileNotFoundError("Station CSV not found in dataset.")

        with archive.open(matches[0]) as file:
            df = pd.read_csv(file)

    print("Dataset loaded:", df.shape)
    return df


def prepare_data(df):
    data = df.copy()

    data["datetime"] = pd.to_datetime(
        data[["year", "month", "day", "hour"]]
    )

    data = data.sort_values("datetime").reset_index(drop=True)

    # Fill missing readings using past observations only.
    numeric_columns = [
        "PM2.5", "TEMP", "PRES", "DEWP", "RAIN", "WSPM"
    ]
    data[numeric_columns] = data[numeric_columns].ffill()

    # Use the previous three PM2.5 readings as features.
    for lag in (1, 2, 3):
        data[f"PM2.5_lag{lag}"] = data["PM2.5"].shift(lag)

    # Predict PM2.5 one hour into the future.
    data["target"] = data["PM2.5"].shift(-1)
    data["next_datetime"] = data["datetime"].shift(-1)

    # Keep only consecutive hourly observations.
    hourly = data[
        data["next_datetime"] - data["datetime"]
        == pd.Timedelta(hours=1)
    ].copy()

    model_data = hourly.dropna(subset=FEATURES + ["target"])

    if len(model_data) < 10:
        raise ValueError("Not enough valid observations.")

    split = int(len(model_data) * 0.8)

    train = model_data.iloc[:split]
    test = model_data.iloc[split:]

    print("Last training timestamp:", train["datetime"].iloc[-1])
    print("First testing timestamp:", test["datetime"].iloc[0])

    return train, test


def main():
    df = load_data()
    train, test = prepare_data(df)

    X_train = train[FEATURES]
    y_train = train["target"]

    X_test = test[FEATURES]
    y_test = test["target"]

    # Persistence baseline: next hour equals the latest reading.
    baseline_predictions = X_test["PM2.5_lag1"].to_numpy()
    baseline_mae = mean_absolute_error(
        y_test, baseline_predictions
    )

    # Linear Regression model.
    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    model_mae = mean_absolute_error(y_test, predictions)

    print("\nEVALUATION RESULTS")
    print("------------------")
    print("Training samples:", len(train))
    print("Testing samples:", len(test))
    print(f"Persistence Baseline MAE: {baseline_mae:.2f} µg/m³")
    print(f"Linear Regression MAE: {model_mae:.2f} µg/m³")

    Path("results").mkdir(exist_ok=True)

    n = min(200, len(test))

    plt.figure(figsize=(12, 5))
    plt.plot(y_test.iloc[:n].values, label="Actual PM2.5")
    plt.plot(
        predictions[:n],
        label="Linear Regression"
    )
    plt.title("One-Hour-Ahead PM2.5 Prediction")
    plt.xlabel("Test observations")
    plt.ylabel("PM2.5 (µg/m³)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("results/actual_vs_predicted.png", dpi=150)
    plt.close()

    print("Graph saved to results/actual_vs_predicted.png")


if __name__ == "__main__":
    main()
```
