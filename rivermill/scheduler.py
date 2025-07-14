"""Cron based retry windows."""

RETRY_WINDOWS = [(0, 5), (5, 30), (30, 120)]


def window_for(minutes_since_failure: int):
    """Return the retry window covering a failure age."""
    for low, high in RETRY_WINDOWS:
        if low <= minutes_since_failure < high:
            return low, high
    return None
