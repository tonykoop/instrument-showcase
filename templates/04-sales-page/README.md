# Template 04 — Sales Page (Serialized Instrument)

A web page selling **one specific serialized instrument** — not the model, the unit. The buyer sees the exact serial, exact build date, exact materials, exact tuning measurements, exact photos of the unit they'd be receiving.

## Format

- **Single-page HTML.**
- **Hero band:** wordmark, "TNG-001 — for sale" header, big photo of the actual unit, price, "buy" CTA (or "inquire" if commission).
- **The exact specs:** serial, build date, materials by row from the actual `validation.csv`, tuning measurements (cents-error per tongue/note), weight, dimensions.
- **Provenance:** maker bio + signature + cert-of-authenticity reference.
- **Carousel/gallery:** 3–8 photos of *this exact unit*.
- **What you'll receive:** instrument, mallet/case/care card, certificate, tuning chart.
- **FAQ block:** shipping, returns (do you accept them?), care, retuning service.

## Files this template consumes

Same as 01-brochure plus:

| Source file | Used for |
|---|---|
| `validation.csv` | Per-tongue measured frequencies and cents-error |
| `images/` | Multiple unit photos for the gallery |
| `data/` (if present) | Optional: link to a recorded sample / FFT image |
| `study/README.md` | Optional: short engineering note for the curious buyer |

## Voice

Confident but not pushy. State the price. State what's included. State limits (no returns, etc.) plainly. The certificate-of-authenticity link is the trust mark — point at it, don't explain it.

## Notes

- Include a sound sample if you have one (`<audio controls>`).
- Link to the build-method landing page (Template 03) for buyers who want the full story.
- Link to the certificate of authenticity (Template 09) as PDF.
