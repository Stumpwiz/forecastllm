# ForecastLLM Restart Context

## Project Goal

Adapt Ed Donner's Week 6-8 capstone notebooks from Amazon-review pricing to time-series forecasting while preserving the course's instructional flow.

## Current State

Week 6 is complete.

- Day 1: dataset curation
- Day 2: supervised lag-feature representation
- Day 3: naive and seasonal-naive baselines
- Day 4: first learned model with LinearRegression
- Day 5: model comparison with LinearRegression, Ridge, and RandomForestRegressor

The current forecasting protocol is one-step-ahead rolling evaluation on a single daily sample/synthetic series.

Week 7 is now started.

- Day 1 (`week7/day1.ipynb`) is adapted and runnable end-to-end.
- Day 1 adapts LoRA/QLoRA model-loading workflow to forecasting prompts derived from Week 6 features.
- End-to-end run completed with non-blocking deprecation warnings.

## Important Design Choices

- Original notebooks remain untouched under `notebooks_original/`.
- Adapted notebooks live under `week6/`, `week7/`, and `week8/`.
- Current dataset uses columns `timestamp` and `value`.
- Supervised features include `lag_1`, `lag_2`, `lag_3`, `lag_7`, `day_of_week`, and `month`.
- Metrics are MAE and sMAPE.
- Chronological splitting is used; no shuffling.
- Day 4 and Day 5 include leakage sanity checks.
- Real M4/multi-series work is deferred.
- Week 7 Day 1 uses local env vars (`BASE_MODEL`, `FINETUNED_MODEL`, `HF_TOKEN`) and does not require Colab secrets.
- A `.env` file is optional; use `huggingface-cli login` or set `HF_TOKEN` only when accessing gated/private Hugging Face assets.

## Next Step

Adapt `notebooks_original/week7/day2.ipynb` into `week7/day2.ipynb`, preserving the Day 2 instructional structure while replacing pricing-specific logic with forecasting equivalents.

## Suggested Session Start Checklist

1. Open and review `notebooks_original/week7/day2.ipynb`.
2. Create/update `week7/day2.ipynb` scaffold.
3. Reuse Week 6 pipeline foundations: data loading, supervised feature creation, baselines, metrics, and model comparison.
4. Keep adaptations incremental and runnable cell-by-cell.
