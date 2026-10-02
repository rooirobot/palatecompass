# Proposal: importing a user's Vivino history

**Status:** proposal / discussion, no code yet.

## The idea

Many wine drinkers already have years of tasting history in
[Vivino](https://www.vivino.com/): star ratings, reviews, comments, and the
wines they scanned. Today a new PalateCompass user starts `ratings.json`
from zero. Bringing their Vivino history across would give the palate
patterns real data on day one, instead of weeks of sparse entries.

The goal is to let a user pull *their own* Vivino history into their own
copy of this repo, as a one-time or occasional import.

## Why not an API or scraping

Both were the obvious first ideas, so it's worth recording why they're the
wrong default:

- **No public API.** As far as I could find, Vivino doesn't offer a public
  API to third parties. Worth re-checking before building anything, since
  this can change.
- **Scraping a logged-in account is against Vivino's terms.** Their terms
  prohibit accessing the platform through automated means, scraping tools,
  crawlers or bots unless Vivino has authorized it. A feature that logs into
  someone's account and crawls it would put every user of this repo in
  breach, and would need the user's Vivino password handled by a tool in this
  repo, which is a bad trade for a personal project.
- **Fragile even if allowed.** Scrapers break whenever the site changes.

## Recommended approach: user-initiated data export, then import

Vivino's privacy policy grants users a right to data portability: a copy of
their personal data in electronic format, requested via privacy@vivino.com or
the contact form at https://www.vivino.com/contact (Vivino may ask to verify
identity first).

That makes the clean path:

1. The user requests their own data export from Vivino. (Docs in this repo
   explain how.)
2. The user drops the file they receive into a local, git-ignored folder.
3. An importer (a skill or script, in the style of `.claude/skills/`) reads
   it and writes entries into `wine/data/ratings.json`.

No credentials, no scraping, no terms violation, and the user stays in
control of their own data.

**Open question:** I haven't seen what an actual export contains (format,
which fields, whether reviews and comments are included). The field mapping
below is a sketch and needs confirming against a real export from a willing
tester before any importer is written.

## Mapping onto this project's rules

This is the part that matters most, because it's where an import could
quietly break the project's invariants. It follows
`docs/importing-tasting-data.md` and `METHODOLOGY.md`:

| Vivino field | Goes to | Notes |
| --- | --- | --- |
| The user's own star rating | `verdict` (`hit`/`ok`/`miss`) | A rating the user explicitly gave is a stated verdict (rule 1). The user picks the cut points, e.g. top/middle/bottom third of their own range. |
| The user's own review / comment | `note` | Free text only, never the verdict. |
| Wine name, producer, region, vintage, style | matching `ratings.json` fields | Tag the source, e.g. `metadata_source_url`. |
| Vivino's **community average**, other people's ratings | **dropped** | Not the user's verdict. A database's community score must never substitute for one (import doc, step 5). |
| Scanned-but-unrated wines | **dropped** | Scanning or buying isn't a verdict, same as purchase history (rule 1). |

Things the importer should do:

- Only import wines the user actually rated.
- Make the user confirm the rating-to-verdict mapping before writing anything.
- Flag likely duplicates against existing entries and ask, rather than merge
  silently.
- Keep categories separate (rule 6): wine goes to `wine/`, nothing else.
- After import, check whether any pattern in `palate.json` is affected, and
  treat those as hypotheses, not facts (rule 5).

## Privacy

A user's Vivino history is personal data, and so is the `ratings.json` it
lands in. The export file and the imported ratings should stay in the user's
own copy of the repo and out of any public fork or PR. The importer should
keep the raw export out of version control by default (git-ignored folder).

## Suggested phases

1. **Agree the approach** (this doc). Decide whether export-and-import is the
   direction.
2. **Document the export request**: short how-to for requesting the data.
3. **Look at a real export** from a tester and finalize the field mapping.
4. **Build the importer** as a skill, with the confirmation steps above.

## Out of scope

- Logging into or crawling a user's Vivino account.
- Any ongoing sync back to Vivino.
- Using Vivino community scores, or other people's reviews, as verdicts.
