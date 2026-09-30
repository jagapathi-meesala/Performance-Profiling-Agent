# Explainability

## Inputs and Data Sources
The agent accepts Python source text, benchmark measurements, and structured profiling records through its tool interfaces. Data sources are limited to the input supplied by the caller; the agent does not silently fetch external performance data.

### Input Requirements
`profile_source` requires a non-empty Python source string. `analyze_benchmark` requires positive baseline and candidate milliseconds, while `detect_hotspots` requires named records with non-negative durations.

### Input Mechanisms
Inputs arrive as validated dictionaries through the framework-independent tool contract. Unknown fields are rejected where the tool schema disallows additional properties.

## Decision and Reasoning
The agent makes deterministic calculations from supplied evidence rather than inventing runtime measurements. It uses AST counts for source analysis, baseline-relative percentage change for benchmark comparison, and duration share for hotspot ranking.

### Rules Applied
For benchmark analysis, percentage change is `(candidate - baseline) / baseline * 100`. For hotspot detection, each record's share is `duration / total_duration * 100` when total duration is non-zero.

### Failure Handling
Malformed input, missing required fields, unexpected fields, invalid benchmark values, and invalid profiling records produce structured errors. The agent does not convert invalid data into a successful-looking result.

### Expected Outputs
Outputs contain structured metrics and an explicit success/error state. Findings should be interpreted as evidence from the supplied measurements, not as proof of a root cause.

### Worked Example
A baseline of 100 ms and candidate of 125 ms yields a 25 percent increase and a regression flag. Profiling records of 80 ms and 20 ms yield hotspot shares of 80 percent and 20 percent respectively.

## Limits and Constraints
Static source analysis cannot measure actual runtime cost, and benchmark comparison cannot remove environmental noise or establish statistical significance. Hotspot ranking is constrained to the records provided and cannot identify unrecorded CPU, memory, I/O, network, or scheduler effects.

### Constraints
The implementation currently profiles Python source structurally and accepts externally supplied benchmark/profile measurements. It does not execute arbitrary submitted code, attach to live processes, or claim framework certification.

### Known Issues
Different hardware, Python versions, workloads, and warm-up states can materially affect benchmark measurements. A ranked hotspot can be correlated with time consumption without proving that changing it will improve end-to-end performance.

### Unsupported Behavior
The agent does not provide fabricated profiling data, execute arbitrary source as part of static analysis, or claim a performance improvement without supplied evidence.
