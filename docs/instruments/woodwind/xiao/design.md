# Xiao Family — Design Document

**Instrument:** Xiao (箫) — Chinese end-blown vertical bamboo flute  
**Family variants:** Bei Xiao (北箫) · Nan Xiao (南箫) · Qin Xiao (琴箫)  
**Scale:** 8-hole chromatic  
**Build ID:** XIAO-001  
**Packet version:** v4.3 root-mode  
**Date:** 2026-05-08  
**Status:** First-order acoustic model. Tuning claims are estimates until prototype measured.

---

## 1. Design Intent

The xiao is one of the oldest Chinese wind instruments — an end-blown, notched-embouchure flute with a characteristically dark, breathy tone. This design packet targets a **G Nan Xiao** (root D4, bore ≈ 0.866 in / 22 mm) as the prototype instrument, with the parametric design table covering 26 keys and all three bore variants. The priority challenges are:

- Long-bore cylindrical drilling (≥ 22 in) without wander
- Accurate tone-hole placement from a first-order acoustic model, with tuning trim allowance baked in
- Embouchure geometry (U-notch vs V-notch) and its effect on attack, intonation, and octave response
- End corrections: both ends treated as open terminations (first-order); embouchure end correction is an assumption pending prototype measurement

CNC production is intended for wooden prototypes; bamboo and lacquered-bore variants are noted as material alternatives.

---

## 2. Governing Acoustic Model

### 2.1 Model choice

The xiao is an **open-open cylindrical pipe** (open at embouchure end, open at foot). Use the open-open pipe model:

```
f = c / (2 · L_eff)
L_eff = c / (2 · f)
```

- `c` = speed of sound = 331.3 × √(1 + T_C / 273.15) m/s  
  At 68°F (20°C): **c = 343.0 m/s = 13,504 in/s**

**Do not apply NAF K2 corrections here.** Those corrections are derived from Tony's NAF bore-diameter data and do not apply to the xiao's different bore range, embouchure geometry, or playing technique. Mark all first-order predictions as estimates; add measured corrections to validation.csv after prototype testing.

### 2.2 End corrections

Each open termination adds approximately 0.6 × radius to the effective acoustic length:

```
δ_end ≈ 0.6 · r    (Levine-Schwinger approximation)
```

For an open-open pipe with two open ends:

```
L_eff = L_bore + 2 · δ_end = L_bore + 1.2 · r
```

**Embouchure-end assumption:** The U-notch embouchure is treated as an open end in this first-order model (δ_emb ≈ 0.6·r). In practice, the notch geometry, player lip coverage, and jet angle all modulate the effective length. Expect the embouchure end correction to require empirical refinement on the prototype. Flag this row in validation.csv.

**Foot-end correction:** Standard open-end correction applies at the foot (δ_foot = 0.6·r).

### 2.3 Prototype target — G Nan Xiao

| Parameter | Value | Source |
|---|---|---|
| Xiao key name | G (四孔 = G4) | Naming convention: 4th hole |
| Root note (all holes closed) | D4 | Key − 5 semitones |
| Root frequency | 293.66 Hz | f = 440 × 2^((62−69)/12) |
| Speed of sound | 13,504 in/s | 68°F, 0% RH (shop estimate) |
| **L_eff (acoustic length)** | **22.99 in** | c / (2 · 293.66) |
| Bore ID | 0.866 in | Nan Xiao design table |
| Bore radius | 0.433 in | Bore ID / 2 |
| End correction (each end) | 0.260 in | 0.6 × 0.433 |
| Total end correction | 0.520 in | 2 × δ_end |
| **L_bore (physical bore)** | **22.47 in** | L_eff − 0.520 |
| Wall thickness | 0.236 in | Design table |
| OD (bore + 2·wall) | 1.338 in | Bore + 2 × wall |
| Mouthpiece section length | 2.5 in | Design table (Nan Xiao) |
| **Total blank length** | **~25.5 in** | L_bore + mouthpiece + trim |

> **⚠ FIRST-ORDER ESTIMATE.** L_bore = 22.47 in is the model prediction with assumed end corrections. Add +0.25 in trim allowance to the blank. Final length determined by tuning measurement on the prototype.

### 2.4 Tone-hole placement (first-order)

Acoustic length method (open-open pipe, Benade first-order approximation):

```
d_from_foot(hole_n) = L_eff × (f_root / f_hole_n)
```

This gives the distance from the foot-end opening to where each tone hole's center should ideally be placed for a lossless open termination at that hole. Real-world corrections for finite hole size, undercutting, and adjacent-hole interaction are applied empirically during voicing.

**G Nan Xiao — 8 tone holes (first-order):**

