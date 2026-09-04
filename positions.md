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

**Reconciliation 2026-09-04 08:27 ET (1-premarket-research):** selftest passed all five checks
(`trading_enabled: true`, LIVE paper account). Market is **closed because it is pre-market, not
a holiday** — `clock` at 08:27:46 ET returns `is_open: false` with `next_open` **today** at
09:30 ET. `alpaca.py positions` returns **one row, VOO** (99.046311231 shares, avg_entry 706.74,
current 710.94, market_value $70,415.98, unrealized_pl **+$415.99, +0.594%**, `lastday_price`
710.72); `alpaca.py sleeves` reports equity **$100,415.98**, cash $30,000.00, core **70.12%**,
satellite **0.0% (count 0)**, cash 29.88%, `core_in_band: true`, `rebalance_needed: false`,
`rebalance_delta: −124.80`.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree. No
discrepancy.** The raw ledger reads *(none)* while the raw broker returns one VOO row; that is
the expected steady state now that core exists. Compare **satellite to satellite**, never raw
ledger to raw broker, or a correct ledger reads as broken.

**`sell_rule_status` — nothing to update, because there is nothing to update it on.** Step 4 of
the pre-market routine ran in full and had no subject:

| §5 rule | Status | Why there is no distance to report |
|---|---|---|
| 5.1 thesis invalidation | **no subject** | No position block exists, so no `invalidation` line exists to test. No Perplexity news check was run on any holding, because there is no holding to check. |
| 5.2 time stop | **no subject** | No `timing_window` and no deadline to have passed. |
| 5.3 hard stop (−7% from entry) | **no subject** | No satellite `entry_price` to measure from. |
| 5.4 trailing stop (−10% from `highest_close`) | **NOT ARMED, not disabled** | No `highest_close` exists. It arms the day the first **satellite** position opens. |

**The core VOO holding is exempt from all four rules (§5) and does not get a block here**, so
its +0.594% unrealized gain is not a `sell_rule_status` line and never will be. **Do not backfill
a `highest_close` from `bars` — there is nothing to backfill.** This is the fifteenth consecutive
run recording the armed/not-armed distinction explicitly rather than assuming it carried.

**High-water mark update 2026-09-03 16:15 ET (4-market-close-journal):** selftest passed all
five checks (`trading_enabled: true`). Market **was open today and has since closed** —
`clock` at 16:15:42 ET returns `is_open: false`, `next_open: 2026-09-04 09:30 ET`. This is a
normal post-close run, **not a holiday skip**. `alpaca.py positions` returns **one row, VOO**
(99.046311231 @ avg_entry 706.74, current 710.45, market_value $70,367.45, unrealized_pl
+$367.46, +0.525%); `alpaca.py sleeves` reports equity **$100,367.46**, cash $30,000.01, core
**70.11%**, satellite **0.0% (count 0)**, cash 29.89%, `core_in_band: true`,
`rebalance_needed: false`, `rebalance_delta: −110.23`.

**Step 2 recorded no closes, and there were none to record — the ledger is *current and
empty*, not stale.** The close routine's core job is to write today's official close into
every open **satellite** position's `highest_close` and to refresh the `(as of ...)` date
whether or not the value moved. **There is no satellite position block in this file, so there
is no `highest_close` to compare against and no `(as of ...)` date to stamp.** A future run
must read this as *"the high-water pass ran and had no subject"*, **not** as *"the close run
skipped its high-water pass"* — distinguishing those two is the entire purpose of the date
field, and with zero satellite positions the distinction has no subject to attach to.
**Do not backfill from `bars` tomorrow. There is nothing to backfill.** The §5.4 trailing stop
is not silently disabled; it is **not yet armed**, and it arms on the day the first satellite
position opens. **Today's core fill did not arm it** — §5 exempts core from all four sell
rules, so VOO deliberately has no thesis, no timing window and no `highest_close`.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree. No
discrepancy.** The raw ledger reads *(none)* while the raw broker returns one VOO row; that is
the expected steady state now that core exists, not a mismatch. Every reconciliation must
compare **satellite to satellite**, never raw ledger to raw broker.

