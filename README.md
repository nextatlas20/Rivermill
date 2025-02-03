# Rivermill

Rivermill receives signed webhooks from partner systems, stores them, and
delivers them to customer endpoints with at-least-once semantics.

- `rivermill/api` - inbound HTTP API (FastAPI)
- `rivermill/delivery` - delivery workers and retry scheduling
- `rivermill/storage` - Postgres persistence
- `docs/release-notes.md` - release history

## Development

```bash
uv sync
uv run pytest
```
