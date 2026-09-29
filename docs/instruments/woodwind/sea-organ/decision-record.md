<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Decision Record

## QMD Step 0

- `qmd search "sea organ wave-driven pipe organ seawall" -c instrument-builds`
  failed before returning context because the sqlite-vec extension was
  unavailable and the database file could not be opened.
- Result: this packet is grounded in the user prompt and general public-safe
  mechanism knowledge, while keeping all pipe, tuning, air-path, wave, marine,
  structural, CAD, and DXF claims at `concept_only` or `pending_measurement`.

## Key Decisions

- Place the repo at `instruments/woodwind/sea-organ` because the sound source
  is air moving through pipes or whistle-like resonators.
- Treat tide/wave energy as the air driver, not as a measured design input.
- Keep seawall integration as a future civil/marine engineering authority
  chain, not an instrument-maker-generated structure.
- Keep pipe tuning, pipe count, bore/length, chamber volume, pressure/flow, and
  acoustic output out of the L1 packet.
- Make the first useful next step a non-structural airflow coupon or site-study
  plan, not a shoreline build.

## Open Questions

- What measured tide and wave data are required before choosing any air-capture
  mechanism?
- What marine structure or permitting review is required before a seawall
  interface can be discussed as build work?
- Which pipe or whistle family should be tested first once airflow evidence
  exists?
- How will drainage, saltwater corrosion, fouling, wildlife, public access, and
  maintenance be handled?
- What acoustic impact review is needed before placing a sound installation in
  a public shoreline environment?

## Promotion Gates

- L2 requires a site-study plan, airflow coupon plan, authority register update,
  and named review owners for marine structure, public safety, and acoustics.
- L3 requires measured site data, reviewed pipe/air-path design inputs,
  structural/marine engineering approval, and reviewed CAD or measured
  templates.
- L4 requires physical test data, installed or coupon-level measurements,
  maintenance observations, and model updates from the measured results.

## Authority Boundary

No pipe dimensions, tuning values, chamber volumes, pressure values, tide
ranges, wave loads, seawall details, CAD geometry, DXF coordinates, or measured
performance claims are made in this repo. Promotion requires measured site
data, reviewed acoustic design, marine/structural safety evidence, and
traceable fabrication authority.
