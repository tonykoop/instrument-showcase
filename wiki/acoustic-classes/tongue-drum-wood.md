---
title: Wood Tongue Drum Acoustic Class
wiki_type: acoustic-class
status: active
last_updated: 2026-05-18
source_count: 1
open_questions: 6
tags:
  - acoustic-class
  - drum
  - tongue-drum
  - wood
---

# Wood Tongue Drum Acoustic Class

## Overview

This page tracks wood slit-tongue instruments where tuned tongues behave as cantilevers cut into a wooden soundboard. The first active member is [[instruments/wood-shell-tongue-drum]].

The class has two branches:

- Rectangular or open-body wooden tongue drums, represented by the legacy `tongue-drum` repo.
- Enclosed round-body wooden tongue drums, represented by `wood-shell-tongue-drum`, where Helmholtz cavity coupling becomes part of the design.

## Active Instruments

- [[instruments/wood-shell-tongue-drum]] - round-body wood tongue drum family with cylinder/hemisphere bodies, flat/domed tops, Padauk soundboard assumptions, Black Walnut shell, and an enclosed gu-port-tuned cavity.

Related source stream:

- [legacy rectangular tongue-drum repo](../../../../idiophones/tongue-drum/README.md)

## Governing Model

The tongue model is flat-cantilever Euler-Bernoulli in the current packets:

```text
f = K * t / L^2
L = sqrt(K * t / f)
```

For domed soundboards, `wood-shell-tongue-drum` starts with an empirical length multiplier:

```text
L_curved = L_flat * 1.025
```

That multiplier is not yet measured for the actual dome rise. The first dome build should cut one calibration tongue, measure it, and then propagate the corrected multiplier.

## Enclosed Cavity Pattern

The round-body wooden shell adds a Helmholtz resonator under the tongue field:

```text
f_H = (c / 2 pi) * sqrt(A_port / (V * L_neck))
```

The `wood-shell-tongue-drum` design target is `f_H/f_ding` between 0.80 and 1.20. The gu port is drilled last and opened while measuring cavity response. Opening the port raises `f_H`; restricting area or lengthening the neck lowers `f_H`.

## Validation Pattern

Reusable rows for this class:

- each tongue frequency and cents error
- A4 or other reference-pitch sanity check
- material K back-calculation
- Helmholtz frequency and `f_H/f_ding` ratio when enclosed
- soundboard thickness and flatness
- slit kerf width
- rim or soundboard seal test
- post-finish pitch drift

## Open Questions

1. How much of the legacy rectangular `tongue-drum` repo should be distilled into this page?
2. Should Padauk K calibration become a shared material page under `materials/padauk`?
3. What is the standard test for post-finish pitch drift in wood tongue instruments?
4. Should enclosed wood tongue drums share a Wolfram notebook with steel and ceramic tongue-drum cousins?
5. What is the best way to represent gu-port tuning curves in the wiki?
6. Should `tongue-drum-wood` split into open-body and enclosed-cavity pages after more examples are ingested?

## Maintenance Notes

When the legacy rectangular `tongue-drum` repo is ingested, merge its empirical flat-cantilever lessons here and distinguish measured results from design-study predictions.
