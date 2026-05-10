from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String, Text

from app.database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(String, unique=True, index=True, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    customer_id = Column(String, nullable=False)
    channel = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    agent_reply = Column(Text)
    product = Column(String)
    order_value = Column(Float)
    customer_country = Column(String)
    resolution_status = Column(String)

    # AI-generated fields
    category = Column(String)
    confidence = Column(Float)
    sentiment_score = Column(Float)
    frustration_level = Column(String)
    summary = Column(Text)
    suggested_response = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)