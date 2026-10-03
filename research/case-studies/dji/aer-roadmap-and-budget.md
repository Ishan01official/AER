# AER: implementation roadmap, illustrative BOM and budget

[Case study home](README.md) · [Subsystem guide](subsystem-development.md) · [Sourcing](manufacturers-and-sourcing.md)

**Proposal date:** 3 October 2026.  
**Status:** Planning assumptions and illustrative calculations. No aircraft specification, procurement quote, measured performance or certification is established.

## 1. Choose the first useful platform

Proposed purpose: a civilian research quadrotor for simulated and later controlled visual-inspection experiments.

### Initial requirements to resolve

| Requirement | Proposed starting position | Evidence needed before hardware freeze |
|---|---|---|
| Mission | Short inspection route around a controlled test structure | Defined target, coverage and output acceptance |
| Aircraft | Conventional quadrotor | Mass, redundancy needs and site constraints |
| Autopilot | One maintained open stack; PX4 is the proposed first baseline | Simulator/board/interface compatibility |
| Positioning | GNSS for outdoor baseline | Environment and operational accuracy requirements |
| Payload | Lightweight documented camera | Image quality, weight and synchronization |
| Companion | Omit initially; add after workload measurement | Compute/power/thermal budget |
| Gimbal | Optional later | Evidence fixed mounting cannot meet image requirements |
| RTK | Optional later | Required map/inspection reference accuracy |
| Flight duration | Derive from measured energy and reserve | Bench and flight power data |
| Frame size / voltage | Select after mass and propulsion trade study | Matched kit curves and packaging |
| Max operating envelope | Establish gradually | Test evidence and applicable operating constraints |

Do not simultaneously demand tiny size, heavy payload, long endurance, low cost and high wind tolerance. Rank mission constraints before selecting hardware.

## 2. A complete first-aircraft parts checklist

| Item | Typical quantity | Selection rule |
|---|---:|---|
| Frame, arms and landing gear | 1 assembly | Prop clearance, payload, stiffness and access |
| Matched BLDC motors | 4 | Thrust/thermal curves at selected pack and prop |
| ESCs | 4, or 1 suitable four-channel unit | Voltage, current, dynamics, cooling and protocol |
| Propellers | 2 CW + 2 CCW operating; spare sets | Exact manufacturer-approved combination |
| Supported autopilot | 1 | Firmware support and required I/O |
| Compatible power module/PDB | 1 system | Selected FC support and total load |
| GNSS/antenna; compass as required | 1 system | Position requirements and placement |
| Manual controller + receiver | 1 pair | Supported protocol and India RF requirements |
| Telemetry link/ground interface | 1 system | Logging and mission workflow |
| Qualified battery | 2 packs for workflow, 1 airborne | Current, mass, voltage and usable energy |
| Matched charger / power supply | 1 set | Chemistry, cell count and balance capability |
| Cables, keyed connectors, mounts, fasteners | Complete set | Pinouts, load, strain relief and serviceability |
| Buzzer/status/safety accessories | As supported | Clear state and recovery workflow |
| Storage/logging media | As required | Endurance, capacity and retrieval |
| Payload camera | Optional initial aircraft; required inspection phase | Supported driver, lens and calibration |
| Companion + regulator + cooling | Optional upgrade | Profiled workload and weight/power margin |
| Gimbal / RTK / range sensor | Mission-dependent upgrades | Demonstrated requirement |

“Pixhawk-compatible” accessories are not automatically interchangeable. Check connector pinouts, electrical levels, analog/digital power-module support and exact firmware.

## 3. Sizing calculations before purchasing

### Mass

`m_total = frame + motors + ESCs + props + avionics + wiring + battery + payload + mounts + mass allowance`

Use measured/vendor masses and track the allowance separately. Iterate: a larger battery changes mass, thrust and power, so adding energy does not produce proportional extra endurance.

### Thrust

Hover requires total thrust approximately equal to weight in a level stationary condition:
`T_hover ≈ m_total × g`.

**Illustrative only:** a 2.0 kg quad has weight about 19.6 N, with ideal balanced hover thrust about 4.9 N per motor. If the early study uses a 2:1 static thrust-to-weight sizing assumption, it would seek total peak thrust around 39.2 N, or 9.8 N per motor.

That ratio is an initial trade-study assumption, not a universal flight qualification criterion. Account for altitude, temperature, pack sag, control margin, airframe interactions and propulsion limits. Use measured thrust at the exact voltage/prop combination.

### Energy and endurance

