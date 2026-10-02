> **🚧 Work in progress.** This is a young project, seeded from a private
> personal tool and opened up for others to build on. Expect the schema,
> the skills, and the artifact to keep shifting for a while yet — this
> will take many moons to settle down. Don't build anything load-bearing
> on top of it just yet.

# PalateCompass

A personal drinks-buying system. It exists to do two things: keep a
permanent record of what you actually liked, and use that record to pick
better bottles next time.

Two things worth knowing up front:

- **This project is South-Africa-focused by design**, not a generic
  international tool. The vendor directory (see `wine/vendors/` and
  `whisky/vendors/`) is built around real South African retailers, and the
  whole thing assumes you're buying (and shipping) within South Africa.
  If that's not you, the schema and methodology still generalize, but
  you'll need your own vendor research.
- **Only wine has a built artifact so far** (`wine/templates/cellar.html`,
  seeded here with fictional example data). Whisky has its schema, budget
  tiers, and scaffolded vendors, but no dashboard yet — a good first
  contribution for someone who wants one.

## What this actually is

A repo, not an app you install. It's organized by category (wine, whisky,
and whatever you add next), each with:

- `data/profile.json`, `data/budget.md` — your buying intent and spending
  tiers.
- `data/ratings.json` — the verdicts. This is the whole point: every entry
  reflects something you actually stated, never an inference from what you
  bought.
- `data/palate.json` — patterns inferred from your ratings, each tracked as
  a hypothesis with a confidence level, not a fact.
- `vendors/` — one file per retailer: delivery policy, constraints, known
  product URLs.
- `templates/` — a browsable dashboard artifact, where one exists.

Read `METHODOLOGY.md` for the six rules this whole system runs on
(verdict-only ratings, budget-as-average, drink-now framing, and so on) —
that's the actual scaffolding value here, independent of whose data ends
up in it.

## Quick start

1. Fill in the root `profile.json` and each category's `data/profile.json`
   with your own details.
2. Set `data/budget.md`'s `day_to_day` target to your own real per-bottle
   average - the other tiers derive from it via the formula documented
   there.
3. Start rating. The first entries in `data/ratings.json` will feel sparse
   - that's normal. If you're importing from an existing spreadsheet or
   tasting log instead of starting from zero, see
   `docs/importing-tasting-data.md`.
4. Once you have a vendor confirmed (free shipping, stock that fits), add
   it to `vendors/` following `_template.json`'s shape.

## Contributing

See `CONTRIBUTING.md`. Contributions that improve the tool itself are
welcome: dashboards (whisky doesn't have one yet), skills, schema changes,
docs and bug fixes. Vendor lists, ratings and palate data are personal to
each copy of this repo, so they aren't accepted as contributions.

## License

MIT - see `LICENSE`.
