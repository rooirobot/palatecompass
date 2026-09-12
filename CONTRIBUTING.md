# Contributing

This is a young, actively-shifting project (see the README's work-in-progress
note) - contributions are welcome, but expect the schema and skills to keep
moving under you for a while.

## Before you open a PR

Read `METHODOLOGY.md`. The six rules there (verdict-only ratings,
budget-as-average, drink-now framing, patterns-as-hypotheses,
categories-never-combine, and the physical repo layout) are the actual
invariants this project is built around - a PR that violates one of them,
even to add a nice feature, is unlikely to get merged as-is.

## Easiest first contribution: a vendor file

If you're a South African drinks buyer and know a retailer with free
shipping and stock that fits (a "hidden gem" the existing vendor list
doesn't have), scaffold it as `<category>/vendors/<slug>.json` following
that folder's `_template.json` shape and open a PR. This is genuinely one
of the most useful things this repo can grow through community
contribution - real, vetted vendor data is worth more than any code change.

A couple of things worth knowing about vendor PRs:

- Prices and delivery policies drift. A vendor file is a snapshot, not a
  guarantee - if you're refreshing an existing one because its numbers
  have gone stale, that PR is just as welcome as a brand new vendor.
- Keep contact/personal information out of it unless it's a generic
  business alias (an `orders@` address, a support line) - see the existing
  vendor files for the pattern.

## Other contributions

- **A whisky (or new-category) artifact.** Wine has a working dashboard
  (`wine/templates/cellar.html`); whisky doesn't yet. Building one, following
  the `rebuild-cellar` skill's definitions for what each tab means, is a
  substantial and welcome contribution.
- **Schema or skill improvements.** Open an issue first if the change is
  bigger than a small fix - given how young this project is, it's easy to
  duplicate effort.
- **Never a data contribution.** `data/ratings.json` and `data/palate.json`
  are inherently personal to whoever's running their own copy of this repo.
  A PR that adds or changes example data in a way that looks like a real
  stated verdict for a real product will be asked to change - see
  `METHODOLOGY.md` rule 1.

## Reporting something sensitive

If you find something that looks like it shouldn't be public (accidentally
committed personal data, a security issue), please don't open a public
issue about it - see `SECURITY.md`.
