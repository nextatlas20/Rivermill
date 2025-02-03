"""Postgres persistence for events."""

import json

import psycopg


class PostgresStore:
    def __init__(self, dsn: str):
        self.dsn = dsn

    def _connect(self):
        return psycopg.connect(self.dsn)

    def insert_event(self, event_id: str, target_url: str, payload: dict) -> None:
        with self._connect() as conn:
            conn.execute(
                "insert into events (id, target_url, payload) values (%s, %s, %s)",
                (event_id, target_url, json.dumps(payload)),
            )

    def claim_pending(self, limit: int = 50) -> list[dict]:
        with self._connect() as conn:
            rows = conn.execute(
                "select id, target_url, payload, attempts from events "
                "where status = 'pending' order by next_attempt_at limit %s",
                (limit,),
            ).fetchall()
        return [
            {"id": r[0], "target_url": r[1], "payload": r[2], "attempts": r[3], "now": None}
            for r in rows
        ]

    def mark_delivered(self, event_id: str) -> None:
        with self._connect() as conn:
            conn.execute("update events set status = 'delivered' where id = %s", (event_id,))

    def mark_dead(self, event_id: str) -> None:
        with self._connect() as conn:
            conn.execute("update events set status = 'dead' where id = %s", (event_id,))

    def schedule(self, event_id: str, when) -> None:
        with self._connect() as conn:
            conn.execute(
                "update events set attempts = attempts + 1, next_attempt_at = %s where id = %s",
                (when, event_id),
            )
