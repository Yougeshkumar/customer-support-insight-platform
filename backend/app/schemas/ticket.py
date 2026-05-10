from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TicketBase(BaseModel):
    ticket_id: str
    timestamp: datetime
    customer_id: str
    channel: str
    message: str
    agent_reply: Optional[str] = None
    product: Optional[str] = None
    order_value: Optional[float] = None
    customer_country: Optional[str] = None
    resolution_status: Optional[str] = None

    category: Optional[str] = None
    confidence: Optional[float] = None
    sentiment_score: Optional[float] = None
    frustration_level: Optional[str] = None
    summary: Optional[str] = None
    suggested_response: Optional[str] = None


class TicketResponse(TicketBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True