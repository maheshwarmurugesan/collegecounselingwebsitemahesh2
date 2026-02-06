"""E-Log Pydantic schemas for API request/response."""

from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field


class LogEntryCreate(BaseModel):
    """Request body for creating a log entry."""

    plant_id: Optional[str] = None
    operator_id: str = Field(..., min_length=1)
    operator_name: Optional[str] = None
    entry_type: str = Field(..., min_length=1, max_length=64)
    body: str = Field(..., min_length=1)
    metadata: Optional[dict[str, Any]] = None


class LogEntryResponse(BaseModel):
    """Response model for a single log entry."""

    id: int
    plant_id: Optional[str]
    operator_id: str
    operator_name: Optional[str]
    entry_type: str
    body: str
    created_at: datetime
    metadata: Optional[dict[str, Any]] = None

    model_config = {"from_attributes": True}


class LogEntryListResponse(BaseModel):
    """Paginated list of log entries."""

    entries: list[LogEntryResponse]
    total: int
    limit: int
    offset: int
