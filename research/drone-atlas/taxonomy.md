# Drone taxonomy: separate the dimensions

An unmanned aircraft is the flying vehicle; an unmanned aircraft **system** includes control stations, communications, payloads, operators and support equipment. “Autonomous,” “military,” “nano” and “quadcopter” describe different properties. A small quadcopter may be manually piloted indoors, automatically map a building, or support scientific sampling without changing airframe class.

## Independent axes

| Axis | Record | Why it matters |
|---|---|---|
| Lift/airframe | multirotor, fixed-wing, helicopter, hybrid VTOL, flapping, buoyant | Determines energy and control physics |
| Geometry | rotor count; coaxial or separated; tilt mechanism; wing layout | Rotor count alone does not establish redundancy |
| Size | takeoff mass kg; dimensions m; payload kg | “Micro/nano” marketing is not a universal regulatory class |
| Energy | battery, combustion, fuel cell, solar, external tether | Infrastructure and reserves differ |
| Mission | imaging, survey, agriculture, inspection, delivery, science, response, public military roles | Defines payload and useful output |
| Autonomy | manual attitude/rate control; stabilization; waypoints; bounded perception; supervised fleet | Scope and human fallback must be explicit |
| Environment | indoor/outdoor, atmosphere/altitude, wind, dust, rain, GNSS availability | Lab success is not all-weather reliability |
| Maturity | announced, prototype, demonstrated, commercial, operational | Evidence of a flight is not evidence of a service |
| Support | docking, launch/recovery, charging, repair, fleet orchestration | Whole-system costs may exceed aircraft costs |

The operating principles and preferences below are **I: engineering synthesis**. Named examples have primary-source evidence linked; some are only candidate-level records. Coverage depth is in [coverage.csv](data/coverage.csv).

| Class | Principle / useful mission | Strength | Constraint; when another design wins | Representative evidence |
|---|---|---|---|---|
| Quadrotor | Four thrust-producing rotors; differential thrust controls moments | Simple hover/inspection platform | Continuous lift power; conventional quad lacks general motor-out recovery; choose a wing for long corridor surveys | Mini 4 Pro [R001](sources.md#r001); Crazyflie [R016](sources.md#r016) |
| Hexacopter | Six rotors distribute thrust | Payload integration and possible fault margin | More actuators/mass; controllability after failure must be proven | Orion 2 is a tethered example [R030](sources.md#r030); layout review remains partial |
| Octocopter / coaxial | Eight rotors, sometimes stacked on four arms | Compact packaging and distributed thrust | Overlapping wakes cost efficiency; redundancy depends on shared power and controllers | AGRAS T50 coaxial agriculture system [R038](sources.md#r038) |
| Fixed-wing | Wing creates lift with forward airspeed | Efficient area/corridor coverage | Cannot simply stop and hover; launch/recovery site needed | RQ-4 public ISR example [R029](sources.md#r029) |
| Single-main-rotor helicopter | Large rotor with cyclic/collective control; anti-torque system | Hover with relatively large disk area | Mechanical and vibration complexity; multirotor easier to assemble | Yamaha RMAX [R028](sources.md#r028) |
| Coaxial helicopter | Counter-rotating rotors share an axis | Cancels torque without a tail rotor | Coupled wakes and rotor mechanics | Ingenuity scientific example [R025](sources.md#r025) |
| Lift-plus-cruise VTOL | Dedicated lift rotors plus separate cruise propulsion | Avoids rotating heavy lift units | Carries inactive lift hardware in cruise | Specific fully reviewed model remains open; distinguish from Trinity tilting architecture |
| Tiltrotor | Propulsors rotate between lift and cruise | Reuses propulsion hardware | Transition, bearings and actuator faults | Trinity Pro candidate [R023](sources.md#r023); detailed mechanism verification pending |
| Tiltwing | Wing and propulsion rotate together | Transition can align wing/flow | Aeroelasticity and transition modeling | NASA GL-10 demonstrator [R031](sources.md#r031) |
| Tailsitter | Entire aircraft rotates from vertical hover into wing-borne flight | No separate wing-tilt mechanism | Wind-sensitive ground stance; changing camera attitude | WingtraOne GEN II [R022](sources.md#r022) |
| Flapping / bio-inspired | Oscillating wings with unsteady lift | Research at insect scales | Actuator/power/control integration dominates | RoboBee X-Wing lab demonstration [R024](sources.md#r024) |
| Tethered aerial platform | Ground cable delivers power and sometimes data | Persistence over a fixed site | Cable mass, drag, snagging and ground-power dependence | Orion 2 test [R030](sources.md#r030) |
| Lighter-than-air | Buoyant gas supports much of the weight | Low power to maintain lift indoors | Large volume and wind sensitivity | Festo AirJelly reference [R032](sources.md#r032) |
| High-altitude long endurance | Low wing loading and energy budgeting; solar variants store energy overnight | Persistent remote sensing/communications | Launch weather, nighttime energy, maintenance and airspace | AALTO Zephyr [R027](sources.md#r027) |

## Missions are an overlay

**FPV** means first-person-view piloting via a camera feed. Racing prioritizes low latency and agility; cinematic work emphasizes repeatable framing, exposure and vibration suppression. Neither is an airframe class. Specific current racing platforms remain to be researched.

Mapping needs calibrated geometry and checkpoints; attractive images alone do not establish survey accuracy. Agriculture adds liquid or granular payload dynamics, application-rate calibration and contamination management. Inspection values defect visibility and complete coverage. Logistics adds packaging, delivery confirmation and recovery infrastructure; Zipline's P2 announcement illustrates separation of transport and final placement [R034](sources.md#r034). Emergency response and conservation add privacy, coordination and disturbance constraints. Scientific sampling requires instrument calibration and a record of airflow contamination.

Docking adds remote readiness checks, weather sensing, landing alignment, charging and maintenance. DJI Dock 2 is a commercial reference [R037](sources.md#r037), not proof that unattended operation is lawful everywhere. Multi-drone orchestration adds shared airspace, localization, scheduling and communication load; the Crazyswarm paper is an indoor research reference [R020](sources.md#r020), not evidence of arbitrary outdoor collective autonomy.

## Military and adjacent technology boundaries

Public military categories include reconnaissance/surveillance, communications relay, logistics, training targets, maritime observation and armed/one-way systems. Their high-level trade-offs include persistence, payload, launch infrastructure, support burden and supply constraints. RQ-4 provides a sourced reconnaissance entry; comparative military histories and supplier provenance remain partial. No weapon design, targeting code, evasion procedure or attack experiment belongs in this library.

Ground robots support wheel/terrain contact; surface vessels add hydrodynamics and sea state; underwater vehicles add buoyancy, pressure and communications limits. They share estimation, autonomy and logs, but aerial stability assumptions do not transfer unchanged. ArduPilot's Rover/Sub ecosystem is an adjacent reference [R009](sources.md#r009). A future comparative page should examine those interface differences without diluting aerial coverage.
