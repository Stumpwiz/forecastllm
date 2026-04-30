import os
from pathlib import Path

import numpy as np
import pandas as pd
from dotenv import load_dotenv

_TIMESTAMP_CANDIDATES = ("timestamp", "date", "datetime", "ds")
_VALUE_CANDIDATES = ("value", "actual", "y", "target")
_SERIES_ID_CANDIDATES = ("series_id", "id", "unique_id")
_DEFAULT_M4_PATH = Path(
    "/home/geo/Projects/Python/forecastllm/data/m4/processed/hourly_longest_series.csv"
)

load_dotenv()


def _read_table(path: Path) -> pd.DataFrame:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(path)
    if suffix in {".parquet", ".pq"}:
        return pd.read_parquet(path)
    raise ValueError(f"Unsupported file type '{suffix}' for {path}")


def _pick_column(columns: list[str], candidates: tuple[str, ...], kind: str) -> str:
    for candidate in candidates:
        if candidate in columns:
            return candidate
    raise ValueError(f"Could not infer {kind} column. Available: {columns}")


def _resolve_dataset_path() -> Path:
    raw_path = os.getenv("FORECAST_DATA_PATH")
    if not raw_path:
        raw_path = str(_DEFAULT_M4_PATH)
    data_path = Path(raw_path).expanduser().resolve()
    if not data_path.exists():
        raise FileNotFoundError(f"Dataset not found: {data_path}")
    return data_path


def load_sample_series(series_id: str | None = None) -> pd.DataFrame:
    """
    Load one M4 hourly series from local data and return columns: timestamp, value.
    """
    data_path = _resolve_dataset_path()
    df = _read_table(data_path)
    if df.empty:
        raise ValueError(f"Dataset is empty: {data_path}")

    columns = list(df.columns)
    ts_col = _pick_column(columns, _TIMESTAMP_CANDIDATES, "timestamp")
    y_col = _pick_column(columns, _VALUE_CANDIDATES, "value")

    series_id_col = next((c for c in _SERIES_ID_CANDIDATES if c in columns), None)
    if series_id is not None:
        if series_id_col is None:
            raise ValueError(
                f"`series_id` was provided ({series_id!r}) but dataset has no series-id column: {data_path}"
            )
        df = df[df[series_id_col].astype(str) == str(series_id)].copy()
        if df.empty:
            raise ValueError(f"Series '{series_id}' not found in {data_path}")

    normalized = df[[ts_col, y_col]].rename(columns={ts_col: "timestamp", y_col: "value"}).copy()
    normalized["timestamp"] = pd.to_datetime(normalized["timestamp"], errors="coerce")
    normalized["value"] = pd.to_numeric(normalized["value"], errors="coerce")
    normalized = normalized.dropna(subset=["timestamp", "value"])
    normalized = normalized.sort_values("timestamp").drop_duplicates(subset=["timestamp"], keep="last")
    normalized = normalized.reset_index(drop=True)
    if normalized.empty:
        raise ValueError(f"Dataset has no valid timestamp/value rows after cleaning: {data_path}")
    return normalized


def load_synthetic_series(periods: int = 240, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    idx = np.arange(periods)
    timestamp = pd.date_range("2024-01-01", periods=periods, freq="h")
    trend = np.linspace(80.0, 110.0, periods)
    daily = 4.0 * np.sin(2 * np.pi * idx / 24.0)
    weekly = 2.0 * np.sin(2 * np.pi * idx / 168.0)
    noise = rng.normal(loc=0.0, scale=0.6, size=periods)
    value = trend + daily + weekly + noise
    return pd.DataFrame({"timestamp": timestamp, "value": value})
