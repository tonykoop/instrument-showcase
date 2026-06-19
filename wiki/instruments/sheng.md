---
title: Sheng
slug: sheng
wiki_type: instrument
status: active
sources:
  - path: ../../../woodwind/sheng/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/sheng/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/sheng/architecture-choice.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/free-reed-pipe-organ
  - fabrication/windchest-construction
  - synthesis/free-reed-pull-down
  - synthesis/wolfram-model-patterns
open_questions:
  - "Has an architecture branch been chosen (traditional-side-branch vs compact-control)?"
  - "Has P0 reed coupon data been recorded in p0-reed-coupon-log.csv?"
  - "Has P1 single-pipe control been validated in p1-single-pipe-control-log.csv?"
  - "Has windchest-geometry-plan.csv been filled with measured chamber and gasket data?"
  - "Have safety gates (safety-gates.csv) been cleared before any reed cutting or pressure test?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - woodwind
  - free-reed
  - sheng
  - mouth-organ
  - chinese
  - parametric-design
  - architecture-branch
---

# Sheng

## Overview

The `sheng` repo is an L2 V5 build-packet candidate for a sheng mouth-organ family. The packet carries two explicit architecture variants and deliberately does not choose between them until reed coupon and single-pipe control data are measured. Fabrication authority: not build-ready.

Primary repo links:

- [README](../../../../woodwind/sheng/README.md)
- [Design](../../../../woodwind/sheng/design.md)
- [Architecture choice](../../../../woodwind/sheng/architecture-choice.md)
- [Free-reed empirical loop](../../../../woodwind/sheng/free-reed-empirical-loop.md)
- [Safety gates](../../../../woodwind/sheng/safety-gates.csv)

## Current Status

- Release state: L2 V5 build-packet candidate; no physical prototype.
- Architecture decision: open — traditional-side-branch vs compact-control; first bench action determines winner.
- Acoustic class: [[acoustic-classes/free-reed-pipe-organ]] — free-reed pipe with windchest coupling.
- CAD: not yet; architecture must be chosen before committing CAD geometry.
- Wolfram model: `sheng-starter.wl` live at Public-Execute cloud URL.
- Release blockers: architecture choice; P0 reed coupon; P1 single-pipe control; windchest geometry.

## Architecture Branches

**Traditional side-branch** (`traditional-side-branch/`): sheng-like side-branch reed model; both pipe ends open; follows classical sheng geometry. Use when preserving long-pipe geometry is the first design goal.

**Compact control** (`compact-control/`): stopped-end prototype; reed acts as the closed end; shorter, more serviceable module. Use when proving a short reed-pipe module is the first design goal.

The two `family-spec.csv` files are intentionally separate. Do not merge unless measured coupon and single-pipe data prove the same acoustic law applies to both.

## Empirical Loop (P0 → P1)

Per `free-reed-empirical-loop.md`:

1. **P0 reed coupon**: measure pitch, onset pressure, pull-down, and socket geometry per coupon. Record in `p0-reed-coupon-log.csv`.
2. **P1 single-pipe control**: couple one reed to one pipe; measure pitch, leakage, branch behavior. Record in `p1-single-pipe-control-log.csv`.
3. **Windchest**: fill `windchest-geometry-plan.csv` with chamber, gasket, inlet, pressure tap, and service-access data.
4. Clear all `safety-gates.csv` rows before any reed cutting, pressure test, or full-body layout.

## Source Notes

- [repo] [README](../../../../woodwind/sheng/README.md) — architecture variants, file map, quick start protocol.
- [repo] [design.md](../../../../woodwind/sheng/design.md) — shared intent, scope, unknowns, and validation gates.
- [repo] [architecture-choice.md](../../../../woodwind/sheng/architecture-choice.md) — first decision point with tradeoff analysis.

## Cross-Links

- [[acoustic-classes/free-reed-pipe-organ]]
- [[fabrication/windchest-construction]]
- [[synthesis/free-reed-pull-down]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Has an architecture branch been chosen (traditional-side-branch vs compact-control)?
2. Has P0 reed coupon data been recorded in `p0-reed-coupon-log.csv`?
3. Has P1 single-pipe control been validated in `p1-single-pipe-control-log.csv`?
4. Has `windchest-geometry-plan.csv` been filled with measured chamber and gasket data?
5. Have `safety-gates.csv` rows been cleared before any reed cutting or pressure test?

## Maintenance Notes

Next ingest should pull in architecture decision, P0 reed coupon measurements, and P1 single-pipe results. Update [[acoustic-classes/free-reed-pipe-organ]] with any empirical pull-down or coupling data.
