# AER System Overview

This is the initial architectural decomposition for AER. It is intentionally implementation-neutral.

## System layers

### 1. Mission and experiment layer
Defines scenarios, mission goals, benchmark metrics, seeds, environmental conditions and acceptance criteria.

### 2. Autonomy layer
Future modules may include:
- mission planning
- local planning
- obstacle avoidance
- perception
- state estimation
- health/fault handling

### 3. Flight-control interface
Provides a stable boundary to an autopilot or simulator. AER should avoid coupling research code to one flight stack until a concrete requirement justifies it.

### 4. Simulation layer
Runs repeatable scenarios before hardware testing. Every benchmark should record simulator version, vehicle model, sensor configuration, seed and software revision.

### 5. Hardware abstraction
Tracks compute, sensors, power, communications, airframe and payload without embedding board-specific assumptions into higher-level research code.

### 6. Telemetry and evaluation
Logs timestamps, states, commands, errors, resource usage and experiment metadata. Evaluation should be reproducible from saved artifacts.

## Cross-cutting rules

- Coordinate frames must be named explicitly.
- Physical units must be documented.
- Timestamps must use a defined clock/source.
- Configuration belongs in version control where practical.
- Failures that matter should become regression tests.
- External research claims must not be presented as measured AER results.

## First architecture milestone

Establish one simulator-backed baseline scenario with:
1. fixed configuration,
2. deterministic/repeatable setup where possible,
3. structured telemetry,
4. a small evaluation script,
5. saved benchmark results.

Only after that baseline exists should AER compare alternative autonomy methods.
