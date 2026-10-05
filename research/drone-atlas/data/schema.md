# Dataset schema v1.0

All files UTF-8. CSV uses a header, comma separator, standard quoting and semicolon-separated multi-ID fields. Dates use ISO year, year-month or full date according to known precision. `unknown` in CSV and `null` in JSON mean **not established**, never zero, unsupported or nonexistent. Non-numeric comparison operators are stored separately. IDs are stable; do not recycle deleted IDs.

## sources.csv

One row per source document/page. `source_id` Rnnn; `title`, `publisher`, `url`; `publication_date` (known precision), `access_date`; `version`; `retrieval` enum `full_text`, `search_excerpt`, `failed`; `limitations`. “full_text” means page/document text was retrieved, not that every section was audited or that media were played. Notification date versus gazette publication is retained in version/limitations where needed.

## platforms.json

Top-level `schema_version`, `research_cutoff`, `null_meaning`, `platforms` array. Each platform has:

| Fields | Meaning / type |
|---|---|
| platform_id, manufacturer, model | Stable ID Pnn, organization and exact product/generation |
| country_of_organization, country_note | Organization context; not origin of chips/cells/factory; null if not established |
| introduction_date, availability | Dated event with context; availability text must not imply unverified stock |
| airframe, missions | Configuration string; list of mission labels |
| maturity | `announced`, `prototype`, `demonstrated`, `commercial`, `operational`; evidence state, not a universal ladder |
| dimensions_m | Object of named dimensions in m or null |
| takeoff_mass_kg | Object with `operator` (`=`, `<`, `<=`), `value` kg and `configuration`; not always maximum mass |
| payload_kg | Numeric kg or null; configuration caveats required |
| propulsion, energy_source | Text or null |
| endurance_s, speed_m_s | Numeric selected manufacturer observation or null; authoritative conditions in observations.csv |
| communication_range_m | Region-to-number object in m, or null; never interpreted as mission radius |
| navigation, sensors, onboard_computing, autonomy | Text, list or null; no inferred hidden silicon |
| payload_specification, environmental_limits, certifications | Text or null; product claim is not independently certified by AER |
| software_ecosystem, repairability, openness, dependencies | Text/list/null; no unsupported scores |
| price | Null until market/currency/date/configuration known; future object must contain those fields |
| independent_results | Null until independent protocol/source captured; absence is not failure |
| source_ids, checked_date, evidence, uncertainty | Source list, access date, evidence label and scope |

## observations.csv

One metric/configuration/condition per row. `observation_id`, `platform_id`, `metric`, `operator`, numeric `value`, `unit`, `configuration`, `test_conditions`, `evidence`, `source_ids`, `checked_date`.

Current allowed units: `s`, `m`, `kg`, `J`, `W`, `m/s`. Convert minutes to seconds, Wh to J (×3,600), g to kg (÷1,000). Exact arithmetic conversion does not increase measurement accuracy. Manufacturer-reported demonstrations remain M, not independent or AER measurements. Never replace multiple observations by a single “best” value without conditions.

## suppliers.csv

`supplier_id`, `name`, `role`, `categories`, `official_product_url`, `region_context`, `manufacturing_location`, `price`, `currency`, `market`, `price_date`, `moq`, `lead_time`, `documentation`, `certification_scope`, `support_traceability`, `alternative_constraint`, `source_ids`, `checked_date`, `evidence`.

Price is numeric text or `unknown`; a known price requires currency, market/configuration and date. MOQ may carry wording such as “1 listed”; it is not a negotiated quote. Certification scope is deliberately unverified unless certificate evidence is obtained. Alternatives are constraints rather than claims of drop-in equivalence.

## coverage.csv

`coverage_id`, `topic`, `depth`, `path`, `remaining_gap`, `source_ids`, `checked_date`. Paths resolve relative to atlas root. Depth: `open` (unresearched), `candidate` (reference identified), `partial` (some sourced analysis), `deep` (substantial guide/case and experiments). Deep never means complete or experimentally validated. Blank source IDs allowed only for open items.

## media.csv

`media_id`, `kind`, `url`, `creator`, `publication_date`, `caption`, `useful_timestamps`, `inspection`, `reuse_status`, `source_ids`, `access_date`. `unknown` timestamps are mandatory when footage has not been inspected; index/source-page URLs are labeled as such rather than passed off as direct video assets. No external media is redistributed in this release.

## Validation and evolution

The [validator](../tools/validate.py) checks parseability, IDs, source references, local links/anchors, coverage paths, numeric units, required price provenance and consistency between selected platform values and observations. It also checks example arithmetic. It does **not** validate scientific truth, current law, remote stock, all external URL status or media licenses. Breaking schema changes require a new schema version and migration notes.
