from datetime import datetime

from rivermill.delivery.retry import backoff_delay, next_attempt_at


def test_backoff_grows():
    assert backoff_delay(1) < backoff_delay(3)


def test_next_attempt_is_in_the_future():
    now = datetime(2025, 4, 1, 12, 0, 0)
    assert next_attempt_at(now, 2) > now


def test_window_lookup():
    from rivermill.scheduler import window_for

    assert window_for(7) == (5, 30)
    assert window_for(500) is None
