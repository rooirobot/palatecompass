# Importing unstructured tasting data

If you (or a group you've tasted with) already has some record of past
tastings — a spreadsheet, a shared notes doc, a tasting club's scoresheet —
you don't have to start a category's `ratings.json` from zero. This
project bootstrapped its own whisky ratings from a multi-person whisky
club's tasting spreadsheet using the technique below, generalized here so
it applies to whatever messy source you've got.

## The core problem

Group tasting records almost always mix several people's opinions in one
place — a "group average," a highlighted "top pick," other tasters'
individual scores sitting in adjacent columns. None of that is *your*
verdict, even when it's sitting right next to your actual score in the
same row.

## The technique

1. **Identify which single column/field is actually your own score.** If
   there isn't one — say only a group average was recorded — that record
   can't be imported at all. You don't have a stated verdict there, only a
   proxy for one. Skip it rather than guessing.
2. **Map your raw score onto this project's verdict scale** (`hit`/`ok`/
   `miss`). Pick your own cut points — top/middle/bottom third of your own
   scoring range is a reasonable default, or whatever mapping matches how
   you actually think about the categories.
3. **Import only your own score as the verdict.** Everything else in the
   source record — other people's scores, a computed average, any
   "recommended" or "top pick" flag — either gets dropped, or at most
   preserved as free-text context in a `note` field. Never as the verdict
   itself.
4. **Enrich afterward, separately.** Once verdicts are in, a second pass
   can fill in metadata (distillery/region/style, flavor descriptors, ABV)
   from an external reference source. Tag each enriched entry with where
   that metadata came from (a `metadata_source_url` field works well) so
   it stays clear the descriptive detail and the verdict came from
   different places.
5. **Never let a competition score, a critic's rating, or any database's
   community score substitute for a real verdict**, even temporarily. If
   you don't have your own stated opinion on something yet, it doesn't go
   in `ratings.json` yet.

## Why this matters

The whole value of a tracker like this is that its ratings are unusually
trustworthy — every entry reflects an opinion someone actually stated, not
an inference, an average, or someone else's taste. That guarantee is worth
protecting even when "someone else's taste" is sitting in the exact same
spreadsheet, one column over.
