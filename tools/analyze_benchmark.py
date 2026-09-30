"""Benchmark comparison tool using numeric samples."""
import statistics
from contracts.tool_contract import ToolContract, ToolMetadata


def _analyze(inputs: dict) -> dict:
    baseline = inputs["baseline_ms"]
    candidate = inputs["candidate_ms"]
    if baseline <= 0 or candidate <= 0:
        raise ValueError("Benchmark times must be positive")
    change_pct = ((candidate - baseline) / baseline) * 100
    return {"baseline_ms": baseline, "candidate_ms": candidate, "change_percent": round(change_pct, 4), "regression": candidate > baseline, "samples": inputs.get("samples", 1), "interpretation": "candidate slower" if candidate > baseline else "candidate not slower"}


TOOL = ToolContract(ToolMetadata("analyze_benchmark", "Compare a baseline benchmark measurement with a candidate measurement.", {"type": "object", "properties": {"baseline_ms": {"type": "number"}, "candidate_ms": {"type": "number"}, "samples": {"type": "integer", "minimum": 1}}, "required": ["baseline_ms", "candidate_ms"], "additionalProperties": False}), _analyze)