| Hole | Finger | Note | MIDI | Freq (Hz) | Dist from foot (in) | Dist from foot (mm) |
|---|---|---|---|---|---|---|
| 1 | RH pinky | E4 | 64 | 329.63 | 20.48 | 520 |
| 2 | RH ring | F4 | 65 | 349.23 | 19.33 | 491 |
| 3 | RH middle | Gb4 | 66 | 369.99 | 18.25 | 464 |
| 4 | RH index | G4 | 67 | 392.00 | 17.22 | 437 |
| 5 | LH ring | A4 | 69 | 440.00 | 15.34 | 390 |
| 6 | LH middle | B4 | 71 | 493.88 | 13.67 | 347 |
| 7 | LH index | C5 | 72 | 523.25 | 12.90 | 328 |
| 8 | LH thumb | Db5 | 73 | 554.37 | 12.18 | 309 |

> **⚠ FIRST-ORDER ONLY.** These distances will shift in practice. Drill holes 1–2 mm closer to the foot than predicted (under-length tuning margin), then reposition by undercutting. Do not finalize positions without prototype measurement.

### 2.5 Scale offsets (xiao 8-hole chromatic)

From acoustic-models.md — verified against design table:

```
+2, +3, +4, +5, +7, +9, +10, +11 semitones from root
```

Notes +1, +6, +8 require cross-fingering or half-holing. Second octave by overblowing (overblow ratio ≈ 2:1 for cylindrical open pipe).

### 2.6 Naming convention

> **"G xiao"** means hole 4 produces G. Root (all holes closed) = G − 5 semitones = D.  
> Design table column: Root Note = D4 → Xiao Key Name = G4.

---

## 3. Bore Variants

Three bore families are covered in the design table. Prototype is **Nan Xiao**.

| Variant | Bore type | Bore ID range | Wall | Mouthpiece | Character |
|---|---|---|---|---|---|
| Bei Xiao (北箫) | Capped U-notch | 0.472–0.787 in | Proportional | 2.0 in | Northern; fuller tone, larger bore |
| Nan Xiao (南箫) | Open (bamboo root end) | 0.630–0.984 in | Proportional | 2.5 in | Southern; warm, breathy; most common |
| Qin Xiao (琴箫) | Capped U-notch (narrow) | 0.315–0.630 in | Proportional | 3.0 in | Narrow bore; refined tone for guqin pairing |

Blank width/thickness cells are marked TBD in the design table — to be filled once stock form (round rod, split-blank, or bamboo) is confirmed.

---

## 4. Material Assumptions

| Parameter | Prototype | Note |
|---|---|---|
| Body material | Black walnut or cherry | CNC-machinable hardwood. Bamboo (madake/zizhu) for traditional build |
| Bore treatment | TBD | Linseed oil, lacquer, or shellac; internal lacquer stabilizes bore and affects tuning |
| Stock form | Round rod or split-blank | See jig-decision.md for drilling method selection |
| Finish | Natural oil + wax | Avoid thick varnish on bore |

---

## 5. Key Assumptions & Open Questions

| Item | Assumption | Status |
|---|---|---|
| Embouchure end correction | 0.6·r (same as foot) | **TBD — measure on prototype** |
| Bore taper | Zero (cylindrical) | Bamboo is slightly tapered; wooden version is truly cylindrical |
| Hole diameter | TBD (traditional: ~8–10 mm for front holes) | Affects cutoff frequency and playability |
| Hole undercutting | TBD | Cross-cut and undercut during voicing |
| Internal lacquer effect | Assumed negligible | Lacquer shifts effective bore diameter; validate |
| Temperature at play | 68°F / 20°C | Tune at 68°F; note 1 cent/°F sensitivity |
| Breath pressure | Assumed constant | Overblowing model: pressure ratio ≈ 4:1 to 6:1 for second octave |

---

## 6. Parametric Formulas

All formulas should be reproduced parametrically in `xiao-design-table.xlsx`:

```
c = 13504 * SQRT(1 + T_F/491.67)          " in/s, T_F in Fahrenheit
f_root = 440 * 2^((MIDI_root - 69) / 12)  " root frequency
L_eff = c / (2 * f_root)                   " acoustic length, in
delta_end = 0.6 * (bore_ID / 2)            " end correction per end, in
L_bore = L_eff - 2 * delta_end             " physical bore length, in
dist_from_foot(n) = L_eff * (f_root / f_hole_n)  " tone hole position, in
f_hole_n = 440 * 2^((MIDI_root + offset_n - 69) / 12)  " hole frequency
```

Offsets: +2, +3, +4, +5, +7, +9, +10, +11 (holes 1–8).
