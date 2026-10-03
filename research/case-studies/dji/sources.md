# Sources, evidence and unresolved questions

**Research date:** 3 October 2026. Sources are linked for review; no external page content is copied wholesale.

## Evidence policy

- **Historical/company facts:** primary DJI material, identified as the company's account.
- **Product capabilities:** manufacturer or project documentation; advertised capability is not an AER validation result.
- **Suppliers:** manufacturer/service/retailer pages establish a shortlist, not a supplier audit or confirmed stock.
- **Engineering guidance:** original AER-oriented synthesis and proposals; calculations show their assumptions.
- **Regulation:** historical official text plus current portal guidance; the report does not claim complete consolidated October 2026 legal verification.
- **Budget/schedule:** planning estimates, not supplier quotes or promised delivery dates.

Public search results and direct page retrieval were used. A retrieved/crawled page is not evidence that every statement on it was recently updated. No supplier emails were sent, quotations obtained or parts ordered.

## Source registry

| ID | Source | Used for / limit |
|---|---|---|
| S01 | [DJI company overview](https://www.dji.com/company) | Company account of beginnings in 2006; promotional primary source. |
| S02 | [DJI: five common myths](https://viewpoints.dji.com/blog/busted-five-common-myths-about-dji) | Founder and university context; DJI's own account, not independent biography. |
| S03 | [DJI commercial drone ecosystem](https://enterprise.dji.com/news/detail/dji-enterprise-empowers-commercial-drone-industry) | Early components, integration and enterprise/partner strategy; historical account. |
| S04 | [Phantom announcement, 7 January 2013](https://www.dji.com/media-center/announcements/dji-launches-industry-best-easiest-to-fly-quadcopter-for-consumer-use) | Announcement date, GPS/Naza-M, GoPro mount and failsafe. |
| S05 | [DJI gimbal development](https://viewpoints.dji.com/blog/the-chase-gimbal-technology-and-the-endless-push-for-innovation) | Historical stabilization development; company narrative. |
| S06 | [Phantom 4 announcement](https://www.dji.com/media-center/announcements/dji-launches-new-era-of-intelligent-flying-cameras) | 2016 intelligent camera/obstacle-sensing product milestone. |
| S07 | [Mavic Pro announcement](https://www.dji.com/newsroom/news/dji-revolutionizes-personal-flight-with-new-mavic-pro-drone) | 27 September 2016 folding drone milestone. |
| S08 | [PX4 companion computer guide](https://docs.px4.io/main/en/companion_computer/) | Flight controller/companion boundaries and interfaces; main documentation can change. |
| S09 | [PX4 ROS 2 guide](https://docs.px4.io/main/en/ros2/) | ROS 2 integration; choose matched stable firmware/message versions for implementation. |
| S10 | [Holybro Pixhawk 6X](https://holybro.com/products/pixhawk-6x) | Manufacturer product candidate; exact board revision matters. |
| S11 | [CubePilot](https://www.cubepilot.org/) | Autopilot/module ecosystem; verify individual SKU and origin. |
| S12 | [T-MOTOR catalog and downloads](https://shop.tmotor.com/) | Matched propulsion candidates; also use https://uav-en.tmotor.com/download/42.html for model documentation. |
| S13 | [Hobbywing](https://www.hobbywing.com/) | Manufacturer propulsion catalog; no selected combination qualified. |
| S14 | [ST ESC reference design](https://www.st.com/en/evaluation-tools/steval-esc001v1.html) | Learning/development reference; not assumed flight-qualified for AER. |
| S15 | [TI TIDA-00643](https://www.ti.com/tool/TIDA-00643) | Brushless drone-propeller controller reference design. |
| S16 | [TI TIDA-00916](https://www.ti.com/tool/TIDA-00916) | Sensorless high-speed FOC reference design. |
| S17 | [TI TIDA-00982](https://www.ti.com/tool/TIDA-00982) | 2S battery-management learning reference. |
| S18 | [Molicel P45B datasheet](https://www.molicel.com/wp-content/uploads/INR21700P45B_1.4_Product-Data-Sheet-of-INR-21700-P45B-80109.pdf) | Exact cell reference; not an assembled AER pack specification. |
| S19 | [Grepow Tattu brand](https://www.grepow.com/brands/tattu.html) | Battery manufacturer/brand relationship and UAV product candidate. |
| S20 | [ST industrial drone components](https://www.st.com/en/applications/industrial-tools-motor-drives-and-equipment/drones.html) | MCUs, sensing, power and reference-platform portfolio. |
| S21 | [Bosch Sensortec](https://www.bosch-sensortec.com/en) | Sensor portfolio; no specific SKU chosen. |
| S22 | [TDK ICM-42688-P](https://www.invensense.tdk.com/en-us/products/6-axis/icm-42688-p) | Documented IMU device candidate. |
| S23 | [u-blox ZED-F9P](https://www.u-blox.com/en/product/zed-f9p-module) | RTK receiver module candidate; carrier/antenna/corrections separate. |
| S24 | [Vector Technics](https://www.vectortechnics.com/) | Vendor propulsion/local manufacturing claims; custom work, MOQ and lead time by quote. |
| S25 | [Reflex Drive](https://reflexdrive.in/) | Search-retrieved vendor description of motors/ESC design capability; direct page fetch failed. Treat as RFQ lead pending direct verification. |
| S26 | [Voltherm drone batteries](https://www.volthermtechnologies.com/products/drone-batteries) | Vendor India-made pack claims; cell origin and certification scope unverified. |
| S27 | [e-con UAV cameras](https://www.e-consystems.com/markets/industrial-cameras/uav-drone-camera-solutions.asp) | OEM camera/module and integration candidate; no exact SKU qualified. |
| S28 | [Arducam](https://www.arducam.com/) | Embedded camera/module catalog. |
| S29 | [Sony global-shutter sensors](https://www.sony-semicon.com/en/products/is/industry/global-shutter.html) | Sensor technology/portfolio; not a turnkey drone camera. |
| S30 | [SIYI gimbals and integration](https://siyi.biz/en/category/gimbals/) | Catalog; SDK documentation also at https://siyi.biz/siyi_file/A2%20mini/A2%20mini%20User%20Manual%20EN%20v1.1.pdf . |
| S31 | [Benewake](https://www.benewake.com/) | Range/lidar catalog; model limits require datasheet. |
| S32 | [NVIDIA Jetson Orin](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/) | Companion compute portfolio; no performance estimate treated as measured. |
| S33 | [RadioMaster receivers](https://radiomasterrc.com/collections/elrs-receivers) | Control hardware candidate; listing does not establish Indian RF compliance. |
| S34 | [DJI developer documentation](https://developer.dji.com/document/) | SDK entry point; exact compatibility must be checked. Historical OSDK introduction: https://developer.dji.com/onboard-sdk/documentation/introduction/onboard-sdk-introduction.html . |
| S35 | [LionCircuits PCBA](https://www.lioncircuits.com/pcb-assembly) | India-based fabrication/assembly service candidate. |
| S36 | [PCB Power company/services](https://www.pcbpower.com/page/about-us) | Indian electronics manufacturing service candidate. |
| S37 | [Robu drone category](https://robu.in/product-category/drone-parts/) | Retail sourcing channel, not evidence of manufacture. |
| S38 | [Robocraze T-MOTOR category](https://robocraze.com/pages/t-motor) | Retail channel; vendor authenticity claims need order-specific confirmation. |
| S39 | [Albatross Microsystems](https://albatrossmicrosystems.com/) | India-based component shop; listed products may be imported. |
| S40 | [Mouser India](https://www.mouser.in/) | Component distributor; verify selected manufacturer's authorization/stock. |
| S41 | [DigiKey India](https://www.digikey.in/) | Component distributor; shipment-specific fulfillment/import details vary. |
| S42 | [element14 India](https://in.element14.com/) | Component distribution channel. |
| S43 | [Official drone import notification, 9 February 2022](https://www.civilaviation.gov.in/sites/default/files/migration/Drone_Import_Policy_9_Feb_2022.pdf) | DGFT Notification 54/2015-20, pp. 0–1: CBU/CKD/SKD restrictions/exceptions and components Free. Historical primary text; check current schedule. |
| S44 | [PIB summary of Drone Rules, 26 August 2021](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1749154&lang=2&reg=48) | R&D and other regulatory summary; not consolidated current legal text. |
| S45 | [DoT ETA portal](https://eservices.dot.gov.in/equipment-type-approval-eta) | Wireless equipment approval guidance; determine device-specific applicability. |
| S46 | [DTPC DH ESC](https://www.dtpc.in/dh-esc) | Legacy vendor product/specification page; active production and current price not confirmed. |
| S47 | [APC propellers](https://www.apcprop.com/) | Propeller catalog; consult technical information and RPM limits for exact model. |
| S48 | [JLCPCB assembly](https://jlcpcb.com/pcb-assembly) | Contract fabrication/assembly service; AER qualification remains separate. |
| S49 | [onsemi drone image sensors](https://www.onsemi.com/design/interactive-block-diagrams/industrial/drone/image-sensors) | Bare image-sensor portfolio and camera-development resources. |
| S50 | [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) | General-purpose companion option; no aircraft integration qualified. |
| S51 | [QGroundControl](https://qgroundcontrol.com/) | Ground-station starting point; exact version/platform support to be checked. |
| S52 | [ArduPilot](https://ardupilot.org/) | Alternative autopilot ecosystem; choose one baseline stack. |
| S53 | [Silicon Labs wireless](https://www.silabs.com/wireless) | Wireless IC/platform portfolio, not a ready-made UAV video system. |
| S54 | [PX4 simulation guide](https://docs.px4.io/main/en/simulation/index) | SITL/HITL and simulation/failure-testing starting point. |
| S55 | [MoCA final Drone Rules entry](https://www.civilaviation.gov.in/ministry-documents/rules/drones-rules-2021-dated-25-august-2021) | Official final-rule entry. Linked gazette PDF failed retrieval in this session; do not substitute draft rules. |
| S56 | [PIB airspace map announcement](https://www.pib.gov.in/newsite/PrintRelease.aspx?lang=2&reg=48&relid=225084) | Historical map guidance; live site/airspace must be checked before operations. |

## Specific limitations

1. No complete DJI internal BOM or current supplier roster was established. The directory is for AER sourcing.
2. No current DJI audited revenue, exact global market share or startup capitalization was verified; these are omitted.
3. Hardware changes across model/revision are material; generic brand names cannot prove compatibility.
4. “Made in India” statements above are vendor claims. Chip/cell origin and local value addition require SKU evidence.
5. Retail catalog access does not prove stock, price, authorization or shipment acceptance.
6. The final 2021 rules entry was found, but its linked gazette PDF failed direct retrieval. Regulatory text here is limited to successfully retrieved official summaries and import notification.
7. Search attempts to verify all subsequent regulatory amendments were inconclusive. Obtain the current official rules/schedule and device-specific applicability before shipment or flight.
8. No supplier was evaluated through samples, factory audit or independent test reports.
9. No proposed budget, mass, power, endurance or schedule is measured AER performance.

## Update triggers

Revisit this study when:
- AER selects a mission, aircraft mass/payload and operating location.
- A specific BOM, board revision and firmware release are chosen.
- Written quotations or supplier test data arrive.
- Bench/flight measurements replace planning assumptions.
- Import, airspace or radio requirements change.
- Customer requirements justify custom hardware or product certification.

For an update, record the changed claim, new evidence, date and resulting AER decision.
