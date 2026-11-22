# Rivermill Release Notes

All notable changes to this project are recorded here. Entries are grouped by
conventional-commit type and listed newest first.

## 3.2.0

### Features

- **api**: add bulk replay endpoint
- **cli**: add dry-run switch to the replay command

### Bug Fixes

- **retry**: cap backoff delay at five minutes
- **cli**: exit non-zero when config file is missing
- **retry**: reset attempt counter after manual replay
- **api**: return 409 for duplicate delivery identifiers

### Performance

- **storage**: batch event inserts in chunks of 500
- **metrics**: pre-aggregate counters per minute

### Documentation

- **migration**: add notes for the 3.2 upgrade
- **api**: document the replay endpoint

### Refactoring

- **config**: centralize environment parsing
- **worker**: extract delivery attempt loop

## 3.1.0

### Features

- **delivery**: initial webhook dispatcher
- **api**: signature verification for inbound callbacks

### Bug Fixes

- **retry**: avoid double scheduling on worker restart

## 3.0.0

### Features

- **storage**: Postgres event store
- **cli**: serve and replay commands
