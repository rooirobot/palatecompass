---
name: vendor-hunter
description: >-
  Search online for new retailer candidates in a given Cellar category (wine,
  whisky, or a future one) that fit the buying brief - free shipping (ideally
  unconditional), stock that actually carries the styles/producers the owner
  buys, and a price band matching that category's budget. Scaffolds each
  finding as a vendors/<slug>.json candidate file. Use when the owner asks to
  find more vendors, check for alternatives to the current one, or hunt for
  retailers for a category that doesn't have one yet.
---

# Vendor hunter

Always operates on exactly one category at a time (`wine/`, `whisky/`, or a
future sibling folder) and only ever writes into that category's own
`vendors/`. Never compare or list candidates across categories in the same
pass or the same output - that's the categories-never-combine rule
(`METHODOLOGY.md` rule 6) applying to process, not just data.

## The brief

Every candidate gets checked against the same bar used for every vendor
already scaffolded in this repo:

- **Free shipping is the hard requirement**, not a nice-to-have
  (`METHODOLOGY.md` rule 3). Unconditional free shipping is the strongest
  signal. A threshold (see the existing vendor files for real examples) is
  acceptable but must be logged precisely, not glossed over - it changes
  whether a small top-up order actually clears it.
- **Stock quality**: does the catalogue actually carry the category's
  relevant styles/regions/producers (check the existing patterns in
  `<category>/data/palate.json` if one exists, or the hit list in
  `<category>/data/ratings.json` otherwise) - not just "sells alcohol."
- **Price band fit**: bottle range should sit near that category's budget
  target (`<category>/data/profile.json`'s `budget`, detailed in
  `<category>/data/budget.md`'s day-to-day tier) - see those files for the
  actual number rather than assuming one.
- **Hard blockers**, logged as a rejection or a low-priority flag rather
  than silently dropped: a site that blocks automated fetching (403s), a
  JS-rendered storefront that returns no readable content, a case-count
  minimum that doesn't fit a typical order, delivery-area exclusions.

## Process

1. Check `<category>/vendors/` first for what's already scaffolded - don't
   re-research a candidate that's already there (update its file instead if
   genuinely new information turns up).
2. WebSearch for retailers in that category, South Africa-first (see the
   root `profile.json` for the owner's actual location) unless told
   otherwise. This is enough tool-call volume to be worth delegating to a
   background agent rather than doing inline.
3. For each real candidate, fetch its delivery/shipping policy page
   specifically - don't infer free shipping from a homepage. If the fetch
   returns no usable content (bot-blocked or JS-rendered), say so explicitly
   in the candidate's `contact.note` / `delivery.note` rather than treating
   silence as "not free."
4. Scaffold `<category>/vendors/<slug>.json` from
   `<category>/vendors/_template.json`'s shape (`id`, `name`, `country`,
   `status: "candidate"`, `contact`, `delivery`, `constraints`, `scraping`,
   `product_urls`). Leave a field null/empty rather than guessing when
   unconfirmed - `whisky/vendors/liquor-city.json` is the reference example
   of an honestly-incomplete candidate file.
5. Never set `status` to anything but `candidate`. Activating a vendor
   (flipping `<category>/data/profile.json`'s `vendor`/`active` fields) is
   the repo owner's call once shipping is actually confirmed, not something
   this skill decides on its own.
6. Any competition score, "award-winning," or star rating encountered while
   evaluating a site is irrelevant to the brief - don't record it, and don't
   let it substitute for checking the actual shipping/stock/price facts.

## Reporting

Summarize candidates ranked by fit (best first), each with: what's
confirmed, what's still unconfirmed, and the single biggest reason it would
or wouldn't beat the current active vendor. Flag explicitly if nothing
found this pass clears the free-shipping bar cleanly - a thin result is
worth saying plainly, not padding out with a marginal candidate presented
as equal to a real one.
