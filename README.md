# AER — Aerial · Engineering · Research

AER is an engineering R&D repository for exploring **civilian autonomous aerial systems**, AI, robotics, simulation, embedded systems, perception, control, and supporting engineering.

The project is being organized around a simple principle:

> Research ideas should become reproducible experiments, measurable simulations, and only then hardware prototypes.

## Current status

AER is in the **research and foundation stage**.

The repository currently contains a dated research briefing archive under `research/briefs/`. The engineering structure below provides a place to turn those findings into experiments, simulations, prototype code, and eventually validated hardware.

## Repository structure

```text
AER/
├── README.md
├── configs/                # Reproducible experiment/simulation configuration
├── data/                   # Dataset metadata and data-handling conventions
├── docs/
│   ├── architecture/       # System architecture and design documents
│   └── roadmap.md          # Project phases and milestones
├── experiments/            # Hypotheses, benchmark plans, results, regressions
├── hardware/               # Airframe, compute, sensors, electronics, BOM notes
├── research/
│   ├── briefs/             # Dated AER research briefings
│   └── papers/             # Paper notes and technical literature tracking
├── simulation/             # SITL/simulator scenarios and benchmark environments
├── src/                    # Production/prototype implementation
├── tests/                  # Unit, integration, simulation and regression tests
└── tools/                  # Developer, analysis and automation utilities
```

## Engineering workflow

1. **Research** — record relevant papers, systems, datasets, and technical developments.
2. **Hypothesis** — define what AER expects to improve and how it will be measured.
3. **Simulation** — reproduce a baseline before changing algorithms or hardware.
4. **Experiment** — change one meaningful variable at a time and preserve configuration.
5. **Regression testing** — turn failures into repeatable tests.
6. **Prototype** — move ideas to hardware only when simulation/bench evidence justifies it.
7. **Flight validation** — validate progressively in controlled, lawful civilian environments.

## Initial technical focus

The first useful platform capability is a **repeatable simulation and measurement benchmark**. It should eventually measure:

- mission/task completion
- trajectory or control error
- perception accuracy
- median and tail latency
- compute and memory usage
- robustness to sensor/environment changes
- regressions between software versions

No numerical acceptance threshold is treated as established until a baseline has been measured.

## Research archive

Dated weekly research briefings are stored as:

`research/briefs/YYYY-MM-DD.md`

The archive should distinguish:

- external author claims
- independently verified availability/reproduction
- AER interpretation
- proposed AER experiments
- measured AER results

## Project principles

- Reproducibility before complexity.
- Measurement before optimization.
- Simulation before unnecessary hardware risk.
- Explicit units, coordinate frames, timestamps, versions, and seeds.
- Keep research claims separate from AER experimental results.
- Preserve failures as regression tests.

## Roadmap

See [docs/roadmap.md](docs/roadmap.md) for the initial project path and [docs/architecture/system-overview.md](docs/architecture/system-overview.md) for the proposed system boundaries.
