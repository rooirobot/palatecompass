---
category: whisky
schema_version: 1
last_updated: 2026-09-12
---

# Whisky budget tiers (example)

Four per-bottle spending tiers you set yourself, that the rest of the repo
reacts to (Hitlist filters, Database filters, Next Order's tier prompt).
Same formula as `wine/data/budget.md`, applied to whisky's own anchor.

**The figures below are illustrative placeholders, not a recommendation.**
Replace `day_to_day`'s target with your own real day-to-day per-bottle
average and the rest follow from the formula.

## The formula

Each tier has a `target` and a `range`. The range is `-30%` to `+20%` of
the target. Tiers stack: a tier's range floor is the prior tier's range
ceiling, so there's no gap and no overlap. That fixes the ratio between
consecutive targets at `1.2 / 0.7 ≈ 1.714×` — set the day-to-day target
and the rest follow. The top tier is the one exception: it has no
`range_high` — "won the lotto" is deliberately open-ended, not bounded by
the same formula that caps every tier below it.

```
range_low  = target * 0.7            (top tier: prior tier's range_high)
range_high = target * 1.2            (top tier: none - open-ended)
next_target = target * (1.2 / 0.7)
```

## Tiers (example figures — replace with your own)

| Tier | Target (R) | Range (R) |
|---|---|---|
| day_to_day | 450 | 315–540 |
| feeling_lush | 770 | 540–920 |
| really_fancy | 1,320 | 920–1,580 |
| won_the_lotto | 2,260 | 1,580+ |

`day_to_day` should be set from your own real whisky spending. The rest
are derived from the formula above, not separately guessed.
`won_the_lotto` uses the same formula but with no ceiling on principle —
there's no number that should stop a lottery-win splurge.

## How the repo should react

- **Hitlist tab / Database tab**: filter chips per tier (day-to-day /
  feeling lush / really fancy / won the lotto / all). A whisky with
  `price == null` stays included but flagged unknown.
- **Next Order tab**: ask which tier before proposing an order, so the
  research pass targets that tier's range rather than a single fixed
  average.
- No per-order minimum spend or case-count logic changes because of this —
  tiers are a per-bottle filter, not an order-level budget.

## Note on wine's rule 2

`METHODOLOGY.md`'s "budget is an average, not a ceiling" rule still applies
independently within whichever tier is selected — a day-to-day order
should average near the target, not have every bottle sit at exactly the
target.
