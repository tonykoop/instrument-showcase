# Template 14 — Wholesale Dealer Line Sheet

A one-page-per-instrument line sheet for dealers and stockists. Different from the spec sheet — this one is *commercial*: wholesale price, MOQ, lead time, MAP (minimum advertised price), case pack.

## Format

- **One letter page, portrait, per instrument.**
- **Top:** wordmark + mark + "Wholesale Line Sheet" label + season/year.
- **Hero photo (1/3 page).**
- **Identity strip:** instrument name, serial-series prefix (e.g., "TNG-"), variants available.
- **Commercial table:**
  - Wholesale price (USD).
  - MAP (Minimum Advertised Price).
  - Suggested retail.
  - MOQ.
  - Lead time.
  - Case pack (units per box).
- **Brief description** (3 sentences).
- **Contact + ordering line.**

## Files this template consumes

| Source | Used for |
|---|---|
| `design.md` → "Target Price" + "Estimated Cost" | Commercial table inputs |
| `bom.csv` | Brief description anchor |
| Confirmed with Tony | MAP, MOQ, lead time, case pack (these are commercial decisions, not derived) |

## Voice

Trade-publication clean. No marketing copy. Numbers and lead times.

## What "done" looks like

- Trade-show or email-attachment ready.
- Per-instrument page; multi-instrument bundle is a separate compile.
- Pricing line is internally consistent (wholesale ≤ MAP ≤ retail).
- Lead time is a real range, not a placeholder.