`E_nominal_Wh = V_nominal × capacity_Ah`  
`t_minutes ≈ 60 × E_usable_Wh / P_average_W`

**Illustrative only:** a conventional 6S 5 Ah pack at 22.2 V nominal stores about 111 Wh nominal. Assuming 75% usable energy for a preliminary model gives 83.25 Wh. With assumed total average power of 450 W, estimated duration is about **11.1 minutes**.

These inputs are not measured AER values. Usable energy and reserve must be established under mission conditions; voltage sag and battery aging can reduce the result. A larger pack may raise average power through increased mass.

### Companion penalty

**Illustrative only:** if the same aircraft's total average load increased from 450 W to 465 W with no mass change, the estimate would fall to about 10.7 minutes. Real compute integration also adds regulator loss, cooling and mass. Model those effects separately.

### Electrical and mechanical compatibility

Verify:
- Maximum charged pack voltage and transient margin across ESCs/regulators.
- Current under actual loads, not only advertised burst rating.
- Prop hub, shaft, attachment and rotation direction.
- UART logic levels, power pinouts and grounding.
- ESC protocol and FC output support.
- GNSS/compass interface and supported drivers.
- Camera connector, host driver, stream modes and timestamps.
- Companion cooling and boot/load current.
- Antenna placement and electromagnetic interference.
- Firmware/message version and ground-station compatibility.

## 4. Budget: estimates, not supplier prices

The following are **rough engineering planning allowances in INR**, not current verified retail prices or a quotation. Tax, shipping and customs are excluded unless explicitly added. Low/high configurations are independent choices; the minimum total is not an assured compatible build.

| Base system category | Low allowance | High allowance |
|---|---:|---:|
| Frame/structure | ₹5,000 | ₹15,000 |
| Four motors + ESCs + propellers | ₹15,000 | ₹35,000 |
| Supported FC + compatible power accessories | ₹15,000 | ₹35,000 |
| GNSS/compass system | ₹3,000 | ₹10,000 |
| Manual radio + receiver | ₹8,000 | ₹20,000 |
| Telemetry system | ₹3,000 | ₹10,000 |
| Two packs + charger | ₹12,000 | ₹25,000 |
| Wiring, storage, mounts and basic spares | ₹5,000 | ₹12,000 |
| **Base planning subtotal** | **₹66,000** | **₹1,62,000** |

Optional upgrade allowances:

| Upgrade | Low allowance | High allowance |
|---|---:|---:|
| Companion, storage, regulator and cooling | ₹12,000 | ₹55,000 |
| Camera/lens integration | ₹5,000 | ₹25,000 |
| Range sensor | ₹3,000 | ₹15,000 |
| **Autonomy/imaging upgrade subtotal** | **₹20,000** | **₹95,000** |
| Gimbal payload, if selected | ₹15,000 | ₹80,000 |
| RTK rover/base/corrections setup, if selected | ₹25,000 | ₹1,00,000 |

Base plus autonomy/imaging allowance is **₹86,000–₹2,57,000**, before gimbal, RTK, landed-cost adjustments and tools. An illustrative 25% procurement/rework contingency gives **₹1,07,500–₹3,21,250** for that combination, but contingency is not a replacement for calculating actual taxes/freight.

Separately budget: laptop/workstation if needed, instruments, fixtures, site, training/operational approvals, insurance, repair, labor and certification. Borrowed lab equipment can change the first-prototype cost substantially.

This budget is for planning a research system, not a DJI-equivalent camera drone or a certified commercial product.

## 5. Development stages and exit gates

Durations are effort assumptions for a small team with relevant skills. They are not guaranteed schedules; part-time work and procurement can extend them.

| Phase | Indicative effort | Deliverables | Exit gate |
|---|---|---|---|
| 0. Mission/specification | 1–2 weeks | Requirements, target scene, metrics, risk register and interface sketch | One bounded mission and acceptance plan |
| 1. Simulation baseline | 2–4 weeks | Pinned stack/simulator, scenario config, logs and evaluation | Reproducible baseline plus tested failure scenarios |
| 2. Bench integration | 2–4 weeks | Compatible hardware, power tree, wiring and sensor logs | No unexplained resets/timing issues; recoverable faults |
| 3. Propulsion/structure validation | 2–4 weeks | Mass/CG, thrust/power curves, thermal/vibration data | Adequate modeled margins and controlled progression approval |
| 4. Basic controlled flight | 2–6 weeks | Stable flight baseline, modes, operator recovery and reserve evidence | Repeatable bounded flights meeting agreed thresholds |
| 5. Perception/inspection | 4–8 weeks | Calibrated camera, dataset, coverage/quality evaluation | Useful output and demonstrated degraded-sensing behavior |
| 6. Custom integration | 1–3 months | Selected mounts/PDB/carrier design and qualification | Measured benefit versus catalog baseline |
| 7. Product pilot | Mission-dependent | Multiple units, QA, maintenance, customer workflow | Repeatability, economics and applicable approvals |

