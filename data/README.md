# Deliverables Manifest Seed

This folder holds a static, machine-readable index for the sprint site hub.

- `deliverables-manifest.json` is the seeded data source for Round 23/24 lanes.
- All paths are repository-relative (for example `../clarinet`) so the site can navigate
  with static files and no runtime dependency.
- Workspace-root paths may also be used with a leading `/` when the source lives beside
  `instrument-showcase` in the broader GitHub checkout, such as `/docs/plans/...`.
- Fields are intentionally additive and lightweight to keep A0 integration simple.
- PR references are seeded from the sprint plan text for navigation context and may need
  periodic refresh if draft PR IDs change.

Suggested contract for consumers (A0):

- Filter by `items[].status_label` and `items[].readiness_label`.
- Render each round row from `items[].rounds[]`.
- Use `links.repo` as the primary card target.
- Fall back to `notes` when `status_label` is `availability-check`.
- Treat `runtime_label` as optional. When it is missing, the hub should display that the
  manifest did not declare runtime evidence instead of inventing stronger validation claims.
