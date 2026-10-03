# Component manufacturers and sourcing: worldwide and India

[Case study home](README.md) · [Subsystem design](subsystem-development.md) · [Roadmap](aer-roadmap-and-budget.md)

**Checked:** 3 October 2026. This is a researched supplier shortlist, not a completed supplier audit. No order, quotation, inventory reservation, sample evaluation or supplier contact was made.

**Important distinction:** These are AER sourcing candidates. They are not a verified list of DJI's suppliers. Company location is not proof of an individual SKU's fabrication or assembly origin.

## 1. Worldwide manufacturers and technology providers

Links are official manufacturer/technology-provider pages retrieved in this research. Geography below describes company/base association at a broad level; request country-of-origin evidence for each SKU.

| Category | Company / geography | What to consider | Procurement level and checks | Source |
|---|---|---|---|---|
| Autopilot hardware | [Holybro](https://holybro.com/products/pixhawk-6x), China | Supported Pixhawk boards and accessories | Complete board; select actual hardware revision, power module and firmware support | S10 |
| Autopilot hardware | [CubePilot](https://www.cubepilot.org/), international supply chain | Cube autopilot/module ecosystem | Module/carrier combination; origin differs by product variant | S11 |
| Propulsion | [T-MOTOR](https://shop.tmotor.com/), China | Motors, ESCs, propellers and matched propulsion kits | Request exact battery/prop curves, CAD, thermal limits and protocol data | S12 |
| Propulsion | [Hobbywing](https://www.hobbywing.com/), China | ESCs and integrated UAV propulsion | Matched system; verify model firmware and rated cooling conditions | S13 |
| Propellers | [APC](https://www.apcprop.com/), United States | Multi-rotor propeller families | Correct direction, hub and RPM limits; availability varies | S47 |
| Battery packs/cells | [Grepow / Tattu](https://www.grepow.com/brands/tattu.html), China | UAV battery packs and charging products | Pack specification, cell traceability, matching charger and shipment documents | S19 |
| Cylindrical cells | [Molicel](https://www.molicel.com/wp-content/uploads/INR21700P45B_1.4_Product-Data-Sheet-of-INR-21700-P45B-80109.pdf), Taiwan association | High-power cells for a professionally designed pack | Exact cell revision, test conditions and authenticated channel | S18 |
| MCU/control | [STMicroelectronics](https://www.st.com/en/applications/industrial-tools-motor-drives-and-equipment/drones.html), Europe / global fabs | STM32, motor-control and sensor components | Bare IC/reference platform; lot origin and lifecycle need checking | S20 |
| Power/control ICs | [Texas Instruments](https://www.ti.com/tool/TIDA-00643), United States / global production | Gate drivers, control, regulators and battery-management components | Reference design is educational; revalidate for the selected pack/load | S15–S17 |
| Inertial sensors | [Bosch Sensortec](https://www.bosch-sensortec.com/en), Germany / global production | IMUs and environmental sensors | Bare sensor; evaluate noise, driver support and thermal behavior | S21 |
| Inertial sensors | [TDK InvenSense](https://www.invensense.tdk.com/en-us/products/6-axis/icm-42688-p), Japan/US association | Six-axis IMUs | Exact device/revision and timestamp/interface support | S22 |
| GNSS | [u-blox](https://www.u-blox.com/en/product/zed-f9p-module), Switzerland | GNSS/RTK receiver modules | Receiver, carrier, antenna and corrections are distinct purchases | S23 |
| Image sensors | [Sony Semiconductor Solutions](https://www.sony-semicon.com/en/products/is/industry/global-shutter.html), Japan | Industrial global-shutter sensor families | Bare sensor generally needs camera module, optics and host integration | S29 |
| Image sensors | [onsemi](https://www.onsemi.com/design/interactive-block-diagrams/industrial/drone/image-sensors), United States / global production | Global-shutter imaging devices | Verify module availability and host drivers before sensor selection | S49 |
| Camera modules | [Arducam](https://www.arducam.com/), China association | Embedded camera modules | Match interface, lens, shutter and driver version | S28 |
| Camera modules | [e-con Systems](https://www.e-consystems.com/markets/industrial-cameras/uav-drone-camera-solutions.asp), India / international operations | OEM cameras and integration support | Appropriate for India-based camera development; request SKU origin | S27 |
| Gimbals/payloads | [SIYI](https://siyi.biz/en/category/gimbals/), China | Stabilized camera payloads | Exact SDK, stream, weight and power documentation | S30 |
| Range/lidar | [Benewake](https://www.benewake.com/), China | Range-sensing catalog | Model-specific outdoors/range/interface limits | S31 |
| AI compute | [NVIDIA](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/), United States / global production | Jetson modules and development kits | Distinguish development kit from production module/carrier | S32 |
| General compute | [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-5/), United Kingdom association | Logging and lighter companion workloads | Aircraft regulator/cooling and camera compatibility still required | S50 |
| RC links | [RadioMaster](https://radiomasterrc.com/collections/elrs-receivers), China | ExpressLRS receivers/control products | Match band, firmware and Indian RF requirements | S33 |
| Wireless IC/platforms | [Silicon Labs](https://www.silabs.com/wireless), United States | Wireless connectivity technologies | Component/platform candidate; not a turnkey UAV video radio | S53 |
| PCB/assembly | [JLCPCB](https://jlcpcb.com/pcb-assembly), China | Prototype PCB fabrication and PCBA | DFM, component sourcing, substitutions and functional fixtures | S48 |

This covers practical subsystem sourcing, not every material vendor. Bearings, copper wire, magnets, laminate, fasteners, lenses, cables, regulators and connectors must be added to the **specific design's** approved BOM. Select these from controlled drawings/specifications and authenticated channels; generic marketplace descriptions are not sufficient.

## 2. Indian manufacturers and engineering partners

These entries are supported by their own product/service pages. Domestic manufacturing statements are **vendor claims**, not independently audited local-content percentages.

| Supplier | Role supported by public material | Parts/services to investigate | What still needs confirmation | Source |
|---|---|---|---|---|
| [Vector Technics](https://www.vectortechnics.com/) — Telangana | UAV propulsion manufacturer/provider | Motors, propellers, power distribution and DC/DC products; ask about exact ESC offering | Small-aircraft suitability, exact production model, MOQ, thrust data, part origin and lead time | S24 |
| [Reflex Drive](https://reflexdrive.in/) | Indigenous propulsion design/provider | Motors and ESCs; custom firmware/design capability advertised | Current catalog, support, validation data and availability | S25 |
| [DTPC Technologies](https://www.dtpc.in/dh-esc) | Vendor-advertised India-made ESC | DH ESC development candidate | Page's legacy firmware/specs, active production, stock and warranty; do not treat old list price as current quote | S46 |
| [Voltherm Technologies](https://www.volthermtechnologies.com/products/drone-batteries) | India-made smart drone-pack offering | Custom/standard UAV packs | Cell manufacturer/origin, current discharge curves, applicable certificates and dimensions | S26 |
| [e-con Systems](https://www.e-consystems.com/markets/industrial-cameras/uav-drone-camera-solutions.asp) | OEM camera designer/manufacturer | Cameras, customization and platform integration | Exact sensor/lens, hardware timestamps, Linux support and SKU manufacturing origin | S27 |
| [LionCircuits](https://www.lioncircuits.com/pcb-assembly) | PCB fabrication/assembly service | Prototype/custom PDB, carrier, avionics or ESC boards | Stack-up, controlled impedance, stencil/assembly capability and AER-specific test fixture | S35 |
| [PCB Power](https://www.pcbpower.com/page/about-us) — Gujarat | PCB/electronics manufacturing service | Fabrication, assembly and component sourcing | Quantities, design rules, inspection level and functional-test coverage | S36 |
| Local qualified CNC/composite/printing partners | Design-specific contract fabrication | Frame plates, arms, mounts, enclosures and fixtures | No named shop was audited in this study; qualify by sample, tolerance and process evidence | AER proposal |

A drone OEM advertising complete aircraft is not automatically a merchant supplier of flight controllers, ESCs or motors. No domestic supplier of standalone autopilot boards, GNSS silicon or image-sensor silicon was independently qualified here. For these, begin with traceable imported modules/ICs and build local integration capability.

## 3. India-based purchasing channels: distributors and retailers

| Channel | Role | Suitable use | Important distinction | Source |
|---|---|---|---|---|
| [Robu.in drone category](https://robu.in/product-category/drone-parts/) | Indian retailer | Frames, propulsion, FC, radio, GNSS and accessories | Many listed brands are imported; retailer address does not imply Indian manufacturing | S37 |
| [Robocraze T-MOTOR catalog](https://robocraze.com/pages/t-motor) | Indian retailer | Compare documented propulsion SKUs and local support | Confirm manufacturer authorization for chosen brand/SKU rather than relying only on seller claims | S38 |
| [Albatross Microsystems](https://albatrossmicrosystems.com/) | India-based FPV/component shop | Alternative component availability | Catalog is procurement evidence, not proof it manufactures listed parts | S39 |
| [Mouser India](https://www.mouser.in/) | Electronic component distributor | ICs, sensors, connectors and passives for custom boards | Confirm fulfillment location, importer arrangements and exact manufacturer part number | S40 |
| [DigiKey India](https://www.digikey.in/) | Electronic component distributor | Traceable components and evaluation boards | India-facing storefront can involve overseas shipment | S41 |
| [element14 India](https://in.element14.com/) | Electronic component distributor | Components and development tools | Check stocking location, actual delivery date and SKU provenance | S42 |

An “in stock” website label was not confirmed at checkout. Availability, delivered price, customs treatment and battery shipping may differ by destination and date.

## 4. A practical sourcing strategy for AER

**Prototype:** Buy a genuine supported autopilot, matched propulsion, documented GNSS and qualified pack. Use India-based channels when support and landed cost are favorable. Manufacture mounts and fixtures locally.

**Research upgrade:** Add a documented camera and companion only after profiling. Request camera synchronization and drivers before purchasing. Add RTK or gimbal only when a measured output requires it.

**Local integration:** Design power distribution, carriers, mounts and wiring harnesses; use Indian fabrication/PCBA partners. Preserve IC and cell origin.

**Productization:** Establish alternates, supply agreements, calibration fixtures, spare-parts plans, controlled substitutions and repair procedures. Evaluate each alternate as a new integration, not simply a pin-compatible replacement.

## 5. What to ask each supplier

### Standard RFQ fields

- Manufacturer and exact part number, revision and full datasheet.
- Quantity: quote 1, 5 and 20 units separately; include spare units.
- Country of manufacture and assembly for the quoted SKU.
- Availability, MOQ, lead time, validity date, shipping origin and Incoterms.
- Unit price, taxes, freight, customs handling and payment terms.
- CAD dimensions, mass, connector pinout and supported protocols.
- Firmware/software versions, update mechanism and change notifications.
- Test curves, environmental limits, serial/lot traceability and relevant reports.
- Warranty scope, returns, repair process and spare-part availability.
- Proposed substitutions must require written approval.

### Subsystem-specific additions

| Part | Ask for |
|---|---|
| Motor/ESC/prop combo | Exact pack voltage, prop and thrust/current/RPM/thermal curves; continuous versus burst conditions |
| Flight controller | Board revision, target firmware, sensor set, power-module compatibility, pinout and logging/debug access |
| Battery | Cell origin, usable energy under load, continuous/peak current, sag/thermal data, cycle conditions, charger and shipment documents |
| Camera | Supported modes, exposure/shutter, latency, triggering/timestamps, drivers and calibration support |
| Gimbal | Payload balance envelope, stabilization performance, range of motion, API/stream and fault response |
| Radio | Band/channel/power configuration, RF test reports, applicable Indian approval documentation and firmware region settings |
| PCB assembly | Gerber/ODB++ requirements, stack-up, BOM/CPL files, inspection, component sourcing and fixture/programming quote |
| Frame | Material/process, tolerances, inserts/joints, fatigue evidence, CAD ownership and tooling costs |

## 6. Indian imports and operations

The official **9 February 2022** notification states that drone imports in CBU/CKD/SKD form are prohibited with specified R&D, defence and security exceptions; drone components are designated “Free.” Eligible R&D drone imports still require the stated authorization. [S43]

“Free” is an import-policy classification, **not zero customs duty, zero tax or exemption from every other requirement**. A complete kit may be classified differently from an independent component. Obtain written classification/clearance advice for the actual consignment before ordering; splitting a kit across shipments is not a valid substitute for compliance.

This research retrieved the historical official notification and government explanations; it did not establish a consolidated October 2026 legal opinion or every subsequent amendment. Check the current DGFT schedule and shipment-specific treatment before import.

For operations, the 2021 government summary describes R&D exemptions for eligible entities operating within the specified premises/green-zone conditions. [S44] It does not establish that every individual project or every field flight qualifies. Before testing, establish applicability of type certification, registration, remote-pilot credentials, site permissions and current airspace restrictions.

Wireless equipment is a separate issue. DoT maintains ETA guidance and approval processes. [S45] Verify the device, band, power, antennas and approval route for India; foreign FCC/CE markings do not by themselves establish Indian permission.

For commercial deployment, also evaluate customer data/privacy requirements, insurance, maintenance records, product certification and destination-country requirements. These are deployment work items rather than assumptions that the research prototype is certified.

## 7. Landed cost and incoming quality

**Landed cost = supplier price + shipping + insurance + applicable customs duties/taxes + clearance/handling + foreign-exchange/payment costs.**

Compare total cost and time to a **usable tested unit**, not only the displayed price. Include replacement delay, warranty handling and test effort.

Incoming inspection should record:
1. Supplier, invoice, part number, serial/lot and date.
2. Hardware revision and firmware/version.
3. Physical damage, dimensions, mass, connectors and polarity.
4. Datasheet/interface match and missing accessories.
5. Electrical/functional screening appropriate to the component.
6. Battery/propulsion baseline measurements.
7. Accepted/rejected status and reason.

## 8. Procurement tracker schema

Keep design facts and commercial facts separate.

`category, manufacturer, manufacturer_part_number, revision, seller, seller_url, country_of_manufacture, assembly_country, quantity, unit_price_currency, unit_price, shipping, tax_duty_estimate, landed_total, quote_date, quote_valid_until, stock_confirmation_date, lead_time_days, firmware, interface, mass_g, power_limits, datasheet_url, test_report_url, warranty, alternate_part, qualification_status, notes`

Use `unknown` for missing evidence. Do not convert a manufacturer's headquarters country into the component's country of origin.
