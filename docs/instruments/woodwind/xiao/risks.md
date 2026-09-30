# Xiao — Risk Register

**Project:** XIAO-001 · G Nan Xiao  
**Date:** 2026-05-08  
**Specialist:** Red-team walk  
**Severity:** High / Medium / Low

Every risk has a verification test. No risk is listed without a test.

---

## Acoustic Risks

### RISK-A01 — Embouchure end correction: model vs reality (HIGH)

**Description:** The first-order model assumes the U-notch embouchure behaves as a simple open end (δ_emb ≈ 0.6·r = 0.260 in). In practice the jet–edge interaction, lip coverage, and notch geometry all modulate the effective acoustic length. If the real end correction differs significantly from the model, the bore length L_bore will be wrong and all tone-hole positions will be systematically off.

**Consequence:** Fundamental frequency error of 10–30 cents; all holes require repositioning.

**Mitigation:** Leave +0.25 in trim allowance on the blank. Drill all tone holes under-length (1–2 mm toward foot). Measure fundamental before drilling holes; compute actual δ_emb = L_eff_measured − L_bore − δ_foot and update design.md.

**Verification test:** After embouchure cut but before tone holes, blow the blank and record the fundamental with a strobe tuner. Compare measured frequency to model prediction (293.66 Hz). Compute cents error. If error > ±15 cents, recalculate L_bore and update hole positions before drilling.

---

### RISK-A02 — Chromatic scale coverage gaps (MEDIUM)

**Description:** The 8-hole layout (+2,+3,+4,+5,+7,+9,+10,+11) does not cover semitones +1, +6, +8, or the octave (+12) by simple hole-open technique. These notes require cross-fingering, half-holing, or overblowing. Cross-fingerings on a short-scale instrument may yield poor intonation or tone quality.

**Consequence:** Instrument is not fully chromatic by simple fingering; some passages require advanced technique.

**Mitigation:** Document the fingering chart explicitly. Test cross-fingerings on the prototype and note cents errors. Consider whether +1 (m2) requires a vent hole (as on some modern xiao).

**Verification test:** After voicing, play all 12 chromatic semitones of the first octave using standard xiao fingerings. Record cents error for each cross-fingered note. Accept if ≤ ±20 cents (playable with embouchure correction); flag if > ±20 cents.

---

### RISK-A03 — Bore finish shifts tuning (MEDIUM)

**Description:** Internal bore finish (BLO, shellac, lacquer) reduces the effective bore diameter and raises the fundamental pitch. The magnitude depends on film thickness and material. Applying finish after voicing will sharpen all notes unpredictably.

**Consequence:** Holes need re-voicing after finish. If finish is too thick, notes may be irrecoverably sharp.

**Mitigation:** Apply bore finish before final voicing (as specified in assembly-manual.md Stage 6). Allow full cure before tuning. Note: BLO raises pitch ~1–3 cents; shellac may raise ~3–8 cents. Mark these as TBD assumptions in validation.csv.

**Verification test:** Measure fundamental before and after bore finish application. Record ΔHz and Δcents. Update validation.csv row V-BORE-FIN.

---

### RISK-A04 — Temperature sensitivity during tuning (LOW)

**Description:** Speed of sound changes ~0.6 m/s per °C (≈ 1 cent per °F in this bore range). If the instrument is tuned in a cold shop and played in a warm room, it will play sharp.

**Consequence:** Pitch drift of ~5–10 cents between cold shop and warm performance space.

**Mitigation:** Tune at 68°F. Note tuning temperature in validation.csv. Advise player to warm instrument before playing (blow through for 2–3 minutes).

**Verification test:** Record room temperature at every tuning session. Compare fundamental at 60°F vs 75°F if both conditions are available during build.

---

## Structural Risks

### RISK-S01 — Bore wander causing eccentric wall (HIGH)

**Description:** A 22.5 in bore through 1.5 in square stock is at the limit of practical straight-bore drilling. If the bit wanders, the wall thickness will be uneven. A thin wall (<1/8 in) at any point may crack under playing stress or during final turning.

**Consequence:** Structural failure of body; wasted tonewood blank.

**Mitigation:** Scrap-blank validation before drilling tonewood (per assembly-manual.md Stage 2). Rigid tailstock carrier with anti-rotation feature. Peck drilling with chip clearing. Step through intermediate bit sizes.

**Verification test (V-BORE-WANDER):** On scrap blank, measure bore entry center vs bore exit center. Wander must be < 0.030 in (less than half wall thickness for minimum 0.118 in Qin Xiao wall). Reject and re-jig if exceeded.

---

### RISK-S02 — Embouchure notch cracks at wall (HIGH)

**Description:** The U-notch removes material from the thin upper wall of the mouthpiece section, creating a stress concentration. Black walnut is strong but the notch introduces a hard corner at the bore tangent line. Cracks may initiate here under the cycling stress of repeated playing.

**Consequence:** Structural crack propagates along grain; instrument unusable.

**Mitigation:** Keep notch width ≤ 12 mm (do not exceed bore diameter). Radius the notch corners (avoid sharp square cuts). Seal grain at notch immediately after cutting (thin CA glue or shellac). Inspect after 5 playing sessions.

