# Methodology

This describes the rules this project's tooling follows, independent of
whose data lives in it. If you're using this repo (or the public
PalateCompass scaffold seeded from it) as a starting point for your own
drinks-buying tracker, these are the invariants worth keeping — `CLAUDE.md`
covers the repo owner's own specifics on top of these.

## Repo layout

The repo is organized by category, physically, not just by convention —
this mirrors rule 6 below:

```
profile.json          shared identity only (owner, location, currency) - not budget or vendor data
<category>/
  data/                profile.json (vendor/status), budget.md (spending tiers), ratings.json, palate.json, orders/
  vendors/             one file per retailer
  templates/           artifacts for this category (dashboards, trackers)
```

A new category (beer, gin, brandy, ...) gets its own sibling folder with
the same shape.

## The rules

**1. A verdict only enters a category's `ratings.json` when the owner
explicitly states it.** Never infer one from purchase history. A bottle
reordered five times can still be a miss — purchase frequency is not
preference. This is the easiest mistake to make with this kind of dataset,
and it corrupts everything downstream.

**2. Budget is an average, not a ceiling.** Say your day-to-day target is
some amount per bottle across a multi-bottle order — a bottle well above
that target is fine if a cheaper one balances it out. Don't filter the
catalogue at the target price. Each category can also define multiple
spending tiers (day-to-day / feeling lush / really fancy / won the lotto,
uncapped) in its own `data/budget.md` — "average, not ceiling" still
governs order-building inside whichever tier is picked.

**3. Shipping is free. Ignore it in comparisons.** For any new vendor,
free delivery is a requirement, not a nice-to-have.

**4. These are drink-now bottles.** No cellaring, no drink windows, no
laying down. If a suggestion depends on keeping a bottle for years, it's
the wrong suggestion. (If your use case genuinely is a cellar/aging
collection, this rule — and a lot of the rest of this repo's design —
isn't built for you.)

**5. Patterns in a category's `palate.json` are hypotheses, not laws.**
Each carries a `status` and most carry an `open_test`. When a new rating
bears on one, update the pattern — including downgrading it.

**6. Categories never combine.** Wine, whisky, and any future category
(beer, gin, brandy, etc.) each get their own data, own artifacts, own
palate patterns. Never merge them into one database, dashboard, or filter
set — not even as a convenience once the tooling could technically support
it. A shared branded artifact with separate tabs per category is fine; a
shared *view* mixing bottles across categories is not.

## Working an order

Open orders live in `<category>/data/orders/` with a `status` per line. As
verdicts come in: update the line, then add or update the bottle in
`<category>/data/ratings.json`, then check whether any pattern in
`<category>/data/palate.json` is affected.

## Rating a bottle outside an order

Not every verdict comes from a tracked order — plenty get tasted on the
go (a restaurant, a friend's place, a bottle bought elsewhere). Same rule
as above: the verdict has to be explicitly stated, but there's no order
line to update. When it happens:

1. Check whether it matches an unrated line in an open order first (if it
   looks like a plausible match — name/producer/vintage can differ
   slightly from a scrape — confirm with the owner before merging rather
   than creating a duplicate entry).
2. If it's genuinely new, add it straight to `ratings.json` with whatever
   detail is known. Fields like `source`, `times_ordered`, or a
   vendor-specific price are optional and can be left out entirely for a
   bottle bought outside any tracked vendor.
3. Check `palate.json` for any pattern this bears on and update it.
4. Bump `count` and `last_updated` in `ratings.json`.

## Building an order

1. Re-scrape the vendor for current prices and stock — prices in a repo
   like this go stale and stock moves constantly.
2. Anchor on proven hits. Most of the order should be bottles already
   rated.
3. Allow one or two experiments, chosen against `palate.json`, not at
   random.
4. Check the running average lands near the day-to-day tier's target.
5. Confirm the vendor's case constraints before finalising — these change.

If you're bootstrapping `ratings.json` from an existing pile of tasting
notes rather than starting from zero — a spreadsheet, a tasting club's
scoresheet — see `docs/importing-tasting-data.md` for the technique this
project used to do that safely.
