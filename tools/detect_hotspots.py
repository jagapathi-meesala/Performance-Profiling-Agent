"""Rank supplied profiling records by cumulative time."""
from contracts.tool_contract import ToolContract, ToolMetadata


def _detect(inputs: dict) -> dict:
    records = inputs["records"]
    if not records:
        return {"hotspots": [], "total_ms": 0.0}
    normalized = []
    total = 0.0
    for record in records:
        name = record.get("name")
        ms = record.get("duration_ms")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Each record requires a non-empty name")
        if not isinstance(ms, (int, float)) or ms < 0:
            raise ValueError("duration_ms must be a non-negative number")
        normalized.append({"name": name, "duration_ms": float(ms)})
        total += float(ms)
    normalized.sort(key=lambda item: item["duration_ms"], reverse=True)
    for item in normalized:
        item["share_percent"] = round((item["duration_ms"] / total * 100) if total else 0.0, 4)
    return {"hotspots": normalized, "total_ms": round(total, 4)}


TOOL = ToolContract(ToolMetadata("detect_hotspots", "Rank profiling records by duration and calculate their share of total observed time.", {"type": "object", "properties": {"records": {"type": "array", "items": {"type": "object"}}}, "required": ["records"], "additionalProperties": False}), _detect)
