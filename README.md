# FlowFact ledger

Every US stock worth $2B or more that makes a big move — at least 2 standard deviations of its own recent
market-adjusted moves and at least 3% — gets one label after the close: **fact** (real news about the company:
an 8-K, earnings that moved it hard), **flow** (no company news: index changes, fund flows, rotation, tax selling,
a no-news move), **mixed** or **unknown**.

Every day's labels are written to one file and fingerprinted into a hash chain the same evening, before the next
market open. The labels themselves are published here 30 days later. Anyone can check that no day was
changed after the fact: `python verify.py` (no dependencies) recomputes every fingerprint and every link.

Each label is scored 5 and 21 trading days later. The claim under test: **moves labelled flow give back more
than moves labelled fact.** The verdict needs at least 300 scored labels of each and a t-statistic of at least 2.

## Status (2026-10-04)

- days chained: **1** · head: `d4af669fcd2a82191442631f259fb5b6db0683d0543dbab16e37e5b6042bf2ca`
- labels so far: **16**
- 5 trading days: not enough scored labels yet (flow n=0, fact n=0, spread None, t None)
- 21 trading days: not enough scored labels yet (flow n=0, fact n=0, spread None, t None)

## Files

- `chain.jsonl` — one line per trading day: date, number of labels, SHA-256 of that day's file, previous link,
  and `chain_sha256 = sha256(prev + date + file_sha256)`
- `labels/YYYY/YYYY-MM-DD.jsonl` — the day's labels, released 30 days after the day
- `scorecard.json` — the live scorecard (and, kept separate, the backtest)
- `verify.py` — the verifier

Labels are research about why prices moved. They are not investment advice and not a recommendation to buy or
sell anything. Labelling rules version: `ff-1`.
