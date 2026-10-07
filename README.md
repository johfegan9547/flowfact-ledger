# FlowFact ledger

Every US stock worth $2B or more that makes a big move — at least 2 standard deviations of its own recent
market-adjusted moves and at least 3% — gets one label after the close: **fact** (real news about the company:
an 8-K, earnings that moved it hard), **flow** (no company news: index changes, fund flows, rotation, tax selling,
a no-news move), **mixed** or **unknown**.

Every day's labels are written to one file and fingerprinted into a hash chain the same evening, before the next
market open. The labels themselves are published here 30 days later. Anyone can check that no day was
changed after the fact: `python verify.py` (no dependencies) recomputes every fingerprint and every link.

Each label is scored 5 and 21 trading days later. The claim under test: **moves labelled fact keep going more
than moves labelled flow** (news drifts; no-news moves stall or give some back). The verdict needs at least 300
scored labels of each and a t-statistic of at least 2, computed with moves grouped by week (5 days) or month
(21 days) so that one busy day cannot count as hundreds of independent results, and with the most extreme 1% of
outcomes at each end capped.

## Status (2026-10-07)

- days chained: **3** · head: `bdeaf5e6a9c14caff0d19737adbbe301bbbff91f361ba9688bc6b64b99110366`
- labels so far: **96**
- 5 trading days: not enough scored labels yet (flow n=0, fact n=0, gap None, clustered t None)
- 21 trading days: not enough scored labels yet (flow n=0, fact n=0, gap None, clustered t None)

## Pre-registered claims

Written down, fingerprinted and published before the live data that will judge them. A registered claim is never edited; only labels dated on or after its *counts from* date count. Full register: `claims.jsonl`.

| id | claim | registered | counts from | horizon | live gap · t · verdict | backtest gap · t |
|---|---|---|---|---|---|---|
| P1 | Fact-labelled moves keep going more than flow-labelled moves (all big moves) | 2026-10-05 | 2026-10-02 | 5d | — · None · not enough scored labels yet (need 300 of each) | +0.47% · 5.76 |
| P1 | Fact-labelled moves keep going more than flow-labelled moves (all big moves) | 2026-10-05 | 2026-10-02 | 21d | — · None · not enough scored labels yet (need 300 of each) | +0.61% · 3.41 |
| S1 | No-news drops recover more than news drops over a month (down moves) | 2026-10-05 | 2026-10-05 | 21d | — · None · not enough scored labels yet (need 200 of each) | +0.82% · 2.67 |
| S2 | The gap is clearest for 3–5σ moves | 2026-10-05 | 2026-10-05 | 5d | — · None · not enough scored labels yet (need 200 of each) | +0.74% · 5.3 |
| S2 | The gap is clearest for 3–5σ moves | 2026-10-05 | 2026-10-05 | 21d | — · None · not enough scored labels yet (need 200 of each) | +1.04% · 3.57 |
| X1 | Up moves over a month — watching, no prediction | 2026-10-05 | 2026-10-05 | 21d | — · None · watching — no prediction registered | +0.38% · 1.52 |

## Files

- `chain.jsonl` — one line per trading day: date, number of labels, SHA-256 of that day's file, previous link,
  and `chain_sha256 = sha256(prev + date + file_sha256)`
- `labels/YYYY/YYYY-MM-DD.jsonl` — the day's labels, released 30 days after the day
- `scorecard.json` — the live scorecard (and, kept separate, the backtest)
- `claims.jsonl` — the register of pre-registered claims: id, date registered, date it counts from, SHA-256 of the definition
- `verify.py` — the verifier

Labels are research about why prices moved. They are not investment advice and not a recommendation to buy or
sell anything. Labelling rules version: `ff-1`.
