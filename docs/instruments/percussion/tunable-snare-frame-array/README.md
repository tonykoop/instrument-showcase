<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Tunable Snare Frame Array

**Family:** Percussion · Membranophone · Frame drum  
**Target tuning:** D3 / A3 / D4 (3-pitch D minor triad cluster, ±50 cents, tunable by head tension)  
**Ergonomic envelope:** Three frame drums (150 mm, 200 mm, 250 mm OD) mounted side-by-side on a 450 mm shared steel bracket frame; total playing width ≈ 550 mm, height ≈ 300 mm, depth ≈ 80 mm  
**Status:** L2 V5 build-packet candidate

---

## Design Thesis

Three small snare-style frame drums of graduated diameter share a single plasma-cut cold-rolled steel mounting bracket. Each drum is independently tensioned via standard drum lug hardware, allowing the player to dial in a chromatic or open-tuned 3-pitch array. Bought drum heads (Remo Ambassador, 6″/8″/10″) and bought snare wires (8–12 strand) keep the build approachable; the sheet-metal work is three rolled cylinders and one flat mounting bracket — well within Maker Nexus slip-roll + plasma workflow.

The instrument reads as a hand-percussion kit (clave-like cross-stick, brushed rim shots, snare rattles on all three pitches) with enough pitch separation to imply melody. It is a greenfield v0.1.0-blueprint — all dimensions and acoustic targets are derived estimates pending a first prototype.

---

## Quick Start

| File | Purpose |
|------|---------|
| `design.md` | Parametric design + acoustic model |
| `parameters.csv` | All dimensions — single source of truth |
| `tunable-snare-frame-array-starter.wl` | First-order membrane frequency model |
| `validation.csv` | Predicted targets + measurement gates |
| `fabrication-plan.md` | Maker Nexus cut → roll → weld → assemble sequence |
| `bom.csv` | Bill of materials with supplier hints |
| `explorer.html` | Single-page packet viewer |
| `cad/tunable-snare-frame-array.scad` | Parametric OpenSCAD shell + frame envelope master (`pending_measurement`) |
| `evolution/` | evolution-pipeline Stage 0 intake: master manifest, design-intent, revision register (Gate A not yet run) |

---

## License

Hardware: CERN-OHL-W v2.0 · Docs: CC BY 4.0 — see `LICENSE`.
