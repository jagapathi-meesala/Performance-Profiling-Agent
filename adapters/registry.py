"""Dynamic tool registry; no framework-specific dependencies."""
from contracts.tool_contract import ToolContract


class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, ToolContract] = {}

    def register(self, tool: ToolContract) -> None:
        if tool.metadata.name in self._tools:
            raise ValueError(f"Tool already registered: {tool.metadata.name}")
        self._tools[tool.metadata.name] = tool

    def get(self, name: str) -> ToolContract | None:
        return self._tools.get(name)

    def names(self) -> list[str]:
        return sorted(self._tools)

    def discover(self) -> dict[str, ToolContract]:
        return dict(self._tools)
