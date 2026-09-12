---
name: rebuild-cellar
description: >-
  Refresh and republish Cellar's consolidated artifact (wine/templates/cellar.html)
  - the single tabbed tool covering the wine database, the Hitlist wishlist,
  the Next Order picker, and the palate patterns dashboard. Use whenever a
  new verdict lands, the Hitlist/palate data changes, or the owner sends
  back their "Copy for Claude" selections from the Next Order tab and wants
  a fresh order proposal. The monthly Next Order round is the main
  recurring trigger.
---

# Rebuild Cellar

`wine/templates/cellar.html` is generated, not hand-edited directly for its
data. The page is a static shell (CSS + JS logic) with a `WINES`, `HITLIST`,
`PATTERNS`, `ASKS`, and `BUDGET` array/object injected straight into its
`<script>` block. `BUDGET` mirrors the tiers in `wine/data/budget.md` -
regenerate it from that file whenever its tier numbers change, same as the
other arrays.

## Regenerating after a data change

1. Edit the source data first, not the HTML: `wine/data/ratings.json` for
   wine verdicts/metadata, the Hitlist array (currently hand-maintained in
   the injector script — no dedicated file yet), `wine/data/palate.json`
   for patterns, `wine/data/budget.md` for tier targets/ranges.
2. Rebuild the injector script (the example fictional data already in
   `cellar.html` shows the exact shape each array needs — `WINES` is
   generated straight from `ratings.json`'s `hit`/`ok` entries; `HITLIST`,
   `PATTERNS`, `ASKS` are hand-authored arrays since they carry editorial
   judgment, not raw data).
3. Run it against `wine/templates/cellar.html` to replace the five consts,
   then double-check nothing was left referencing stale data.
4. Publish via whatever artifact-hosting mechanism you're using,
   republishing to the same URL rather than creating a new one each time.

## The monthly Next Order round

This is the recurring trigger, and the reason this workflow is worth having
as a skill:

1. The owner opens the Cellar artifact's Next Order tab, taps what they're
   interested in (reorder-worthy hits + Hitlist wishlist items), hits
   "Copy for Claude," and pastes the result into chat.
2. Re-scrape stock/pricing for exactly the items selected - the active
   vendor first (its `vendors/<slug>.json` file has known product URLs),
   then a secondary vendor if not found there. Worth delegating to a
   background agent given the tool-call volume.
3. Come back with an actual proposal in chat - not necessarily a new
   artifact - respecting the day-to-day tier's per-bottle average from
   `wine/data/budget.md` (average, not ceiling) and preferring vendors with
   no free-shipping threshold where possible.
4. If a stock-status fact changes (a hit comes back in stock, a
   never-priced wine gets priced), patch `wine/data/ratings.json`'s `note`
   and price fields and regenerate the artifact per above.

## Definitions

- **Database tab**: every `hit`/`ok` wine, filterable by cultivar/style,
  producer, region, and budget tier from `wine/data/budget.md`; hits+ok by
  default, toggle to hits-only.
- **Hitlist tab**: untried wines matching a live palate pattern or producer
  loyalty, filterable by the four tiers in `wine/data/budget.md`
  (day-to-day/feeling lush/really fancy/won the lotto) rather than a single
  flat band (price unknown is fine, flagged rather than excluded), sourced
  broadly - not gated by current stock.
- **Next Order tab**: NOT a static suggestion - a two-step interactive
  process, see above. The artifact only handles step 1 (the long list, a
  budget-tier picker from `wine/data/budget.md`, and the owner's picks);
  step 2 (research + proposal targeting whichever tier's range was picked)
  happens in conversation.
- **Patterns tab**: read-only - each `palate.json` pattern with
  status/evidence/open test, plus standing asks.

## Categories never combine

This artifact is wine-only, permanently - not "wine for now." This
project's core rules (see `METHODOLOGY.md`) say categories never share a
database, dashboard, or filter set, even once the tooling could technically
support it. If whisky (or another category) needs a Database/Hitlist/Next
Order/Patterns view, build it as its own separate artifact with its own
tabs - never add a category selector to this one or merge its filters
across categories.

This is enforced by the repo's physical layout, not just prose: `wine/`
and `whisky/` are separate top-level folders, each with its own `data/`,
`vendors/`, and (once one exists) `templates/`. A third category (beer,
gin, brandy, ...) gets its own sibling folder with the same `data/` +
`vendors/` shape.
