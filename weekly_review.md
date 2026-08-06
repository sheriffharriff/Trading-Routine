# Weekly Review

**AGENT-OWNED. Newest first. Written by the Friday routine.**

The objective in §1 is to beat the S&P 500 total return over a rolling 12-month window.
This file is the only place that question actually gets answered.

**One benchmark, used everywhere: VOO total return.** §1 names S&P 500 total return and the
core sleeve holds VOO, so the review measures against the same instrument the account
actually owns — using SPY here would make the headline number quietly disagree with the
core sleeve's own performance for no reason. Bars are pulled with `adjustment=all` so
dividends are included; a price-only series understates the benchmark by roughly its yield,
which would flatter the agent a little more every single week.

---

## Template

```
### Week ending YYYY-MM-DD

**Performance**
| | Week | 1M | 3M | 12M (rolling) | Since inception |
|---|---|---|---|---|---|
| Account | | | | | |
| VOO (total return) | | | | | |
| Excess | | | | | |

12-month figures use the full window once available; before then, state the actual elapsed
period rather than annualizing a short run into a number that means nothing.

**Sleeves:** core 0.0% | satellite 0.0% | cash 0.0%
**Breaker:** INACTIVE | ACTIVE since YYYY-MM-DD

**Trades closed this week**
| Ticker | Thesis | Held | Exit rule | P&L |
|---|---|---|---|---|

**Thesis scoreboard — including rejects**
- Theses written: N (N accepted, N rejected)
- Of accepted theses now closed: N reached their timing window, N invalidated, N stopped out
- **Of rejected theses: what happened to them since?** Track the ones that ran without you.
  A rejection rate that is never wrong means the filters are too loose, not that the
  judgment is perfect.

**Recurring errors**
<what shows up across multiple weeks — the point of this section is patterns, not incidents.
If the same failure appears three weeks running, say so plainly and name it.>

**Housekeeping**
- Monthly archive rollover: <done / not due>
- Weekly counter reset: new_positions_this_week → 0, week_of → <next Monday>
```

---

## Reviews

*(none yet)*