For reference only, and deliberately **not** recorded as a high-water mark anywhere: VOO closed
**710.70** on 2026-09-03 (`bars --days 3 --adjustment all`) against 703.34 on 09-02 and 700.14
on 09-01 — **+1.047% on the session**. The position snapshot marks at 710.45 (last trade at
16:15 ET) rather than the 710.70 official close, a $24.76 difference across 99.046 shares; the
account figures below and in the journal use the broker's 710.45 mark, which is what `equity`
is computed from. The core sleeve is not tracked in this file by design (§5 exempts it), so
this figure is context for the journal, not ledger state.

**Reconciliation 2026-09-03 12:35 ET (3-midday-management):** selftest passed all five checks
(`trading_enabled: true`). Market confirmed **open** — `clock` at 12:35:13 ET returns
`is_open: true`, next close 16:00 ET. `alpaca.py positions` returns **one row, VOO**
(99.046311231 shares, avg_entry 706.74, current 710.09, market_value $70,331.80, unrealized_pl
+$331.81, +0.474%); `alpaca.py sleeves` reports equity **$100,331.81**, cash $30,000.01, core
**70.1%**, satellite **0.0% (count 0)**, cash 29.9%, `core_in_band: true`,
`rebalance_needed: false`, `rebalance_delta: −99.53`.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree. No
discrepancy.** This is the comparison the 09:36 carry-forward instructed, and it is the first run
to perform it in the post-fill world: the raw ledger reads *(none)* while the raw broker returns
one row, and that is **not** a mismatch — the core holding is exempt from all four §5 rules and is
deliberately untracked here. A run that compares raw-to-raw will read a correct ledger as broken.

**Nothing to manage, and nothing was done.** Routine 3 is exits-only and may not open a position.
With zero open **satellite** positions, §5.1 (no `invalidation` line exists to test), §5.2 (no
`timing_window` to expire), §5.3 and §5.4 (no `entry_price` and no `highest_close` to measure
against) all had empty input. **No Perplexity invalidation queries were run** — with no position
to defend, a news query would be manufacturing activity, which §4's honest-broker rule forbids,
and Step 1 of this routine says so directly: no open satellite positions means note it and exit,
not go looking for something to do. **The core was excluded from the working list before §5 was
evaluated, not after** (§5: core is never sold on news).

**Step 2 high-water repair: nothing to repair, and this is the thirteenth consecutive run to
record the distinction rather than assume it carried.** The `highest_close` staleness check has no
subject — no satellite block exists, so no `(as of ...)` date can be stale and no `bars` backfill
was needed. **Do not backfill from `bars`. There is nothing to backfill.** The §5.4 trailing stop
is **not silently disabled; it is not yet armed** — it arms the day the first *satellite* position
opens, and yesterday's core fill was not that day. "Current and empty" and "the high-water pass was
skipped" are exactly what the `(as of ...)` date exists to tell apart; with zero satellite blocks
the distinction has no subject.

**No exit should have executed and did not.** No §5 rule had a subject, so no `sell` was attempted
and nothing was suppressed. `TRADING_ENABLED` is now `true`, so the dry-run suppression path that
shaped the first three days is no longer in play — had a stop fired, it would have executed.

For reference only, and deliberately **not** recorded as a high-water mark anywhere: VOO traded
**710.09** at 12:35 ET against its 703.41 close of 2026-09-02, **+0.95%** on the session. The core
sleeve is now deployed, so unlike every prior run this move is being captured rather than sat out.

---

**Reconciliation 2026-09-03 09:36 ET (2-market-open-execution — the first fill in this repo's
history):** selftest passed all five checks (`trading_enabled: true`). Market confirmed **open** —
`clock` at 09:36:07 ET returns `is_open: true`, next close 16:00 ET. Pre-trade: `alpaca.py
positions` returned `[]`, `alpaca.py sleeves` reported equity $100,000.00, cash $100,000.00, core
0.0%, cash 100.0%, `core_in_band: false`, `rebalance_needed: true`, `rebalance_delta: 70000.0` —
one condition with one remedy, as pre-noted.

