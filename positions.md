# Open Positions Ledger

**AGENT-OWNED.** One block per open **satellite** position. The core holding is not
tracked here — it is never sold on news (§5) and needs no thesis state.

Alpaca is authoritative for what is held and at what cost. This file exists for the
things Alpaca does not store and that §5 cannot be enforced without:

- the **highest close since entry**, without which the §5.4 trailing stop does not exist
- the **timing window deadline**, without which the §5.2 time stop never fires
- the **invalidation condition**, verbatim, because §7 forbids softening it later —
  keeping it written down is what makes softening visible

**High-water maintenance:** the market-close routine writes every open position's official
close into `highest_close` each day (only if it is higher). If a close run was skipped, the
next run must backfill from `python scripts/alpaca.py bars --symbol X --days N` before
evaluating §5.4. A gap in this field silently disables the trailing stop, which is the kind
of failure that looks like nothing is wrong.

---

## Template

```
### <TICKER> — <thesis-id>

- entry_date:            YYYY-MM-DD
- entry_price:           0.00
- qty:                   0.000
- notional_at_entry:     0.00
- pct_of_account_entry:  0.0%
- voo_close_at_entry:    0.00  (adjustment=all — the same-period baseline for this position)
- asset_type:            stock | etf
- market_cap_at_entry:   $00.0B
- market_cap_source:     <where the figure came from>
- highest_close:         0.00  (as of YYYY-MM-DD)
- timing_window:         <next earnings | Q_ YYYY>  → deadline YYYY-MM-DD
- invalidation:          <verbatim from the thesis, part 4 — never reworded>
- sell_rule_status:      <which of §5.1–5.4 are near triggering, and the distance to each>
- driver:                <the underlying catalyst, for the §4 correlation check>
```

The `driver` line is what makes the correlation check possible. Before opening anything new,
the pre-market routine reads every `driver` here and rejects a candidate exposed to the same
one — otherwise you are making a single bet spread across several tickers and mistaking it
for diversification.

`voo_close_at_entry` is recorded once, at entry, and never updated. The Friday review needs
each position measured against what the same capital would have done in VOO over that
position's own holding window; capturing the baseline at entry means the review never has to
re-derive it from price history, and it stays correct for positions closed months later.

---

## Open positions

*(none — no **satellite** positions have been opened yet. Core VOO exists and is deliberately not tracked here, per the top-of-file rules and the fill note further down.)*

**Reconciliation 2026-09-10 12:34 ET (3-midday-management) — RECONCILED ON A LIVE TAPE. NO
SATELLITE POSITION EXISTS, SO THERE IS NOTHING TO MANAGE: NO HIGH-WATER MARK TO REPAIR, NO §5 RULE
WITH A SUBJECT, NO EXIT TAKEN. ZERO ORDERS WERE PLACED.** *(This block replaces the 09-10 09:36
open reconciliation, which was read and acted on by this run and carries nothing this one does not.
Collapse, do not append — tenth consecutive run.)* Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, equity $98,986.75). **`clock` at 12:34:49 ET returns
`is_open: true`, `next_close: 2026-09-10T16:00 ET` — the market was OPEN and this run reconciled
against a live tape, not a dry run and not a closed-market skip.**

`alpaca.py positions` returns **one row, VOO core** (99.046311231 shares, avg_entry 706.74,
market_value $68,986.75, broker `current_price` **696.51**, `lastday_price` 700.87, `change_today`
**−0.622%**, unrealized_pl **−$1,013.24, −1.447%**). `alpaca.py sleeves`: equity **$98,986.75**,
cash $30,000.00, core **69.69%**, satellite **0.0% (count 0)**, cash 30.31%, `core_in_band: true`,
`rebalance_needed: false`, `rebalance_delta: +303.98`.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.**
Compare **satellite to satellite**, never raw ledger to raw broker.

**⚠ THIS RUN IS EXITS-ONLY AND OPENED NOTHING — the rule that was most exposed today.** The midday
routine may not open a position; new positions go through pre-market research and the 09:35
execution run, always, because that path is what forces every buy to sleep on a written thesis.
**The setup at 12:34 was the maximally tempting one:** breaker clear, weekly cap 0 of 3, **30.31% of
the book in cash**, a core red for an eighth session, and a run whose whole output is "nothing to
do." **The six names rejected at 08:23 — LMT, GFS, MPWR, EQT, LEU, the sponsor banks — were sitting
in the log with prices four hours stale, and re-pricing any of them here would have routed a new
idea through the one door built to stop exactly that.** None was re-priced. **No `move` call, no
Perplexity query, no quote was pulled for a candidate.** A midday entry does not read as a rule
breach in a one-line summary; it reads as initiative.

