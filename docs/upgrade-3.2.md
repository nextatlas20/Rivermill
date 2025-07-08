# Upgrading to 3.2

## Database

No schema changes are required for this release.

## CLI

`rivermill replay` now accepts `--dry-run`, which prints the events that would
be queued without scheduling them.

## API

`POST /events` returns `409 Conflict` when the same delivery identifier is
posted twice. Clients that retried on any 4xx response must stop retrying on
409.
