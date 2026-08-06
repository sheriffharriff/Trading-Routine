# Trading Strategy

**Read this file in full at the start of every run. It overrides your own judgment. When this file and your reasoning disagree, this file wins.**

---

## 1. Objective

Beat the S&P 500 total return over a rolling 12-month window.

This is a swing / fundamentals horizon, not day trading. Positions are expected to be held for weeks to a few months. You are not looking for intraday moves, technical setups, or candlestick patterns.

Account is **paper trading**. Treat it as real money anyway — the point of the exercise is to find out whether the strategy works, and sloppy paper trading answers nothing.

---

## 2. Portfolio structure

The account is split into two sleeves. Check current allocation at the start of every run and report drift.

| Sleeve | Target | What it holds |
|---|---|---|
| **Core** | 70% | A broad US index ETF. Held permanently. Not traded on news. |
| **Satellite** | 30% | News-driven single-name positions per Section 4. |

**Core rules:**
- Buy once, hold. Do not sell core to fund satellite trades.
- If core drifts below 65% or above 75% of account value, rebalance back to 70% at the next market-open run and log it.

**Satellite rules:**
- If the satellite sleeve is fully deployed, you may not open a new position without closing an existing one.
- Uninvested satellite cash is fine. Do not force trades to stay fully invested.

---

## 3. Universe

**Eligible:**
- US-listed common stock, market cap above $10B
- US-listed ETFs with average daily volume above 500,000 shares

**Not eligible, ever:**
- Options, futures, or any derivative
- Margin or leverage of any kind, including leveraged ETFs (2x, 3x, inverse)
- Crypto or crypto-tracking products
- OTC, pink sheets, ADRs of companies below the cap floor
- Anything that cannot be bought outright with settled cash

---

## 4. Buy rules — second-order catalyst

The strategy is: news breaks about Company A; you look for Company B, whose economics improve because of it. You are not chasing the headline name.

### The four-part thesis

You may **not** submit a buy order until all four of these are written to `research_log.md`. If you cannot write one of them honestly, there is no trade.

**1. The mechanism, in one sentence.**
> "[Event] causes [Company B]'s [specific revenue or cost line] to [improve] because [causal path]."

If the sentence needs a second clause to make sense, the link is too weak. Reject it.

**2. The dollar path.**
Name the business segment affected, estimate the magnitude, and state what share of Company B's total revenue that segment represents. A tailwind to a segment that is under 10% of revenue is not material. Reject it.

**3. The timing window.**
When should this show up in reported results — next earnings, next quarter, two quarters out? Anything beyond two quarters is outside this strategy's horizon. Reject it.

**4. The invalidation condition.**
A specific, observable event that would prove the thesis wrong. "The stock goes down" is not an invalidation condition. "Company B's Q3 filing shows segment revenue flat or declining" is.

### Hard filters

Apply these before writing the thesis, not after:

- **Priced-in check.** If the candidate has already moved more than 4% over the last five sessions on this news, you are late. Skip it.
- **Correlation check.** Before buying, list every open satellite position and ask whether this new position is exposed to the same underlying driver. If two or more positions would move together on the same news cycle, you are making one bet in multiple tickers. Do not open it.
- **Universe check.** Section 3.

### Honest-broker rule

You will always be able to construct a plausible-sounding connection between any news event and any company. That is a limitation of how you reason, not evidence of an opportunity.

The correct output of most research runs is **no trade**. A run that finds nothing worth buying is a successful run. Do not manufacture theses to justify activity.

---

## 5. Sell rules

Evaluate every open satellite position against these at every run, in this order:

1. **Thesis invalidation.** The condition written in part 4 of the thesis has occurred → exit at the next open, regardless of P&L. This applies to winners too. Do not rewrite the thesis to keep the position.
2. **Time stop.** The timing window from part 3 has passed with no observable movement in the underlying business → exit. Dead capital is a real cost.
3. **Hard stop.** Position is down 7% from entry → exit. No averaging down. No exceptions.
4. **Trailing stop.** Position is down 10% from its highest close since entry → exit.

Core positions are exempt from all four. Core is not sold on news.

---

## 6. Risk limits

- **Max 5% of total account value in any single satellite position** at entry. If a winner grows past 5%, that is fine — do not trim on size alone.
- **Circuit breaker:** after **three consecutive closed positions at a loss**, stop opening new positions entirely. Continue managing existing positions per Section 5, continue research and journaling, and flag the halt prominently in the ClickUp summary. The halt lifts only when the human explicitly clears it in this file.
- **Max 3 new positions per week.** Slow down.

---

## 7. Never do

- Trade any instrument in the "not eligible" list in Section 3
- Open a position without a four-part thesis in `research_log.md`
- Average down into a losing position
- Sell core holdings to fund a satellite trade
- Rewrite or soften an invalidation condition on a position you already hold
- Place a trade during a circuit-breaker halt
- Trade when the market is closed, or place orders you cannot verify filled

---

## 8. Every run

**Start:** read this file, `trade_log.md`, `research_log.md`, and current Alpaca positions. Know where you stand before you think about what to do.

**End:** write back what happened, what you learned, and anything the next run needs to know. Every trade gets a `trade_log.md` entry with the thesis ID it came from. Every thesis gets a `research_log.md` entry whether or not it became a trade — rejected theses are the most useful data you generate, because they are how the human finds out what you keep almost getting wrong.

Commit and push all file changes to `main` before the run ends. If you do not push, the next run starts blind and everything you learned is gone.
