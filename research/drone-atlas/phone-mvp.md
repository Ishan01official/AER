# Smallest useful AER project: phone capture and timing recorder

**Proposal:** an Android-first recorder for one rear camera plus raw accelerometer and gyroscope logs, exporting a self-describing session and an offline quality report. Start with one phone; expand using capability detection. “Runs on any phone” is not a credible promise of identical manual camera control, RAW output or timestamp quality.

This project should precede training a color-grading model. A model trained on uncontrolled exposure, automatic tone mapping and poorly synchronized motion can learn phone-specific processing artifacts. A repeatable recorder reveals whether the desired training evidence exists.

## Capability and capture contract

On startup enumerate camera IDs, supported formats/resolutions, manual controls, RAW support, stabilization options and timestamp source. Camera2 exposes capability declarations; do not infer support from Android version or camera marketing [R004](sources.md#r004). Save requested settings **and observed capture-result metadata**. A setting accepted by a UI is not proof the camera applied it.

Prefer a fixed physical camera, focus and resolution for the first dataset. Where supported, lock exposure and white balance after establishing a reference; record unsupported controls rather than emulate them silently. Store exposure duration, sensitivity, white-balance mode/gains, lens information, frame timestamp and any available rolling-shutter timing. Treat JPEG/YUV and DNG RAW as distinct pipelines. The image signal processor (ISP) can perform demosaicing, denoising, sharpening and tone mapping; a color transform cannot generally invert unknown nonlinear processing.

A first iOS port requires a separate AVFoundation/Core Motion capability and clock review. That research is explicitly outstanding. Do not substitute a generic cross-platform camera wrapper without checking the metadata it preserves.

## Dataset layout and clock handling

A session contains `manifest.json`, `frames.csv`, `imu.csv`, image/video files outside Git, calibration metadata, hashes and a quality report. The manifest includes device model, OS/build, camera ID, app commit, schema version, temperature if available, settings, consent/scene description and storage location. Use integer nanoseconds; keep wall-clock UTC only for session indexing.

`frames.csv`: frame_id, sensor_timestamp_ns, callback_timestamp_ns, exposure_ns, iso, wb_mode, width_px, height_px, file_path, dropped_before, metadata_status.

`imu.csv`: sensor_id, timestamp_ns, callback_timestamp_ns, x, y, z, unit, accuracy_status. Accelerometer units are m/s²; gyroscope units rad/s. Preserve Android device axes, then store an explicit rotation to the chosen analysis frame [R005](sources.md#r005).

If camera timestamp source is UNKNOWN, label the clock relationship unknown. A fitted model `t_imu = a t_camera + b` may estimate relative drift and offset, but its residual uncertainty must accompany the mapping. Arrival timestamps only bound delivery behavior; they do not replace acquisition timestamps. Validate spatial/temporal calibration on a separate sequence; Kalibr is a candidate tool, not a guarantee for every phone pipeline [R013](sources.md#r013).

## Color experiment

Use a stationary camera, a known chart or neutral reference, repeatable illumination and recorded distance. A printed chart without measured reflectances can test repeatability but cannot establish absolute color accuracy. Collect locked versus automatic settings, repeat after restarting the app, and compare across light conditions. Hold out entire capture sessions when evaluating a learned transform to avoid near-duplicate leakage.

For a simple baseline, fit a linear color matrix to linearized values and compare held-out patch residuals before introducing a neural network. State the input/output color spaces, transfer functions and reference illuminant. If only processed JPEG is available, present results as pipeline-specific. Never label attractive color grading as sensor calibration.

## First deliverables and pass conditions

| Deliverable | Proposed evidence |
|---|---|
| Capability manifest | Unsupported/manual/RAW/timestamp capabilities visible per camera |
| Five-minute session export | Every file parses; IDs unique; hashes match; interruptions recorded |
| Timing report | Actual sample/frame-rate distributions, largest gaps, clock status and dropped samples |
| Color repeatability report | Repeated fixed-scene captures with settings and held-out session comparison |
| Replay tool | Same exported session produces the same summary with pinned analysis code |
| Privacy controls | Local capture by default; explicit export; deletion; no silent upload or location collection |

Five minutes is a proposed test duration, not an achieved benchmark. Begin around 30 frames/s and 100–200 IMU samples/s only if the device supports them; record achieved rates rather than demand unsupported values. Start with short image sequences if simultaneous video/metadata recording is unreliable.

## Transfer to an aircraft

Transfers: calibration discipline, timestamps, data schemas, exposure experiments, blur metrics, reproducible analysis and privacy handling. Does not transfer automatically: propeller vibration, airborne thermal/power constraints, rigid sensor synchronization, rolling-shutter behavior of another camera, radio latency, flight-control deadlines, lens/gimbal extrinsics or regulatory eligibility.

**Decision:** build the recorder and report first, then decide whether a color model, dedicated camera module or visual-inertial experiment is justified. Equipment and budget assumptions are in the [development path](development-path.md). Nothing here proposes using an ordinary phone as the sole safety-critical flight controller.
