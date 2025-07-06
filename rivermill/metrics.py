"""Counters exposed on the metrics endpoint."""

from collections import Counter
from datetime import datetime, timezone

_counters: Counter = Counter()
_bucket: str = ""


def _current_bucket() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d%H%M")


def increment(name: str, amount: int = 1) -> None:
    global _bucket
    bucket = _current_bucket()
    if bucket != _bucket:
        _counters.clear()
        _bucket = bucket
    _counters[name] += amount


def render() -> str:
    lines = [f"rivermill_{name}_total {value}" for name, value in sorted(_counters.items())]
    return "\n".join(lines) + "\n"