**BUY VOO 99.046311231 @ $706.74, notional $70,000.00** — order
`d177d8f0-cd0c-41bf-95c1-4772318265fd`, filled at 09:36:21 ET, verified terminal before writing.
Post-trade: `alpaca.py positions` returns one VOO row (99.046311231 shares, avg_entry 706.74,
market_value $69,983.15, unrealized_pl −$16.84, −0.024% intraday); `alpaca.py sleeves` reports
equity $99,983.16, cash $30,000.01, **core 69.99%**, satellite 0.0%, cash 30.01%,
`core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: 5.06`.

**This ledger is deliberately still empty and the broker now shows one row. That is not a
discrepancy.** The core holding is **not** tracked in this file by design — §5 exempts it from
all four sell rules, so there is no thesis state, no timing window and no `highest_close` to
keep. `state.md` records the fill; `trade_log.md` → *Entries* carries the audit record. **Every
future reconciliation note must check satellite blocks against satellite Alpaca positions**, not
the raw ledger against the raw broker — the first run that does the raw comparison will read this
as broken. This is the mismatch the pre-market notes flagged in advance, and it is now the live
state.

**§5 evaluation: still empty input.** Zero satellite blocks means §5.1–5.4 have nothing to test.
No `sell_rule_status` fields were updated, because there are none to update. The §5.4 trailing
stop remains **not silently disabled, not yet armed** — it arms on the day the first *satellite*
position opens, and today's core fill is not that day.

**Do not backfill from `bars` tomorrow.** There is nothing to backfill. Twelve consecutive runs
have now each recorded this distinction rather than assume it carried; the state is the same
today, one day into a live account, as it was before trading was enabled. Only the first
satellite fill changes it.

---

**Reconciliation 2026-09-03 08:27 ET (1-premarket-research):** selftest passed all five checks,
and for the first time in this repo's history it reports **`trading_enabled: true`** with
`"control.md ok - LIVE (paper account)"`. Market **is open today** — `clock` at 08:27:45 ET
returns `is_open: false` with `next_open: 2026-09-03T09:30:00-04:00`, i.e. closed because it is
pre-market, **not a holiday**. `alpaca.py positions` returned `[]`; `alpaca.py sleeves` reports
equity $100,000.00, cash $100,000.00, core 0.0%, satellite 0.0% (count 0), cash 100.0%,
`core_in_band: false`, `rebalance_needed: true`, `rebalance_delta: 70000.0` — unchanged from every
run since 2026-09-01 00:48 ET. This ledger is empty and **agrees with the broker.** No
discrepancy, so Step 1's reconciliation requirement is satisfied and research proceeded on a
ledger known to be correct.

**No `sell_rule_status` fields were updated, because there are none to update.** Step 4 asks for
each open position's distance to the §5.3 hard stop (−7% from entry) and the §5.4 trailing stop
(−10% from `highest_close`). With zero position blocks there is no entry price, no high-water
mark and no invalidation line — §5.1 through §5.4 all have empty input. **No Perplexity
invalidation queries were run**, deliberately: with no `invalidation` line to defend, a news
query on a name I do not hold would be activity for its own sake, which §4's honest-broker rule
forbids.

**Do not backfill from `bars`.** The high-water warning at the top of this file is still not in
play — the §5.4 trailing stop is **not silently disabled; it is not yet armed**, and it arms on
the day the first satellite position opens. This is the eleventh consecutive run to record the
distinction rather than assume it carried, because "current and empty" and "the high-water pass
was skipped" are exactly what the `(as of ...)` date exists to tell apart.

**⚠ Today's core buy will NOT create a block in this file, and a future run must not read its
absence as a missing entry.** Trading went live overnight and the 09:35 run is expected to fill
a real ~$70,000 VOO order. The core holding is **deliberately not tracked here** — §5 exempts it
from all four sell rules, so it has no thesis state, no timing window and no high-water mark to
keep. After today this ledger should still read *(none)* while `alpaca.py positions` returns one
VOO row. **That is not a discrepancy.** It is the one case where this file and the broker
legitimately disagree, and it is worth stating now, before it happens, because every prior
reconciliation note in this file asserted that an empty ledger and an empty broker agreeing was
the thing being checked.

