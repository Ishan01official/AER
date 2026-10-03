# Developing each subsystem: from component purchase to custom design

[Case study home](README.md) · [Sourcing](manufacturers-and-sourcing.md) · [Roadmap](aer-roadmap-and-budget.md)

**All steps below are proposed engineering workflows.** No subsystem has been built or validated by AER in this study. Supplier specifications need validation in the selected operating conditions.

## 1. Airframe, arms, landing gear, enclosures and mounts

**Parts:** frame plates, arms, joints, motor mounts, landing gear, vibration isolation, fasteners, payload mounts and covers.

**Develop:** Define all-up mass, payload envelope, propeller clearance, center of gravity and access needs. Create CAD and a mass roll-up. Analyze arm stiffness and load paths; compare modes against propulsion excitation. Prototype nonstructural mounts with additive manufacturing and structural parts with appropriate machining/composites processes. Test joints, fatigue-sensitive areas and repeated assembly.

**Manufacture:** Carbon plates can be cut from purchased laminates; molded composite shells require lay-up, molds, cure control and inspection. Aluminum parts need machining and corrosion considerations. Injection-molded plastic requires material selection, tooling, shrinkage and draft design. Carbon dust and sharp edges require suitable fabrication controls.

**Source:** Buy an established frame first; commission local CAD/CNC/composite work when geometry is known. A local machine shop is a fabrication partner, not automatically an aerospace-qualified supplier.

**Evidence:** measured mass/CG, stiffness, vibration spectra, fastener retention, structural inspection and repeatable assembly. Do not infer structural adequacy from attractive CAD.

## 2. BLDC motors

**Parts:** stator laminations, copper windings, permanent magnets, rotor bell, shaft, bearings, housing, insulation and retention materials.

**Technology:** Electromagnetic design, torque/speed characteristics, thermal behavior, balancing and bearing life. Kv describes approximate unloaded speed per volt, not delivered thrust or power quality.

**Develop:** Begin with an existing motor and characterize it with the selected propeller and ESC. A custom motor requires defining torque/speed/voltage objectives, choosing pole/slot geometry, modeling losses and thermal behavior, manufacturing stator/windings/rotor, controlling the air gap, retaining magnets and dynamically balancing. Then validate over the mission load envelope.

**Source:** T-MOTOR and Hobbywing are worldwide candidates; Vector Technics and Reflex Drive are Indian candidates. [S12–S13, S24–S25] Require exact model datasheets and matched-propeller test data.

**Evidence:** thrust, current, voltage, RPM and temperature curves; response to command changes; repeated starts; bearing/vibration behavior. A power rating alone is insufficient.

## 3. Propellers

**Parts:** blades, hubs, inserts, folding hinges where applicable, attachment hardware.

**Technology:** Airfoil shape, pitch, diameter, blade stiffness, aerodynamic loading, noise and structural fatigue.

**Develop:** Select validated catalog props before designing custom geometry. For a custom design, set thrust/RPM targets, analyze aerodynamic loads, choose material and process, evaluate balance and attachment, then use controlled thrust testing. CFD supports design; measurements must check its assumptions.

**Manufacture:** Injection-molded polymer and composite props require repeatable tooling and material control. A home-printed propeller should not be treated as a qualified substitute for a tested product.

**Evidence:** static and dynamic balance, efficiency, retention, clearance, repeatable batch quality and environmental condition limits. Always obtain rated operating constraints.

## 4. Electronic speed controllers

**Parts:** MCU, gate drivers, three-phase power bridge, current measurement, capacitors, regulators, protection and signal interface.

**Technology:** Six-step commutation or field-oriented control, back-EMF/rotor estimation, switching losses, current limits, thermal design and EMI.

**Develop:** Start on a protected bench using a documented reference platform. Study ST's ESC reference designs and TI's drone-propeller/high-speed FOC reference designs. [S14–S16] Derive a design from the selected motor, battery and transient requirements; do not simply increase a reference design's voltage/current ratings.

Specify supported PWM/DShot/CAN behavior and actual autopilot compatibility. Design the schematic and layout, bring up supplies and logic, verify gate timing/protection, test unloaded motor behavior, then controlled loaded operation.

**Manufacture:** PCBA supplier builds the board; AER owns schematic review, firmware, fixture requirements and acceptance. Specify MOSFET substitutions, copper/thermal design and solder inspection.

**Evidence:** current/thermal limits in actual cooling conditions, starts/restarts, commutation stability, response latency, fault behavior and bus-voltage transients. High current labels are not guaranteed continuous capability in an enclosed aircraft.

## 5. Battery cells, pack, BMS and charger

**Parts:** LiPo pouch or cylindrical Li-ion cells, interconnects, insulation, enclosure, connectors, balancing/monitoring, protection and charger.

**Technology:** Chemistry, internal resistance, series/parallel topology, state of charge/health, discharge temperature and protection coordination.

