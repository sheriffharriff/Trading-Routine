# Trade Log

**AGENT-OWNED. Newest first.**

Every order gets an entry, with the thesis ID it came from (§8). Only write an entry after
the order has been **polled to a terminal state** — §7 forbids orders you cannot verify
filled, and an entry written at submission time records an intention, not a trade.

Rejected and canceled orders get entries too. An order the broker refused is something the
next run needs to know about.

**Monthly rollover:** the Friday review archives prior months into
`archive/trade_log/YYYY-MM.md`.

---

## Template

```
### YYYY-MM-DD HH:MM ET — BUY | SELL — <TICKER> — <filled | rejected | canceled>
- thesis_id:      T-YYYY-MM-DD-NN   (or "core" for the core sleeve)
- order_id:       <alpaca order id>
- qty:            0.000
- fill_price:     0.00
- notional:       0.00
- pct_of_account: 0.0%
- routine:        <which of the five runs placed it>

For buys (satellite):
- asset_type:     stock | etf
- market_cap:     $00.0B
- market_cap_src: <source — this is what makes the §3 floor auditable after the fact>

For sells:
- rule:           §5.1 invalidation | §5.2 time stop | §5.3 hard stop | §5.4 trailing stop | §2 rebalance
- evidence:       <the observable fact that triggered it>
- realized_pnl:   +/-0.00 (+/-0.0%)
- streak_effect:  consecutive_closed_losses N → M

- notes:          <anything odd: slippage, partial fill, retry>
```

The `market_cap_src` field matters more than it looks. The $10B floor is checked against a
figure the agent supplies from research, so the script can catch a missing or below-floor
number but cannot catch a wrong one. Recording where the number came from is what lets you
audit it later.

---

## Entries

**📁 2026-09 ARCHIVED — 2026-10-02 (routine 5, monthly rollover).** The full 2026-09 section
of this file — the core fill below plus the `## Dry-run intents` block (2026-09-02 and
2026-09-01 VOO core bootstrap intents, neither of which was a trade) — was moved verbatim to
**`archive/trade_log/2026-09.md`**.

⚠ **THE 2026-09-03 CORE FILL IS DELIBERATELY RETAINED BELOW RATHER THAN REMOVED.** It is the
only fill in this account history and **the position is still open.** The rollover rule exists
because *"skimming the trade log is how a system quietly stops knowing what it holds"* — and
removing the only record of a live $70,000 holding would make the live ledger read as an
account that has never traded, which is that same failure arriving by a different door. The
archive carries the audit trail; this copy is the ledger. **At 6KB this file is under 1% of the
corpus, so nothing is bought by shrinking it.** ⚠ **Flagged for the human in the 2026-10-02
weekly review: the prompt says to move entries older than the current month, and this run
judged that the rule's purpose outranks its letter for an OPEN position. If the human
disagrees, say so in `control.md` and the next review will move it.**

### 2026-09-03 09:36 ET — BUY — VOO — filled
- thesis_id:      core
- order_id:       d177d8f0-cd0c-41bf-95c1-4772318265fd
- qty:            99.046311231
- fill_price:     706.74
- notional:       70000.00
- pct_of_account: 70.0% (at entry, against $100,000.00 pre-trade equity)
- routine:        2-market-open-execution
- asset_type:     etf
- market_cap:     n/a — VOO is the designated core sleeve ticker; §3 stock market-cap floor
                  does not apply and `alpaca.py buy --core` does not require it. ADV is well
                  above the §3 500k-shares ETF threshold (VOO trades in the millions daily).
- market_cap_src: n/a (core sleeve, ETF — §3 checks ADV, not market cap)
- notes:          **First real fill in this repo's history.** Bootstrapped the §2 core sleeve
                  from 0% to 70% in a single order — Step 3's bootstrap and Step 7's rebalance
                  are the same order on this account, so this fill satisfies both. Verified
                  terminal (`"status": "filled", "terminal": true`) before writing this entry.
                  Post-fill sleeves check: core 69.99%, cash 30.01%, `core_in_band: true`,
                  `rebalance_needed: false`, `rebalance_delta: 5.06` (residual from fractional
                  share rounding against a moving mark, well inside §2's 65–75% band). Live
                  equity was $100,000.00 at the open, so the plan's $70,000 notional was also
                  70% of live equity — no size-to-equity adjustment needed. Fill price 706.74
                  is +0.483% from VOO's 703.41 prior close, i.e. a normal open bar.

---