For reference only, and deliberately **not** recorded as a high-water mark anywhere: VOO's last
trade is the **703.34** close of 2026-09-02, up 0.457% from 700.14 on 09-01.

---

**High-water mark update 2026-09-02 16:15 ET (4-market-close-journal):** selftest passed all five
checks (`trading_enabled: false`). Market **was open today and has since closed** — `clock` at
16:15:36 ET returns `is_open: false` with `next_open: 2026-09-03T09:30:00-04:00`. This is a normal
post-close run, **not a holiday skip**. `alpaca.py positions` returned `[]`; `alpaca.py sleeves`
reports equity $100,000.00, cash $100,000.00, core 0.0%, satellite 0.0% (count 0), cash 100.0%,
`core_in_band: false`, `rebalance_needed: true`, `rebalance_delta: 70000.0` — unchanged from the
08:30, 09:36 and 12:35 ET reads today and from every run since 2026-09-01 00:48 ET. This ledger is
empty and **agrees with the broker.** No discrepancy.

**Step 2 recorded no closes, and there were none to record — this is "current and empty", not a
skipped high-water pass.** The close routine's whole invisible job is to write today's official
close into every open satellite position's `highest_close` and to refresh the `(as of ...)` date
whether or not the value moved. There is no position block in this file, so there is no
`highest_close` to compare against and no date to stamp. **Do not backfill from `bars` tomorrow —
there is nothing to backfill.** The §5.4 trailing stop is **not silently disabled; it is not yet
armed**, and it arms on the day the first satellite position opens, which under
`TRADING_ENABLED: false` cannot be today. Ten runs across two trading days have now each recorded
this distinction rather than assuming it carried, because a mark that is merely *not updated* and a
mark that is *current and unchanged* look identical in a summary — and here there is no mark at all.

For reference only, and deliberately **not** recorded as a high-water mark anywhere: VOO closed
**703.34** on 2026-09-02 (`bars --days 3 --adjustment all`) against 700.14 on 09-01, **+0.457%**.
The core sleeve is not tracked in this file by design (§5 exempts it), so this figure is journal
context, not ledger state — but note the direction: today the un-deployed sleeve sat out an **up**
day, which is the other half of yesterday's −0.67% and the reason yesterday's "no harm done" was
never a safe reading.

**No exit should have executed and did not.** No §5 rule had a subject, so no `sell` was attempted
and the dry run suppressed nothing. `alpaca.py orders --status all` returned `[]` — no order exists
in any state, terminal or otherwise, so nothing is carried into tomorrow in limbo (§7).

---

**Reconciliation 2026-09-02 12:35 ET (3-midday-management):** selftest passed all five checks
(`trading_enabled: false`). Market confirmed **open** — `clock` at 12:35:31 ET returns
`is_open: true`, next close 16:00 ET. `alpaca.py positions` returned `[]`; `alpaca.py sleeves`
reports equity $100,000.00, cash $100,000.00, core 0.0%, satellite 0.0% (count 0), cash 100.0%,
`core_in_band: false`, `rebalance_needed: true`, `rebalance_delta: 70000.0` — unchanged from the
08:30 ET pre-market and 09:36 ET open reads today, and from every run since 2026-09-01 00:48 ET.
This ledger is empty and **agrees with the broker.** No discrepancy.

**Nothing to manage, and nothing was done.** Routine 3 is exits-only and may not open a position.
With zero open satellite positions, §5.1 (no `invalidation` line exists to test), §5.2 (no
`timing_window` to expire), §5.3 and §5.4 (no `entry_price` and no `highest_close` to measure
against) all had empty input. **No Perplexity invalidation queries were run** — with no position
to defend, a news query would be manufacturing activity, which §4's honest-broker rule forbids.
The routine's own Step 1 says so directly: no open satellite positions means note it and exit,
not go looking for something to do.