**Develop:** Buy a reputable flight-suitable pack initially. Later specify a custom pack with a specialist: voltage range, usable energy, continuous/peak current, mass, mechanical retention, thermal environment, cycle-life requirements and telemetry. Cell production requires electrode processing, dry-room operations, filling, formation and industrial quality control; it is separate from pack assembly.

For cylindrical designs, evaluate exact cell specifications such as Molicel's P45B datasheet rather than extrapolating from another cell. [S18] Define behavior when a pack protection threshold is approached. Electrical protection, aircraft reserve logic and landing policy must work together; casually disabling protections is not a design solution.

TI offers a small 2S battery-management reference design useful for learning, not a drop-in design for a larger flight pack. [S17]

**Source:** Grepow/Tattu globally; Voltherm's drone-pack offering in India. [S19, S26] India-based pack assembly does not establish Indian cell manufacture.

**Evidence:** capacity, cell consistency, sag under load, temperature, connector/wiring heating, charger compatibility, telemetry accuracy and transport documentation. Ask for applicable test reports and UN 38.3 documentation where required for the selected shipment; confirm requirements with the carrier.

## 6. Power distribution, DC/DC conversion and wiring

**Parts:** PDB, power monitor, regulators/BECs, connectors, cables, capacitors and distribution protection.

**Develop:** Draw a power tree covering every rail, load and return path. Calculate steady and transient current, including motor changes and companion boot/compute peaks. Select regulators with validated input range, thermal margin and electromagnetic behavior. Design mounting and strain relief.

6S conventional 4.2 V/cell lithium packs can reach 25.2 V fully charged; a nominal-voltage label is not the maximum voltage. Other chemistries/high-voltage cells differ. Rate all parts against the actual pack and transients.

**Evidence:** startup/brownout tests, measured rail ripple, temperature, current-sensor calibration and wiring continuity/polarity. Flight-controller and companion rails must remain stable during propulsion load steps.

## 7. Flight-controller hardware

**Parts:** MCU, IMUs, barometer, optional magnetometer, memory, clock, watchdog, regulated supplies, connectors and debug/programming interface.

**Develop:** Buy a supported board such as an appropriate Holybro or CubePilot model. Holybro's Pixhawk 6X documentation describes an STM32H753-based design with sensor redundancy; exact sensor combinations vary by hardware revision. [S10–S11] Record the actual revision.

A custom board starts with required interfaces and timing, then component selection, schematic/layout review, controlled sensor placement and power domains, board bring-up, drivers, calibration, logging and HIL tests. Reusing a processor does not guarantee firmware compatibility.

**Technology:** RTOS behavior, interrupts/DMA, SPI sensor buses, temperature drift, watchdog recovery and timestamp consistency. Multiple IMUs can help fault detection but do not remove shared power, vibration or software failures.

**Evidence:** loop timing, sensor noise/bias, supply integrity, log completeness, reset behavior, thermal behavior and integration regression results.

## 8. IMU, barometer and magnetometer

**Source examples:** ST motion sensors, Bosch Sensortec and TDK InvenSense devices, including ICM-42688-P. [S20–S22] Use manufacturer documentation and an authorized component channel.

**Develop:** First evaluate breakout modules or a supported FC. Custom integration requires layout/decoupling, device drivers, filtering, calibration and temperature characterization. MEMS sensor manufacture requires specialized microfabrication and packaging; AER can design a board around sourced MEMS devices.

**Evidence:** stationary noise, bias over temperature/time, saturation, vibration susceptibility, measurement timing and interaction with propulsion currents. Magnetometer calibration must be evaluated under powered conditions.

## 9. GNSS and RTK

**Parts:** receiver module, antenna, ground plane, RF feed, optional base/correction service and time synchronization.

**Source:** u-blox ZED-F9P module family and compatible carrier/module providers. [S23] The receiver vendor, breakout-board vendor and antenna vendor are different roles.

**Develop:** Integrate a documented module before custom RF boards. Establish antenna placement, correction data transport, fix-quality reporting and autopilot interface. Evaluate open-sky, multipath and degraded-signal conditions. RTK requires suitable correction information and favorable reception; do not assume every fix is centimeter accurate.

**Evidence:** time to usable fix, status transitions, error against reference, correction age, interference effects and loss/recovery behavior.

## 10. Navigation cameras and payload cameras

**Parts:** image sensor, lens, optical mounts, interface/carrier, ISP where needed and cabling.

**Source:** e-con Systems and Arducam modules; Sony industrial sensor families as underlying device candidates. [S27–S29] A bare sensor is not a ready-to-use camera.

**Develop:** Choose a camera from latency, exposure, field of view, shutter behavior, synchronization and host support requirements. Verify Linux drivers and streaming modes. Calibrate intrinsics, distortion and camera/body extrinsics. Use recorded datasets before introducing closed-loop behavior.

