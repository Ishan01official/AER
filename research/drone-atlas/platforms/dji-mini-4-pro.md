# Case study: DJI Mini 4 Pro as an integration benchmark

**Maturity:** commercial product reference; stock and lawful Indian sourcing not verified. **Scope:** standard battery unless stated. It is a selected historical/currently documented benchmark, not a claim that it is DJI's newest small drone. Manufacturer specifications are **M**, all design conclusions below **I**. Related company history remains in the [existing DJI study](../../case-studies/dji/README.md).

## What the evidence establishes

DJI specifies takeoff mass below 0.249 kg with the standard battery; the Plus configuration exceeds that threshold. Published standard-battery flight time is 2,040 s, with 1,800 s hover time. Its flight test uses 6 m/s forward motion in controlled sea-level-equivalent conditions, Photo mode and depletion ending in forced landing. The standard battery is 18.96 Wh. DJI lists a three-axis gimbal, 48 MP 1/1.3-inch-type camera, omnidirectional visual sensing, and 20,000 m FCC versus 10,000 m CE transmission claims under unobstructed interference-free conditions. These are not mission radii or reserved-energy flight times [R001](../sources.md#r001). The dated manual is a separate review lead [R002](../sources.md#r002).

See [platform data](../data/platforms.json) and [observations](../data/observations.csv). No independently measured endurance, current Indian price, processor identity, component BOM or repairability score was established.

## Why the integration is difficult

A compact imaging drone solves several coupled problems. Lower mass reduces required thrust, but thinner structure can increase vibration. A heavier camera may improve image performance but leaves less mass for battery and enclosure. Larger propellers can reduce ideal induced power yet complicate folding, ground clearance and packaging. The gimbal must remain controllable despite aircraft rotation, airflow and finite travel. Battery placement shifts the center of mass, changing the moment required from each motor.

AER should benchmark the **system outputs**: how often a session starts successfully, whether imagery is usable, whether logs explain failures, and how much maintenance is needed. It should not copy a headline mass limit as its first design requirement. A slightly larger modular research aircraft can be a better engineering tool because connectors, debugging and replaceable parts are accessible.

## Energy calculation: useful, but limited

**E:** treating the whole rated 18.96 Wh as usable over 34 min gives equivalent average power `18.96 / (34/60) = 33.46 W`. This is arithmetic using nominal energy, not a measured electrical trace. Actual usable energy, voltage behavior and power vary with the test. Multiplying the advertised time by a reserve percentage is not a validated return-to-home model: wind, climb, battery temperature and route geometry matter.

For AER, measure voltage and current over the complete mission, integrate energy, and retain a separate reserve policy. Report time to a defined landing threshold, time spent collecting usable data, and remaining energy. A forward-flight result and a hovering result belong in separate observations.

## Software and repair boundaries

The public product specification does not establish source access to the flight stack, support for arbitrary onboard research code or the exact support matrix of DJI SDKs. Treat these as unverified capabilities. A documented camera product can be excellent for collecting reference imagery and still be unsuitable for testing a custom estimator.

Repairability requires evidence about replaceable assemblies, calibration after replacement, spare supply, tools, service documentation and firmware pairing. Avoid scoring it from appearance. AER can learn the interface discipline of an integrated product while using an open autopilot for implementation.

## Civilian benchmark experiment

**Proposal, not performed:** photograph the same permitted static test scene from a tripod-mounted phone and a lawful reference camera-drone session. Control illumination as far as practical. Compare blur, clipping, color repeatability and image coverage. Keep aircraft stabilization, camera stabilization and postprocessing as separate factors. Do not infer geometric accuracy from image sharpness.

Acceptance evidence should include original files, capture settings, scene distance, chart reference, timestamps, processing version and failure examples. This connects to the [phone MVP](../phone-mvp.md) without requiring AER to recreate a compact aircraft first.

## Visuals, unknowns and decisions

Use the [official tutorial index](https://www.dji.com/mini-4-pro/video) for unfolding, controls and capture workflows; only its page was inspected [R054](../sources.md#r054). No video timestamps or footage-derived conclusions are claimed. Product images remain linked, not redistributed.

Priority unknowns: exact firmware in any benchmark; serviceability evidence; raw versus processed camera output; independent endurance with reserve; Indian procurement eligibility. **Decision proposal:** use the Mini as an integration reference, not as the default AER flight-control development platform.
