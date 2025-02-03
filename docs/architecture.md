# Delivery Pipeline

Inbound events are accepted by `rivermill/api/routes.py`, written to the
`events` table by `rivermill/storage/postgres.py`, and picked up by workers in
`rivermill/delivery/worker.py`.

## Retry policy

Failed deliveries are retried with exponential backoff. The schedule is
calculated in `rivermill/delivery/retry.py`; attempts are capped so a single
event cannot occupy a worker slot indefinitely.

## Observability

Counters are exposed from `rivermill/metrics.py` and scraped from the
`/metrics` endpoint.
