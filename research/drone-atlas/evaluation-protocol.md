# AER evaluation protocol: measurement before algorithm comparison

Proposed protocol, not executed. It connects [paper analysis](research-papers.md), the [phone recorder](phone-mvp.md) and [state-estimation guide](subsystems/state-estimation.md). All acceptance choices below are engineering proposals that need a measured baseline.

## Reproducibility manifest

Record experiment ID and hypothesis; dataset source/license/hash; split definition; device/sensor serial or anonymized stable ID; calibration and clock model; firmware/algorithm commit; compiler and libraries; parameters; compute/power/cooling configuration; evaluation implementation; random seeds; raw/log locations and known interruptions. Keep identifying imagery and large raw data outside Git; commit metadata and permitted summaries.

A dataset hash identifies bytes, not truth. An inaccurate ground-truth trajectory remains inaccurate after hashing. Record reference-system uncertainty, time alignment and any portions with missing reference.

## Separate four outcomes

1. **Input validity:** timestamp order, missing frames, missing metadata, sensor saturation and calibration provenance.
2. **Output availability:** initialization, intervals with valid output, tracking loss/recovery, discontinuities and stale states.
3. **Accuracy/consistency:** trajectory error against independent reference and residual behavior under the declared noise model.
4. **Resource cost:** wall time, latency tails, memory, temperature and energy for the entire pipeline.

Never compute accuracy only over successful segments without reporting excluded durations and failure reasons. Offline completion faster than recording duration does not necessarily establish bounded real-time latency.

## Trajectory metrics and alignment

Let `p_i` be estimated position after a declared alignment and `p_i*` the reference at matched timestamps. Position absolute trajectory error RMSE is

$$\operatorname{ATE}_{RMSE}=\sqrt{\frac{1}{N}\sum_i\|p_i-p_i^*\|^2}.$$

Report units in m, alignment type and sequence. For metric visual–inertial output, allowing arbitrary scale correction can hide a scale-estimation failure. If using similarity alignment for monocular-only evaluation, explicitly distinguish it from rigid alignment. Avoid fitting transformations independently to short segments simply to improve the score.

Relative pose error evaluates estimated motion between pairs separated by a fixed time/distance; choose the interval before comparing algorithms. Report translational and rotational errors separately. Define whether metrics use online output, smoothed output or loop-corrected output. AER's control-facing decision needs the first.

## Controlled perturbations

| Variable changed | Hold fixed | Record | Purpose |
|---|---|---|---|
| Timestamp offset: 0, 5, 10, 20 ms | Sensor values and frame order | Initialization, error, residuals, valid-output time | Quantify timing sensitivity; values are proposed replay settings |
| Frame drop schedule | Original timestamp semantics, calibration | Gaps and estimator response | Test robustness without inventing replacement observations |
| Exposure mode | Scene/reference, lens, motion protocol | Applied exposure/gain and clipping | Separate auto-control effects from a color model |
| Compute load/power mode | Dataset, algorithm and parameters | p50/p95/p99 latency, thermal history | Identify sustained onboard limits |
| Sensor ablation | Dataset and evaluation contract | Missing sensors and changed observability | Avoid attributing sensor advantage to algorithm alone |

Use a held-out set of sessions for the final comparison. Fit calibration/noise models on the training set; do not tune and report on identical trajectories. Preserve run-to-run variation and seed. Repeated computation on one deterministic log tests numerical repeatability; it does not substitute for independent capture sessions.

## Minimum result package

A brief states the hypothesis, baseline, configuration, number of sessions/runs, all exclusions, plots with units, summary metrics, failure examples, uncertainty and the next decision. Keep practical conclusions proportional to evidence. If the reference is unavailable, report repeatability or internal consistency, not absolute accuracy.

Initial success means AER can reproduce and explain a baseline, including its failures. Numerical pass thresholds for flight authority must come from mission requirements and reference uncertainty. No arbitrary centimeter target is imposed by this document.
