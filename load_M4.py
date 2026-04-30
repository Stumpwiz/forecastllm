import pandas as pd
from pathlib import Path

train_path = Path("data/m4/Train/Hourly-train.csv")
out_path = Path("data/m4/processed/hourly_longest_series.csv")
out_path.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(train_path)
ids = df.iloc[:, 0]
vals = df.iloc[:, 1:]

lengths = vals.notna().sum(axis=1)
i = lengths.idxmax()
series_id = ids.loc[i]
series = vals.loc[i].dropna().astype(float).reset_index(drop=True)

ts = pd.date_range("2000-01-01", periods=len(series), freq="h")
out = pd.DataFrame({"timestamp": ts, "value": series})
out.to_csv(out_path, index=False)

print(f"series_id={series_id}")
print(f"rows={len(out)}")
print(f"saved={out_path}")
