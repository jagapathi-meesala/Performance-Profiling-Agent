# Performance Profiling Agent

A framework-independent OpenGAP 0.1.0 agent for source-performance inspection, benchmark comparison, and profiling-hotspot analysis.

## Architecture
The core agent depends on a dynamic registry and framework-neutral tool contract. Three domain tools implement static source metrics, benchmark comparison, and hotspot ranking. Adapters expose a simple invocation protocol for external runtimes.

## Installation
Use Python 3.10+ and install the test dependency from `requirements.txt`.

```bash
python -m pip install -r requirements.txt
pytest -q
```

## Configuration
Runtime configuration is environment-only. Copy `.env.example` into your environment and provide values for the required variables; no production credentials are included.

## Tools
- `profile_source.py` — deterministic AST-based source indicators.
- `analyze_benchmark.py` — baseline/candidate comparison.
- `detect_hotspots.py` — duration ranking and share calculation.

## Skills
- performance-analysis
- benchmark-analysis
- hotspot-detection

## Usage
Register the tools and invoke them through `PerformanceProfilingAgent`. Tools return structured `ToolResult` objects and reject invalid inputs.

## Testing
The suite covers core execution, contracts, registry behavior, adapters, security/input validation, documentation, and OpenGAP manifest checks.

## Portability
The core does not import OpenAI, CrewAI, Claude, or Lyzr. `PortableAdapter` defines a neutral request/response boundary. Runtime compatibility with any particular external framework requires an integration layer and separate runtime testing.

## Limitations
Static source counts are not runtime profiles. Benchmark comparisons do not prove statistical significance, and supplied hotspot records cannot establish causality.

## OpenGAP
The manifest declares `spec_version: "0.1.0"` and references only repository-local skills and tools. The official OpenGAP reference documents `agent.yaml` as the strict manifest and provides `opengap validate` for validation.
