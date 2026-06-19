---
title: Aeolian Harp Pillar
slug: aeolian-harp-pillar
wiki_type: instrument
status: active
sources:
  - path: ../../../strings/aeolian-harp-pillar/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/aeolian-harp-pillar/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/aeolian-harp-pillar/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/wind-excited-string
  - fabrication/brake-formed-sheet-metal
  - fabrication/outdoor-structural-enclosure
  - synthesis/wolfram-model-patterns
open_questions:
  - "Have bend coupons been tested for spring-back on 1.5mm 304 stainless?"
  - "Have string/rail tests been run to verify Voss wind-excitation onset?"
  - "Has outdoor wind validation been completed at the target site?"
  - "Has site-specific base anchoring been engineered and reviewed?"
  - "Have string tensions been measured against the D pentatonic tuning targets?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - strings
  - aeolian-harp
  - wind-excited
  - sheet-metal
  - outdoor
  - parametric-design
  - structural
---

# Aeolian Harp Pillar

## Overview

The `aeolian-harp-pillar` repo is an L2 shop-packet candidate for a 2.4 m outdoor sheet-metal aeolian harp pillar with 12 wind-excited strings tuned to a D pentatonic set. Parameters, fabrication tables, and Wolfram source are complete. Not build-ready (L3) until bend coupons, string/rail tests, outdoor wind validation, and site-specific base anchoring are complete.

Primary repo links:

- [README](../../../../strings/aeolian-harp-pillar/README.md)
- [Design](../../../../strings/aeolian-harp-pillar/design.md)
- [Parameters](../../../../strings/aeolian-harp-pillar/parameters.csv)
- [Fabrication plan](../../../../strings/aeolian-harp-pillar/fabrication-plan.md)
- [Validation](../../../../strings/aeolian-harp-pillar/validation.csv)

## Current Status

- Release state: L2 shop-packet candidate; no physical prototype.
- Build target: 2.4 m outdoor pillar, 12 strings, D pentatonic (D3–E5).
- Acoustic class: [[acoustic-classes/wind-excited-string]] — aeolian excitation, not player-driven.
- Fabrication: two brake-formed U-channel halves (1.5 mm 304 SS), internal baffles, backing strips, drains, weather caps.
- Wolfram model: `aeolian-harp-pillar-starter.wl` live at Public-Execute cloud URL.
- Release blockers: bend coupons; string/rail tests; outdoor wind validation; site anchoring.

## Design Snapshot

| Parameter | Value | Status |
|-----------|-------|--------|
| Height | 2400 mm | design |
| Cross-section | 250 mm square | design |
| Wall | 1.5 mm 304 stainless | design |
| Strings | 12 stainless music wire, 30 mm off body | design |
| Scale | D pentatonic, D3–E5 | target |
| Wind onset | ≤10 km/h audible | target |
| Wind max | 40 km/h, no problematic rattle/deflection | target |

## Acoustic Model

The Wolfram starter estimates string tension, wind-mode multiples, column modes, and a Helmholtz-like port frequency. Aeolian excitation follows Voss's model: wind velocity → vortex shedding → string resonance at Strouhal frequency. String tension and diameter determine the resonant frequency. The 12-string D pentatonic layout was derived from this model.

## Source Notes

- [repo] [README](../../../../strings/aeolian-harp-pillar/README.md) — design snapshot, packet map, readiness statement.
- [repo] [design.md](../../../../strings/aeolian-harp-pillar/design.md) — acoustic and structural concept.
- [spreadsheet] [validation.csv](../../../../strings/aeolian-harp-pillar/validation.csv) — bend, string, wind, and site checks; all rows pending until prototype.

## Cross-Links

- [[acoustic-classes/wind-excited-string]]
- [[fabrication/brake-formed-sheet-metal]]
- [[fabrication/outdoor-structural-enclosure]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Have bend coupons been tested for spring-back on 1.5 mm 304 stainless?
2. Have string/rail tests been run to verify Voss wind-excitation onset?
3. Has outdoor wind validation been completed at the target site?
4. Has site-specific base anchoring been engineered and reviewed?
5. Have string tensions been measured against the D pentatonic tuning targets?

## Maintenance Notes

Next ingest should pull in bend coupon results, string/rail test data, and any site wind measurements. Update [[acoustic-classes/wind-excited-string]] with empirical Strouhal onset data when available.
