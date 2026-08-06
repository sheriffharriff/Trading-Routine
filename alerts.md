# Alerts — incident ledger

**AGENT-OWNED. Written by `scripts/commit.py` and `scripts/clickup.py`.**

Operational incidents, separate from trading activity. Four things get alerted:

| Incident key | Trigger |
|---|---|
| `push-failure` | A run could not push to `main`. Its work is at risk of being lost. |
| `guard-violation:<file>` | A run modified `strategy.md` or `control.md`. Reverted before commit. |
| `selftest-abort` | Missing env var or dead API killed the run before it did anything. |
| `circuit-breaker` | §6 halt tripped — three consecutive closed losses. |

Each incident becomes one ClickUp task titled `[ALERT] YYYY-MM-DD — <incident>`, **not one
per run**. A condition that persists across runs gets a comment on the existing task instead
of a new one, so a breaker that stays active for a week produces one task with seven
comments rather than seven tasks.

**Dedupe is resolved against ClickUp, not against this file.** `clickup.py alert` searches
the list for an open task carrying the incident key before deciding to create or comment.
That indirection exists for `push-failure` specifically: an alert about a failed push cannot
look up its own history in a file that lives in the repo whose push just failed. Since that
path needs a ClickUp-side lookup anyway, all four incidents use it rather than maintaining
two mechanisms that would drift.

This file is the local mirror — it survives as the audit trail and carries the occurrence
counts that drive escalation.

---

## Escalation

`occurrences` is per incident key and never resets on its own.

A `guard-violation` on the same file **more than once** stops being an incident and is
reported as **SYSTEMIC**: the alert title and body say so explicitly. One accidental write
to `control.md` is a slip. The same routine reaching for the same protected file on repeated
runs means a prompt is steering it wrong, and that is a bug in the instructions to be fixed,
not an event to keep logging. The escalated alert names the routine so the offending prompt
is identifiable without cross-referencing.

Clear an entry by hand once the underlying cause is fixed — move it to **Resolved** with a
date and a one-line cause. Nothing clears these automatically.

---

## Template

```
### <incident-key>
- first_seen:      YYYY-MM-DD
- last_seen:       YYYY-MM-DD
- occurrences:     N
- clickup_task_id: <id>
- routines:        <which runs hit it>
- status:          OPEN | SYSTEMIC | RESOLVED
- detail:          <file, error, or the reverted diff — enough to act on without the task>
```

---

## Open incidents

*(none)*

---

## Resolved

*(none)*
