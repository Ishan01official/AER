# AER Drone Atlas

**Research cutoff: 5 October 2026 (Asia/Kolkata).** An expandable evidence library for civilian aerial engineering; public military history and comparisons remain non-operational. This is a researched foundation, not an exhaustive encyclopedia or flight-qualified design. No aircraft, supplier, algorithm or performance figure has been independently tested by AER for this atlas.

## Read in this order

1. [Repository-aware plan and method](methodology.md).
2. [Taxonomy](taxonomy.md) and [coverage matrix](data/coverage.csv).
3. [History and enabling technologies](history.md).
4. [Platform comparisons](platforms/comparisons.md), [DJI Mini 4 Pro case](platforms/dji-mini-4-pro.md), [Crazyflie research-platform case](platforms/crazyflie.md), [ArduPilot and PX4](platforms/open-ecosystems.md).
5. [State estimation and timing](subsystems/state-estimation.md), [propulsion and energy](subsystems/propulsion-energy.md), [subsystem engineering map](subsystems/engineering-map.md).
6. [Global/Indian supply chains](supply-chain/README.md) and [regulatory evidence](supply-chain/regulation.md).
7. [Civilian development path](development-path.md) and [phone capture MVP](phone-mvp.md).
8. [Challenges and future scenarios](challenges.md), [visual reference catalog](visuals.md), [open questions](open-questions.md).
9. [Dataset schema](data/schema.md), [source register](sources.md), [research changelog](CHANGELOG.md).

## What this adds to AER

The existing [DJI company and sourcing study](../case-studies/dji/README.md), [project roadmap](../../docs/roadmap.md) and [system boundaries](../../docs/architecture/system-overview.md) remain authoritative project context. The atlas adds cross-platform comparisons, explicit provenance, testable research questions and a phone-to-aircraft measurement path. It does not silently turn research proposals into selected requirements.

Start with **a capability-aware phone image/IMU recorder and replayable quality report**, alongside one simulation baseline. These establish reliable measurements before AER trains vision models or designs custom avionics. Proposed metrics and budgets are labeled estimates; no purchases are implied.

## Maintaining it

Run `python3 research/drone-atlas/tools/validate.py` from repository root. Every research increment should add a checked claim, its source and conditions, an uncertainty or question, and an AER implication. Coverage status means depth of evidence, never a percentage of the entire drone industry.
