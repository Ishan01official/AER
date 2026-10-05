# Research papers: what transfers to AER, and what does not

Evidence cutoff: **2026-10-05**. Added in the continuation batch on 2026-10-06. These are selected foundational and recently released research systems relevant to AER's immediate measurement problem, not an exhaustive or “latest papers” ranking. Paper author claims are **M** under the atlas's project-claim convention; proposed interpretations/experiments are **I**. None were reproduced by AER.

## VINS-Mono: learn initialization and data requirements first

Qin, Li and Shen's preprint dates to 13 August 2017. It describes tightly coupled monocular visual–inertial estimation with IMU pre-integration, feature observations, initialization and failure recovery [R067](sources.md#r067). “Tightly coupled” means raw observation constraints participate in joint estimation rather than merely averaging two finished position outputs.

The official repository documents Linux/ROS software and a separate VINS-Mobile route. Its README exposes legacy Ubuntu/ROS/Ceres prerequisites and emphasizes accurate timestamps and calibration [R068](sources.md#r068). Treat those instructions as version-specific evidence, not a recommendation to install obsolete packages on the AER host.

**I — AER implication:** a phone capture app is useful because it can reveal whether camera and IMU observations satisfy an estimator's input contract. Initialization can fail even when each sensor produces plausible samples: motion may not excite the unknown quantities, clocks may disagree, or the camera's geometry may change with stabilization. An online calibration feature should not be interpreted as permission to ignore data quality.

**Proposed experiment:** take a supported public benchmark sequence before any custom phone recording. Record initialization success, time to usable output, tracking loss and restart behavior. Then introduce one known timestamp offset in replay. Keep the image content, IMU values and evaluation alignment unchanged. Compare failures, not only successful trajectory error. The phone app must pass timing/capability checks before this comparison is attempted.

Open question: which maintained build environment and exact revision can AER reproduce without silently changing numerical dependencies? No mobile-platform compatibility claim is made merely because an older iOS demonstration exists.

## ORB-SLAM3: mapping and recovery change the evaluation question

Campos and colleagues describe visual, visual–inertial and multi-map simultaneous localization and mapping (SLAM). The cited preprint version is 23 April 2021; the official repository identifies V1.0 dated 22 December 2021, benchmark examples and GPLv3 licensing [R069](sources.md#r069), [R070](sources.md#r070).

A multi-map system can preserve or recover information across losses of tracking. This changes what “error” means: final corrected map quality and the real-time pose available to a controller are different outputs. Do not rank a system solely by a retrospectively improved trajectory if the aircraft would have received stale, discontinuous or unavailable estimates during flight.

**Proposed experiment:** replay an indoor loop with a known reference, then a segment with deliberately degraded imagery. Report tracking availability, number/duration of losses, recovery behavior, online latency and both pre- and post-correction trajectory metrics. Count missing output explicitly. Compare the same sensor mode across systems; a stereo-inertial result is not a fair baseline against monocular-only input without explaining the difference.

**I — AER implication:** use mapping software first as an offline analysis tool. Do not give it control authority simply because a final map looks accurate. License and dependency review belongs before commercial integration; the main license does not summarize every third-party asset.

Open question: how sensitive is the chosen configuration to phone rolling shutter, changing focus and stabilization? This requires recordings and a supported model, not extrapolation from benchmark accuracy.

## FAST-LIVO2: direct photometric residuals connect to the camera project

Zheng and colleagues' v2 paper describes fusion of lidar, inertial and image observations with sequential filter updates and a shared voxel map. The visual part uses photometric residuals, while the method also estimates relative exposure. The paper distinguishes synthetic brightness variation from recordings with camera exposure metadata and discusses remaining response/vignetting effects [R071](sources.md#r071).

The official repository records code release on 23 January 2025, provides a hardware-synchronization reference and lists dependencies [R072](sources.md#r072). These improve reproducibility but do not establish compatibility with arbitrary unsynchronized phone cameras or guarantee performance on AER hardware.

**I — AER implication:** color consistency is not purely aesthetic. If an estimator assumes corresponding scene patches have predictable brightness, an ISP or exposure change can corrupt the residual. A learned color transform that improves appearance may remove or distort information an estimator relies on.

**Proposed experiment:** before buying lidar, collect repeated stationary and slowly moving chart/texture sequences under locked and automatic exposure. Preserve actual exposure/gain metadata. Compare patch residual distributions after a simple brightness normalization and after the proposed color pipeline. Separate geometric motion, clipping, nonlinear tone mapping and illumination changes. This is a diagnostic camera experiment, not a reproduction of FAST-LIVO2.

For a later real reproduction, use the authors' data and exact sensor timing/calibration. Evaluate the full system and explicit sensor ablations with the same reference and compute budget. Do not use total return-to-start drift as the only accuracy measure: a trajectory can deviate substantially and return near its initial point.

Open questions: sensor synchronization achievable in AER, retained exposure information, processing latency on chosen compute, and whether lidar provides enough mission benefit to justify cost/mass/power.

## Swift: a systems lesson from a bounded racing demonstration

Kaufmann and colleagues' 2023 Nature paper describes Swift, combining onboard perception/state estimation and a learned control policy trained in simulation. The study used a specified racing track and empirical data to reduce simulation-to-reality mismatch. Onboard sensing at race time is distinct from external motion-capture measurements used during development/data collection [R073](sources.md#r073).

**I — AER implication:** the valuable transferable idea is evidence-driven modeling of the gap between simulation and real sensors/dynamics. It is not a reason to make aggressive flight AER's first objective. A known racing environment also differs from an unknown inspection scene with changing lighting and people.

**Proposed experiment:** in civilian low-speed simulation, compare an idealized sensor model with a model using measured phone/bench delay and dropout distributions. Keep the controller and task fixed. Evaluate mission completion, constraint violations and estimator health across held-out disturbances. Only then investigate whether a more complex controller improves the same bounded task.

The [research video reference](https://www.youtube.com/watch?v=fBiataDpGIo) was located but not watched [R074](sources.md#r074). No timecodes or footage-based conclusions are claimed. The original article's architecture figure is a useful visual reference; check individual figure/photograph credits before reuse.

Open question: which measured modeling errors dominate AER's baseline? That must be learned from logs rather than assumed from a different aircraft.

## Compare the research roles

| System | Main question for AER | Essential dependency | First feasible experiment |
|---|---|---|---|
| VINS-Mono | Can visual/IMU inputs initialize and remain consistent? | Clocks, calibration, excitation, pinned numerical stack | Public-data replay with deliberate timing offsets |
| ORB-SLAM3 | What remains available during tracking loss and map recovery? | Sensor mode, reference frames, online vs corrected outputs | Report availability and recovery alongside trajectory error |
| FAST-LIVO2 | How do geometry and photometric changes affect fusion? | Lidar/camera timing, exposure model and calibration | Camera brightness/metadata experiment first |
| Swift | Which simulation assumptions fail on real measurements? | Empirical noise/dynamics model and bounded task | Low-speed simulation with measured delay distributions |

Recommended sequence: [phone measurement](phone-mvp.md), one public-data replay, the [evaluation protocol](evaluation-protocol.md), then a deliberately scoped algorithm comparison. No new flight behavior is authorized by a literature result alone.