**Verification test (V-STRUCT):** Visual inspection with loupe after embouchure cut. No grain separation or cracks visible at notch corners. Tap test: body should ring cleanly, not produce a dead thud.

---

### RISK-S03 — Tone hole undermining wall integrity (MEDIUM)

**Description:** Eight holes drilled through a 0.236 in wall — if any hole is off-axis or oversized, the through-wall remaining material may be dangerously thin at the bore tangent.

**Consequence:** Hole-edge splitting or crack between adjacent holes.

**Mitigation:** Use pilot bit before finish bit. Keep hole diameter ≤ 10 mm on front holes (wall clearance = 0.236 in − hole_radius_projected). Minimum spacing between holes: hole diameter + 2 × wall thickness.

**Verification test:** After each hole, inspect bore interior (mirror or flashlight through foot) for any visible wall penetration beyond the intended hole footprint. No cracks or splits visible.

---

## Ergonomic Risks

### RISK-E01 — Hole spacing vs hand span (MEDIUM)

**Description:** The first-order hole positions (holes 1–8 at 20.48 to 12.18 in from foot) produce a hole group spanning about 8.3 in. This is within the reach of most adult hands but may be uncomfortable for players with smaller hands, particularly the span from hole 4 (RH index) to hole 5 (LH ring) — a gap of approximately 1.88 in (47.8 mm).

**Consequence:** Instrument may be difficult or impossible for players with hand spans below ~17 cm.

**Mitigation:** This is the traditional xiao geometry — the hand span requirement is intrinsic to the key. Note the minimum hand span in documentation. For accessibility, a smaller key (higher pitch) can be used — the design table covers all 26 keys.

**Verification test:** Measure the actual hole 4-to-hole 5 center distance on the finished instrument. Compare to ergonomic database: 5th-percentile female adult hand span ≈ 175 mm; the gap should be ≤ 50 mm for comfortable reach. Record in validation.csv.

---

### RISK-E02 — Playing angle and embouchure fatigue (LOW)

**Description:** The xiao is held at approximately 45° from vertical (angled toward player) or near-vertical. The embouchure requires more lip control than a transverse flute. Beginners commonly find the instrument difficult to produce a tone from initially.

**Consequence:** Not a build risk, but a documentation risk — the instrument should be clearly labeled as requiring technique to produce a tone.

**Mitigation:** Include embouchure setup notes in assembly-manual.md. Recommend 30-minute sustained practice sessions over multiple days before concluding that the instrument is defective.

**Verification test:** Any person familiar with end-blown flutes can produce a stable tone on the finished instrument within 2–3 minutes. If no one can produce a tone, inspect embouchure geometry (notch width, inner bevel angle).

---

## Supply Risks

### RISK-SU01 — Long-series drill bit availability (MEDIUM)

**Description:** 55/64 in bits in 18+ in overall length are not stocked at every supplier. McMaster-Carr carries these but lead time may be 3–5 days.

**Consequence:** Build is blocked waiting for bits.

**Mitigation:** Order bits before cutting stock. Verify McMaster-Carr availability before any other procurement. Alternative: use 7/8 in (0.875 in) as finish bit and lap down — this avoids the 55/64 in odd size.

**Verification test:** Confirm bit is in hand before cutting the blank.

---

### RISK-SU02 — Walnut blank grain straightness (MEDIUM)

**Description:** A 26 in walnut blank with interlocked or irregular grain may tear during turning or produce a wandering bore if grain causes bit deflection during drilling.

**Consequence:** Unusable blank; wasted time and material.

**Mitigation:** Inspect grain direction before purchase. Prefer riftsawn or quartersawn stock. Reject blanks with visible runout > 5° from long axis. Buy a spare blank.

**Verification test:** Sight down blank before drilling. Grain should run within ~5° of the long axis for 90% of the blank length.

---

## Fit and Finish Risks

### RISK-FF01 — Bore finish pooling in tone holes (LOW)

**Description:** If BLO or shellac is applied after tone holes are drilled, finish may pool in the holes and partially obstruct them, sharpening the affected notes.

**Consequence:** Notes are sharp after finishing; difficult to correct without re-voicing.

**Mitigation:** Apply bore finish before drilling tone holes, OR mask tone holes with tape during finishing, OR apply finish sparingly with a cloth strip (not flooding).

**Verification test:** After bore finishing, sight through each tone hole (when drilled). Hole bore should be clean, no pooled finish visible. Probe with a toothpick if uncertain.

---

### RISK-FF02 — Mouthpiece section surface checks (LOW)

**Description:** Walnut can develop hairline checks (end-grain cracks) in the mouthpiece section if the wood is not fully stabilized. These checks can appear days after cutting, particularly in a dry shop.

**Consequence:** Cosmetic defect; potential crack propagation to notch zone.

**Mitigation:** Use kiln-dried (MC ≤ 8%) stock. Stabilize endgrain immediately after cutting with thin CA or shellac. Keep instrument in a moderate-humidity environment (40–50% RH) during build.

**Verification test:** Inspect mouthpiece end-grain face at 48 hr after cutting and again at 1 week. No new checks visible under 10× loupe.
