from tools import profile_source, analyze_benchmark, detect_hotspots


def test_profile_source():
    result = profile_source.execute({"source": "def f():\n    for x in xs:\n        print(x)"})
    assert result.success
    assert result.data["metrics"]["loop_count"] == 1
    assert result.data["metrics"]["function_count"] == 1


def test_benchmark():
    result = analyze_benchmark.execute({"baseline_ms": 200, "candidate_ms": 150, "samples": 5})
    assert result.success
    assert result.data["change_percent"] == -25.0
    assert result.data["regression"] is False


def test_hotspots():
    result = detect_hotspots.execute({"records": [{"name": "a", "duration_ms": 10}, {"name": "b", "duration_ms": 30}]})
    assert result.success
    assert result.data["hotspots"][0]["name"] == "b"
    assert result.data["hotspots"][0]["share_percent"] == 75.0
