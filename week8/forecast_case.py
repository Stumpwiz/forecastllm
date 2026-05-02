from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ForecastCase:
    series_id: str
    horizon: int
    cutoff_timestamp: str
    context: dict[str, Any] = field(default_factory=dict)
    features: dict[str, float] = field(default_factory=dict)
    actual: float | None = None
    naive_forecast: float | None = None
    seasonal_naive_forecast: float | None = None
    model_forecast: float | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ForecastResult:
    case: ForecastCase
    forecast: float
    model_name: str
    mae_vs_actual: float | None = None
    smape_vs_actual: float | None = None
    notes: str = ""


def _safe_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def case_from_row(
    row: Any,
    *,
    series_id: str = "m4_hourly_default",
    horizon: int = 1,
    feature_keys: list[str] | tuple[str, ...] | None = None,
    metadata: dict[str, Any] | None = None,
) -> ForecastCase:
    feature_keys = feature_keys or (
        "lag_1",
        "lag_2",
        "lag_3",
        "lag_7",
        "lag_24",
        "lag_168",
        "day_of_week",
        "month",
    )
    metadata = metadata or {}

    features: dict[str, float] = {}
    for key in feature_keys:
        value = _safe_float(getattr(row, key, None))
        if value is not None:
            features[key] = value

    timestamp_value = getattr(row, "timestamp", None)
    timestamp_str = str(timestamp_value) if timestamp_value is not None else ""

    return ForecastCase(
        series_id=series_id,
        horizon=horizon,
        cutoff_timestamp=timestamp_str,
        context={
            "day_of_week": int(features["day_of_week"]) if "day_of_week" in features else None,
            "month": int(features["month"]) if "month" in features else None,
        },
        features=features,
        actual=_safe_float(getattr(row, "value", None)),
        naive_forecast=_safe_float(getattr(row, "lag_1", None)),
        seasonal_naive_forecast=_safe_float(getattr(row, "lag_24", None)),
        metadata={
            "protocol": "one_step_ahead_chronological_no_shuffle",
            "metrics": ["mae", "smape"],
            **metadata,
        },
    )


def result_from_forecast(
    case: ForecastCase,
    *,
    forecast: float,
    model_name: str,
    notes: str = "",
) -> ForecastResult:
    actual = case.actual
    mae_value: float | None = None
    smape_value: float | None = None

    if actual is not None:
        mae_value = abs(float(forecast) - actual)
        denominator = abs(actual) + abs(float(forecast))
        if denominator > 0:
            smape_value = 200.0 * abs(float(forecast) - actual) / denominator
        else:
            smape_value = 0.0

    return ForecastResult(
        case=case,
        forecast=float(forecast),
        model_name=model_name,
        mae_vs_actual=mae_value,
        smape_vs_actual=smape_value,
        notes=notes,
    )
