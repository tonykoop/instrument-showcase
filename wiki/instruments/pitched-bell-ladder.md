---
title: Pitched Bell Chime Ladder Blueprint (13-Note C5–C6 Chromatic)
slug: pitched-bell-ladder
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/pitched-bell-ladder/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/bell-idiophone
  - fabrication/hammer-forming-brass
  - instruments/carillon
  - instruments/tubular-bells
open_questions:
  - "What is the dome forming sequence — press-forming, spinning, or hammering over a mandrel?"
  - "How is each dome mounted on the ladder — suspended by a wire, clamped, or resting on foam?"
  - "What are the hum-tone and strike-tone targets for the C5 and C6 domes?"
  - "Have the C5, F#5/Gb5, and C6 coupon bells been formed and tuned?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, bell, chime, ladder, 13-note, chromatic, C5-C6, brass-dome, L2]
---

# Pitched Bell Chime Ladder Blueprint — 13-Note C5–C6 Chromatic

## Overview

A 13-note chromatic idiophone ladder made from hammer-formed C268 yellow-brass domes arranged vertically in an 800 × 200 mm structure. Each dome is a bell-like struck idiophone with a target hum tone and a strike tone approximately one octave + a fifth above it. The chromatic range C5 through C6 covers one octave of the soprano voice.

- **Family:** idiophone / struck bell chime ladder
- **Notes:** 13, chromatic C5–C6 (C5, C#5, D5, D#5, E5, F5, F#5, G5, G#5, A5, A#5, B5, C6)
- **Structure:** 800 × 200 mm vertical ladder
- **Material:** C268 yellow brass domes, hammer-formed
- **Validation:** formed-shell tuning, coupon tests (C5, F#5/Gb5, C6 first)
- **Status:** L2 V5 build-packet candidate — blueprint only; coupon tests required before full cut

Primary repo links:
- [README](../../../../idiophones/pitched-bell-ladder/README.md)
- [Design notes](../../../../idiophones/pitched-bell-ladder/design.md)
- [Parameters](../../../../idiophones/pitched-bell-ladder/parameters.csv)
- [Wolfram starter](../../../../idiophones/pitched-bell-ladder/pitched-bell-ladder-starter.wl)

## Current Status

- Release state: L2 V5 build-packet candidate — blueprint only. Formed-shell tuning, CAD/DXF authority, and acoustic claims require coupon tests.
- Library family: idiophone.
- Acoustic class: bell idiophone (hammer-formed brass dome).
- Wolfram state: first-pass note and shell-size model present; Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan defined; no confirmed `.glb`.

## Source Notes

- [README](../../../../idiophones/pitched-bell-ladder/README.md) — 13 C268 yellow-brass domes, C5–C6 chromatic, 800 × 200 mm ladder, hum tone + strike tone target (~octave + fifth above hum), coupon sequence (C5, F#5/Gb5, C6 first — do NOT cut all 13 before coupons).

Artifacts not ingested: `design.md`, `parameters.csv`, `fabrication-plan.md`, `validation.csv`.

## Design Knowledge

The bell partial structure: a well-formed bell has a hum (fundamental), a minor third (tierce), a fifth (quint), a nominal (octave above hum), and a super-octave. The partial ratios are set by the bell profile (dome shape and wall thickness distribution). A simple hammer-formed dome does not produce perfectly tuned partials; the focus here is achieving a recognizable hum + strike tone relationship within approximately ±20 cents per partial.

C268 (free-cutting yellow brass, 65% Cu / 35% Zn) is appropriate for hammer forming: good ductility, visible work-hardening cues, excellent acoustic ring. Yellow brass (vs red brass or pure copper) has a higher stiffness-to-density ratio in the temperature range used for annealing between forming passes.

Ladder mounting: each dome must be suspended at its node — not gripped rigidly (which damps the hum) but suspended by wire or cord through a small hole near the dome's center, analogous to glockenspiel bar node suspension.

Related: [[instruments/carillon]] (tower bells at a much larger scale, same bell partial structure challenge), [[instruments/tubular-bells]] (tube geometry rather than dome, same C4–F5 orchestral range challenge).

## Cross-Links

- [[acoustic-classes/bell-idiophone]]
- [[fabrication/hammer-forming-brass]]
- [[instruments/carillon]]
- [[instruments/tubular-bells]]

## Open Questions

1. What is the dome forming sequence — press-forming, spinning, or hammer-forming over a mandrel?
2. How is each dome mounted on the ladder (wire suspension, clamp, foam rest)?
3. What are the hum-tone and strike-tone targets for C5 and C6?
4. Have the coupon bells (C5, F#5/Gb5, C6) been formed and tuned?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for dome geometry and `pitched-bell-ladder-starter.wl` for hum/strike-tone predictions. Do not cut the full 13-note set before coupon validation.
