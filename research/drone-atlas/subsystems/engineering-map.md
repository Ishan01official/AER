# Whole-system engineering map

This is a **working engineering synthesis**, with detailed guides for [estimation](state-estimation.md) and [energy](propulsion-energy.md). Other rows are substantive starting guides, not claims of equal depth or complete design instructions. Each interface should have a requirement, a failure response and a test before AER makes it custom.

## Airframe, structures, vibration and thermal design

Lift, drag, moments and inertia define the plant the controller must stabilize. A wing's lift can be modeled as `L = ½ρV²SC_L`; the coefficient depends on angle of attack, Reynolds number and geometry. A rotor supplies lift without forward aircraft speed at a continuous power cost. Structural stiffness preserves alignment; mass and stiffness together set resonance. Carbon fiber can provide high directional stiffness, but fiber orientation, joints and defects control the actual structure. A carbon-fiber label is not a structural test [R062](../sources.md#r062).

Interfaces: motor mounts, sensor mounts, payload center of mass, enclosure airflow and landing loads. Failure modes: loose fasteners, delamination, fatigue, resonant sensor mounts, thermal throttling and cooling blockage. Test: inspect parts, weigh components, measure center of mass, perform appropriate static load/modal checks and log temperature under representative computing load. Tools/skills: CAD, fixtures, mechanical measurements, vibration spectra, thermal sensors and composite-aware design. Buy a proven airframe first; customize payload mounts before primary load paths.

## Flight controller and real-time computing

