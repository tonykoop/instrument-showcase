---
title: Handpan (D Kurd Research Packet)
slug: handpan
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/handpan/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - instruments/handpan-sheetmetal
  - acoustic-classes/tuned-shell-idiophone
  - instruments/steel-pan
  - instruments/wooden-hang
open_questions:
  - "What is the current measured-vs-predicted state of the tone fields — have any real shells been struck and measured?"
  - "What heat/surface treatment (nitriding DC04 vs stainless) was selected for the first controlled build?"
  - "What tuning technique is used — dedicated hammers and tuning spikes, or general forming approach?"
  - "Has the validation-loop.csv been populated with any measured shell/tone-field data?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, handpan, D-kurd, steel-shell, tuned-tone-field, nitrided, ding, gu, research-packet]
---

# Handpan — D Kurd Research Packet

## Overview

Engineering documentation and parametric design table for a D Kurd root-mode handpan — the contemporary tuned-shell, tongueless metal hand drum built from two formed steel shells, a center Ding tone field (D3), eight surrounding tone fields (A3, Bb3, C4, D4, E4, F4, G4, A4), and a bottom Gu port. This is explicitly a private research packet, not a promise that a spreadsheet can predict a finished handpan.

- **Family:** idiophone / tuned steel shell instrument
- **Scale:** D Kurd, 9 notes (D3 Ding + 8 tone fields: A3, Bb3, C4, D4, E4, F4, G4, A4)
- **Shell:** 21 in nominal diameter, 9.5 in total height, 1.0 mm steel
- **Material path:** nitrided DC04 preferred; stainless as a separate measured branch
- **Gu port:** 3.5 in nominal, 0.5 in rolled lip, ~115 Hz Helmholtz estimate
- **Status:** private research/prototype planning packet — useful for procurement, fixture planning, and tuner review; not build-ready

Primary repo links:
- [README](../../../../idiophones/handpan/README.md)
- [Design notes](../../../../idiophones/handpan/design.md)
- [Tuning notes](../../../../idiophones/handpan/tuning-tonality-notes.md)
- [Validation](../../../../idiophones/handpan/validation.csv)

## Current Status

- Release state: private research packet — deep documentation but no build-ready status. Validation loop defined; all measurement rows remain `measurement_required`.
- Library family: idiophone.
- Acoustic class: tuned shell idiophone (handpan).
- Wolfram state: starter model (`.wl`) present; Wolfram Cloud Public-Execute URL available.
- CAD state: `capstone-manifest.json` present; SolidWorks/CNC/drawing briefs defined; no confirmed `.glb`.

## Source Notes

- [README](../../../../idiophones/handpan/README.md) — D Kurd layout (9 notes), shell geometry (21 in, 9.5 in, 1 mm), material path (nitrided DC04 preferred), Gu port (~115 Hz Helmholtz), packet map (validation loop, strike/FFT log template, public-release checklist, risks).

Artifacts not ingested: `design.md`, `validation-loop.csv`, `measured-partial-strike-log.csv`, `tuning-tonality-notes.md`, `public-release-checklist.md`.

## Design Knowledge

Handpan tone fields are elliptical dimpled regions hammered into a steel shell. Each tone field, when struck, produces 3–4 partial pitches: the fundamental, an octave (2× fundamental), and a fifth-above-octave (3× fundamental). Tuning means balancing these three partials across all 9 tone fields while minimizing cross-field coupling (vibration in one field should not measurably excite an adjacent field).

The nitriding process (iron nitride case hardening): hardens the outer steel surface, reducing creep and pitch drift after playing. DC04 mild steel nitriding is the standard modern handpan material path; stainless steel is harder and does not require nitriding but is more difficult to form and tune.

The Gu port (bottom opening) functions as a Helmholtz resonator coupled to the shell interior — its resonance adds bass warmth and affects lower tone fields.

Real handpan tuning is a craft: it cannot be solved by geometry alone. Every shell has residual stress from forming, heat affected zones, and material variation that shift partial pitches from the model. Measured tuning (strike → FFT → trim hammer blow) is the only path to a playable instrument.

Related: [[instruments/handpan-sheetmetal]] (sheet-metal execution blueprint for the same D Kurd target), [[instruments/wooden-hang]] (wooden variant research question), [[instruments/steel-pan]] (related tuned-dimple steel family, Trinidadian origin).

## Cross-Links

- [[instruments/handpan-sheetmetal]]
- [[acoustic-classes/tuned-shell-idiophone]]
- [[instruments/steel-pan]]
- [[instruments/wooden-hang]]

## Open Questions

1. Have any real shells been struck and measured — is any validation-loop data logged?
2. What heat/surface treatment was selected for the first controlled build?
3. What specific tuning technique (hammers, spikes, annealing)?
4. Has the public-release checklist been completed for any instrument built from this packet?

## Maintenance Notes

First ingest from README only. Next pass: read `tuning-tonality-notes.md` for D Kurd partial targets, `validation-loop.csv` for measurement state, and `risks.md` for known failure modes.
