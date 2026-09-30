# Risks

## Executive Summary

This packet should be treated as private research documentation until a human handpan tuner, metal-forming reviewer, and safety/IP reviewer have signed off. The design is buildable as a disciplined prototype packet, but it is not a guaranteed path to a finished instrument.

## Metal Forming Hazards

- Thin steel shells can crack, crease, buckle, or oil-can under forming and tuning impacts.
- Hammering creates flying chips, rebound hazards, high sound levels, and repetitive strain risk.
- Sharp Gu and rim edges can cut the builder or player if not fully deburred/protected.
- Torch or heat-treatment work creates burn, fire, fume, oxidation, and distortion hazards.
- Clamping a curved shell under stress can release suddenly or dent the shell.

Mitigation: PPE, hearing protection, smooth hammer faces, deburred edges, stable fixtures, scrap practice, fire-safe setup, and stop-work criteria for cracks or uncontrolled deformation.

## Heat And Work-Hardening Assumptions

- The packet assumes nitrided DC04 as a first controlled material path, but actual supplier shells may have different forming history, hardness, and residual stress.
- Nitriding or other heat treatment can change shell stiffness, surface hardness, corrosion behavior, and tuning stability.
- Work-hardening from hammering is not represented by the first-order plate equation.
- Heat applied after rough tuning can move pitch or relax stresses unpredictably.

Mitigation: request material/process data, perform coupon tests, record hardness/process information where possible, and never mix stainless and nitrided assumptions in one measurement set.

## Tuning Repeatability

- Tone fields are dominated by hand-shaped curvature, dimple geometry, local stress, and coupling to neighboring fields.
- The same nominal oval dimensions can produce different pitches on different shells.
- Tuning one field can detune fields already completed.
- Shell closure, adhesive cure, settling time, and transport can move pitch.
- The 1:2:3 partial relationship may not be reachable on a first shell without expert hammer technique.

Mitigation: tune iteratively, record every pass, measure all prior fields after each change, and plan multiple settle/retune cycles.

## Acoustic Model Risk

- Plate and Helmholtz equations are sanity checks only.
- The shell is a coupled curved structure, not an isolated flat plate.
- Gu predictions depend on actual volume, port shape, edge treatment, and assembled-shell leakage.
- FEM without measured material/stress calibration can look authoritative while being wrong.

Mitigation: label formulas as first-order, use measured cents error as the authority, and back-fit models only after prototype data exists.

## Manufacturing Limits

- First-time hand sinking is unlikely to produce consistent shells for a musical prototype.
- Purchased shells may still vary enough to require packet updates.
- CNC can make fixtures and templates, but cannot cut final pitch into a handpan field.
- Adhesive choice and rim compression can alter shell response.

Mitigation: buy or professionally form shells for the first prototype, keep CNC scope to fixtures/templates, and run adhesive coupons before closure.

## IP And Public Release Review

- The handpan family has a sensitive maker history, brand/trade-name distinctions, and technique knowledge that may not be appropriate to publish as a definitive recipe.
- Supplier photos, proprietary shell dimensions, tuner methods, and heat-treatment details may be copyrighted, confidential, or trade-secret-like.
- Public claims that the packet teaches finished handpan tuning could mislead builders.

Mitigation: keep the repo private until reviewed, avoid brand confusion, cite sources sparingly, use original measurements, and publish only as a research/build-log packet with clear uncertainty labels.

## Specialist Boundary

- Tone-field forming, partial balancing, and drift control are specialist handpan-maker work.
- CAD, CNC, SVG drawings, and workbook estimates in this repo are allowed to define fixtures, templates, measurement points, and documentation, but not final tuned field geometry.
- If an experienced tuner changes the field order, hammer approach, material path, Gu detail, or acceptance targets, the packet should be revised before any public release.

Mitigation: route the packet through `public-release-checklist.md`, preserve the tuning log, and treat specialist feedback as design data rather than commentary.

## Difference Between This Packet And A Guaranteed Instrument

This packet provides: procurement specs, layout geometry, first-order physics, build order, validation gates, drawing briefs, and documentation scaffolding.

It does not provide: a proven hammer recipe, final tone-field contours, supplier-verified process windows, calibrated FEM, measured prototype corrections, or assurance that the first build will be musically acceptable.

## Red-Team Verdict

Proceed only as a controlled prototype. Keep private until human review, measured tuning evidence, supplier/process evidence, and public-claims review exist.
