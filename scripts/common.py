#!/usr/bin/env python3
"""Shared helpers for the trading routines.

Standard library only. The cloud runner clones this repo and executes a routine
prompt with no install step, so anything requiring pip does not exist here.

Every rule that strategy.md treats as non-negotiable is enforced in this package
rather than in the routine prompts. A prompt is an instruction a model can reason
its way around on a bad day; a non-zero exit code is not.

Fail-safe direction throughout: when state is unknown or unreadable, the answer is
"do not trade". An unknown is never grounds to act.
"""

import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone

# --------------------------------------------------------------------------
# Strategy constants. Referenced by the scripts and the routine prompts so the
# numbers live in exactly one place -- a threshold restated in prose is a
# threshold that will eventually disagree with itself.
# --------------------------------------------------------------------------

CORE_TICKER = "VOO"                  # strategy.md 2 -- the core sleeve
BENCHMARK_TICKER = "VOO"             # strategy.md 1 -- S&P 500 total return
CORE_TARGET = 0.70
CORE_BAND = (0.65, 0.75)             # rebalance outside this
MAX_SATELLITE_PCT = 0.05             # 6 -- max 5% of account at entry
MARKET_CAP_FLOOR = 10_000_000_000    # 3 -- US common stock above $10B
ETF_MIN_ADV = 500_000                # 3 -- ETF average daily volume
MAX_NEW_POSITIONS_PER_WEEK = 3       # 6
CONSECUTIVE_LOSS_LIMIT = 3           # 6 -- circuit breaker
PRICED_IN_MOVE_PCT = 4.0             # 4 -- >4% over 5 sessions means you are late
PRICED_IN_LOOKBACK = 5
HARD_STOP_PCT = -7.0                 # 5.3
TRAILING_STOP_PCT = -10.0            # 5.4

REQUIRED_ENV = (
    "ALPACA_API_KEY_ID",
    "ALPACA_API_SECRET_KEY",
    "ALPACA_BASE_URL",
    "PERPLEXITY_API_KEY",
    "CLICKUP_API_TOKEN",
    "CLICKUP_LIST_ID",
)

ALPACA_DATA_URL = "https://data.alpaca.markets"
PERPLEXITY_URL = "https://api.perplexity.ai/chat/completions"
PERPLEXITY_MODEL = "sonar-pro"
CLICKUP_API = "https://api.clickup.com/api/v2"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROTECTED_FILES = ("strategy.md", "control.md")   # human-owned, agent never writes

ORDER_TERMINAL_STATES = {
    "filled", "canceled", "cancelled", "expired", "rejected",
    "done_for_day", "stopped", "suspended",
}


class ApiError(Exception):
    """A remote call failed in a way the caller cannot proceed through."""


# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------

def emit(obj, code=0):
    """Print a JSON result on stdout and exit. Routines parse this."""
    print(json.dumps(obj, indent=2, default=str))
    sys.exit(code)


def fail(msg, **extra):
    """Print a JSON error on stderr and exit non-zero.

    Exiting non-zero is the whole point: a routine that ignores the message
    still cannot mistake this for a successful call.
    """
    payload = {"ok": False, "error": msg}
    payload.update(extra)
    print(json.dumps(payload, indent=2, default=str), file=sys.stderr)
    sys.exit(1)


# --------------------------------------------------------------------------
# Environment
# --------------------------------------------------------------------------

def missing_env(names=REQUIRED_ENV):
    return [n for n in names if not os.environ.get(n)]


def require(*names):
    """Return the named env vars, or exit naming exactly what is missing.

    Never reads a .env file. Credentials come from the cloud environment only,
    and a .env fallback is how a secret ends up committed.
    """
    names = names or REQUIRED_ENV
    absent = missing_env(names)
    if absent:
        fail(
            "missing required environment variable(s): " + ", ".join(absent),
            missing=absent,
            hint="credentials come from the cloud environment; this system never reads a .env file",
        )
    return {n: os.environ[n] for n in names}


