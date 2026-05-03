# ForecastLLM Restart Context

## Current State (Week 8 Complete)

ForecastLLM adaptation status:

- Week 6 complete (`week6/day1.ipynb` ... `week6/day5.ipynb`)
- Week 7 complete (`week7/day1.ipynb`, `week7/day2.ipynb`, `week7/day3 and 4.ipynb`)
- Week 8 complete (`week8/day1.ipynb` ... `week8/day5.ipynb`, `week8/results.ipynb`)

## Project Goal

Adapt Ed Donner's Weeks 6-8 capstone from pricing/deal agents to forecasting and alert workflows while preserving instructional structure.

## Week 8 Final Flow

1. Day 1: ForecastCase and gasoline schema setup.
2. Day 2: forecast alert detection (`week8/run/week8_day2_alerts.jsonl`).
3. Day 3: email-ready notification drafting (no sending).
4. Day 4: local deterministic pipeline orchestration.
5. Day 5: review/report markdown generation.
6. Results: consolidated capstone narrative and tables.

## Important Design Choices

- `notebooks_original/` remains untouched as reference.
- Local-first execution only (no Modal/Gradio/deployment requirements).
- Week 8 data source is local GASREGW CSV via `GASOLINE_DATA_PATH`.
- Alert threshold is fixed at `$0.05/gallon` for interpretability.
- Notification records include `schema_version=forecastllm.week8.notification.v1`.

## Before Running

1. Ensure local datasets exist and `.env` paths are set as needed.
2. Run Week 8 Day 4 and Day 5 before `week8/results.ipynb`.
3. Keep generated run/checkpoint artifacts uncommitted.

