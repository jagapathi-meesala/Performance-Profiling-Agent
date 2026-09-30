from adapters.registry import ToolRegistry
from core.agent_core import PerformanceProfilingAgent
from tools import profile_source, analyze_benchmark, detect_hotspots


def make_agent():
    registry = ToolRegistry()
    for tool in (profile_source, analyze_benchmark, detect_hotspots):
        registry.register(tool)
    return PerformanceProfilingAgent(registry)


def test_discovery_and_execution():
    agent = make_agent()
    assert agent.discover_tools() == ["analyze_benchmark", "detect_hotspots", "profile_source"]
    result = agent.execute("analyze_benchmark", {"baseline_ms": 100, "candidate_ms": 125})
    assert result.success is True
    assert result.data["change_percent"] == 25.0
