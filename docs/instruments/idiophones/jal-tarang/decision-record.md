<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Decision Record

## Decisions

- Readiness is `L2 concept / pending-measurement packet`; this repo is not a
  shop packet.
- Treat the jal tarang as a tuned vessel idiophone where water-volume
  repeatability is the central engineering problem.
- Keep bowl material open: porcelain, ceramic, glass, and metal remain
  candidate branches until real bowls are measured.
- Add a cut-list as candidate test/setup classes only, with all quantities,
  sizes, pitch targets, and water states still pending measurement.
- Separate bowl inventory, fill workflow, pitch logging, mallet trials, support
  behavior, and session drift as independent evidence streams.
- Do not create CAD, DXF, tuning tables, water-volume tables, pitch targets,
  acoustic predictions, or mallet specifications in this round.
- Keep every artifact authority at `concept_only` or `pending_measurement`.

## Alternatives Considered

- **Final scale first:** rejected because measured bowl response and performer
  context should govern any future scale choice.
- **Permanent water-level marks now:** rejected because labels could imply
  tuning authority before repeatability data exists.
- **One support tray design now:** deferred until bowl size, material, and
  resonance behavior are observed.
- **Mallet specification now:** deferred until rim safety and attack tests exist.
- **CAD tray layout now:** rejected because no bowl inventory or support
  geometry has measured authority.

## Open Questions

- Which reference tradition, repertoire, or performer setup should anchor the
  next packet?
- Should the first study use a graduated found-bowl set or a more uniform bowl
  family?
- How should water volume be measured so tuning is repeatable after draining
  and refilling?
- What mallet material gives clear attack without damaging bowl rims?
- What support surface keeps bowls stable without damping them too much?
- How should labels show bowl ID and fill state without implying final tuning?
- How much evaporation or handling drift matters during a practice session?
- What bowl condition notes are needed before deciding whether a candidate bowl
  is usable?
- How should a measured fill state be reset after transport or rehearsal?
- What evidence distinguishes true tuning drift from measurement-room or
  striking variability?

## Promotion Gates

- L2 records subsystem intent, candidate part classes, and pending measurement
  gates only; it does not authorize fabrication or performance setup.
- L3 requires measured bowl dimensions or reviewed drawings plus measured
  pitch-versus-water data and validated support behavior.
- L4 requires physical setup logs, repeatability tests, player feedback, and
  documented tuning drift over time.

## V5 Refresh Pass (2026-07-01)

- Normalized the README status line to the approved V5 value
  `L2 V5 build-packet candidate`, keeping the original
  `L2 concept / pending-measurement packet` caveat prose alongside it — no
  promotion of readiness level.
- Added the missing baseline files (`risks.md`, `sourcing.csv`,
  `validation.csv`, `drawing-brief.md`) and `evolution/` Stage 0 intake,
  scaffolded honestly with TBD/measurement_required values — no new bowl
  dimensions, counts, or pitch data were introduced.
- **Deliberately did NOT author a `cad/*.scad` master this pass.** This
  repo's own Decisions (above) explicitly reject creating CAD before bowl
  inventory/geometry is measured, and no bowl count, diameter, wall profile,
  or water volume exists anywhere in this packet to parameterize a model
  from — the only numeric bowl-related value in the repo is
  `bowlCountEstimate = 12` in `wolfram/jal-tarang-wolfram-model.wl`, itself
  labeled "estimate — pending measurement, not fabrication authority." Adding
  geometry (even an "envelope") would require inventing a bowl diameter that
  does not exist anywhere in this packet, which conflicts with the V5 honesty
  rule against inventing dimensions. Escalated to the orchestrator for
  confirmation rather than fabricating a placeholder dimension.
