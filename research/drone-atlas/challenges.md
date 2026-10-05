# Engineering challenges and conditional future directions

Cutoff: 2026-10-05. The table combines cited reference approaches with **I: proposed experiments**. It is not a ranking of solved technologies. No proposed AER result has been measured.

| Challenge / underlying constraint | Current approach and evidence | Remaining limitation | Measurable AER research question / experiment |
|---|---|---|---|
| Endurance versus payload | Wing-borne cruise and payload-specific planning [R022](sources.md#r022); solar demonstration [R027](sources.md#r027) | Added energy hardware increases mass; test conditions differ | How does useful imaging time per Wh change with added mass? Start with the [power model](subsystems/propulsion-energy.md), then matched bench data |
| Wind and weather | Environmental limits in manufacturer documents [R001](sources.md#r001), [R022](sources.md#r022) | Wind resistance rating is not precision, rain or reserve guarantee | Sweep simulated gusts; compare tracking error, saturation and reserve margin; no dangerous-weather flight |
| Vibration | Mechanical isolation and sensor-aware installation [R045](sources.md#r045) | Isolation resonance and clipping can defeat filtering | Compare vibration spectrum and clipped samples for two bench mounts under controlled excitation |
| GNSS-unreliable localization | Inertial/visual/range fusion [R003](sources.md#r003), [R013](sources.md#r013) | Drift, weak observability, moving objects and feature loss | Measure pose error and consistency versus duration of synthetic GNSS loss using an independent reference |
| Perception generalization | Calibrated vision and indoor lidar systems [R033](sources.md#r033) | Dust, glass, low texture, poor illumination and unseen conditions | Measure detection/pose failures across held-out lighting/texture sessions from the phone recorder |
| Communication quality | Explicit link and regional conditions [R001](sources.md#r001) | Latency and reconnection are different from nominal range | Inject packet delays/dropouts in simulation; measure stale-command rejection and recovery state |
| Compute and heat | Modular companion processors [R060](sources.md#r060) | Power/cooling mass; sustained performance differs from peak throughput | Benchmark a fixed recorded sequence; log p99 latency, temperature and energy at two supported power settings |
| Synchronization | Capture clocks and calibrated delay [R004](sources.md#r004), [R013](sources.md#r013) | Clock offsets, drift, rolling shutter and callback jitter | Recover injected offsets from held-out motion sequences; report confidence intervals |
| Cybersecurity | MAVLink message signing [R015](sources.md#r015) | No encryption implied; keys and update chain remain | In owned test systems, verify unsigned/stale input handling and update rollback without aircraft motion |
| Privacy / data governance | Local-first collection is an AER design proposal | Location and imagery may identify people or property | Measure whether export removes selected metadata while preserving calibration/reproducibility; use consented scenes |
| Certification | Indian official rules and certification context [R040](sources.md#r040), [R066](sources.md#r066) | Full applicable requirements and approvals not yet consolidated | Map every proposed requirement to an official provision, verification artifact and responsible owner |
| Reliability / maintenance | System-level logging and module revision control [R045](sources.md#r045) | Common-cause faults and unobserved degradation | Log repeated bench power cycles and connector checks; estimate failure counts with sample size, not “zero failures = perfect” |
| Docking | Integrated aircraft/dock specification [R037](sources.md#r037) | Weather, contact wear and failed alignment | Bench docking/contact tests plus simulated aborted approaches; record success distribution and recovery time |
| Multi-vehicle coordination | Crazyswarm research ecosystem [R020](sources.md#r020), [R021](sources.md#r021) | External localization, shared radio and scaling assumptions | Simulate increasing vehicle count, clock skew and dropped data; track minimum separation and scheduling delay |
| Cost / supply concentration | Qualified alternatives; IEA materials risk [R063](sources.md#r063) | Different resellers can share upstream sources | Build a BOM dependency graph; replace one sensor in replay/integration tests and quantify requalification effort |

## Scenarios, not predictions of inevitable progress

| Horizon from cutoff | Conditional scenario | Assumptions | Confidence / disconfirming evidence | Practical AER response |
|---|---|---|---|---|
| Near: 2026–2028 | More capable bounded inspection and repeat-flight workflows | Improved integration, maintainable software and accessible approvals | Medium for incremental capability; low for universal unattended legality; high field-failure rates would weaken case | Prioritize measurement, failure recovery, datasets and serviceability |
| Medium: 2029–2033 | Wider mixed-sensor autonomy and economically useful docked operations in selected settings | Demonstrated reliability, affordable payloads, viable maintenance and insurance | Medium-low; technical demos alone insufficient | Compare total operating cost and intervention rate, not just model accuracy |
| Long: 2034 onward | Expanded persistent aerial sensing and more varied energy/airframe architectures | Storage/materials progress, climate/site suitability, scalable certification and supply | Low on timing and adoption; no universal energy breakthrough assumed | Maintain modular interfaces and scenario models; avoid tying AER to a speculative component |

RoboBee demonstrates why maturity labels matter: the cited untethered system relied on intense external illumination and lacked onboard steering/control [R024](sources.md#r024). Zephyr's sustained flight is a different scale and energy regime. Neither establishes an imminent battery-free general-purpose quadcopter.

## Ranked next research priorities

1. Measure phone data quality and synchronization; this resolves an immediate dependency at modest cost.
2. Pin and reproduce a simulation baseline with fault/replay evaluation.
3. Select a civilian mission and derive payload/airframe requirements.
4. Complete regulatory and sourcing verification for the exact proposed configuration.
5. Acquire independent comparative performance evidence and original teardown/patent records.

The useful research outcome is a decision that changes because evidence improved, including a decision to postpone hardware.

## Research-to-experiment expansion

The [paper analysis](research-papers.md) now examines VINS-Mono, ORB-SLAM3, FAST-LIVO2 and Swift, with dependencies and bounded civilian experiments. The [evaluation protocol](evaluation-protocol.md) separates availability, accuracy, latency and data quality. These are literature analyses and proposals, not reproduced results.
