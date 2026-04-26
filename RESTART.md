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

## Important Design Choices

- Original notebooks remain untouched under `notebooks_original/`.
- Adapted notebooks live under `week6/`, `week7/`, and `week8/`.
- Current dataset uses columns `timestamp` and `value`.
- Supervised features include `lag_1`, `lag_2`, `lag_3`, `lag_7`, `day_of_week`, and `month`.
- Metrics are MAE and sMAPE.
- Chronological splitting is used; no shuffling.
- Day 4 and Day 5 include leakage sanity checks.
- Real M4/multi-series work is deferred.

## Next Step

Begin adapting `notebooks_original/week7/` into `week7/`, preserving the same course-day structure while replacing pricing-specific logic with forecasting logic.

## Suggested First Week 7 Focus

Use the Week 6 pipeline as a reusable foundation:
- data loading
- supervised feature creation
- baselines
- metrics
- model comparison

Then adapt Week 7 according to the original notebook's role in Ed Donner's course.
