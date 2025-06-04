"""Retry scheduling for failed deliveries."""

from datetime import datetime, timedelta

BASE_DELAY_SECONDS = 2
MAX_ATTEMPTS = 12


def backoff_delay(attempt: int) -> int:
    """Seconds to wait before the next attempt."""
    return min(BASE_DELAY_SECONDS ** attempt, 300)


def next_attempt_at(now: datetime, attempt: int) -> datetime:
    """Timestamp of the next delivery attempt."""
    return now + timedelta(seconds=backoff_delay(attempt))


def max_attempts_reached(attempt: int) -> bool:
    """True once the retry budget is exhausted."""
    return attempt >= MAX_ATTEMPTS