def alpaca_base():
    """Trading API base, normalised to no trailing slash and no trailing /v2.

    Refuses a non-paper endpoint. strategy.md 1 defines this as a paper account
    and live-money trading is out of scope for the whole system, so a base URL
    pointing at live trading is treated as a configuration error rather than an
    instruction. Remove this check deliberately if that ever changes.
    """
    raw = require("ALPACA_BASE_URL")["ALPACA_BASE_URL"].strip().rstrip("/")
    raw = re.sub(r"/v2$", "", raw)
    host = urllib.parse.urlparse(raw).netloc.lower()
    if "paper" not in host:
        fail(
            f"ALPACA_BASE_URL host '{host}' is not a paper endpoint",
            hint="strategy.md section 1 defines this as a paper account; refusing to place "
                 "orders against a live-money endpoint",
        )
    return raw


# --------------------------------------------------------------------------
# HTTP
# --------------------------------------------------------------------------

def _decode(raw):
    try:
        return json.loads(raw)
    except (ValueError, TypeError):
        return raw


def http(method, url, headers=None, body=None, params=None, timeout=30):
    """Return (status_code, parsed_body). Raises ApiError only on transport failure."""
    if params:
        url = url + ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
    headers = dict(headers or {})
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers.setdefault("Content-Type", "application/json")
    headers.setdefault("Accept", "application/json")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, _decode(resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as exc:
        return exc.code, _decode(exc.read().decode("utf-8", "replace"))
    except urllib.error.URLError as exc:
        raise ApiError(f"{method} {url}: {exc.reason}")
    except TimeoutError:
        raise ApiError(f"{method} {url}: timed out after {timeout}s")


def alpaca_headers():
    env = require("ALPACA_API_KEY_ID", "ALPACA_API_SECRET_KEY")
    return {
        "APCA-API-KEY-ID": env["ALPACA_API_KEY_ID"],
        "APCA-API-SECRET-KEY": env["ALPACA_API_SECRET_KEY"],
    }


def alpaca(method, path, body=None, params=None, timeout=30):
    """Call the Alpaca trading API. `path` starts with /v2/."""
    status, payload = http(method, alpaca_base() + path, headers=alpaca_headers(),
                           body=body, params=params, timeout=timeout)
    return status, payload


def alpaca_data(method, path, params=None, timeout=30):
    """Call the Alpaca market data API (a different host from trading)."""
    return http(method, ALPACA_DATA_URL + path, headers=alpaca_headers(),
                params=params, timeout=timeout)


def ok(status):
    return 200 <= status < 300


# --------------------------------------------------------------------------
# US/Eastern time
#
# Computed from the DST rules directly rather than via zoneinfo: the cloud image
# is not guaranteed to carry the tzdata package, and a routine that silently runs
# an hour off would misjudge whether the market is open.
# --------------------------------------------------------------------------

def _nth_weekday(year, month, weekday, n):
    """nth <weekday> of a month. Monday=0 ... Sunday=6."""
    first = date(year, month, 1)
    return first + timedelta(days=(weekday - first.weekday()) % 7 + 7 * (n - 1))


def eastern_offset(moment_utc):
    """-4 during EDT, -5 during EST.

    DST runs from the second Sunday in March at 07:00 UTC (02:00 EST) to the
    first Sunday in November at 06:00 UTC (02:00 EDT).
    """
    year = moment_utc.year
    start_day = _nth_weekday(year, 3, 6, 2)
    end_day = _nth_weekday(year, 11, 6, 1)
    start = datetime(start_day.year, start_day.month, start_day.day, 7, tzinfo=timezone.utc)
    end = datetime(end_day.year, end_day.month, end_day.day, 6, tzinfo=timezone.utc)
    return -4 if start <= moment_utc < end else -5


def et_now():
    utc = datetime.now(timezone.utc)
    return utc.astimezone(timezone(timedelta(hours=eastern_offset(utc))))


def et_today():
    return et_now().date()


def et_stamp():
    return et_now().strftime("%Y-%m-%d %H:%M ET")


def week_anchor(day=None):
    """Monday of the ISO week containing `day`.

    The weekly position counter resets off this rather than off the Friday
    review having run, so a skipped Friday cannot leave the 6 cap stuck at its
    limit for the following week.
    """
    day = day or et_today()
    return day - timedelta(days=day.weekday())


def parse_date(value):
    if not value:
        return None
    text = str(value).strip().lower()
    if text in ("none", "-", "", "n/a", "null"):
        return None
    match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
    if not match:
        return None
    try:
        return date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    except ValueError:
        return None


# --------------------------------------------------------------------------
# Repo files
# --------------------------------------------------------------------------

def repo_path(*parts):
    return os.path.join(ROOT, *parts)


def read_text(*parts):
    try:
        with open(repo_path(*parts), encoding="utf-8") as handle:
            return handle.read()
    except OSError:
        return ""


def write_text(text, *parts):
    path = repo_path(*parts)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def _first_fenced_block(text):
    """The first ``` fenced block. Both control.md and state.md put their
    machine-readable settings there, which keeps parsing off the prose -- the
    surrounding documentation mentions these key names constantly."""
    match = re.search(r"```[a-zA-Z]*\n(.*?)```", text, re.S)
    return match.group(1) if match else ""


def _parse_kv(block):
    out = {}
    for line in block.splitlines():
        line = line.split("#", 1)[0].strip()
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", line)
        if match:
            out[match.group(1)] = match.group(2).strip()
    return out


def read_control():
    """control.md is human-owned. Missing or unparseable means trading is OFF.

    A missing control file means something is wrong with the checkout or the
    repo, and the safe reading of "I cannot tell whether I am allowed to trade"
    is that I am not.
    """
    text = read_text("control.md")
    if not text.strip():
        return {"present": False, "trading_enabled": False, "halt_cleared_at": None,
                "reason": "control.md missing or empty -- trading disabled by default"}
    fields = _parse_kv(_first_fenced_block(text))
    enabled = fields.get("TRADING_ENABLED", "").strip().lower() == "true"
    return {
        "present": True,
        "trading_enabled": enabled,
        "halt_cleared_at": parse_date(fields.get("HALT_CLEARED_AT")),
        "reason": "" if enabled else "TRADING_ENABLED is not true in control.md",
    }


def read_state():
    return _parse_kv(_first_fenced_block(read_text("state.md")))


def halt_active(state=None, control=None):
    """(bool, explanation) for the 6 circuit breaker.

    The clearance date must be strictly later than the trigger date. Without
    that comparison a stale HALT_CLEARED_AT left in control.md from a previous
    incident would silently clear the *next* halt the instant it tripped, which
    would void 6 without anyone noticing it had happened.
    """
    state = read_state() if state is None else state
    control = read_control() if control is None else control

    if str(state.get("circuit_breaker", "")).strip().upper() != "ACTIVE":
        return False, ""

    triggered = parse_date(state.get("halt_triggered_at"))
    cleared = control.get("halt_cleared_at")

    if triggered is None:
        return True, ("circuit breaker is ACTIVE but state.md records no halt_triggered_at; "
                      "an unknown trigger date is not grounds to resume trading")
    if cleared and cleared > triggered:
        return False, ""
    if cleared:
        return True, (f"HALT_CLEARED_AT ({cleared}) is not later than halt_triggered_at "
                      f"({triggered}); the halt stands")
    return True, (f"circuit breaker ACTIVE since {triggered}; strategy.md section 6 requires "
                  f"the human to clear it via HALT_CLEARED_AT in control.md")


def thesis_exists(thesis_id):
    """A thesis ID must already be written to research_log.md before it can be
    traded. strategy.md 7: no position without a four-part thesis."""
    if not thesis_id:
        return False
    return bool(re.search(re.escape(thesis_id), read_text("research_log.md")))


# --------------------------------------------------------------------------
# Parsing helpers
# --------------------------------------------------------------------------

_SUFFIX = {"k": 1e3, "m": 1e6, "b": 1e9, "t": 1e12}


def parse_amount(value):
    """'$47.2B' / '47.2b' / '4.7e10' / '1,200' -> float. None if unparseable."""
    if value is None:
        return None
    text = str(value).strip().lower().replace("$", "").replace(",", "").replace("_", "")
    if not text:
        return None
    match = re.match(r"^([0-9]*\.?[0-9]+(?:e[-+]?[0-9]+)?)\s*([kmbt])?$", text)
    if not match:
        return None
    amount = float(match.group(1))
    if match.group(2):
        amount *= _SUFFIX[match.group(2)]
    return amount


def money(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def pct(part, whole):
    return 0.0 if not whole else round(100.0 * part / whole, 2)


# --------------------------------------------------------------------------
# Git
# --------------------------------------------------------------------------

def git(*args, check=False):
    """Run a git command in the repo root. Returns (returncode, stdout, stderr)."""
    proc = subprocess.run(
        ("git",) + args, cwd=ROOT, capture_output=True, text=True,
    )
    if check and proc.returncode != 0:
        raise ApiError(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()
