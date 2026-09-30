<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Decision Record

## Decisions

- Treat the glass harp as a set of individual friction idiophones rather than a
  single fabricated structure.
- Keep pitch and tuning claims out of the first packet until real glasses are
  measured.
- Use water level as a future measured variable, not as a fabricated design
  table in this pass.
- Record every artifact as `concept_only` or `pending_measurement`.
- Do not create CAD, DXF, glass dimensions, fill-height tables, pitch maps, or
  tuning values in this pass.
- Uplift readiness to `L2 V5 build-packet candidate` because the packet now
  separates glass inventory, water-fill workflow, tray/support planning, BOM,
  cut-list, and repeatability gates.
- Add `cut-list.csv` as estimated tray, label, log, and storage families only;
  all sizes remain `TBD`.

## Alternatives Considered

- **CAD-first tray design:** rejected because glass count, glass spacing,
  damping, and spill behavior are unknown.
- **Pitch-map-first packet:** rejected until real dry and filled glass responses
  are measured.
- **Permanent fill marks:** deferred until a repeatable water-level workflow is
  proven.
- **Uniform glass set only:** kept as a possible branch, but not assumed; found
  or mixed glasses may be musically useful after measurement.
- **Publishing estimated water volumes:** rejected; all fill values remain
  pending measurement.

## Open Questions

- Which real glasses will define the first measured set?
- How will each glass be labeled without interfering with play or cleanup?
- What water-level recording method is repeatable enough for retuning?
- What table, tray, or fixture keeps glasses stable while preserving resonance?
- How will pitch drift be tracked during a playing session?
- What safety protocol handles cracks, chips, and breakage?
- What tray or pad material preserves sustain while preventing glass movement?
- How many drain/refill cycles are needed before a fill record is trusted?
- How should dry response and filled response be compared without implying a
  final scale?

## Promotion Gates

- L2 now provides the review scaffold; promotion beyond L2 requires a selected
  glass set, measured dry and filled response logs, and a repeatable
  fill-recording method.
- L3 requires reviewed setup authority and repeatable tuning/playability tests.
- L4 requires empirical session data, retuning notes, and documented revisions.
