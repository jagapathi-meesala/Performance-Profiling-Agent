"""Portable agent core with dynamic tool discovery and structured execution."""
from contracts.tool_contract import ToolContract, ToolResult
from adapters.registry import ToolRegistry


class PerformanceProfilingAgent:
    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    def discover_tools(self) -> list[str]:
        return self.registry.names()

    def execute(self, tool_name: str, inputs: dict) -> ToolResult:
        tool = self.registry.get(tool_name)
        if tool is None:
            return ToolResult(False, {}, f"Unknown tool: {tool_name}")
        return tool.execute(inputs)
