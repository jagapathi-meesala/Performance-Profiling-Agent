---
name: hotspot-detection
description: Rank profiling records by observed duration.
---
# Hotspot Detection

## Purpose
Identify the highest-duration records in a supplied profiling dataset.

## Inputs
A list of named records containing non-negative duration values in milliseconds.

## Processing
Validate records, calculate total observed time, sort descending by duration, and calculate percentage share.

## Outputs
Return ordered hotspots and total observed time.

## Limitations
The result is limited to the supplied records and does not infer causality or profile resources that were not recorded.

## Expected behavior
Invalid names or negative/non-numeric durations are rejected with a structured error.
