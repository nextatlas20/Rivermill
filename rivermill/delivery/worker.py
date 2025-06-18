"""Delivery workers."""

import logging

from rivermill.delivery.retry import MAX_ATTEMPTS, next_attempt_at
from rivermill.storage.postgres import PostgresStore

logger = logging.getLogger(__name__)


class DeliveryWorker:
    def __init__(self, store: PostgresStore, sender):
        self.store = store
        self.sender = sender

    def run_once(self) -> int:
        delivered = 0
        for event in self.store.claim_pending(limit=50):
            if self._attempt_delivery(event):
                delivered += 1
        return delivered

    def _attempt_delivery(self, event) -> bool:
        attempt = event["attempts"] + 1
        try:
            self.sender(event["target_url"], event["payload"])
        except Exception:
            logger.warning("delivery failed for %s", event["id"])
            if attempt >= MAX_ATTEMPTS:
                self.store.mark_dead(event["id"])
            else:
                self.store.schedule(event["id"], next_attempt_at(event["now"], attempt))
            return False
        self.store.mark_delivered(event["id"])
        return True
