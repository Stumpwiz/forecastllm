# M4 Hourly Data

ForecastLLM uses local M4 hourly data for adapted forecasting notebooks.

The full M4 dataset is not committed to git.

Set `FORECAST_DATA_PATH` in `.env` to point to the local hourly CSV, for example:

```text
FORECAST_DATA_PATH=/home/geo/Projects/Python/forecastllm/data/m4/raw/Hourly-train.csv
```

Synthetic data is retained only as an explicit development helper and is not used automatically.
