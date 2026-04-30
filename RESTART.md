# ForecastLLM Restart Context

## Project Goal

Adapt Ed Donner's Week 6-8 capstone notebooks from Amazon-review pricing to time-series forecasting while preserving the course's instructional flow.

## Current State

Week 6 is complete.

- Day 1: dataset curation
- Day 2: supervised lag-feature representation
- Day 3: naive and daily seasonal-naive baselines
- Day 4: first learned model with LinearRegression
- Day 5: model comparison with LinearRegression, Ridge, and RandomForestRegressor

The current forecasting protocol is one-step-ahead rolling evaluation on one selected local M4 hourly series.

Week 7 is now started.

- Day 1 (`week7/day1.ipynb`) is adapted and runnable end-to-end.
- Day 1 adapts LoRA/QLoRA model-loading workflow to forecasting prompts derived from Week 6 features.
- End-to-end run completed with non-blocking deprecation warnings.
- Day 2 (`week7/day2.ipynb`) is adapted and runnable end-to-end.
- Day 2 adapts prompt dataset creation/token-length analysis/truncation to forecasting records and prepares a `DatasetDict` for training.

## Important Design Choices

- Original notebooks remain untouched under `notebooks_original/`.
- Adapted notebooks live under `week6/`, `week7/`, and `week8/`.
- Current dataset uses columns `timestamp` and `value`.
- Project default data source is local M4 hourly data from `FORECAST_DATA_PATH` (or the loader default path).
- Synthetic series is retained only as an explicit fallback path.
- Supervised features preserve week6 protocol and add hourly seasonality:
  - core: `lag_1`, `lag_2`, `lag_3`, `lag_7`, `lag_24`, `day_of_week`, `month`
  - optional: `lag_168` when selected series is long enough
- Lag interpretation:
  - `lag_1`, `lag_2`, `lag_3`, `lag_7` are short-memory lags
  - `lag_24` is the daily seasonal lag for hourly data
  - `lag_168` is the weekly seasonal lag for hourly data
- Baseline convention:
  - naive baseline = `lag_1`
  - daily seasonal naive baseline = `lag_24`
  - weekly seasonal naive baseline = `lag_168` only if that lag is present
- Metrics are MAE and sMAPE.
- Chronological splitting is used; no shuffling.
- Day 4 and Day 5 include leakage sanity checks.
- Multi-series work is deferred.
- Week 7 Day 1/2 use local env vars (`BASE_MODEL`, `FINETUNED_MODEL`, `HF_TOKEN`, optional `HF_USERNAME`) and do not require Colab secrets.
- A `.env` file is optional; use `huggingface-cli login` or set `HF_TOKEN` only when accessing gated/private Hugging Face assets.

## Next Step

Adapt `notebooks_original/week7/day3.ipynb` into `week7/day3.ipynb`, preserving the Day 3 instructional structure while replacing pricing-specific logic with forecasting equivalents.

## Suggested Session Start Checklist

1. Open and review `notebooks_original/week7/day3.ipynb`.
2. Create/update `week7/day3.ipynb` scaffold.
3. Reuse Week 7 Day 2 artifacts (prompt/completion schema, cutoff logic, dataset splits).
4. Keep adaptations incremental and runnable cell-by-cell.