Phases overlap only when dependencies permit. No calendar milestone should override unresolved flight-critical failures.

## 6. First 90 days: a practical sequence

### Days 1–15

Read official PX4 simulation and companion documentation; choose one maintained version. ArduPilot remains an alternative, not a parallel first implementation. Record versions and rationale.

Define a simulator inspection route and produce a baseline report. Log position/attitude, timestamps, commands, modes and battery assumptions. Create tests for coordinate conventions.

### Days 16–30

Test simulated link loss, stale commands, position degradation and perception dropout. Compare behavior to intended recovery policy. Create mass/power trade studies and a hardware interface matrix. Request 1/5/20-unit quotations only when requirements are coherent.

### Days 31–60

Integrate the chosen autopilot and power system on the bench. Review wiring/polarity and log timing. Evaluate camera capture separately. Acquire propulsion curves and validate with suitable fixtures and experienced supervision. Archive serial/revision information and incoming inspection results.

### Days 61–90

If bench, propulsion, site and operational prerequisites are met, progress to controlled basic flight. Keep the mission bounded, log all outcomes and investigate anomalies. Add companion-driven behavior only after baseline flight and timeout/override behavior are established.

A successful 90-day result may be a reproducible simulation and well-characterized bench system. It need not include autonomous flight if exit gates are not satisfied.

## 7. Measurement plan

Set numerical thresholds **before** claiming success, informed by baseline and mission requirements. Do not choose thresholds merely to match observed results.

| Domain | Metrics |
|---|---|
| Mission | Completion fraction, operator interventions and abort causes |
| Control | Position/attitude error, response, saturation and disturbances |
| Estimation | Innovation/health measures, fix/status changes and recovery |
| Power | Average/peak current, sag, rail stability and usable reserve |
| Perception | Precision/recall on defined scene, missed surfaces and stale frames |
| Imaging | Coverage, blur, exposure failures and repeatability |
| Compute | Median/p95/p99 latency, deadline misses, temperature and resets |
| Communication | Loss/latency, outages, recovery and operator observability |
| Reliability | Failures per test, repair time, repeat faults and unit variation |

Do not equate a small sample of successful flights with a statistically established reliability rate.

## 8. Proposed repository organization for implementation

Preserve the current structure; add only when artifacts exist.

- `configs/`: versioned simulator/mission/hardware parameters.
- `simulation/`: baseline scenes, launch instructions and failure scenarios.
- `src/`: interface adapter, mission supervisor and evaluation code.
- `tests/`: coordinate, timestamp, interface and regression checks.
- `hardware/`: approved BOM, power tree, wiring, mass budget and calibration records.
- `experiments/`: dated hypotheses, configurations, logs/manifests and results.
- `data/`: dataset metadata and storage pointers; avoid large raw binaries in Git.
- `docs/`: decisions, requirements, operating envelope and maintenance.
- `research/case-studies/dji/`: this study and subsequent evidence updates.

The folders above describe future work. This research update does not claim simulator code, procurement or hardware has been completed.

## 9. Suggested capability/team map

| Workstream | Skills / responsibility |
|---|---|
| Controls/robotics | Dynamics, estimation, autopilot configuration, simulation and fault analysis |
| Embedded/electrical | Schematics, power, PCB integration, firmware and timing |
| Mechanical | CAD, structure, mounts, vibration and assembly |
| Perception/software | Cameras, datasets, compute pipeline, planning and evaluation |
| Test/operations | Fixtures, progressive validation, site/airspace and flight records |
| Product/supply chain | RFQs, traceability, QA, maintenance and customer economics |

One person can learn across these domains, but custom avionics, propulsion and product qualification benefit from specialist review.

## 10. Investment decision

Proceed to custom development only when at least one condition is demonstrated:
- Catalog options cannot meet the mission requirement.
- A custom component improves measured performance or reliability enough to justify lifecycle cost.
- Supply continuity or packaging requires ownership.
- Customer demand supports the engineering/qualification investment.

Prefer custom mounts, fixtures, power distribution and mission software before custom MEMS sensors, radio baseband or battery cells.

**Next concrete step:** define the first inspection scenario and implement the simulator baseline; do not buy the entire optional-payload list at once.
