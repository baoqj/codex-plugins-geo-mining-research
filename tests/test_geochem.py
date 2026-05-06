from geomine.geochem import anomaly_class, median_absolute_deviation, percentile_rank, robust_z_score


def test_percentile_rank():
    assert percentile_rank([1, 2, 3, 4, 5], 4) == 80.0


def test_mad_and_robust_z_score():
    values = [1, 2, 2, 2, 3, 10]
    assert median_absolute_deviation(values) == 0.5
    assert robust_z_score(values, 10) > 3


def test_anomaly_class():
    values = [1, 2, 2, 2, 3, 4, 5, 10]
    assert anomaly_class(values, 10) == "strong anomaly"
    assert anomaly_class(values, 2) == "background"
