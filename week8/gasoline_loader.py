from __future__ import annotations

import os
from pathlib import Path

import pandas as pd

DEFAULT_DATA_CANDIDATES = (
    "data/gasoline/GASREGW.csv",
    "data/gasoline/gasoline_weekly.csv",
    "data/gasoline/fred_gasregw.csv",
)
DEFAULT_SOURCE = "FRED/EIA"
DEFAULT_DESCRIPTION = "U.S. Regular All Formulations Gasoline Price (Weekly)"
DEFAULT_UNIT = "dollars_per_gallon"
DATE_COLUMN_CANDIDATES = (
    "observation_date",
    "Observation Date",
    "DATE",
    "date",
    "timestamp",
)


def _clean_column_name(name: object) -> str:
    return str(name).replace("\ufeff", "").strip()


def _find_column(df: pd.DataFrame, candidates: tuple[str, ...]) -> str | None:
    normalized = {_clean_column_name(c).lower(): c for c in df.columns}
    for candidate in candidates:
        key = _clean_column_name(candidate).lower()
        if key in normalized:
            return normalized[key]
    return None


def _resolve_data_path(path: str | None) -> Path:
    if path:
        candidate = Path(path).expanduser()
        if candidate.exists():
            return candidate
        raise FileNotFoundError(
            f"Gasoline data file not found at explicit path: {candidate}\n"
            "Download FRED/EIA weekly gasoline data (series GASREGW), save it as CSV, "
            "then set GASOLINE_DATA_PATH in .env or pass `path=` directly."
        )

    env_path = os.getenv("GASOLINE_DATA_PATH")
    if env_path:
        candidate = Path(env_path).expanduser()
        if candidate.exists():
            return candidate
        raise FileNotFoundError(
            f"GASOLINE_DATA_PATH is set but file does not exist: {candidate}\n"
            "Update GASOLINE_DATA_PATH in .env to point at a valid local CSV."
        )

    project_root = Path(__file__).resolve().parent.parent
    for relative_path in DEFAULT_DATA_CANDIDATES:
        candidate = project_root / relative_path
        if candidate.exists():
            return candidate

    searched = "\n".join(str(project_root / p) for p in DEFAULT_DATA_CANDIDATES)
    raise FileNotFoundError(
        "No local gasoline CSV found.\n"
        "Expected one of:\n"
        f"{searched}\n\n"
        "Fix: download FRED/EIA series GASREGW as CSV and either:\n"
        "1) Save to data/gasoline/GASREGW.csv, or\n"
        "2) Set GASOLINE_DATA_PATH in .env, or\n"
        "3) Pass `path=` to load_gasoline_series()."
    )


def _detect_value_column(df: pd.DataFrame, series_id: str) -> str:
    lower_map = {_clean_column_name(col).lower(): col for col in df.columns}

    if series_id in df.columns:
        return series_id
    series_id_lower = series_id.lower()
    if series_id_lower in lower_map:
        return lower_map[series_id_lower]
    if "value" in df.columns:
        return "value"
    if "value" in lower_map:
        return lower_map["value"]

    excluded = {
        "observation_date",
        "observation date",
        "date",
        "timestamp",
        "series_id",
        "source",
        "description",
        "unit",
    }
    numeric_candidates = [
        c
        for c in df.columns
        if _clean_column_name(c).lower() not in excluded and pd.api.types.is_numeric_dtype(df[c])
    ]
    if len(numeric_candidates) == 1:
        return numeric_candidates[0]

    raise ValueError(
        "Could not identify value column in gasoline CSV.\n"
        f"Expected either '{series_id}' or 'value' column. Found columns: {list(df.columns)}"
    )


def load_gasoline_series(path: str | None = None, series_id: str = "GASREGW") -> pd.DataFrame:
    data_path = _resolve_data_path(path)
    df = pd.read_csv(data_path)

    if df.empty:
        raise ValueError(f"Gasoline CSV is empty: {data_path}")

    timestamp_column = _find_column(df, DATE_COLUMN_CANDIDATES)
    if timestamp_column is None:
        columns = ", ".join(_clean_column_name(c) for c in df.columns)
        raise ValueError(
            "Gasoline CSV must include a date column named one of: "
            "'observation_date', 'Observation Date', 'DATE', 'date', or 'timestamp'. "
            f"Found columns: [{columns}]"
        )

    value_column = _detect_value_column(df, series_id)

    normalized = pd.DataFrame(
        {
            "timestamp": pd.to_datetime(df[timestamp_column], errors="coerce"),
            "value": pd.to_numeric(df[value_column], errors="coerce"),
            "series_id": (
                df["series_id"].astype(str)
                if "series_id" in df.columns
                else pd.Series([series_id] * len(df), index=df.index, dtype="string")
            ),
            "source": (
                df["source"].astype(str)
                if "source" in df.columns
                else pd.Series([DEFAULT_SOURCE] * len(df), index=df.index, dtype="string")
            ),
            "description": (
                df["description"].astype(str)
                if "description" in df.columns
                else pd.Series([DEFAULT_DESCRIPTION] * len(df), index=df.index, dtype="string")
            ),
            "unit": (
                df["unit"].astype(str)
                if "unit" in df.columns
                else pd.Series([DEFAULT_UNIT] * len(df), index=df.index, dtype="string")
            ),
        }
    )

    normalized = normalized.dropna(subset=["timestamp", "value"]).sort_values("timestamp")
    normalized = normalized.reset_index(drop=True)

    if normalized.empty:
        raise ValueError(
            f"Gasoline CSV at {data_path} produced no valid rows after parsing timestamps/values."
        )

    return normalized
