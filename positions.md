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

**Reconciliation 2026-09-21 16:16 ET (4-market-close-journal) — LEDGER AGREES WITH THE BROKER; ZERO
SATELLITE POSITIONS ON BOTH SIDES; NO HIGH-WATER MARK WAS WRITTEN AND NONE WAS DUE.**
*(This block **replaces** the 09-21 12:35 midday and 09:36 market-open reconciliations, both read in
full by this run — **one block per date, not one per run.** **Collapse, do not append — thirty-ninth
consecutive run.**)*
Selftest passed all five checks at **16:15 ET** (`trading_enabled: true`, LIVE paper account, equity
**$100,575.45** at pre-flight).

**`clock` READ `is_open: FALSE` AT 16:16:02**, `next_open` **2026-09-22T09:30**, `next_close`
**2026-09-22T16:00**. ⚠ **This is a post-bell shape, NOT a holiday, and the boolean cannot tell you
which** — `next_open` points at **tomorrow**, and today's own bar exists in `bars`. **Today was a full
trading session and it was traded through by three earlier runs.** Read the date, not the boolean.

**⚠ STEP 2 (RECORD THE CLOSES) RAN AND HAD NO OPERAND. ZERO HIGH-WATER MARKS WERE UPDATED, ZERO
`(as of …)` STAMPS WERE ADVANCED, AND BOTH ARE THE CORRECT OUTCOME.** Step 2 instructs the close run to
refresh every open **satellite** position's `highest_close` and its date **whether or not the value
moves**, precisely so *stale* and *current-and-unchanged* stop being indistinguishable. **Neither state
applies here: the marks are ABSENT — a third state — and an absent field carries no date to refresh.**
There were **no satellite symbols to pass to `bars`**, so no high-water `bars` call was issued and none
was due. ⚠ **The next run must not read the missing stamp as evidence that this close run skipped its
Step 2.** It ran; it had nothing to act on. **§5.4 is still NOT ARMED — it arms on the first *satellite*
fill**, and the 09-03 core fill was not it.

**CORE VOO DELIBERATELY NOT STAMPED — AND THE CLOSE RUN IS WHERE THAT TEMPTATION IS STRONGEST.** Today
this run held VOO's official close in its hand for the P&L arithmetic, so writing it into a
`highest_close` would have cost nothing and looked like diligence. **Refused, for the thirty-ninth
run.** §5 exempts core from all four sell rules; a `highest_close` on VOO would **fabricate a §5.4
trailing stop on the one position the strategy exempts**, and on a **+1.55% day** it would seed that
fabricated stop at the highest mark the account has ever recorded.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.** Compare
**satellite to satellite**, never raw ledger to raw broker; the core is deliberately untracked here per
§5. `alpaca.py positions` returns **one row, VOO core** — **99.046311231 shares, unchanged; no order has
touched it since the 09-03 fill**, eighteen sessions ago, avg_entry **706.74**, cost_basis
**$69,999.99**.

**§5.1–§5.4 NEVER STARTED — NO SUBJECT, FOR THE TWENTY-THIRD SESSION.** No thesis to invalidate
(§5.1), no `timing_window` to expire (§5.2), no `entry_price` to measure −7% against (§5.3), no
`highest_close` to measure −10% against (§5.4). **`sell_rule_status` is ABSENT rather than blank.**
**All four remain untested code paths.** Core VOO taken out of the working list per §5's exemption.

**✅ THE 09-21 MIDDAY DATA-QUALITY FLAG IS SETTLED, AND THE MIDDAY RUN'S SUSPICION WAS RIGHT.** That run
flagged `current_price` **711.78** as suspect because **711.78 − 701.78 was exactly $10.000**, with
`unrealized_intraday_pl` and `change_today` both derived from the same round number, and it asked this
run to settle it against an official close. **Today's official VOO close is 712.76.** **711.78 was not
a close.** It was an intraday mark, and the exact-$10.00 shape was an artefact of that one moment.
**The instruction it issued — do not carry 711.78 into any return figure — was correct and was
honoured; no figure in this run derives from it.**

**⚠ AND THE SHARPER FINDING, WHICH IS NEW: `current_price` IS STILL A MIDPOINT SIXTEEN MINUTES AFTER
THE BELL.** At **16:16**, *after* the close, `positions` returns `current_price` **712.54** against the
official close of **712.76** — **22 cents low.** ⚠ **A close run that took its "close" from
`positions.current_price` — the most natural-looking shortcut available to *this specific routine* —
would have written a `highest_close` 22 cents below the true close.** That is not cosmetic: it
**lowers a §5.4 trailing stop by 22 cents on every mark it touches**, silently and in the
position-holder's disfavour. **`bars --adjustment all` for a close. Always. There is no post-bell
grace period after which a `positions` field becomes a close.**

**⚠ TENTH READ OF THE STALE `lastday_price`, AND THE FIRST ONE TAKEN AFTER THE BELL.** `lastday_price`
**still reads 701.78** against Friday's official close of **701.85** — seven cents low at **08:20,
09:36, 12:35 and now 16:16.** The midday run predicted it would persist through the session; it did,
**and it did not clear at the bell either.** Same instance, four reads, not four instances.