**Step 2 high-water repair: nothing to repair, and this is the seventh consecutive run to record
the distinction rather than assume it carried.** The `highest_close` staleness check has no
subject — no position block exists, so no `(as of ...)` date can be stale and no `bars` backfill
was needed. This is materially different from a backfill that was skipped: the §5.4 trailing stop
is **not silently disabled, it is not yet armed**, and it arms on the day the first satellite
position opens, which under `TRADING_ENABLED: false` cannot be today. "Current and empty" and "the
high-water pass was skipped" are exactly what the `(as of ...)` date exists to tell apart.

**No exit should have executed and did not.** Step 4's dry-run warning — an intended exit blocked
by `TRADING_ENABLED: false` — has no subject either: no rule triggered, so no `sell` was
attempted, so nothing was suppressed. The dry run is costing this account entries (the VOO core
bootstrap, three days running), not exits.

For reference only, and deliberately **not** recorded as a high-water mark anywhere: VOO's prior
close is 700.14 (2026-09-01) and it traded 700.555 at the 09:36 ET open, about +0.06%.

---

**Reconciliation 2026-09-02 09:36 ET (2-market-open-execution):** selftest passed all five checks.
Market confirmed **open** — `clock` at 09:36:14 ET returns `is_open: true`, next close 16:00 ET.
`alpaca.py positions` returned `[]`; `alpaca.py sleeves` reports equity $100,000.00, cash
$100,000.00, core 0.0%, satellite 0.0% (count 0), cash 100.0%, `core_in_band: false`,
`rebalance_needed: true`, `rebalance_delta: 70000.0` — unchanged from the 08:30 ET pre-market read
and from every run since 2026-09-01 00:48 ET. This ledger is empty and **agrees with the broker.**
No discrepancy, so no reconciliation was required before placing orders.

**Nothing was opened or closed, and no block was written.** The plan carried no BUY and no SELL
intents — both of today's theses were rejected pre-market — so Step 4 and Step 5 had empty input
and §5.1–5.4 had nothing to evaluate. The §2 core bootstrap was submitted and returned
`"dry_run": true` (`TRADING_ENABLED: false`); it would not have produced a block here in any case,
since the core holding is deliberately not tracked in this file (§5 exempts it).

**Do not backfill from `bars`.** The high-water warning at the top of this file is still not in
play — the §5.4 trailing stop is **not silently disabled, it is not yet armed**, and it arms on
the day the first satellite position opens. Under `TRADING_ENABLED: false` that cannot be today.
This is the fifth consecutive run to record the distinction rather than assume it carried, because
"current and empty" and "the high-water pass was skipped" are exactly what the `(as of ...)` date
exists to tell apart, and with zero position blocks the distinction has no subject.

For reference only, and deliberately **not** recorded as a high-water mark anywhere: VOO traded
**700.555** at 09:36:15 ET against its 700.14 close of 2026-09-01, about +0.06%. Unlike the 08:30
read, the regular-hours book was live and tight (700.15 / 700.71, 40x40) — the stale after-hours
spread the pre-market run flagged had cleared by the open, as expected.

---

**Reconciliation 2026-09-02 08:30 ET (1-premarket-research):** selftest passed all five checks.
Market **is open today** — `clock` at 08:30:11 ET returns `is_open: false` with
`next_open: 2026-09-02T09:30:00-04:00`, i.e. closed because it is pre-market, **not a holiday**.
`alpaca.py positions` returned `[]`; `alpaca.py sleeves` reports equity $100,000.00, cash
$100,000.00, core 0.0%, satellite 0.0% (count 0), cash 100.0%, `core_in_band: false`,
`rebalance_needed: true`, `rebalance_delta: 70000.0` — identical to all four runs on 2026-09-01.
This ledger is empty and **agrees with the broker.** No discrepancy, so Step 1's reconciliation
requirement is satisfied and research proceeded on a ledger known to be correct.

