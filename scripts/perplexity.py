#!/usr/bin/env python3
"""Perplexity research client. All research goes through here, not native web search.

Usage:
  python scripts/perplexity.py query --prompt "What happened overnight in ..." \
      [--recency day|week|month] [--model sonar-pro]
  python scripts/perplexity.py ping

Returns the answer plus citations. Citations are the point -- a thesis in
research_log.md is only auditable if the claim underneath it can be traced back
to something that was actually published.
"""

import argparse

import common as c

# The system prompt does real work here. The failure mode this strategy is most
# exposed to is a plausible-sounding causal chain assembled out of nothing
# (strategy.md section 4, the honest-broker rule), and a research tool that
# happily obliges is how that failure starts.
SYSTEM_PROMPT = (
    "You are a research assistant for an equity analyst. Report only what is actually "
    "reported by sources, with dates and figures where they exist. Distinguish clearly "
    "between what a source states, what is an estimate, and what is your inference. "
    "If the evidence for something is thin or absent, say so plainly rather than "
    "constructing a plausible narrative around it. Do not speculate about price "
    "movement. Do not offer investment advice or recommendations."
)


def query(prompt, model=None, recency=None, system=None, timeout=90):
    env = c.require("PERPLEXITY_API_KEY")
    body = {
        "model": model or c.PERPLEXITY_MODEL,
        "messages": [
            {"role": "system", "content": system or SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    }
    if recency:
        body["search_recency_filter"] = recency

    status, payload = c.http(
        "POST", c.PERPLEXITY_URL,
        headers={"Authorization": f"Bearer {env['PERPLEXITY_API_KEY']}"},
        body=body, timeout=timeout,
    )
    if not c.ok(status):
        c.fail("Perplexity request failed", status=status, response=payload)

    choices = (payload or {}).get("choices") or []
    answer = choices[0]["message"]["content"] if choices else ""
    return {
        "ok": True,
        "model": body["model"],
        "answer": answer,
        "citations": payload.get("citations") or payload.get("search_results") or [],
        "usage": payload.get("usage", {}),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("query")
    p.add_argument("--prompt", required=True)
    p.add_argument("--model", default=c.PERPLEXITY_MODEL)
    p.add_argument("--recency", choices=["hour", "day", "week", "month"])
    p.add_argument("--system")

    sub.add_parser("ping")

    args = parser.parse_args()
    try:
        if args.cmd == "ping":
            result = query("Reply with the single word: ok", recency=None)
            c.emit({"ok": True, "model": result["model"],
                    "answer": result["answer"][:80]})
        else:
            c.emit(query(args.prompt, args.model, args.recency, args.system))
    except c.ApiError as exc:
        c.fail(str(exc))


if __name__ == "__main__":
    main()
