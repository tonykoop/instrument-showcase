# Template 10 — Care & Tuning Card

A wallet-card or postcard-sized customer-facing card that ships with every instrument. Tells the new owner how to keep the instrument healthy and how to recognize when it needs retuning.

## Format

- **4×6 in postcard, or 3.5×2 in wallet card** — both fit one card per letter sheet (with bleed) for printing.
- **Side A:** wordmark + mark + instrument name + serial. Three care rules in imperative tense.
- **Side B:** tuning section — *"Your instrument left the bench tuned to ±X cents."* Plus a 4-step retuning service contact + URL/QR.

## Files this template consumes

| Source | Used for |
|---|---|
| `design.md` | Serial, instrument type |
| `validation.csv` | Cents-error tolerance line |
| `assembly-manual.md` → "maintenance notes" if present | Care rules |

## Voice

Imperative care rules; first-person on the tuning service offer.

## Care-rule defaults by family

If `assembly-manual.md` doesn't have maintenance notes, fall back to family defaults:

- **Drums (idiophones):** keep dry; oil top with food-safe mineral oil annually; never strike with metal.
- **Winds (aerophones):** swab after every play; keep below 70% RH; oil bore quarterly.
- **Strings:** wipe strings after play; loosen if storing > 1 month; humidity 40–55%.
- **Marimba/keyboard:** wipe with dry cloth; cover when not in use; do not stack.

## What "done" looks like

- Fits on a 4×6 postcard with bleed.
- Three rules, no more.
- Tuning tolerance line cites the actual measured `validation.csv` value, not a placeholder.
- Retuning offer has a real contact path (email or repo issue link).