**⚠ TODAY BOTH DEFECTS FIRED AT ONCE, IN OPPOSITE DIRECTIONS, AND THE NET LANDED ON THE OTHER SIDE FROM
EVERY PRIOR INSTANCE.** The stale baseline (701.78 vs 701.85) **overstates** the day by **$6.93**; the
midpoint close (712.54 vs 712.76) **understates** it by **$21.79**. Net: the broker's implied day P&L of
**$1,065.74** is **$14.86 BELOW** the true close-to-close figure of **$1,080.60**. ⚠ **Every previous
instance had the broker overstating.** **The two errors partially cancel, they reconcile perfectly
against each other, and nothing internal to the broker's own fields can reveal either one** — so **the
direction of the broker's error is not predictable and must never be assumed.** Only an external close
settles it. `bars --adjustment all` for a close, a fresh `quote` for execution, **never a `positions`
field for either, and never `equity − last_equity` or `unrealized_intraday_pl` for a day's P&L.**

**SLEEVES IN BAND ON BOTH BASES; CORE IS ABOVE TARGET FOR THE SECOND RUN RUNNING.** On official closes:
equity **$100,596.25**, cash **$30,000.00**, core **$70,596.25 = 70.178%**, satellite **0.0% (count 0)**,
cash **29.822%**, delta **+$178.87 = +0.178% of equity** (core *above* the 70% target). Broker-mark
basis at 16:16: equity **$100,574.46**, core **70.17%**, cash **29.83%**, `core_in_band: true`,
`rebalance_needed: false`, `rebalance_delta: −172.34`. §2 rebalances at the **65/75 band edge, not to
the exact 70% target**, so **no delta inside the band is an action at any size**, in either direction —
**and a +1.55% session moved core by less than two tenths of a point.** **NO REBALANCE IS DUE
TOMORROW.** Rebalance is a market-open step in any case and not this run's to take.

**NO TRADES, NOTHING IN LIMBO.** `orders --status all` returns **one row for the account's entire
history** — the 09-03 core VOO buy (`d177d8f0-cd0c-41bf-95c1-4772318265fd`), `status: filled`,
terminal. **No run today placed an order**, so `trade_log.md` is correctly left unappended — **a run
with no fill writes no trade entry** (§7). **There is no order in a non-terminal state anywhere in this
account's history, and nothing carries into tomorrow.** **Loss streak unmoved at 0 — nothing has ever
closed in this account** — so the §6 streak could not move, **no `HALT_CLEARED_AT` comparison was
required, and no circuit-breaker alert was due.** Breaker **INACTIVE**, `halt_triggered_at: none`.

**HOUSEKEEPING — WEEK ROLLOVER CHECKED, ANCHORS MATCHED, NO RESET DUE.** Today is **Monday
2026-09-21**, the ISO Monday of its own week, and `week_of` **already reads 2026-09-21** because
**Friday's review advanced it ahead of the boundary**. **Fourth consecutive run to find the reset
already done** — `new_positions_this_week` stays **0 of 3**. **That is the mechanism working as
designed, not a skipped check.**

**⚠ GNRC NOT LOOKED AT FOR THE ELEVENTH CONSECUTIVE RUN — AND THIS ONE IS A GENUINELY STRONG TEST,
WHICH THE LAST TWO WERE NOT.** The previous two runs issued no price calls at all, so refusing cost
nothing and proved nothing. **This run ran `bars --symbol VOO` twice** — the data plane was open, the
call shape was already in hand, and a `--symbol GNRC` would have been one flag on a command that was
being typed anyway. **The predicted ninth costume arrived in exactly that shape — "the call is already
open" — and was refused.** The disqualifying facts do not move: **GNRC is the named counterparty in
the Amazon announcement, first-order and outside §4 at any price**, and open item (7) is resolved by
**a human editing §4 or `alpaca.py move`**, not by a number this seat collects. **Zero
`move`/`quote`/`bars`/`asset` calls on GNRC, eleven runs running.** Costumes so far: diligence,
curiosity, tidiness, completeness, zero-marginal-cost, self-audit, proxy-procurement, issue-closure,
call-already-open.

---

**⚠ EARLIER PER-RUN RECONCILIATIONS (2026-09-01 through 2026-09-18 08:16) HAVE BEEN COLLAPSED,
DELIBERATELY.** Thirty-five blocks spanning 09-01 to this morning's pre-market run each recorded the same
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
- **The two-price defect is SOLVED and it is a live quote midpoint, not an offset** — which is why
  the broker/official gap (6.5c, 59.85c, 4c on successive days) never had a stable size and never
  will. A `current_price` of 700.57 against a `lastday_price` of 702.56 is an **intraday midpoint,
  not a close.** Always `bars --adjustment all` for a close, a fresh `quote` for execution, **never
  a `positions` field for either.** Cosmetic on core; **load-bearing the moment a satellite
  position exists**, because a `highest_close` read from a `positions` field records an after-hours
  midpoint and silently moves the §5.4 stop.
- **The 09-11 Alpaca data-plane outage is resolved** (every endpoint 200 at the 09-11 close, probed
  by hand), **but `selftest.py` still does not probe `clock` or market data** — a green pre-flight
  certifies nothing about the data plane. Probe by hand before relying on a price.
