"""Small deterministic geochemical statistics helpers."""

from __future__ import annotations

from statistics import median


def _clean(values: list[float | int | None]) -> list[float]:
    return sorted(float(value) for value in values if value is not None)


def percentile_rank(values: list[float | int | None], target: float | int) -> float:
    """Return the percentage of values less than or equal to target."""

    clean = _clean(values)
    if not clean:
        raise ValueError("values must include at least one numeric value")
    target_f = float(target)
    count = sum(1 for value in clean if value <= target_f)
    return (count / len(clean)) * 100.0


def median_absolute_deviation(values: list[float | int | None]) -> float:
    clean = _clean(values)
    if not clean:
        raise ValueError("values must include at least one numeric value")
    med = median(clean)
    return median([abs(value - med) for value in clean])


def robust_z_score(values: list[float | int | None], target: float | int) -> float:
    """Return a MAD-based robust z-score.

    The 0.6745 factor makes the score comparable to a standard z-score for
    normally distributed data. If MAD is zero, return 0 for the median and inf
    for values above or below it.
    """

    clean = _clean(values)
    if not clean:
        raise ValueError("values must include at least one numeric value")
    med = median(clean)
    mad = median_absolute_deviation(clean)
    target_f = float(target)
    if mad == 0:
        if target_f == med:
            return 0.0
        return float("inf") if target_f > med else float("-inf")
    return 0.6745 * (target_f - med) / mad


def anomaly_class(values: list[float | int | None], target: float | int) -> str:
    """Classify a value using percentile rank and robust z-score."""

    pct = percentile_rank(values, target)
    rz = robust_z_score(values, target)
    if pct >= 98 or rz >= 3:
        return "strong anomaly"
    if pct >= 95 or rz >= 2:
        return "moderate anomaly"
    if pct >= 90 or rz >= 1.5:
        return "weak anomaly"
    return "background"
