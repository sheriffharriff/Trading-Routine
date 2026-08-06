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

*(none yet)*
