"""Framework-independent tool contract used by the registry."""
from dataclasses import dataclass
from typing import Any, Callable, Mapping


@dataclass(frozen=True)
class ToolMetadata:
    name: str
    description: str
    input_schema: Mapping[str, Any]


@dataclass(frozen=True)
class ToolResult:
    success: bool
    data: dict[str, Any]
    error: str | None = None


class ToolContract:
    metadata: ToolMetadata

    def __init__(self, metadata: ToolMetadata, executor: Callable[[dict[str, Any]], dict[str, Any]]):
        self.metadata = metadata
        self._executor = executor

    def validate(self, inputs: dict[str, Any]) -> None:
        if not isinstance(inputs, dict):
            raise TypeError("Tool inputs must be an object")
        required = self.metadata.input_schema.get("required", [])
        properties = self.metadata.input_schema.get("properties", {})
        missing = [key for key in required if key not in inputs]
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")
        if self.metadata.input_schema.get("additionalProperties") is False:
            unknown = sorted(set(inputs) - set(properties))
            if unknown:
                raise ValueError(f"Unexpected fields: {', '.join(unknown)}")

    def execute(self, inputs: dict[str, Any]) -> ToolResult:
        try:
            self.validate(inputs)
            return ToolResult(True, self._executor(inputs))
        except (TypeError, ValueError, OSError) as exc:
            return ToolResult(False, {}, str(exc))
