# Civilian AER development path

This extends the [existing roadmap](../../docs/roadmap.md), preserving simulation before airborne autonomy. All budgets below are **E: rough October 2026 INR planning allowances**, not verified market quotations. They assume an existing computer/phone, unpaid development time and access to a lawful test setting. Import taxes, training, insurance, site rental, certification and labor are excluded unless explicitly budgeted later. Stage allowances are incremental and overlap in reusable tools; do not sum them into a product price.

| Stage | Prerequisites and skills | Deliverables / equipment | Planning allowance | Test and exit condition |
|---|---|---|---|---|
| 0 Foundations and simulation | Python/C++, Git, vectors, basic control; existing computer | One pinned supported autopilot/simulator, repeatable mission, saved logs and analysis | ₹0–15,000 for incidental storage/tools; computer excluded | Baseline repeats, version/seed manifest, failure scenario replay; thresholds agreed after baseline |
| 1 Phone measurement | Android programming, acquisition, basic imaging | Capability-aware recorder, chart/target, tripod, storage, calibration and timing report | ₹2,000–12,000; existing phone; calibrated commercial chart may require separate quote | Three repeat sessions; declared clock relationship; dropped samples counted; replay works |
| 2 Small civilian prototype | Stage 0 evidence, appropriate operator/legal/site clearance, electronics assembly | Supported ready baseline or matched kit; batteries/charger, basic spares, guarded work area, multimeter | ₹35,000–100,000 for simple modular baseline; specialized localization excluded | Exact BOM/firmware recorded; manufacturer procedures followed; power/failsafe bench checks; bounded manual trials |
| 3 Reliability and logging | Baseline aircraft stable; disciplined experiment design | Calibrations, current sensing, maintenance log, test matrix and reference measurements | ₹15,000–50,000 for fixtures/instruments/spares; lab rental extra | Repeat mission dataset; faults explained; reserve assumptions measured; unresolved critical faults block progression |
| 4 Selected custom software/hardware | A measured requirement unavailable in stock modules | Host/companion feature or low-risk adapter PCB; oscilloscope/logic analyzer access; review | ₹30,000–150,000 per limited prototype iteration | Interface tests, rollback, power/timing margin and regression evidence; unchanged baseline remains reproducible |
| 5 Advanced civilian research | Validated logging, localization and fallback | Indoor perception, mapping, precision landing or multi-vehicle simulation; external reference access | ₹100,000–500,000+ depending on sensing; motion capture not included | Compare against baseline; uncertainty and adverse cases reported; airborne authority expanded only with evidence |
| 6 Product readiness | Selected civilian customer/mission, stable requirements, compliance plan | Design/manufacturing reviews, pilot builds, supplier qualification, test fixtures, service and update process | ₹1,000,000–5,000,000+ placeholder for limited pilot engineering, not full certification or factory | Traceable repeat builds, verified requirements, maintainability and applicable approvals; full business case required |

**Budget sensitivity:** a thermal payload, lidar, dedicated synchronization hardware or motion-capture installation can overwhelm the basic aircraft budget. Obtain configuration-specific written quotes before selecting hardware. No price in this table is a supplier offer.

## Recommended first project

Build [the phone capture recorder](phone-mvp.md) and a single simulation evaluation scenario in parallel within the project workflow. The recorder answers “can AER trust its measurements?” The simulator answers “can AER reproduce and score a flight-control baseline?” Neither requires first manufacturing a custom motor or training a large model.

A compact initial backlog: define session schema; export one stationary recording; validate capture/arrival clocks; produce a rate/dropout chart; lock/record camera controls; repeat the same scene; preserve analysis configuration; document one failure. Then decide on a measurable image-quality objective. This is a proposed backlog, not completed software.

## Mission before BOM

Choose one civilian task, such as controlled visual inspection of a permitted static structure. Specify required image detail, coverage, working distance, lighting, duration, wind envelope, operator involvement and acceptable failure response. Derive camera/payload and airframe requirements from these. The smallest possible aircraft is not automatically the cheapest research platform.

Use established matched propulsion and a supported flight controller for the first prototype. Keep a companion computer optional until the task needs onboard processing. Buy adequate logging and spares before adding advanced sensors.

## “From scratch” has distinct meanings

| Level | What AER owns | Equipment and expertise | Feasibility/capital implication |
|---|---|---|---|
| Assemble modules | Mission, wiring, mounting, parameters and validation | Soldering/inspection, multimeter, fixtures, basic mechanical/electrical skills | Feasible initial stage within prototype allowance |
| Custom PCB using bought chips | Schematics, layout, power integrity, firmware, test | EDA, oscilloscope, reflow/assembly partner, EMC prechecks, embedded engineers | Multiple board spins and test fixtures; scope-dependent tens/hundreds of thousands INR |
| Custom motor/propeller/airframe | Electromagnetic/aerodynamic design, materials and process | Balancing, dynamometer, winding/lamination supplier, tooling, composite/CNC expertise | Specialized workshop and outsourced processes; quote-driven investment |
| Custom optics/camera module | Lens stack, alignment, sensor interface, ISP tuning | Optical bench, clean assembly, alignment/calibration equipment | Buy sensor/lens initially; precision production is a separate industrial effort |
| Semiconductor design | Circuit/IP design using external fabrication | IC design team, EDA/IP access, foundry process and test/package partners | Far beyond initial AER budgets; no fabricated cost estimate offered |
| Semiconductor fabrication | Wafer process, yield, cleanroom and equipment | Industrial facilities, process engineers, materials and metrology supply chain | Not a credible small-project milestone; different business and capital scale |

Local PCB assembly does not imply local semiconductor manufacture. Local battery-pack production does not imply domestic cell chemistry, separators or cathode supply.

## Advancement and stopping rules

Advance when the previous stage produces reviewable evidence. Stop an experiment when data cannot explain behavior, power/timing margins are unknown, the environment exceeds demonstrated limits, or a required authorization is unresolved. Keep logs of both successes and failures. Simulated success permits another test; it never by itself grants aircraft certification.

Source basis: [PX4 simulation](sources.md#r012), [Android APIs](sources.md#r004), [supplier evidence](supply-chain/README.md), [regulatory limits](supply-chain/regulation.md). Original architecture and stage decisions are AER proposals. No measured AER readiness is implied.
