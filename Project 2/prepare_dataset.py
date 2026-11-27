
import pandas as pd
import numpy as np
from pathlib import Path


PROJECT_ROOT = Path(r"C:\Users\sohaib\Downloads\project")
INPUT_FILE = PROJECT_ROOT / "energydata_complete.csv"
OUTPUT_FILE = PROJECT_ROOT / "observations.csv"


data = pd.read_csv(INPUT_FILE)
print("Shape (rows, columns):", data.shape)
print("Columns:", list(data.columns))
print(data[["date", "Appliances"]].head())

print("Missing values in the whole table:", data.isna().sum().sum())
print("Rows:", len(data), "| Different dates:", len(np.unique(data["date"])))

sorted_data = data.sort_values("date")


same_place = np.sum(data["date"].values == sorted_data["date"].values)
print("Rows already in time order:", same_place, "of", len(data))

dates = sorted_data["date"].values
appliances = sorted_data["Appliances"].values


mean_value = np.mean(appliances)
median_value = np.median(appliances)
print("\nMean:  ", mean_value)
print("Median:", median_value)
print("Std:   ", np.std(appliances))
print("Min / Max:", np.min(appliances), np.max(appliances))


# Low    : Appliances < median
# Medium : median <= Appliances <= mean
# High   : Appliances > mean
symbol = np.where(appliances < median_value, "Low",
                  np.where(appliances <= mean_value, "Medium", "High"))

# Number and percentage of observations in each category
n_low = np.sum(symbol == "Low")
n_medium = np.sum(symbol == "Medium")
n_high = np.sum(symbol == "High")
total = len(symbol)

print("\nLow:    ", n_low, "->", round(n_low / total * 100, 2), "%")
print("Medium: ", n_medium, "->", round(n_medium / total * 100, 2), "%")
print("High:   ", n_high, "->", round(n_high / total * 100, 2), "%")
print("Total:  ", n_low + n_medium + n_high)


obs = pd.DataFrame({
    "t": np.arange(total),          # 0, 1, 2, ... = position in the sequence
    "date": dates,
    "Appliances": appliances,
    "symbol": symbol
})


print("\nAppliances per symbol:")
print(obs.groupby("symbol").agg({"Appliances": ["min", "max", "mean"]}))


obs.to_csv(OUTPUT_FILE, index=False)
print("\nSaved", len(obs), "rows to:", OUTPUT_FILE)