**No `sell_rule_status` fields were updated, because there are none to update.** Step 4 asks for
each open position's distance to the §5.3 hard stop (−7% from entry) and the §5.4 trailing stop
(−10% from `highest_close`). With zero position blocks in this file there is no entry price, no
high-water mark, and no invalidation line to check — §5.1 through §5.4 all have empty input. **No
Perplexity invalidation queries were run**, deliberately: with no `invalidation` line to defend, a
news query on a name I do not hold would be activity for its own sake, which §4's honest-broker
rule forbids.

**Do not backfill from `bars`.** The high-water warning at the top of this file is still not in
play — the §5.4 trailing stop is **not silently disabled, it is not yet armed**, and it arms on
the day the first satellite position opens. Under `TRADING_ENABLED: false` that cannot be today.
This is the fourth consecutive run to record that distinction, and it is recorded again rather
than assumed carried, because "current and empty" and "the high-water pass was skipped" are
exactly what the `(as of ...)` date exists to tell apart.

For reference only, and deliberately **not** recorded as a high-water mark anywhere: VOO's last
trade is the **700.14** close of 2026-09-01. At 08:30 ET no pre-market quote had printed — the
`latestQuote` field still carried yesterday's 16:00 ET stamp with a stale 679.52 / 721.61
after-hours book, which is not a usable reference price and was not used as one.

---

