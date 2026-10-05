# Research plan and evidence method

Cutoff/access date: **2026-10-05**. Baseline inspected: `21756ec8ce96769e3820bb0a4ff37f37198a7b7d` on `main`. README, research README, roadmap, architecture, DJI study and its source register were read. No AGENTS.md or contribution policy was found in the checked-out repository. Existing research is retained; its linked sources are not automatically treated as reverified.

## Repository-aware delivery

| Batch | Concrete contribution | Verification gate |
|---|---|---|
| 1 — foundations | Method, schemas, taxonomy, historical analysis, three platform/ecosystem studies, estimation guide, staged civilian path and phone MVP | Local links; IDs and units; claim/source association; diff scope |
| 2 — engineering and dependencies | Propulsion calculations, every-subsystem map, supplier roles, Indian regulatory evidence, challenges and visual catalog | Recompute examples; supplier provenance; unknowns retained; source retrieval status |
| 3 — next priority | Model-specific Indian platforms, current regulatory consolidation, independent endurance tests, patents and original teardowns | Complete primary documents; board/version evidence; permissions and test conditions |
| Later increments | Deepen one airframe class or subsystem at a time; add measured AER outcomes | Versioned experiment, raw-data location/hash, evaluation method, repeatability |

No unattended research schedule is created by this document. It defines how later work can extend this library without resetting it.

## Evidence labels

- **F — established/documented fact:** the narrow fact is supported by a primary institutional record; this does not validate all associated claims.
- **M — manufacturer/project claim:** a specification, self-reported test, development history or availability statement. A specification sheet is not independent measurement.
- **E — estimate:** planning allowance or calculation with assumptions; not a quotation.
- **I — engineering inference:** a derived consequence, decision or proposed experiment, explicitly distinguishable from what the source says.
- **S — scenario:** conditional forecast, with horizon and confidence.
- **A — AER measurement:** reserved for experiments actually run. There are no A records in this release.

A source ID resolves through [sources](sources.md). Keep citations next to the relevant table row or paragraph. A source documenting a sensor interface cannot support a claim about a complete aircraft's reliability. Important historical firsts need separate corroboration; unresolved priority disputes remain open. Supplier pages verify a product claim exists, not stock, provenance, certification or quality.

## Extraction rules

Record event date separately from announcement/publication/access dates. Record the product revision, payload, battery, firmware, region and measurement protocol. Never merge a later payload into an earlier base-aircraft specification. Prefer explicit `unknown`/null and a question over inferred numbers. Keep original units in notes when conversion is material; SI comparison values are numeric. Do not turn optical-format labels such as “1/1.3-inch type” into a literal sensor diagonal.

For contradictory sources retain both observations, dates and conditions, then state what would resolve them. Example: a payload-specific flight-time table can differ from a headline maximum without contradiction. A payload mass larger than the same brochure's capacity is unresolved until the manufacturer explains configuration applicability.

## Research workflow

1. Search primary sources by class and claim, then inspect the actual document where possible.
2. Capture source metadata, retrieval depth and the narrow evidence obtained. A search snippet alone is a lead for detailed engineering.
3. Add platform records separately from numeric observations, so multiple test conditions can coexist.
4. Write physical explanation, comparisons and AER implications in original language; link figures rather than redistribute unclear-license assets.
5. Update the coverage matrix and open questions. Mark announced, prototype, demonstrated, commercial and operational evidence separately from current market availability.
6. Run the validator, review the diff, commit a coherent increment, push without force and read back the remote branch hash.

## Limits of this release

No supplier outreach, price quotations, factory audits, hardware teardowns, actual video playback, aircraft flights or software-stack reproduction were performed. External pages retrieved through browsing were checked for supporting content, not certified as permanently live URLs. Latest fleet inventory, market share, a complete 2026 release sweep, patent freedom-to-operate and consolidated legal clearance remain unverified. These are visible coverage gaps, not omitted qualifiers.
