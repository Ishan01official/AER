# AER Roadmap

## Phase 0 — Foundation

- Organize research, experiment, simulation and implementation areas.
- Preserve weekly research briefings.
- Define experiment metadata and naming conventions.
- Select an initial civilian benchmark scenario.

## Phase 1 — Reproducible simulation baseline

- Bring up one supported SITL/simulation environment.
- Define one simple mission.
- Capture telemetry and software/environment versions.
- Re-run the baseline enough times to understand normal variance.
- Store evaluation results in a reproducible form.

## Phase 2 — Autonomy experiments

Candidate areas:
- visual perception
- state estimation
- planning
- adaptive compute
- fault/recovery behavior

Each experiment should state a hypothesis and compare against the preserved baseline.

## Phase 3 — Hardware-in-the-loop / bench validation

- Validate timing and interfaces on representative compute.
- Measure CPU/GPU/memory/power where applicable.
- Test sensor and communication failure cases.
- Confirm coordinate frames, units and timestamps.

## Phase 4 — Controlled prototype validation

Move only mature, measured capabilities to a physical prototype. Begin with controlled civilian test scenarios and conservative operating limits.

## Phase 5 — R&D platform

Longer term, AER should become a reusable platform where new papers or algorithms can be evaluated against stable scenarios, metrics and regression tests instead of one-off demos.
