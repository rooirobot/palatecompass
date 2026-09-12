---
category: wine
schema_version: 1
last_updated: 2026-09-12
---

# Wine budget tiers (example)

Four per-bottle spending tiers you set yourself, that the rest of the repo
reacts to (Hitlist filters, Database filters, Next Order's tier prompt).
This sits alongside, not instead of, `METHODOLOGY.md` rule 2 — "budget is
an average, not a ceiling" still governs how an order is built inside
whichever tier is selected.

**The figures below are illustrative placeholders, not a recommendation.**
Replace `day_to_day`'s target with your own real day-to-day per-bottle
average and the rest follow from the formula.

## The formula

Each tier has a `target` and a `range`. The range is `-30%` to `+20%` of
the target. Tiers stack: a tier's range floor is the prior tier's range
ceiling, so there's no gap and no overlap. That fixes the ratio between
consecutive targets at `1.2 / 0.7 ≈ 1.714×` — set the day-to-day target
and the rest follow. Same formula as `whisky/data/budget.md`, applied to
wine's own anchor. The top tier is the exception: "won the lotto" has no
`range_high` — deliberately open-ended rather than capped by the same
formula.

```
range_low  = target * 0.7            (top tier: prior tier's range_high)
range_high = target * 1.2            (top tier: none - open-ended)
next_target = target * (1.2 / 0.7)
```

## Tiers (example figures — replace with your own)

| Tier | Target (R) | Range (R) |
|---|---|---|
| day_to_day | 100 | 70–120 |
| feeling_lush | 170 | 120–200 |
| really_fancy | 290 | 200–350 |
| won_the_lotto | 500 | 350+ |

`day_to_day` should be *your* real running order average, not a guess.
`feeling_lush` and `really_fancy` are derived from the formula, not
separately set. `won_the_lotto` uses the same formula but with no ceiling.

## How the repo should react

- **Hitlist tab / Database tab**: filter chips per tier (day-to-day /
  feeling lush / really fancy / won the lotto / all). A wine with
  `price == null` stays included but flagged unknown.
- **Next Order tab**: ask which tier before proposing a case, so the
  research pass targets that tier's range. Rule 2 (average, not ceiling)
  still applies inside the chosen tier — a day-to-day order should average
  near the target, not have every bottle priced at exactly the target.
