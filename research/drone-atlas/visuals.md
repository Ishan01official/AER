# Image, diagram and video reference catalog

**Access: 2026-10-05.** External media are linked only. Creator attribution does not automatically grant reuse permission. No footage was played in this research; no timecodes are invented. `unknown` means duration/date/license or timestamp was not established. Dataset: [media.csv](data/media.csv).

| ID / type | Original reference / creator | Caption and what it helps explain | Inspection and reuse status |
|---|---|---|---|
| V01 image | [Kettering Bug museum photo](https://www.nationalmuseum.af.mil/Upcoming/Photos/igphoto/2003357307/), National Museum of USAF; individual photographer not established | Museum **reproduction**; illustrates early fixed-wing form, not an original surviving operational vehicle | Search description; government-image restrictions/endorsement terms need checking; link only |
| V02 image/animation | [Ingenuity first flight](https://www.jpl.nasa.gov/images/pia24586-perseverances-navcam-view-of-ingenuitys-first-flight/), NASA/JPL-Caltech, 2021-04-19 | Navigation-camera view from Perseverance; establishes the observation context for the demonstration | Source page inspected; animation not played; consult JPL image policy before embedding |
| V03 video/source page | [RoboBee flies solo](https://wyss.harvard.edu/news/the-robobee-flies-solo/), Harvard Microrobotics Lab/Harvard SEAS, 2019-06-26 | Observe illumination, wing motion and laboratory setup; the written description records external lighting and lack of steering | Article inspected; linked video retrieval failed; timestamps unknown; rights not established |
| V04 technical diagram | [Crazyflie Rev G schematic](https://www.bitcraze.io/documentation/hardware/crazyflie_2_1_brushless/cf2.1_bl_schematics_Rev.G.pdf), Bitcraze | MCU, radio, sensing and ESC interface organization | Search-indexed diagram description only; full schematic audit/reuse terms pending |
| V05 video index | [DJI Mini 4 Pro tutorials](https://www.dji.com/mini-4-pro/video), DJI | Capture, handling and control workflow; no inference about internal chips | Page inspected; videos not played; individual dates/timestamps unknown; proprietary media |
| V06 report/figures | [GL-10 flight-test campaign](https://ntrs.nasa.gov/citations/20170007194), NASA Langley, 2017 | Tiltwing research, transition testing and experimental configuration | Report record found; figure-level inspection pending; work-of-US-government metadata does not waive all third-party figure checks |
| V07 technical diagrams | [PX4 controller diagrams](https://docs.px4.io/v1.16/en/flight_stack/controller_diagrams), PX4 contributors | Cascaded control and signal flow | Documentation retrieved; link only; check figure-specific reuse terms |
| V08 product/reference diagrams | [ST ESC reference design](https://www.st.com/en/evaluation-tools/steval-esc001v1.html), STMicroelectronics | Power stages, control and available schematics/BOM; use to plan a later board-design review | Product page inspected; not a physical teardown; document rights need checking |
| V09 manufacturing reference | [LionCircuits assembly](https://www.lioncircuits.com/pcb-assembly), LionCircuits | Assembly/inspection processes and local manufacturing-service evidence | Page inspected; no factory visit or photo provenance audit; link only |
| V10 platform brochure | [Wingtra specifications](https://wingtra.com/wp-content/uploads/Wingtra-Technical-Specifications.pdf), Wingtra, 2024-08 | Airframe/payload and mission-condition comparison | PDF text inspected; figure screenshots not analyzed; copyrighted brochure linked |

Original diagrams in [estimation](subsystems/state-estimation.md) and [supply chain](supply-chain/README.md) describe proposed/general relationships, not actual reverse-engineered hardware. No synthetic image is used as evidence.

## Next visual work

Inspect original video footage and record useful timestamps with the exact URL, publisher and date. Retrieve a rights-clear early aviation image, one original model-specific teardown and one manufacturing-lab reference. A teardown must identify the sampled model/revision and distinguish readable markings from inferred component identity. This release does not contain a verified teardown photograph or component-level DJI BOM.

## V11 — research demonstration video

[Champion-level Drone Racing using Deep Reinforcement Learning](https://www.youtube.com/watch?v=fBiataDpGIo), associated with the 2023 Swift research [R073](sources.md#r073), [R074](sources.md#r074). Landing page located; footage not played, uploader identity not verified in retrieved text, exact publication day and useful timecodes unknown. Link only; rights unverified. Use the written paper to distinguish race-time onboard sensing from development-time external measurements.
