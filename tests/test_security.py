from tools import profile_source, analyze_benchmark, detect_hotspots


def test_missing_fields_rejected():
    assert not profile_source.execute({}).success
    assert not analyze_benchmark.execute({"baseline_ms": 10}).success


def test_unexpected_fields_rejected():
    assert not analyze_benchmark.execute({"baseline_ms": 10, "candidate_ms": 11, "secret": "x"}).success


def test_invalid_values_rejected():
    assert not analyze_benchmark.execute({"baseline_ms": 0, "candidate_ms": 11}).success
    assert not detect_hotspots.execute({"records": [{"name": "x", "duration_ms": -1}]}).success