**⚠ THE HIGH-WATER FIELD IS ABSENT, NOT STALE, AND NO BACKFILL WAS OWED — checked against the
actual trigger, not assumed.** Step 2 compares the `(as of ...)` date on `highest_close` to the last
trading day. There is **no `highest_close` and no `(as of ...)` date anywhere in this file**, because
there is no satellite position block to carry one — **an absent field has no date, so it cannot be
behind.** The marks are **ABSENT: a third state, distinct from both "current and unchanged" and
"stale."** **No `bars` call was due for a high-water purpose and none was made for one.** Core VOO
was again deliberately not given a mark — stamping one would fabricate a §5.4 trailing stop on the
one position §5 exempts from all four rules. **§5.4 remains NOT ARMED, not disabled, not skipped.**
**The failure this step exists to catch is still ahead of us:** the day a satellite position exists
and a close run is missed, the mark goes stale while every field still reads present and plausible,
and the trailing stop silently stops existing.

**Step 3 (§5.1–§5.4) had no subject.** No thesis to test for invalidation (§5.1); no timing window
to expire (§5.2); no entry price to measure −7% against (§5.3); no high-water mark to measure −10%
against (§5.4). `sell_rule_status` is **absent rather than blank** — there is no position block to
carry the field. **No §5.1 Perplexity invalidation query was issued and none was due**, since there
is no holding to check news against. **Step 4 executed no exits because none triggered — not
because an exit was suppressed.** Nothing should have fired and did not.

**⚠ The two-price trap, still live at midday.** Broker `current_price` **696.51** at 12:34,
`lastday_price` **700.87**, against 09-09's official close **700.805** — the broker's "last day"
figure is **6.5 cents above** the official close it purports to be, unchanged from this morning and
from the bell. Always pull `bars --adjustment all` for a close and a fresh `quote` for execution —
**never a `positions` field for either.** The day a satellite position exists, that shortcut writes
a wrong high-water mark that does not error, does not look stale, and silently moves the §5.4 stop
to a level nobody chose.

**§2 rebalance: NOT DUE, and not this routine's call in any case.** 69.69% sits well inside the
65–75% band; `core_in_band: true`, `rebalance_needed: false`, and the +$303.98 delta is **0.31% of
equity** — VOO's mark moving, not drift. §2 rebalances at the **band edge** (65/75), not to the
exact target, and §2 places the rebalance at the **next market-open run**, not at midday.

**⚠ The core's mark has now been negative eight sessions running and is through −1.4%. It still
means nothing procedurally.** −$1,013.24 (−1.447%) against the 706.74 fill, with **−0.622% of that
coming today**, and the loss crossing $1,000 for the first time. **§5 exempts core from all four
sell rules.** A round number is not a threshold — not −1.4%, and not $1,000 — and there is no §5.3
or §5.4 on this position to cross. **A midday run whose only holding is a core through −1.4%, on a
book with 30% cash and a clear breaker, is precisely the setup in which core gets sold "as a stop"
by a routine whose entire vocabulary today is selling.** It was available and was not taken. **It is
not a stop, available capacity is not a mandate, and a quiet run is not a reason to act.**

---

**⚠ EARLIER PER-RUN RECONCILIATIONS (2026-09-01 through 2026-09-10 09:36) HAVE BEEN COLLAPSED,
DELIBERATELY.** Twenty-three blocks spanning 09-01 to the 09-10 open run each recorded the same
null result — zero satellite blocks checked against zero satellite Alpaca positions, agreeing; no
§5 rule evaluated; no high-water mark to stamp; no backfill due. `state.md` flags this
accumulation as
actively harmful rather than untidy: this repo's only continuity mechanism is the next run
*reading* these files, and padding them with restatements of one null fact raises the odds that
a genuinely live item gets skimmed. Carry-forward is defined as **cleared once acted on**, and
each of those blocks was acted on by the run that read it. **The correct response to the pull to
append is to collapse, not to add another.** Nothing live was discarded — the load-bearing facts
those blocks carried are preserved here:

- **The only fill in this account's history: BUY VOO 99.046311231 @ $706.74, notional
  $70,000.00**, order `d177d8f0-cd0c-41bf-95c1-4772318265fd`, filled **2026-09-03 09:36:21 ET**,
  verified terminal before it was written. Audit record in `trade_log.md`.
- **Measure the core from the 706.74 fill, not from a prior VOO close.** The fill landed
  **+0.483% above the previous close**, and that one-time entry gap — not tracking error and
  never skill — is the whole of the core's reported divergence from VOO.
- **The core is not tracked in this ledger by design.** §5 exempts it from all four sell rules,
  so it has no thesis state, no timing window and no `highest_close`. **Every reconciliation
  compares satellite blocks to satellite Alpaca positions**; a run that compares the raw ledger
  to the raw broker will read a correct ledger as broken.
- **§5.4 has never been armed.** It arms on the first *satellite* fill. The 09-03 core fill was
  not that day, and no day since has been either.
- **All four §5 sell rules remain untested code paths.** Nothing has ever closed, so the string
  of "no exits" entries recorded the absence of a subject, not clean bills of health.
