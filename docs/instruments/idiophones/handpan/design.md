# Handpan Root-Mode Design

## Intent

Build a D Kurd handpan research packet that gives Tony's shop a practical first shell, tuning workflow, procurement list, validation plan, and documentation bundle while staying honest about the core unknown: handpan pitch is not determined by a single spreadsheet dimension. The root deliverable is a prototype-planning packet for a tuner-led build, not a guarantee of final musical quality or a measured V5 build packet.

## Design Position

- Instrument: handpan / hang-style steel idiophone.
- Mode: root-mode packet at repo root.
- Scale: D Kurd, Ding plus eight tone fields.
- Target use: first controlled prototype, tuning practice shell, documentation baseline.
- Existing source artifact: `handpan-design-table.xlsx`, sheet `Handpan`.
- Governing model: coupled curved steel plate fields plus Helmholtz Gu cavity.
- Model confidence: low for final pitch, medium for rough geometric scale and Gu sanity checks.

## Starting Inputs From Workbook

| Parameter | Value | Status |
|---|---:|---|
| Shell outside diameter | 21 in / 533 mm | workbook input |
| Total shell height | 9.5 in / 241 mm | workbook input |
| Steel thickness | 1.0 mm | workbook input |
| Gu port diameter | 3.5 in / 89 mm | workbook input |
| Gu lip / neck depth | 0.5 in / 13 mm | workbook input |
| Tuning standard | A4 = 440 Hz | workbook input |
| Number of tone fields | 9 | workbook input |
| Material | nitrided DC04 preferred | workbook input |

The workbook estimates Gu frequency from a Helmholtz expression using a lenticular volume approximation. With the current inputs, the Gu estimate is about 115 Hz, near Bb2, before real shell volume, port edge shape, and air/loading effects are measured.

## Target Scale

| Field | Note | MIDI | Fundamental Hz | Octave Hz | Compound 5th Hz | Layout | First field size estimate |
|---|---:|---:|---:|---:|---:|---|---|
| Ding | D3 | 50 | 146.83 | 293.66 | 440.00 | center | formed convex dome, tuner-defined |
| Field 1 | A3 | 57 | 220.00 | 440.00 | 660.00 | lower left | 3.50 x 4.55 in oval estimate |
| Field 2 | Bb3 | 58 | 233.08 | 466.16 | 699.23 | lower right | 3.40 x 4.42 in oval estimate |
| Field 3 | C4 | 60 | 261.63 | 523.25 | 784.88 | mid left | 3.21 x 4.17 in oval estimate |
| Field 4 | D4 | 62 | 293.66 | 587.33 | 880.00 | mid right | 3.03 x 3.94 in oval estimate |
| Field 5 | E4 | 64 | 329.63 | 659.26 | 988.88 | upper left | 2.86 x 3.72 in oval estimate |
| Field 6 | F4 | 65 | 349.23 | 698.46 | 1047.69 | upper right | 2.78 x 3.61 in oval estimate |
| Field 7 | G4 | 67 | 392.00 | 784.00 | 1176.00 | top left | 2.62 x 3.41 in oval estimate |
| Field 8 | A4 | 69 | 440.00 | 880.00 | 1320.00 | top right | 2.47 x 3.22 in oval estimate |

Field sizes are only layout starters. They should be used to make removable templates and inspection overlays, not final machining drawings.

## Acoustic Model

The first-order plate sanity check is:

```text
f1 ~= (kappa / (2 pi)) * (h / a^2) * sqrt(E / (rho * (1 - nu^2)))
```

where `h` is sheet thickness, `a` is an effective tone-field radius, and `E`, `rho`, and `nu` are steel properties. For a real handpan this equation is incomplete because hammered curvature, residual stress, work-hardening, anisotropic stiffness, dimple shape, shell boundary conditions, and coupling to other fields all shift the modes.

The Gu sanity check is:

```text
fH = (c / (2 pi)) * sqrt(A / (V * Leff))
```

where `A` is the Gu area, `V` is enclosed shell volume, and `Leff` is the port neck with end correction. The Gu should be measured after the shells are joined, because the actual cavity volume and port edge are build-specific.

## Empirical Tuning Strategy

The prototype is accepted by measurement, not prediction:

1. Form or purchase matched shells and document diameter, height, thickness map, mass, and material certificate.
2. Mark the Ding and eight fields using removable templates from the table above.
3. Rough-form the Ding and fields, leaving pitch intentionally flat enough to allow upward tuning.
4. Record baseline impulse response for every field before final tuning.
5. Tune the Ding first, then the lowest surrounding field upward through the scale.
6. For each field, tune three partial targets: fundamental, octave, and compound fifth.
7. After each field is adjusted, remeasure all previously tuned fields for drift and cross-talk.
8. Join shells only after the top shell is stable enough to survive a 24-hour rest without large drift.
9. After glue cure, tune through the Gu, then repeat rest and retune cycles until drift is acceptable.

## Acceptance Targets

- Fundamental cents error: goal within +/-8 cents after final settle, stretch target +/-5 cents.
- Octave partial: goal within +/-12 cents relative to 2x fundamental.
- Compound fifth partial: goal within +/-15 cents relative to 3x fundamental.
- Sustain: record T60 or practical decay-to-noise time per field; flag fields that choke or ring excessively.
- Cross-talk: striking any field should not pull a neighbor louder than -18 dB relative to the struck field's fundamental unless musically intentional.
- Retuning drift: after a one-week rest, each fundamental should remain within +/-10 cents of its last accepted measurement.

## Deliberate Unknowns

- Final field geometry after tuning is TBD until measured.
- Hammer recipes are TBD and must be logged by the tuner.
- Heat treatment schedule is supplier/process dependent.
- Dimple geometry, shoulder shape, and tone-field isolation are measurement-required and must not be inferred from the starter SVG layout.
- Adhesive selection needs compatibility testing with shell finish and rim geometry.
- Public release status is TBD until IP, safety, supplier, and human tuning review are complete.

## Build Classification

This is a root-mode research packet. It is suitable for a controlled first prototype, quote requests, fixture planning, shop review, and build-log setup. It is not suitable as a public "make a guaranteed handpan" recipe. See `validation-loop.csv` for the measurement gates that must close before any stronger readiness claim.
