# raw-sources

Source streams for the Heifer Zephyr instrument wiki. The wiki **reads from** this folder; it never writes to it. The vault and clippings are mirrored in via symlinks, not copies.

## Contents

```
raw-sources/
  inbox/                Drop new sources here for the next ingest pass.
  processed/<YYYY-MM>/  Inbox items move here after ingest. Audit trail.
  second-brain/         Symlink → C:\Users\Tony\Documents\Second_Brain
  obsidian-clips/       Symlink → C:\Users\Tony\Documents\Second_Brain\Clippings
  .ingest-allowlist     Path globs the wiki agent may read.
  README.md             This file.
```

## Setup (one-time)

From the repo root, run `scripts/setup-symlinks.ps1` in an **elevated PowerShell** (Run as Administrator). This creates the two symlinks. After that, both the LLM and Obsidian see the same files at the same paths.

If symlinks aren't available, the fallback is a junction or a regular mklink directory mirror — the script handles both.

## Policy

- **Read-only.** The wiki agent does not modify, delete, or rename anything under `second-brain/` or `obsidian-clips/`.
- **Allowlist-gated.** `.ingest-allowlist` controls what the agent may read. Default policy allowlists instrument-related folders and clippings; personal/finance/health are off-limits unless explicitly added.
- **Citation, not copy.** When a wiki page references a vault note, cite it by relative path (`second-brain/Instruments/Kora field notes 2025-11.md`). The path resolves both for the LLM and for Obsidian when you open the wiki page in the vault.
- **Inbox is ephemeral.** Items in `inbox/` are expected to move to `processed/<YYYY-MM>/` after ingest. If something sits in inbox for >2 weeks, lint will surface it.
