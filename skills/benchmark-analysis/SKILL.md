---
name: benchmark-analysis
description: Compare baseline and candidate performance measurements.
---
# Benchmark Analysis

## Purpose
Quantify change between two positive benchmark measurements.

## Inputs
Baseline and candidate times in milliseconds, with an optional sample count.

## Processing
Calculate percentage change using the baseline as denominator and identify whether the candidate is slower.

## Outputs
Return measurements, percentage change, regression flag, and interpretation.

## Limitations
The tool does not establish statistical significance and does not control benchmark environment variability.

## Expected behavior
Non-positive measurements are rejected and no result is invented for invalid input.
