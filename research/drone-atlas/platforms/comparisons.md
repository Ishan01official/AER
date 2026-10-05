# Comparing platforms without creating false equivalence

The [platform database](../data/platforms.json) contains representative records; the [observation table](../data/observations.csv) preserves units and conditions. Null fields are intentional evidence gaps. “Commercial” identifies a documented product, not guaranteed October 2026 stock, Indian availability or certification.

| Need | Plausible architecture | Reference | Why another option could win |
|---|---|---|---|
| Portable imagery | Integrated camera quad | [Mini 4 Pro](dji-mini-4-pro.md) | Open research platform better when modifying flight software |
| Indoor repeatable research | Small open quad plus positioning | [Crazyflie](crazyflie.md) | Simulator first when infrastructure cost or safety dominates |
| Large-area survey | Wing-borne VTOL | WingtraOne [R022](../sources.md#r022) | Hovering multirotor for tight inspection or limited transition space |
| Agricultural work | Purpose-built rotorcraft | Yamaha [R028](../sources.md#r028), DJI T50 [R038](../sources.md#r038), Dhaksha [R065](../sources.md#r065) | Ground equipment may be better where flight adds little coverage value |
| Persistent fixed-site sensing | Tethered rotorcraft | Orion [R030](../sources.md#r030) | Mast/ground camera may be simpler and cheaper |
| Indoor confined inspection | Protected aircraft plus local sensing | Elios 3 [R033](../sources.md#r033) | Handheld/ground robot if reachable; avoids airborne localization burden |
| Stratospheric persistence | Solar fixed-wing | Zephyr [R027](../sources.md#r027) | Satellite or terrestrial network depending on coverage and availability |

## Endurance and range are not single comparable numbers

DJI's hover and forward-flight tests differ. Wingtra's August 2024 document gives a headline maximum of 3,540 s, while RGB61 mission references give 2,940 s at 0–500 m takeoff altitude and 2,280 s at 2,000 m [R022](../sources.md#r022). These are distinct configurations/conditions, not an independent head-to-head test. Link distance, total flight distance and safe round-trip mission radius must remain separate.

**Unresolved document inconsistency:** the same Wingtra brochure lists general payload capacity 0.800 kg and lidar payload mass 1.030 kg. Do not substitute one into the other configuration without clarification. This issue is Q09 in the [backlog](../open-questions.md).

AALTO's multi-day flight uses solar energy and a different flight regime; Orion uses external energy. Comparing either to battery hover time as though all carry equal payload and energy would be misleading. RoboBee's very small mass also does not establish outdoor autonomous endurance.

## AER comparison protocol

Choose a common task and output quality. Record payload, wind, altitude/density, battery age, reserve, route, capture settings, firmware and operator involvement. Report energy per useful output, setup/maintenance time, intervention rate and uncertainty. Separate source claims, independent tests and AER measurements into different rows. This release has no independent/AER performance rows.

Open comparisons: current FPV/racing products, lift-plus-cruise platforms, verified logistics deployments, model-specific Indian civilian performance, service/repair cost, and publicly documented military categories beyond the representative ISR entry.