**High-water mark update 2026-09-01 16:16 ET (4-market-close-journal — the first close run in
this repo's history):** selftest passed all five checks. Market **was open today and has since
closed** (`clock`: `is_open: false` at 16:16:22 ET, `next_open: 2026-09-02 09:30 ET`) — this is
a normal post-close run, **not a holiday skip**. `alpaca.py positions` returned `[]`;
`alpaca.py sleeves` reports equity $100,000.00, cash $100,000.00, core 0.0%, satellite 0.0%
(count 0), cash 100.0%, `core_in_band: false`, `rebalance_delta: 70000.0` — identical to the
09:36 and 12:35 reads. This ledger is empty and **agrees with the broker.** No discrepancy.

**Step 2 recorded no closes, and there were none to record.** The close routine's core job is to
write today's official close into every open satellite position's `highest_close` and to refresh
the `(as of ...)` date whether or not the value moved. There is no position block in this file,
so there is no `highest_close` to compare against and no date to stamp. **A future run must read
this as "current and empty", not as "the close run skipped its high-water pass"** — those two
states are exactly what the `(as of ...)` date exists to distinguish, and with zero positions the
distinction has no subject. **Do not backfill from `bars` tomorrow. There is nothing to backfill.**
The §5.4 trailing stop is not silently disabled; it is not yet armed, and it arms on the day the
first satellite position opens.

For reference only, and deliberately **not** recorded as a high-water mark anywhere: VOO closed
**700.14** on 2026-09-01 (`bars --days 2 --adjustment all`) against 704.875 on 2026-08-31,
−0.67%. The core sleeve is not tracked in this file by design (§5 exempts it), so this figure is
context for the journal, not ledger state.

---

**Reconciliation 2026-09-01 12:35 ET (3-midday-management — the first midday run in this repo's
history):** selftest passed all five checks. Market confirmed open (`is_open: true`, timestamp
12:35:21 ET, next close 16:00 ET). `alpaca.py positions` returned `[]`; `alpaca.py sleeves`
reports equity $100,000.00, cash $100,000.00, core 0.0%, satellite 0.0% (count 0), cash 100.0%,
`core_in_band: false`, `rebalance_delta: 70000.0` — unchanged from the 09:36 ET open run. This
ledger is empty and **agrees with the broker.** No discrepancy.

**Nothing to manage, and nothing was done.** Routine 3 is exits-only and may not open a position;
with zero open satellite positions there was nothing to evaluate. §5.1 (no invalidation condition
exists to test), §5.2 (no timing window to expire), §5.3 and §5.4 (no entry price and no
high-water mark to measure against) all had empty input. No Perplexity invalidation queries were
run, because there is no `invalidation` line in this file to check — running news queries with no
position to defend would be manufacturing activity, which §4's honest-broker rule forbids.

**Step 2 high-water repair: nothing to repair.** The `highest_close` staleness check has no
subject — no position block exists, so no `(as of ...)` date can be stale and no `bars` backfill
was needed. This is materially different from a backfill that was skipped: the trailing stop is
not silently disabled, it is simply not yet armed. It becomes live the day the first satellite
position is opened, which under `TRADING_ENABLED: false` cannot be today.

**Read this next to the 09:36 note, not as new information.** The two runs saw an identical
account three hours apart. The absence of a VOO core position is the dry-run intent recorded in
`trade_log.md`, not a failed fill.

---

**Reconciliation 2026-09-01 09:36 ET (2-market-open-execution — the first open run in this repo's
history):** checked against live Alpaca from inside regular trading hours (`clock`: `is_open:
true`, timestamp 09:35:59 ET). `alpaca.py positions` returned `[]`; `alpaca.py sleeves` reports
equity $100,000.00, cash $100,000.00, core 0.0%, satellite 0.0% (count 0), cash 100.0%,
`core_in_band: false`, `rebalance_delta: 70000.0`. This ledger is empty and **agrees with the
broker.** No discrepancy, so no reconciliation was required before placing orders.

**Nothing was opened or closed.** The plan carried no BUY and no SELL intents — all six of
today's theses were rejected pre-market — so §5.1–5.4 had nothing to evaluate and no new block
was written. The §2 core bootstrap was attempted and returned `"dry_run": true`
(`TRADING_ENABLED: false`); it would not have produced a block here in any case, since the core
holding is deliberately not tracked in this file.

The high-water backfill warning at the top of this file is **not** in play — there is no
`highest_close` gap to backfill, because there is no position. It goes live the day the first
satellite position is opened, which under `TRADING_ENABLED: false` cannot be today.

---

**Reconciliation 2026-09-01 08:56 ET (1-premarket-research, third run of the day):** re-checked
against live Alpaca from inside the pre-market session. `alpaca.py positions` returned `[]`;
`alpaca.py sleeves` reports equity $100,000.00, cash $100,000.00, core 0.0%, satellite 0.0%
(count 0), cash 100.0% — unchanged from both earlier runs today. This ledger is empty and
**agrees with the broker.** No discrepancy.

No §5 evaluation was possible or required: with no open positions there is no invalidation to
test (5.1), no timing window to expire (5.2), and no entry or high-water mark to measure a stop
against (5.3, 5.4). No `sell_rule_status` fields exist to update.

The high-water backfill warning at the top of this file is **not** in play — there is no
`highest_close` gap to backfill, because there is no position. It becomes live the day the first
satellite position is opened, which under `TRADING_ENABLED: false` is not today.

---

**Reconciliation 2026-09-01 01:15 ET (1-premarket-research, second run of the day):** re-checked
against live Alpaca. `alpaca.py positions` returned `[]`; `alpaca.py sleeves` reports equity
$100,000.00, cash $100,000.00, core 0.0%, satellite 0.0% (count 0), cash 100.0% — identical to
the 00:48 ET run. This ledger is empty and **agrees with the broker.** No discrepancy.

No §5 evaluation was possible or required: with no open positions there is no invalidation to
test (5.1), no timing window to expire (5.2), and no entry or high-water mark to measure a stop
against (5.3, 5.4). No `sell_rule_status` fields exist to update.

The high-water backfill warning at the top of this file is **not** in play — there is no
`highest_close` gap to backfill, because there is no position. It becomes live the day the
first satellite position is opened.

---

**Reconciliation 2026-09-01 00:48 ET (1-premarket-research, first run of the day):** checked against live Alpaca.
`alpaca.py positions` returned `[]`; `alpaca.py sleeves` reports equity $100,000.00, cash
$100,000.00, core 0.0%, satellite 0.0% (count 0), cash 100.0%. This ledger is also empty.
**They agree — no discrepancy.** No §5 evaluation was possible or required: with no open
positions there is no invalidation to test (5.1), no timing window to expire (5.2), and no
entry or high-water mark to measure a stop against (5.3, 5.4). No `sell_rule_status` fields
to update.

The core sleeve is not tracked in this file by design (§5 exempts it), so the fact that core
is 0% is a `plan_today.md` / `state.md` matter, not a gap here.
