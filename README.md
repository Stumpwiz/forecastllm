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

## Current Status (as of 2026-04-27)

- Week 6 adapted notebooks are complete: `day1.ipynb` through `day5.ipynb`.
- Week 7 Day 1 is adapted in `week7/day1.ipynb` and runs end-to-end.
- Week 7 Day 2 is adapted in `week7/day2.ipynb` and runs end-to-end.
- Week 7 Day 3+ and Week 8 are not yet adapted.
- Original notebooks remain present under `notebooks_original/week6`, `notebooks_original/week7`, and `notebooks_original/week8`.


## Current Progress

### Week 6: Complete

- Day 1: Built forecasting dataset workflow
  - Loaded/normalized a single primary time series
  - Established load -> inspect -> clean -> visualize -> sample -> split pipeline

- Day 2: Built supervised forecasting representation
  - Created lag features
  - Added calendar features
  - Established chronological train/test split

- Day 3: Added baselines and evaluation
  - Naive forecast
  - Seasonal naive forecast
  - MAE and sMAPE

- Day 4: Added first learned forecasting model
  - Linear regression using lag/calendar features
  - Explicit one-step-ahead evaluation protocol
  - Leakage sanity checks
  - Exported evaluated test slice

- Day 5: Compared forecasting models
  - Linear regression
  - Ridge regression
  - Random forest
  - Baseline comparison table
  - Exported evaluated test slice

Note: Week 6 currently uses a single daily sample/synthetic time series; real M4 and multi-series work is deferred.

### Week 7: In Progress

- Day 1: LoRA/QLoRA setup adapted to forecasting prompts
  - Reuses Week 6 supervised features (`lag_1`, `lag_2`, `lag_3`, `lag_7`, `day_of_week`, `month`)
  - Builds instruction-style forecasting prompt/completion records
  - Includes full-precision, 8-bit, and 4-bit model loading paths
  - Includes optional LoRA adapter attach path via `FINETUNED_MODEL`
  - Includes LoRA parameter-size estimation walkthrough
  - End-to-end run succeeded with some deprecation warnings (non-blocking)
- Day 2: Prompt-dataset and tokenizer-prep flow adapted to forecasting
  - Builds forecasting prompt/completion records from Week 6-style lag/calendar features
  - Computes token-length distributions and selects truncation cutoff
  - Produces `DatasetDict` for train/validation/test
  - Includes optional Hugging Face dataset push via `HF_USERNAME` and `HF_TOKEN`
  - End-to-end run succeeded

### Next Step

- Adapt `notebooks_original/week7/day3.ipynb` into `week7/day3.ipynb`, preserving Day 3 training structure while using forecasting prompt datasets from Week 7 Day 2.


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

## Auth and Secrets

- `week7/day1.ipynb` and `week7/day2.ipynb` do not require a `.env` file for default execution.
- For public models (current default: `TinyLlama/TinyLlama-1.1B-Chat-v1.0`), no Hugging Face token is typically needed.
- If using gated/private Hugging Face models or private adapters, authenticate with:
  - `huggingface-cli login`
  - or set `HF_TOKEN` in your shell/session
- Optional environment variables currently used:
  - `BASE_MODEL`
  - `FINETUNED_MODEL`
  - `HF_TOKEN`

## Practical Next Steps

1. Adapt `notebooks_original/week7/day3.ipynb` into `week7/day3.ipynb`.
2. Reuse Week 7 Day 2 prompt datasets and tokenization/truncation decisions.
3. Keep Day 3 runnable end-to-end before moving to Day 4.
4. Continue sequentially through Week 7 and Week 8, preserving the original course order.

## Notes

This repo is a personal learning adaptation of course material. The structure is intentionally simple: originals are archived for reference, and adapted work progresses in parallel week folders.
