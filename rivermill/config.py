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


def _env(name: str, default: str) -> str:
    value = os.environ.get(name)
    return default if value in (None, "") else value


def load_settings() -> Settings:
    """Build settings from the process environment."""
    return Settings(
        database_url=_env("DATABASE_URL", DEFAULT_DATABASE_URL),
        concurrency=int(_env("DELIVERY_CONCURRENCY", str(DEFAULT_CONCURRENCY))),
        signature_tolerance_seconds=int(
            _env("SIGNATURE_TOLERANCE", str(DEFAULT_SIGNATURE_TOLERANCE))
        ),
        webhook_secret=_env("WEBHOOK_SECRET", ""),
    )
