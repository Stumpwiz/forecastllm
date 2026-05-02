# Week 8 Gasoline Data

Week 8 uses local weekly gasoline price data for the agentic forecasting domain.

Recommended source:
- FRED/EIA series `GASREGW` (U.S. Regular All Formulations Gasoline Price, weekly).

Data policy:
- Full/raw gasoline files are not committed to this repository.
- Store your CSV locally and reference it through `.env`.

Configuration:
- Set `GASOLINE_DATA_PATH` in `.env` to your local CSV path.
- Example:
  - `GASOLINE_DATA_PATH=/absolute/path/to/GASREGW.csv`

Loader:
- `week8/gasoline_loader.py::load_gasoline_series()` checks:
  1. explicit function `path`
  2. `GASOLINE_DATA_PATH` from `.env`
  3. local defaults under `data/gasoline/`
