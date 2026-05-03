# ForecastLLM

ForecastLLM is a learning adaptation of Ed Donner's Weeks 6-8 capstone sequence, shifting the domain from product pricing to time-series forecasting and alert workflows.

## Purpose

- Preserve Donner's capstone progression and engineering mindset.
- Translate pricing/deal logic into forecasting/alert logic.
- Keep the workflow local-first, reproducible, and inspectable.

## Adaptation Summary

- Original domain: product pricing and deal opportunities.
- ForecastLLM domain: forecasting cases and operational alerts.
- Week 6-7: M4 hourly data for forecasting mechanics and model discipline.
- Week 8: weekly gasoline prices (FRED/EIA GASREGW) for price/action/agent-style workflow.

## Week 8 Workflow

1. Day 1: ForecastCase schema + gasoline domain setup.
2. Day 2: deterministic alert detection.
3. Day 3: email-ready notification drafting (no sending).
4. Day 4: deterministic orchestration pipeline (data -> alerts -> notifications -> summary).
5. Day 5: human-readable review/reporting.
6. Results: capstone summary in `week8/results.ipynb`.

## Environment Setup

```bash
uv sync
cp .env.example .env
uv run jupyter lab
```

`.env` is optional for many cells, but supports local configuration for model/data paths and optional tokens.

## Local Datasets

This repo is local-data-first. Datasets are not committed.

- Week 6-7 (M4 hourly):
  - Provide local M4 CSV and set `FORECAST_DATA_PATH`.
- Week 8 (gasoline weekly):
  - Provide local GASREGW CSV and set `GASOLINE_DATA_PATH`.

See:

- `data/m4/README.md`
- `data/gasoline/README.md`

## Canonical Walkthrough

Run in order:

- `week6/day1.ipynb` -> `week6/day5.ipynb`
- `week7/day1.ipynb` -> `week7/day2.ipynb` -> `week7/day3 and 4.ipynb`
- `week8/day1.ipynb` -> `week8/day5.ipynb`
- `week8/results.ipynb`

## Notes on Outputs

- Runtime artifacts are written under `week8/run/` (and similar run/export folders) and are intentionally ignored by git.
- Model checkpoints/training outputs are local and ignored.

## Course Material Attribution

This repository is a community learning adaptation of Ed Donner's course material.

- Original instructional material belongs to Ed Donner and the original course repository.
- `notebooks_original/` was used as local reference material in this workspace and is not included in the repo.