Global shutter avoids line-by-line temporal distortion; motion blur still depends on exposure and motion. Rolling-shutter cameras may be appropriate for some payload imaging.

**Manufacture:** Custom camera modules add high-speed layout, optical alignment, lens sourcing, ISP tuning and factory calibration. Do this only after catalog modules fail a documented requirement.

**Evidence:** usable image quality, motion blur, end-to-end latency, dropped frames, calibration repeatability, illumination robustness and data synchronization.

## 11. Gimbal

**Parts:** lightweight structure, bearings, three-axis actuators, encoder/IMU feedback, driver/controller, isolation and cables.

**Develop:** Buy a documented gimbal first if stabilized imagery is required. SIYI offers gimbal products with integration documentation; compatibility is model-dependent. [S30] A custom gimbal needs inertia and balance design, actuator sizing, axis limits, cable routing, feedback, control tuning and image validation.

**Evidence:** stabilization error, vibration, horizon behavior, thermal loading, payload balance, hard-limit response and communication faults. Changing lens or payload changes the dynamics.

## 12. Range sensors and obstacle sensing

**Parts:** single-point rangefinder, stereo/depth cameras, multi-beam lidar or other mission-appropriate sensors.

**Source:** Benewake range/lidar products are a catalog starting point. [S31] Confirm each model's interface, range and environmental limits.

**Develop:** Start by logging readings. Model blind spots, reflective/absorbing surfaces, sunlight and invalid returns. One forward rangefinder cannot establish omnidirectional obstacle avoidance.

**Evidence:** detection performance by surface and lighting, false/no returns, field of view, latency and behavior when sensing becomes unreliable. Flight clearance includes braking distance and total perception/control delay.

## 13. Companion compute

**Parts:** compute module/board, storage, carrier, power conversion and cooling.

**Source:** NVIDIA Jetson Orin family for accelerated workloads; lighter compute may suffice for logging or simpler vision. [S32]

**Develop:** Profile the actual model and data pipeline before selecting compute. Evaluate device power modes, OS/driver versions, camera support, memory, thermal throttling and startup behavior. A desktop model's speed is not aircraft performance.

Use MAVLink/MAVSDK or compatible PX4 ROS 2 interfaces as appropriate; pin firmware/message/bridge versions. [S08–S09]

**Evidence:** median/tail latency, deadlines, load, power, temperature, reboot recovery and heartbeat/command timeout. Containerization helps reproducibility but does not remove hardware timing variation.

## 14. RC, telemetry and video

**Parts:** transmitter, receiver, RF modules, antennas, ground equipment, video encoder/decoder when required.

**Source:** RadioMaster's ExpressLRS products illustrate documented control-link hardware; Holybro catalogs include telemetry options. [S33, S10] These examples do not establish legality of every frequency/power setting in India.

**Develop:** Prefer existing compliant equipment. Separate manual recovery, telemetry and payload streaming requirements. Create link-loss policies and test interference/antenna orientation within lawful bounds. A proprietary digital video system would require RF/baseband, codecs, networking, ground hardware and substantial validation.

**Evidence:** latency/loss distributions, recovery, antenna placement, mode transitions and operator observability. Do not choose a 915 MHz device simply because foreign guides use it.

## 15. Ground station, application and data platform

**Develop:** Use established ground tools for initial mission planning and logging. Build AER's evaluation layer first: mission metadata, hardware revision, firmware/parameters, time alignment, image manifests and computed metrics. Later add customer-specific reporting and workflow integration.

**Evidence:** replayability, clear status/error messages, configuration validation, data integrity and report repeatability. An offline operator workflow can be useful where connectivity is unreliable.

## 16. Software, licenses and intellectual property

PX4 and ArduPilot are alternative baseline stacks, not interchangeable parts of one firmware image. Check licenses of the exact code and dependencies before distributing modifications; preserve required notices and source obligations.

DJI SDKs expose supported platform functions; they do not provide the source for DJI's complete autopilot, radio or imaging system. Match aircraft, controller, OS, firmware and SDK release before buying. [S34] Develop independent implementations and use licensed/reference material appropriately.

## 17. Manufacturing flow for the assembled aircraft

1. Freeze requirements, drawings, approved BOM and hardware/firmware revisions.
2. Procure traceable parts and record substitutions.
3. Inspect incoming material and screen batteries/propulsion as appropriate.
4. Assemble with controlled torque, wiring, polarity checks and retained records.
5. Program approved firmware and parameter sets.
6. Calibrate sensors, power measurement and cameras with versioned fixtures.
7. Run electrical/functional checks, then controlled propulsion tests.
8. Perform staged flight validation under the applicable operational conditions.
9. Archive logs and pass/fail evidence against the aircraft serial number.
10. Package, provide operating limits and establish repair/return handling.

Prototype, engineering validation, design validation and production validation should answer different questions. A prototype confirms a concept; later stages establish robustness, repeatability, manufacturability and supportability.
