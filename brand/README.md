# Heifer Zephyr — Brand System Seed

This folder is the **Heifer Zephyr design system seed** that Claude Design ingests when you point it at the `instrument-showcase` repo.

## Files

| File | What it does |
|---|---|
| `tokens.css` | Single source of truth for color, typography, spacing, and rule weights. Every template imports this file and uses the `--hz-*` CSS custom properties. |
| `voice.md` | Voice and tone rules. Engineering-honest, first-person when Tony is the subject, concrete over abstract. |
| `components.html` | Visual exemplar of the core components: wordmark+mark lockup, document header, spec block, hero photo slot, pull quote, colophon footer, family-accent stripes. |
| `assets/` | Drop your bison-mark SVG, Heifer Zephyr wordmark file, hero photo treatments, and any other static assets here. |

## Drop your assets here

The skill is shipped without binary brand assets — drop yours into `assets/`:

- `bison-mark.svg` (or `.png` at 1024px) — the bison head line-art mark
- `wordmark.svg` (or `.png`) — "Heifer Zephyr" italic-serif wordmark
- `lockup.svg` — combined mark + wordmark
- `hero-treatments/` — examples of the cream/linen ground hero shot
- `signature.svg` — Tony's signature for certificates of authenticity

Templates reference these by relative path (e.g., `../../brand/assets/lockup.svg`).

## Pointing Claude Design at this folder

When you open Claude Design and want to set up the design system for a new project:

1. In Claude Design, choose "Set up design system."
2. Either upload this folder or paste the GitHub URL `tonykoop/instrument-showcase/brand`.
3. Claude Design reads `tokens.css`, `voice.md`, `components.html`, and the contents of `assets/` and learns the Heifer Zephyr style.
4. From that point on, every artifact you generate inherits this style automatically.

See: [Set up your design system in Claude Design](https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design).

## Family-accent rule

Every document picks one accent based on the instrument family. Set it on the `<body>` tag (or the topmost container):

```html
<body class="hz-family-percussion">  <!-- terracotta — drums, idiophones -->
<body class="hz-family-winds">       <!-- slate — flutes, aerophones -->
<body class="hz-family-strings">     <!-- walnut — guitars, lutes, harps -->
<body class="hz-family-keyboard">    <!-- olive-stone — marimba, glockenspiel -->
<body class="hz-family-electronic">  <!-- graphite — electric instruments -->
```

The rest of the page should stay monochrome ink-on-cream. The accent is for one rule, one underline, one pull-quote bar — never a flood fill.
