"""Framework-neutral adapter boundary.

This adapter exposes a plain dictionary protocol so OpenAI SDK, CrewAI,
Claude Code, and Lyzr integrations can wrap it without coupling core logic
or tools to a particular framework. Compatibility is architectural, not a
claim of runtime certification.
"""
from core.agent_core import PerformanceProfilingAgent


class PortableAdapter:
    def __init__(self, agent: PerformanceProfilingAgent):
        self.agent = agent

    def capabilities(self) -> dict:
        return {"tools": self.agent.discover_tools(), "protocol": "tool-name + object-input"}

    def invoke(self, request: dict) -> dict:
        if not isinstance(request, dict):
            return {"success": False, "error": "Request must be an object"}
        result = self.agent.execute(request.get("tool", ""), request.get("input", {}))
        return {"success": result.success, "data": result.data, "error": result.error}
