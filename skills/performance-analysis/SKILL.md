---
name: performance-analysis
description: Analyze Python source for deterministic static performance indicators.
---
# Performance Analysis

## Purpose
Analyze source without executing it and expose structural indicators such as loops, calls, comprehensions, and function count.

## Inputs
A Python source string.

## Processing
Parse the source with Python AST and count supported constructs.

## Outputs
Return structured metrics and discovered function names.

## Limitations
Static counts do not measure wall-clock runtime, I/O wait, memory pressure, or hardware effects.

## Expected behavior
Malformed Python raises a structured tool error rather than producing a fabricated profile.
