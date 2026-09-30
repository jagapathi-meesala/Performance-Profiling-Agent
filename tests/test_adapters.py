from adapters import PortableAdapter, ToolRegistry
from core.agent_core import PerformanceProfilingAgent
from tools import analyze_benchmark


def test_portable_adapter():
    registry = ToolRegistry(); registry.register(analyze_benchmark)
    adapter = PortableAdapter(PerformanceProfilingAgent(registry))
    response = adapter.invoke({"tool": "analyze_benchmark", "input": {"baseline_ms": 10, "candidate_ms": 12}})
    assert response["success"] is True
    assert response["data"]["change_percent"] == 20.0
