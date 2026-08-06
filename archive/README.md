# Archive

Monthly rollover of the growing logs. The Friday review moves entries older than the current
month into:

```
archive/research_log/YYYY-MM.md
archive/trade_log/YYYY-MM.md
archive/journal/YYYY-MM.md
```

leaving a dated index line behind in the live file.

This exists for one reason: every run reads the live logs in full, and a file that grows
without bound eventually costs more context than the run can afford — at which point the
run starts skimming, and skimming the trade log is how a system quietly stops knowing what
it holds. Archived months are still readable; a run just has to go looking for them
deliberately rather than paying for them every time.

`weekly_review.md` and `positions.md` are not archived. Reviews are low-volume and their
value is in reading them consecutively; `positions.md` only ever holds open positions.
