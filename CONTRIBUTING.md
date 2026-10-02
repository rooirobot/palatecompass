# Contributing

This is a young, actively-shifting project (see the README's work-in-progress
note) - contributions are welcome, but expect the schema and skills to keep
moving under you for a while.

## What this repo accepts

PalateCompass is a **tool**, not a shared database. Contributions should
make the tool better for everyone running their own copy - they shouldn't
add anyone's personal buying data to it.

**Welcome:**

- **Artifacts and dashboards.** Wine has a working dashboard
  (`wine/templates/cellar.html`); whisky doesn't yet. Building one,
  following the `rebuild-cellar` skill's definitions for what each tab
  means, is a substantial and welcome contribution. Improvements to the
  existing wine artifact are welcome too.
- **Skills.** Improvements to `rebuild-cellar`, `vendor-hunter`, or a new
  skill that fits the methodology.
- **Schema changes and new categories.** Changes to the JSON shapes, or
  scaffolding a new category folder (beer, gin, brandy, ...) with the same
  layout as `wine/` and `whisky/`.
- **Docs and bug fixes.** Typos, clearer explanations, broken behaviour.

**Not accepted:**

- **Vendor files.** The vendor files already in `wine/vendors/` and
  `whisky/vendors/` are seed examples that show the schema in use. They
  aren't a directory to grow. Which retailers you buy from is your own
  research, and it belongs in your own copy (the `vendor-hunter` skill is
  there to help with it). PRs that add new vendors, or refresh prices and
  delivery details on the existing ones, will be closed.
- **Ratings, palate patterns, or recommendations.** `data/ratings.json`,
  `data/palate.json` and your favourite bottles are personal to whoever
  runs their copy of this repo. Example data in a PR has to be clearly
  fictional (see the seeded `cellar.html`) and must never read like a real
  verdict on a real product - see `METHODOLOGY.md` rule 1.

**South Africa only, for now.** The project assumes buying and shipping
within South Africa. Changes that generalize it to other countries
(currency, regions, non-SA vendor conventions) aren't in scope yet - if you
think one is worth it, open an issue to discuss before writing code.

## Before you open a PR

1. Read `METHODOLOGY.md`. The six rules there (verdict-only ratings,
   budget-as-average, free shipping, drink-now framing,
   patterns-as-hypotheses, categories-never-combine) and the physical repo
   layout are the actual invariants this project is built around. A PR
   that breaks one of them, even to add a nice feature, is unlikely to get
   merged as-is.
2. **Open an issue first for anything bigger than a small fix** - schema
   changes, skill changes, new artifacts, new categories. Given how young
   this project is, it's easy to duplicate effort or build in a direction
   that's about to change. Typos, docs, and obvious bug fixes can go
   straight to a PR.

## Using AI tools

AI-assisted PRs (Claude Code or anything else) are welcome. The bar is the
same as for any PR: you've read the whole change, you've run or tested it,
and you can answer review questions about it yourself.

## Reporting something sensitive

If you find something that looks like it shouldn't be public (accidentally
committed personal data, a security issue), please don't open a public
issue about it - see `SECURITY.md`.
