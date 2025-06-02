"""HTTP routes for inbound event ingestion."""

from fastapi import APIRouter, Header, HTTPException, Request

from rivermill.api.signature import verify_signature
from rivermill.config import load_settings

router = APIRouter()
settings = load_settings()


@router.post("/events")
async def ingest_event(request: Request, x_rivermill_signature: str = Header(default="")):
    body = await request.body()
    if not verify_signature(settings.webhook_secret, body, x_rivermill_signature):
        raise HTTPException(status_code=401, detail="invalid signature")
    event_id = request.headers.get("x-rivermill-event-id", "")
    return {"accepted": True, "event_id": event_id}


@router.get("/events/{event_id}")
async def get_event(event_id: str):
    return {"event_id": event_id, "status": "pending"}


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.post("/events/replay")
async def replay_events(request: Request):
    payload = await request.json()
    event_ids = payload.get("event_ids", [])
    return {"queued": len(event_ids), "event_ids": event_ids}
