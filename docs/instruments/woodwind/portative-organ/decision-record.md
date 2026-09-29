<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Decision Record

## qmd Step 0

- `timeout 30 qmd query "portative organ medieval flue pipe windchest bellows pallet key slider rank"` started, expanded lexical/vector searches, reranked chunks, and timed out before returning usable context.
- `qmd search "organ" -c instrument-builds` returned generic instrument-maker golden-example and vessel-flute packet references, not portative-organ-specific mechanics.
- Round 7 uplift qmd Step 0: `qmd search "portative-organ" -c instrument-builds` returned `No results found`; `qmd query "portative organ small portable pipe organ hand-pumped bellows one hand keyboard pipes windchest pallet valves wind pressure regulator"` searched and reranked chunks, then Bun/node-llama-cpp crashed before returning usable context.
- Result: this packet uses the lane contract and established portative-organ mechanism knowledge as its grounding source, with all physical details held at concept or pending-measurement status.

## Family Placement

The repo is placed at `instruments/woodwind/portative-organ` as instructed. A portative organ is more precisely a keyed flue-pipe aerophone, but the current workspace taxonomy groups air-column/flue-pipe work under `woodwind` for this lane.

## Key Decisions

- Start with a single-hand bellows feeding a reservoir, then a windchest.
- Use key-operated pallet valves as the core action.
- Treat flue pipes, pipe feet, mouths, languids, and voicing as conceptual until a pipe-scale study and mule exist.
- Prefer a single rank for the first proof of mechanism, with a second rank only as a future expansion option.
- Keep the case portable by design, but defer strap, lap, and table-support geometry until handling tests.
- Uplift readiness to `L2 V5 build-packet candidate` because the packet now separates wind-system, windchest, keyboard, pipe-rank, case, BOM, and cut-list review questions.
- Add `cut-list.csv` as blank-family planning only; it contains no released sizes.

## Alternatives Considered

- **Pipe-rank-first design:** rejected for this uplift because wind stability and pallet sealing should be proven before pipe scaling is treated as meaningful.
- **Two-rank first prototype:** deferred because it increases wind demand and windchest complexity before one rank is understood.
- **Direct bellows-to-pipe path:** rejected as the primary L2 path because a reservoir is the review mechanism for smoothing player pump pulses.
- **Decorative case-first work:** deferred until handling, support mode, and pipe protection questions are measured.
- **Publishing pipe lengths or wind pressure estimates:** rejected; these remain pending measurement.

## Open Questions

- Which support mode is most playable: strap-supported, lap-supported, table-supported, or a hybrid?
- How much wind smoothing is needed before key attack feels musical?
- What pallet material and return strategy gives quiet sealing without heavy touch?
- Should the first rank use open pipes, stopped pipes, or a mixed proof set?
- What measurements should define promotion from L1 concept to L2 build-packet candidate?
- What wind-system mule should isolate bellows cadence, reservoir behavior, pallet leakage, and key attack?
- How should case support be tested without distorting the windchest?
- Which service panels are necessary for pallet and gasket inspection?
- What evidence is required before a pipe-scale table can be added?

## Authority Boundary

No dimensions, pipe lengths, tuning values, wind-pressure values, CAD geometry, DXF coordinates, or measured performance claims are made in this repo. Promotion beyond L2 requires measured wind-system behavior, pipe-scale research, ergonomic mockup evidence, and reviewed design tables.
