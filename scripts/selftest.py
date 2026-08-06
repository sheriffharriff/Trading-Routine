#!/usr/bin/env python3
"""Pre-flight check. Step 0 of every routine.

  python scripts/selftest.py [--routine 1-premarket-research] [--no-alert]

Verifies all six environment variables and that all three APIs answer, then exits
non-zero if anything is wrong. Every routine runs this first and stops on failure.

A run on a partial credential set is worse than no run at all. If Perplexity is
unreachable, the research routine produces a day with no theses -- which reads in
research_log.md exactly like a legitimate quiet day where nothing met the bar.
The failure has to be loud at the start, because it is invisible at the end.

Reports every problem it finds rather than stopping at the first, so one run tells
you everything that needs fixing.
"""

import argparse

import common as c


def check_env():
    absent = c.missing_env()
    if absent:
        return False, "missing environment variables: " + ", ".join(absent)
    return True, "all six environment variables present"


def check_alpaca():
    try:
        status, payload = c.alpaca("GET", "/v2/account", timeout=20)
    except c.ApiError as exc:
        return False, f"Alpaca unreachable: {exc}"
    if not c.ok(status):
        return False, f"Alpaca /v2/account returned {status}: {payload}"
    return True, (f"Alpaca ok - account {payload.get('status')}, "
                  f"equity {payload.get('equity')}, "
                  f"trading_blocked={payload.get('trading_blocked')}")


def check_perplexity():
    import perplexity
    try:
        result = perplexity.query("Reply with the single word: ok", timeout=45)
    except c.ApiError as exc:
        return False, f"Perplexity unreachable: {exc}"
    except SystemExit:
        return False, "Perplexity request failed"
    return True, f"Perplexity ok - model {result['model']}"


def check_clickup():
    import clickup
    try:
        result = clickup.ping()
    except c.ApiError as exc:
        return False, f"ClickUp unreachable: {exc}"
    except SystemExit:
        return False, "ClickUp list read failed"
    return True, f"ClickUp ok - list '{result['list_name']}'"


def check_control():
    control = c.read_control()
    if not control["present"]:
        return False, "control.md missing or empty - trading is disabled by default"
    mode = "LIVE (paper account)" if control["trading_enabled"] else "DRY RUN"
    return True, f"control.md ok - {mode}"


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--routine", default="unknown")
    parser.add_argument("--no-alert", action="store_true")
    args = parser.parse_args()

    checks = [("env", check_env)]
    if not c.missing_env():
        # Only worth calling the APIs once the credentials are all present --
        # otherwise every check fails for the same already-reported reason.
        checks += [("alpaca", check_alpaca), ("perplexity", check_perplexity),
                   ("clickup", check_clickup)]
    checks.append(("control", check_control))

    results, failures = {}, []
    for name, fn in checks:
        passed, detail = fn()
        results[name] = {"ok": passed, "detail": detail}
        if not passed:
            failures.append(f"{name}: {detail}")

    if not failures:
        c.emit({"ok": True, "routine": args.routine, "et": c.et_stamp(),
                "checks": results,
                "trading_enabled": c.read_control()["trading_enabled"]})

    # Best-effort alert. If ClickUp itself is the dead API this cannot send, which
    # is a known limit of having one out-of-band channel rather than a bug.
    if not args.no_alert and not c.missing_env():
        try:
            import clickup
            clickup.alert(
                key="selftest-abort",
                title="Selftest failed - routine aborted before doing any work",
                detail="\n".join(f"- {f}" for f in failures),
                routine=args.routine,
            )
        except BaseException:
            pass

    c.fail("selftest failed - abort the run, do not research or trade",
           routine=args.routine, failures=failures, checks=results)


if __name__ == "__main__":
    main()
