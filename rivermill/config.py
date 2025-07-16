"""Runtime configuration for the Rivermill service."""

import os
from dataclasses import dataclass

DEFAULT_DATABASE_URL = "postgresql://localhost:5432/rivermill"
DEFAULT_CONCURRENCY = 8
DEFAULT_SIGNATURE_TOLERANCE = 300


@dataclass
class Settings:
    """Resolved service settings."""

    database_url: str = DEFAULT_DATABASE_URL
    concurrency: int = DEFAULT_CONCURRENCY
    signature_tolerance_seconds: int = DEFAULT_SIGNATURE_TOLERANCE
    webhook_secret: str = ""


def load_settings() -> Settings:
    """Build settings from the process environment."""
    return Settings(
        database_url=os.environ.get("RIVERMILL_DATABASE_URL", DEFAULT_DATABASE_URL),
        concurrency=int(os.environ.get("RIVERMILL_CONCURRENCY", DEFAULT_CONCURRENCY)),
        signature_tolerance_seconds=int(
            os.environ.get("RIVERMILL_SIGNATURE_TOLERANCE", DEFAULT_SIGNATURE_TOLERANCE)
        ),
    )
