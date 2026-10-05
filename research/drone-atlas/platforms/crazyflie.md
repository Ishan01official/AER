# Case study: Crazyflie 2.1 Brushless for reproducible small-scale research

**M:** Bitcraze's Rev 3 datasheet describes a 0.032 kg open development platform with stock flight time 600 s and recommended maximum stock payload 0.040 kg. It lists STM32F405 and nRF51822 processors, BMI088 inertial sensing, BMP388 pressure sensing, integrated single-cell ESCs and expansion interfaces. Endurance and maximum payload must not be assumed simultaneous. Its long line-of-sight radio claim is not a tested indoor operating radius [R016](../sources.md#r016).

The [product page](https://www.bitcraze.io/products/crazyflie-2-1-brushless/) establishes a current catalog reference, not Indian stock [R017](../sources.md#r017). The development blog describes motor/propeller matching [R018](../sources.md#r018), and a Rev G schematic is available as a technical review lead [R019](../sources.md#r019). Schematics, firmware and expansion options make this an unusually useful educational comparison to a closed consumer product; their existence does not constitute an AER electrical audit.

## What makes it useful for AER

**I:** small aircraft can reduce experimental space and damage energy, but small size does not eliminate propeller, battery or people-related risk. A repeatable indoor laboratory allows changes in lighting, target texture and localization to be measured without simultaneously changing weather. An expansion interface exposes the engineering cost of adding a sensor: power, mass, timing, bus throughput and changed center of mass.

A useful experiment is not simply “make it fly.” It is “does a logged state estimate remain consistent when a known observation becomes stale?” That question can first be answered by replay and simulation; a small lab platform later checks whether actual sensor timing and vibrations invalidate the model.

## Architectural lessons

| Boundary | Why it matters | AER test question |
|---|---|---|
| Main controller / radio-power processor | Flight code and communication/power functions have distinct timing | Does data loss affect control scheduling or only telemetry? |
| Integrated ESC / replaceable propulsion | Tight integration saves wiring but couples repair and revision choice | Can motor replacement restore the same response and current draw? |
| Expansion deck / aircraft | An added sensor changes mechanics as well as software | Is sensor mass included in every measured configuration? |
| Positioning system / vehicle | Indoor absolute positioning can be external infrastructure | What performance remains when the external reference disappears? |
| Host orchestration / onboard control | Host latency should not be mistaken for onboard control bandwidth | Are timestamps capture-time or host-arrival-time? |

These are research questions, not verified descriptions of every fault response of the product.

## Do not conflate ecosystems or generations

Crazyswarm is a separate research/software system. USC identifies the 2017 paper; the available documentation reports version 0.3 [R020](../sources.md#r020), [R021](../sources.md#r021). That does not establish out-of-box support for this newer Brushless hardware, ROS 2, every deck or every localization system. Compatibility must be pinned at hardware, firmware, host and positioning layers.

Likewise, a 2017 multi-vehicle demonstration is not evidence that the 2026 AER setup can reproduce it. Start with one vehicle and one positioning method. Infrastructure costs can dominate the airframe price; do not buy motion capture solely to reproduce an attractive video.

## Proposed evaluation sequence

1. **Offline:** document message types, coordinate frames and clocks. Replay a synthetic trajectory and deliberate delayed measurements.
2. **Bench:** inspect the exact board revision, batteries and expansion interfaces against official documentation. Verify logging continuity and graceful host disconnection without propulsion.
3. **Single-aircraft lab:** use an approved controlled environment and a qualified operator; measure a simple hover/reference trajectory with the chosen positioning system.
4. **Regression:** repeat identical configurations and preserve failed runs. Compare distributions, not the best attempt.
5. **Multiple vehicles:** only after localization, scheduling and separation behavior are validated in simulation; this atlas supplies no deployment claim.

## Build versus buy

Buy a documented baseline when the research variable is estimation or perception. Designing a microcontroller board at the same time confounds software errors with soldering, power and vibration errors. Study the schematic to learn architecture; create a custom sensor adapter only when an actual requirement cannot be met by existing interfaces.

Unknowns include exact present price and landed cost, firmware/deck compatibility, expected endurance with the chosen sensor, calibration stability and domestic service options. **Decision proposal:** shortlist this class for indoor research, while retaining an established larger autopilot platform as a separate later option for outdoor payload experiments. Do not make either purchase before the mission and laboratory constraints are selected.

Visual reference: [schematic Rev G](https://www.bitcraze.io/documentation/hardware/crazyflie_2_1_brushless/cf2.1_bl_schematics_Rev.G.pdf). It illustrates interface organization, not independently inspected manufacturing quality.
