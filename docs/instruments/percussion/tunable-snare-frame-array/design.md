<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Tunable Snare Frame Array — Design

## Design Position

| Field | Value |
|-------|-------|
| Instrument class | Frame drum array · membranophone |
| Scale / pitch set | D3 (147 Hz) · A3 (220 Hz) · D4 (294 Hz) |
| Governing model | Circular tensioned membrane — Bessel mode (0,1) |
| Build readiness | L0 — design packet only, no prototype |
| Confidence | Medium on geometry; low on absolute pitch until prototype |

---

## Starting Inputs

| Parameter | Drum A | Drum B | Drum C | Source |
|-----------|--------|--------|--------|--------|
| Shell OD (nominal) | 250 mm | 200 mm | 150 mm | Design intent |
| Shell OD (standard head) | 254 mm (10″) | 203 mm (8″) | 152 mm (6″) | Remo Ambassador catalog |
| Shell depth | 60 mm | 50 mm | 40 mm | Proportional to OD |
| Shell material | 1.0 mm CRS | 1.0 mm CRS | 1.0 mm CRS | Maker Nexus stock |
| Head type | Remo Ambassador | Remo Ambassador | Remo Ambassador | Bought |
| Snare wire count | 12 strand | 10 strand | 8 strand | Scaled to head area |
| Target fundamental | D3 = 146.8 Hz | A3 = 220.0 Hz | D4 = 293.7 Hz | Musical target |

---

## Acoustic Model — Circular Membrane

The fundamental frequency of a circular tensioned membrane (mode 0,1) is:

```
f₀₁ = (α₀₁ / (2π·r)) · √(T/σ)
```

Where:
- `α₀₁ = 2.4048` — first zero of Bessel function J₀
- `r` — head radius (m)
- `T` — membrane tension per unit length (N/m)
- `σ` — membrane area density (kg/m²)

**Remo Ambassador head** (bought): σ ≈ 0.18 kg/m² (typical Mylar head). Tension is set by lug hardware; practical range T ≈ 500–2500 N/m.

Predicted frequencies at nominal tension T = 1200 N/m:

| Drum | r (m) | f₀₁ predicted | Target | Delta |
|------|--------|--------------|--------|-------|
| A (10″) | 0.127 | 143 Hz | D3 147 Hz | −27 cents |
| B (8″) | 0.0965 | 189 Hz | A3 220 Hz | −260 cents |
| C (6″) | 0.076 | 240 Hz | D4 294 Hz | −350 cents |

The large negative deltas at T=1200 N/m show that target pitches require higher tensions (1600–2800 N/m) — well within the Remo Ambassador spec (~3000 N/m burst). `tunable-snare-frame-array-starter.wl` solves for required tension at each target. See `validation.csv` for refined predicted values.

---

## Intonation Strategy

Each drum is independently tensioned via 4-lug (6″) or 6-lug (8″, 10″) hardware. Tuning procedure:
1. Seat head, finger-tighten all lugs evenly.
2. Use drum key, 90° turns opposite-lug pattern (clock method) to raise pitch.
3. Tap near each lug — equalize pitch around circumference before striking center.
4. Verify center fundamental with chromatic tuner.
5. Mark lug rod extension at target pitch for repeatability.

Snare wire: thumb-wheel mechanism per drum. Disengage for clear membrane tone; engage for characteristic buzz. Snare wire tuning does not change membrane pitch.

---

## Frame Geometry

Shared mounting bracket: 1.5 mm CRS flat plate, 450 mm × 80 mm overall, with three circular cut-outs (⌀250 + OD clearance, ⌀200 + clearance, ⌀150 + clearance) plus 90° flanged edges top and bottom (20 mm flange for stiffness). Drums clip into the cut-outs via 4 radial bolts each through stand-off ears welded to the shell OD.

---

## Acceptance Targets

| Metric | Target | Method |
|--------|--------|--------|
| Center fundamental | ±50 cents of D3/A3/D4 | Chromatic tuner, center strike |
| Head evenness | All 4/6 lug positions ±10 cents | Tap near each lug |
| Snare disengage | No rattle after release | Thumb-wheel test |
| Frame rigidity | No drum movement under strike | Hold frame, strike hard |
| Cross-talk | Adjacent drum resonance < −12 dB | Strike one, measure others |

---

## Deliberate Unknowns

- Real σ of bought Remo heads (nominal 0.18 kg/m²; actual varies by batch).
- Effective r: drum head seat diameter ≈ OD − 3 mm (head rim seating); use in wolfram model.
- Bearing edge geometry on rolled steel shell (standard 45° chamfer vs. rounded).
- Snare wire buzz threshold tension — empirical only.

---

## Build Classification

`L0_blueprint` — design packet, no prototype. Fabricator can start cutting blanks; acoustic targets are first-order estimates requiring head-tensioning iteration on first build.
