# ForecastLLM

Adaptation workspace for the capstone portion (weeks 6-8) of Ed Donner's 8-week LLM Engineering course.

This repo keeps Ed's original pricing notebooks intact under `notebooks_original/` and recreates them day-by-day as a forecasting-focused project in:

- `week6/`
- `week7/`
- `week8/`

The goal is to preserve the learning path and engineering techniques from the course while redirecting the domain from pricing to forecasting.

## Project Intent

- Follow the original capstone sequence in order.
- Translate each day's exercises from pricing logic to forecasting logic.
- Keep adaptation incremental so each day stays testable and reviewable.
- Maintain a clean separation between original source material and adapted work.

## Repository Layout

- `notebooks_original/`: Ed Donner's original week 6-8 notebooks and helper code.
  - `week6/`: daily notebooks, results, and baseline pricer package used in the course.
  - `week7/`: daily notebooks, utility code, and pricer components.
  - `week8/`: daily notebooks and agent/service orchestration code.
- `week6/`, `week7/`, `week8/`: adapted forecasting notebooks and support files (your work).
- `data/`: local datasets and intermediate artifacts for forecasting experiments.
- `pyproject.toml`: project dependencies.

## Current Status (as of 2026-04-26)

- Original notebooks present: `notebooks_original/week6`, `notebooks_original/week7`, `notebooks_original/week8`.
- Adapted folders initialized: `week6/`, `week7/`, `week8/`.
- Adapted notebooks and code: not started yet (folders are currently empty).

## Initial Forecasting Task

- Dataset: M4 (daily subset)
- Initial scope: single time series
- Forecast horizon: 7 steps ahead
- Metrics: MAE, sMAPE
- Goal: replicate Week 6 pipeline using time-series inputs instead of text

## Day-by-Day Adaptation Workflow

For each original day notebook:

1. Open the original notebook in `notebooks_original/weekX/dayY.ipynb`.
2. Create a corresponding adapted notebook in `weekX/dayY.ipynb`.
3. Port one section at a time:
   - Preserve the engineering pattern (prompting, eval, architecture, tooling).
   - Replace pricing-specific assumptions, labels, and metrics with forecasting equivalents.
4. Keep notes at the top of each adapted notebook:
   - What changed vs the original.
   - Any forecasting-specific assumptions.
   - Known limitations or TODOs.
5. Run cells end-to-end before moving to the next day.
6. Save any helper modules directly under the corresponding adapted week folder.

## Suggested Adaptation Rules

- Keep original filenames when practical (`day1.ipynb`, `day2.ipynb`, etc.) for easy diffing.
- Preserve the order of days; avoid skipping ahead.
- Prefer small, frequent commits (one logical adaptation chunk per commit).
- Do not edit `notebooks_original/`; treat it as read-only reference.

## Environment Setup

This project uses Python 3.12+ and currently depends on:

- `jupyterlab`
- `matplotlib`
- `pandas`

Using `uv`:

```bash
uv sync
uv run jupyter lab
```

Using `pip`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
jupyter lab
```

## Practical Next Steps

1. Copy/adapt `notebooks_original/week6/day1.ipynb` into `week6/day1.ipynb`.
2. Define your first forecasting target/task (for example: horizon, granularity, metric).
3. Add minimal helper modules in `week6/` as they emerge from the notebook work.
4. Repeat daily through week 8, preserving the same progression as the course.

## Notes

This repo is a personal learning adaptation of course material. The structure is intentionally simple: originals are archived for reference, and adapted work progresses in parallel week folders.
