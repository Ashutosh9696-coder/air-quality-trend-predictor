import io
import zipfile
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import requests

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

DATA_URL = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/"
    "00501/PRSA2017_Data_20130301-20170228.zip"
)

STATION_FILE = "PRSA_Data_Aotizhongxin_20130301-20170228.csv"

FEATURES = ["PM2.5", "TEMP", "PRES", "DEWP", "RAIN", "WSPM"]


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

    data = data.sort_values("datetime").set_index("datetime")
    data["target"] = data["PM2.5"].shift(-1)

    next_time = pd.Series(data.index, index=data.index).shift(-1)

    hourly = data[
        next_time - data.index == pd.Timedelta(hours=1)
    ].copy()

    model_data = hourly[FEATURES + ["target"]].dropna()

    if len(model_data) < 10:
        raise ValueError("Not enough valid observations.")

    split = int(len(model_data) * 0.8)

    return model_data.iloc[:split], model_data.iloc[split:]


def main():
    df = load_data()
    train, test = prepare_data(df)

    X_train = train[FEATURES]
    y_train = train["target"]

    X_test = test[FEATURES]
    y_test = test["target"]

    # Baseline: next hour equals the current hour
    baseline_predictions = X_test["PM2.5"].to_numpy()
    baseline_mae = mean_absolute_error(y_test, baseline_predictions)

    # Model 1: Linear Regression
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)
    linear_predictions = linear_model.predict(X_test)
    linear_mae = mean_absolute_error(y_test, linear_predictions)

    # Model 2: Random Forest
    forest_model = RandomForestRegressor(
        n_estimators=100,
        max_depth=12,
        min_samples_leaf=3,
        random_state=42,
        n_jobs=-1
    )

    forest_model.fit(X_train, y_train)
    forest_predictions = forest_model.predict(X_test)
    forest_mae = mean_absolute_error(y_test, forest_predictions)

    results = {
        "Persistence Baseline": (baseline_mae, baseline_predictions),
        "Linear Regression": (linear_mae, linear_predictions),
        "Random Forest": (forest_mae, forest_predictions),
    }

    print("\nEVALUATION RESULTS")
    print("------------------")
    print("Training samples:", len(train))
    print("Testing samples:", len(test))

    for name, (mae, _) in results.items():
        print(f"{name} MAE: {mae:.2f} µg/m³")

    best_name = min(results, key=lambda name: results[name][0])
    print(f"\nBest result on this test set: {best_name}")

    Path("results").mkdir(exist_ok=True)

    n = min(200, len(test))

    plt.figure(figsize=(12, 5))
    plt.plot(y_test.iloc[:n].values, label="Actual PM2.5")
    plt.plot(
        linear_predictions[:n],
        label="Linear Regression"
    )
    plt.plot(
        forest_predictions[:n],
        label="Random Forest"
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