The flight controller samples sensors, estimates state, computes commands and manages mode/fault logic. Real-time means deadlines are part of correctness: a mathematically correct command delivered too late can be harmful. Interface contracts include sensor buses, ESC protocol, power rails, timebase, watchdog and configuration storage. PX4 architecture and controller documentation provide modular examples [R011](../sources.md#r011), [R055](../sources.md#r055).

Failure modes: bus contention, blocked tasks, corrupted parameters, scheduler overload or power reset. Test: deadline/loop-rate logging, power-transient measurements, hardware-in-the-loop and replay of faults. Skills/tools: C/C++, MCU debugging, RTOS concepts, oscilloscope/logic analyzer and firmware build discipline. Buy a supported board; custom PCB work must include test points, production programming and recovery. Board name alone is insufficient: Holybro's current 6X page explicitly identifies Rev 8 sensors [R045](../sources.md#r045).

## Sensors and calibration

IMU noise/bias, magnetometer interference, barometric pressure disturbances, GNSS geometry/multipath, optical-flow scale and ranging reflectivity limits must be modeled separately. A receiver module is not an antenna, correction service or complete navigation solution [R046](../sources.md#r046). A MEMS chip is not a calibrated aircraft sensor installation [R047](../sources.md#r047).

Use per-sensor data-ready timestamps where possible. Record axes, units and covariance semantics. Test calibration repeatability and sensor failure cases on the bench before airborne integration. Buy documented sensors; fabricate mounting and interfaces only as needed. See the detailed [fusion guide](state-estimation.md).

## Stabilization, navigation and civilian autonomy

A control loop compares a requested state with an estimate and acts through limited actuators. Cascaded loops separate trajectory/position, velocity, attitude and rate behavior. Saturation, latency and estimator errors couple them. Navigation then selects feasible motion; perception supplies imperfect evidence of the surroundings. “Obstacle detected” does not prove a collision-free path.

Define bounds on velocity, acceleration, command age and estimator health. A navigation failure may require hold, controlled landing or operator intervention depending on available sensing; return-to-home is not universally safe. Test delays, model mismatch, actuator limits and missing observations in simulation [R012](../sources.md#r012). Skills: control, optimization, dynamics, probability and system identification. Keep an established stabilizing controller while evaluating autonomy in replay or simulation.

## Communications, antennas and ground station

Separate command/control, health telemetry and payload data. Bandwidth, latency, packet loss and jitter are different metrics. Antenna placement, polarization, enclosure attenuation and interference affect the link; electrical compatibility does not establish lawful spectrum use. Regional transmission claims cannot be transplanted into Indian operation.

Interfaces: serial/Ethernet/radio messages, versioned schemas, authentication and clock synchronization. Failure modes: stale commands, ambiguous reconnect, overloaded telemetry, key compromise and operator misinterpretation. Test link loss in simulation/bench, message freshness, reconnect behavior and status display. Tools: protocol capture, latency logs and appropriate RF expertise. Buy approved modules and antennas for the intended jurisdiction; verify [radio requirements](../supply-chain/regulation.md) before selecting frequencies or power.

## Cameras, optics, ISP and gimbals

A lens maps scene rays onto a sensor; focal length, aperture, focus and distortion affect usable detail. Pixel count alone does not determine optical resolution. Exposure integrates motion: first-order angular blur in pixels is approximately `f_px × ω_rad/s × exposure_s` for small rotations. Global shutter and rolling shutter have different motion distortions; Sony's industrial portfolio supplies a technology reference [R059](../sources.md#r059).

The ISP converts sensor output into images; demosaicing and denoising may trade detail for appearance. A gimbal changes the camera orientation relative to the aircraft and requires travel limits, alignment and feedback. Interfaces include MIPI/USB/Ethernet, power, trigger, timestamps and lens controls. Failure modes: blur, clipping, focus drift, rolling-shutter geometry errors, gimbal saturation and lost metadata. Test chart sequences, geometric calibration and vibration with metadata preserved. Skills/tools: optics, imaging, calibration targets and synchronized logging. Buy camera modules/gimbals first; e-con is a module-integration candidate [R050](../sources.md#r050). Begin with the [phone project](../phone-mvp.md).

## Computer vision, mapping and obstacle sensing

Vision estimates properties from imperfect images; illumination changes, textureless surfaces, reflections, motion and domain shift create failures. Mapping joins observations into a coordinate-consistent representation. Lidar observes range samples but still needs motion compensation, extrinsic calibration and scene interpretation. Flyability's indoor platform is a commercial reference, not proof of universal operation in dust or reflective spaces [R033](../sources.md#r033).

Interfaces: calibrated frames, depth/range, confidence, estimated pose and timestamps. Test on held-out sessions and deliberate lighting/texture changes. Report false negatives, false positives, distance/pose error and tail latency, not just mean model accuracy. Tools/skills: image processing, geometry, dataset design and reproducible evaluation. Buy sensing; build task-specific analysis only when a baseline demonstrates benefit. Unknown observations must remain unknown rather than becoming “free space.”

## Companion computing and software architecture

A companion handles noncritical research/payload tasks while the autopilot retains stabilization authority. Data capture, decoding, inference and planning all consume time and energy. Advertised operations per second on a module do not equal end-to-end latency. NVIDIA's module family is a candidate source; benchmark the exact model, precision, power mode and cooling [R060](../sources.md#r060).

Interfaces: bounded setpoints, heartbeats, state, clock mapping and logs. Failure modes: process crash, memory exhaustion, thermal throttling, storage full and incompatible messages. Test recorded data at realistic rate, profile p50/p95/p99 latency, interrupt the research process and verify the defined autopilot response. Tools/skills: Linux, profiling, C++/Python, containers where suitable and embedded power measurement. Buy compute; optimize only after measuring the bottleneck.

## Payloads, landing and docking

A payload interface is mechanical, electrical, data and timing at once. Swapping it changes mass distribution, drag, power and calibration. Landing introduces ground contact, uncertain terrain and possible sensing occlusion. Docking adds alignment, charging contacts, drainage, weather sensing, remote readiness and recovery from a failed approach; a weather-protected dock does not make the aircraft all-weather [R037](../sources.md#r037).

Test repeated payload swaps and calibration checks, contact reliability, power interlocks and interrupted charge cycles using appropriate certified charging equipment. Use static fixtures and simulation before automated flight. Skills: mechanical design, power interfaces and state-machine design. Build a bench docking mockup only after an actual repeat-inspection mission justifies it.

## Cybersecurity, updates and reliability

Threat boundaries include operator identity, radios, ground computers, update servers, removable storage and supplier firmware. MAVLink 2 signing authenticates messages; it is not payload encryption [R015](../sources.md#r015). A secure deployment also needs provisioned keys, restricted access, update authenticity, rollback/recovery and protected logs.

Test rejection of malformed/stale inputs in owned lab systems, update interruption, recovery and least-privilege access. Do not include credentials in source or research datasets. Reliability requires failure-mode analysis, maintenance intervals, serial/lot history and repeat-build testing. Independent sensor copies sharing one power rail can still fail together. “Redundant” needs a common-cause analysis.

Buy critical flight hardware first, build observability and recovery into custom software, and keep updates separate from active flight. An ordinary watchdog reset is not automatically a safe airborne response; it must be analyzed within the complete system.

## Integration artifact AER should produce next

A single interface-control document: each module's voltage/current, connector, protocol/version, frame/time convention, update rate, failure timeout and acceptance test. Then a fault matrix linking detected failures to allowed mode transitions. This is more useful than adding sensors before their role is defined.
