# Propulsion and energy: sizing a civilian measurement platform

This guide develops **ideal physics and illustrative estimates**, not a flight-ready BOM. Manufacturer curves, actual assembly tests and environmental margins are required before selection. NASA's actuator-disk explanation supplies a first-principles starting point [R014](../sources.md#r014).

## From weight to ideal hover power

For mass `m`, steady level hover requires total thrust `T = mg`. For separated rotors with total disk area `A`, an ideal hover model gives induced speed and power:

$$v_i=\sqrt{\frac{T}{2\rho A}},\qquad P_i=T v_i=\frac{T^{3/2}}{\sqrt{2\rho A}}.$$

Assumptions: uniform induced flow, incompressible air, no ground effect, no profile drag, no rotor overlap/interference and steady hover. At fixed area, power scales with mass to the three-halves power. A coaxial pair does not simply double effective isolated disk area.

**E, worked example:** assume a 1.00 kg civilian quadrotor, four 0.254 m diameter rotors, air density 1.225 kg/m³ and `g = 9.81 m/s²`. Then `A = 4π(0.254/2)² = 0.2027 m²`, `T = 9.81 N`, `v_i ≈ 4.45 m/s`, and ideal induced power `P_i ≈ 43.6 W`. This is a lower bound, not expected battery draw.

For illustration only, assume aerodynamic figure of merit 0.55 and motor/ESC efficiency 0.80, then propulsion input is `43.6/(0.55×0.80) ≈ 99.1 W`. Add an assumed 10 W payload/avionics load for approximately 109 W total. A nominal 14.8 V, 5 Ah pack contains 74 Wh; an assumed usable fraction 0.75 gives `55.5/109 ≈ 0.509 h`, about 1,832 s. This optimistic toy estimate does **not** select that pack: the assumed total aircraft mass must include its actual mass, and losses/reserve must be measured.

If mass rises to 1.25 kg with the same disk area, ideal power rises by `1.25^1.5 ≈ 1.40`. Adding battery may increase energy and still reduce useful payload or agility. Close the mass–power–energy loop iteratively rather than sizing battery last.

## Propeller, motor and ESC are a matched system

A propeller converts shaft work into momentum change. Blade geometry, airfoil, diameter, pitch and rotational speed determine load. A motor's `K_v` convention describes approximate no-load speed per volt; it is not a power or thrust rating. Real torque requires current, and winding resistance creates heat. Use electrical and mechanical limits for the exact motor/propeller/voltage combination.

An **electronic speed controller (ESC)** switches power into motor phases and commutates the motor. Sensorless control estimates rotor state from electrical behavior; startup, rapid load changes and voltage sag can expose limitations. ST's reference design provides an example of field-oriented control, current measurement and protective circuitry [R058](../sources.md#r058). Its existence does not validate a new PCB or every connected motor. APC's technical resources are a route to exact propeller data and limits [R061](../sources.md#r061).

| Design decision | Dependency to verify | Failure mechanism |
|---|---|---|
| Propeller diameter/pitch | Frame clearance, stiffness, motor curve and allowed speed | Contact, excess current, fatigue or poor response |
| Motor winding/size | Torque-speed requirement and cooling | Overheating or insufficient thrust at low pack voltage |
| ESC voltage/current | Pack maximum voltage, transients, cooling and command protocol | Component damage, desynchronization or resets |
| Battery and connector | Continuous/peak current, resistance, age and temperature | Sag, heat, connector failure or early failsafe |
| Power regulation | Avionics rail transient response | Controller/companion brownout during thrust changes |

## Battery accounting and alternatives

Electrical energy is `E = ∫ V(t) I(t) dt`; convert joules to Wh by dividing by 3,600. Capacity in Ah alone does not compare different pack voltages. State-of-charge estimation, cell imbalance and voltage under load complicate reserve decisions. A battery-management system and charger must match cell chemistry and pack design; not every “Li-ion” product uses the same charge limit.

Bought packs are the practical initial option. Cell manufacture, pack assembly and charger design are distinct capabilities. Molicel supplies a cell reference [R048](../sources.md#r048); that does not establish a safe AER pack topology or welded assembly process. No home cell fabrication or improvised charging procedure is proposed.

| Energy path | Physical attraction | Remaining constraint | AER-scale experiment |
|---|---|---|---|
| Rechargeable battery | Direct electrical output and simple propulsion integration | Pack energy/mass, current, charging and aging | Log energy per useful inspection minute |
| Combustion / hybrid generator | Fuel can store substantial energy per mass | Engine/generator mass, vibration, heat, emissions, control and service | Model break-even mission duration; no initial hardware |
| Hydrogen fuel cell | Potential endurance for suitable duty cycles | Tanks, balance-of-plant, supply, peak-power buffer and certification | Compare complete system mass using verified vendor curves later |
| Solar/storage | Harvest ambient energy over long missions | Available area, weather, nighttime storage and latitude | Ground power-budget simulation; Zephyr is a demonstration reference [R027](../sources.md#r027) |
| Tether | Move energy storage to ground | Cable drag/mass and limited operating volume | Simulate cable force and failure states; Orion test is vendor evidence [R030](../sources.md#r030) |

## Test methods and tools

Begin with supplier-provided matched combinations. In an appropriately equipped lab, use a protected thrust stand, calibrated force/current/voltage measurement, temperature sensing and a documented sweep within rated limits. Record atmospheric conditions, pack state, motor/ESC firmware, propeller model and measurement uncertainty. Never hold a running propulsion assembly by hand. Repeat measurements and compare low-voltage behavior, thermal steady state and response lag.

Bench static thrust alone is not flight endurance. Flight validation needs whole-system power, actual payload, wind and reserve policy. AER's next useful output is a **measured thrust/current/voltage/temperature table with uncertainty**, not a claimed universal “best motor.”

Skills: mechanics, circuits, power electronics, controls and experimental design. Build-versus-buy: buy propulsion and packs first; design a power monitor/fixture before a custom ESC; manufacture a motor only after requirements justify winding, magnetic, balancing and endurance-test investment.

Open questions: selected mass/payload, exact component curves, battery chemistry, manufacturing variability, permitted lab and test equipment. See [supply-chain dependencies](../supply-chain/README.md).
