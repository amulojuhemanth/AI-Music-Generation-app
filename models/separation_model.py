from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SeparationResponse(BaseModel):
    id: str
    user_id: str
    project_id: str
    original_filename: str
    status: str
    vocals_url: Optional[str] = None
    drums_url: Optional[str] = None
    bass_url: Optional[str] = None
    other_url: Optional[str] = None
    error_message: Optional[str] = None
    created_at: datetime
