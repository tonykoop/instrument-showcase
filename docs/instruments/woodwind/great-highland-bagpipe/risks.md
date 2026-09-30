# Risks - Great Highland Bagpipe

### Acoustic Chanter Bore And Reed Do Not Agree

**Symptom:** Low A speaks, but the chanter scale cannot be brought into tune by
normal tape and hole enlargement.

**Mechanism:** The conical bore, reed compliance, tone-hole network, and bag
pressure form a coupled system. A first-order `c/(2L)` estimate does not capture
the full behavior.

**Test:** Build the prototype chanter in low-cost material, record every note at
stable pressure, and compare cents error against `validation.csv`.

**Mitigation:** Keep holes undersize, test with multiple commercial reeds, and
adjust bore/hole plan before using blackwood.

**Severity:** High - human decision required before final-material chanter.

### Structural Long Bore Wanders Or Cracks

**Symptom:** Chanter or bass middle section shows off-center bore, thin wall, or
cracking during reaming/turning.

**Mechanism:** Long small-diameter bores in dense wood create heat, tool wander,
and hoop stress. Blackwood is hard and expensive but not forgiving.

**Test:** Bore and ream a prototype blank, then measure wall thickness at both
ends and inspect for heat checking.

**Mitigation:** Use headstock-supported drilling, clear chips often, prototype
in Delrin/ipe/cherry first, and reject blanks with runout or checks.

**Severity:** High - human decision required before final-material bore work.

### Ergonomic Pressure And Reach Fatigue

**Symptom:** The set can be tuned on the bench but is tiring or unstable during
real playing.

**Mechanism:** Bag size, blowpipe length, stock placement, chanter hand spacing,
and reed strength interact with player posture and arm pressure.

**Test:** Run a timed 10-minute playing simulation with manometer readings and
note any hand stretch, neck/arm fatigue, or pressure instability.

**Mitigation:** Start with a known synthetic bag size, use medium reeds, keep
the practice chanter step, and adjust blowpipe/stock ergonomics before final
decoration.

**Severity:** Medium.

### Supply Reed Or Bag Substitution Changes The Whole System

**Symptom:** A substitute reed or bag part fits mechanically but changes pitch,
pressure threshold, or stock layout.

**Mechanism:** Reed body/staple dimensions and bag stock-hole positions are not
universal across makers. The acoustic and mechanical interface can shift.

**Test:** Measure purchased reed bodies, staple OD, bag stock layout, and valve
fit before cutting reed seats or tying in stocks.

**Mitigation:** Buy coupling parts first, update drawings from measured parts,
and keep supplier substitutions out of final dimensions until measured.

**Severity:** Medium.

### Fit/Finish Decorative Mounts Lock In Before Tuning Is Stable

**Symptom:** Ferrules, imitation ivory mounts, or engraving prevent later slide,
stock, or bore corrections.

**Mechanism:** Decorative parts can hide joints, limit slide travel, or make a
prototype feel "finished" before acoustic validation is done.

**Test:** Assemble and tune the plain prototype for 24 hours before installing
permanent decorative parts.

**Mitigation:** Make mounts removable in prototype, omit engraving until the
validation report is clean, and keep slide access visible.

**Severity:** Low.
