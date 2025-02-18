"""HMAC helpers for inbound webhook signatures."""

import hashlib
import hmac


def compute_signature(secret: str, body: bytes) -> str:
    """Return the sha256 signature header value for a payload."""
    digest = hmac.new(secret.encode("utf-8"), body, hashlib.sha256).hexdigest()
    return f"sha256={digest}"


def verify_signature(secret: str, body: bytes, header: str | None) -> bool:
    """Check a signature header against the payload."""
    if not header or not header.startswith("sha256="):
        return False
    return hmac.compare_digest(compute_signature(secret, body), header)
