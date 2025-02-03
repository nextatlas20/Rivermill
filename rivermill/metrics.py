"""Counters exposed on the metrics endpoint."""

from collections import Counter

_counters = Counter()


def increment(name: str, amount: int = 1) -> None:
    _counters[name] += amount


def render() -> str:
    lines = [f"rivermill_{name}_total {value}" for name, value in sorted(_counters.items())]
    return "\n".join(lines) + "\n"
