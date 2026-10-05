# ArduPilot, PX4 and the meaning of an open platform

The [DJI company study](../../case-studies/dji/README.md) describes product integration. Open flight stacks solve a different accessibility problem: researchers can inspect, modify and reproduce portions of aircraft behavior rather than accepting an opaque product interface.

## Historical evidence

ArduPilot's project history attributes early boards and code to Jordi Muñoz and collaborators, records thermopile-era hardware, IMU development and subsequent autopilot/community expansion. It dates the initial code repository to November 2009, hardware abstraction work to 2012 and EKF integration to 2014 [R008](../sources.md#r008). This is participant-written evidence, not an independent adjudication of every priority or organizational dispute.

PX4 must be distinguished from Pixhawk hardware and the MAVLink protocol. The history source includes a July 2012 PX4 release milestone; this does not establish a unique founding date for the entire ecosystem. This batch uses PX4 **v1.16 documentation as a bounded engineering reference**, not as a claim that it is the latest stable version or a release AER has installed [R011](../sources.md#r011), [R012](../sources.md#r012).

## Architecture and selection

PX4 documents modular flight-stack and middleware organization. State estimation, controllers and application logic communicate through defined interfaces [R011](../sources.md#r011). Its controller diagrams show the relationship between desired motion, estimated state and actuator commands [R055](../sources.md#r055). Understanding those boundaries is more valuable than modifying a gain until one flight looks acceptable.

| Criterion | ArduPilot | PX4 | AER action |
|---|---|---|---|
| Main license evidence | GPLv3 project guidance [R009](../sources.md#r009) | BSD-3-Clause main license [R010](../sources.md#r010) | Audit actual source/dependencies before distribution; not a legal conclusion about an entire product |
| Baseline research role | Candidate established autopilot | Candidate established autopilot | Choose one supported vehicle and stable release; avoid simultaneous porting |
| Hardware | Board/vehicle support must match chosen release | Board/vehicle support must match chosen release | Verify exact board revision and sensor driver support |
| Simulation | Reproduction pending here | SITL/HITL documented [R012](../sources.md#r012) | Preserve simulator, vehicle model, firmware commit and seeds |
| Custom autonomy | Can use companion/interface boundary | Can use companion/interface boundary | Keep research-process failure separate from stabilization |
| Evaluation | Logs and fault behavior must be examined | Logs and fault behavior must be examined | Same mission and error metrics for a fair comparison |

**I:** openness is not a reliability certificate. It makes diagnosis and long-term maintenance possible, but transfers integration responsibility to AER. A permissive license does not establish that every bundled driver, model or dataset is permissively licensed. A source-available board is not proof that a substituted IMU is calibrated or functionally equivalent.

## Suggested first controlled modification

Log an additional quality indicator on the host side; do not alter the stabilizing controller first. Measure data delay, stale-sample count and estimator consistency on saved logs. Next inject synthetic latency in simulation and evaluate an existing timeout/fallback mechanism. Only after reproducible evidence should a firmware change be proposed.

A software bill of materials should include firmware commit, submodules, compiler, board target, parameters, simulation assets, message definitions and ground-station version. Never store signing keys in that manifest.

Open questions: independent ecosystem history; current long-term support expectations; board replacement compatibility; licensing of the selected full dependency graph; exact estimator implementation in the chosen release. Visual references: [PX4 architecture](https://docs.px4.io/v1.16/en/concept/px4_systems_architecture) and [controller diagrams](https://docs.px4.io/v1.16/en/flight_stack/controller_diagrams).
