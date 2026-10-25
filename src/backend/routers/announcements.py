import os
from typing import Any, Dict

from fastapi import APIRouter

router = APIRouter(prefix="/announcement", tags=["announcement"])

DEFAULT_ANNOUNCEMENT = (
    "📢 Activity registration is open until the end of the month. Don't lose your spot!"
)
ANNOUNCEMENT_TEXT = os.getenv("ANNOUNCEMENT_TEXT", DEFAULT_ANNOUNCEMENT).strip()
ANNOUNCEMENT_ENABLED = os.getenv("ANNOUNCEMENT_ENABLED", "true").strip().lower() in {
    "1",
    "true",
    "yes",
    "on",
}


@router.get("")
def get_announcement() -> Dict[str, Any]:
    return {
        "enabled": ANNOUNCEMENT_ENABLED and bool(ANNOUNCEMENT_TEXT),
        "message": ANNOUNCEMENT_TEXT,
    }
