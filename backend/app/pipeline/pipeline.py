from pathlib import Path

import pandas as pd
from sqlalchemy.orm import Session

from app.models.ticket import Ticket
from app.services.categorizer import categorize_ticket
from app.services.responder import generate_response
from app.services.sentiment import analyze_sentiment
from app.services.summarizer import summarize_ticket


def process_csv(file_path: str, db: Session) -> int:
    csv_path = Path(file_path)
    df = pd.read_csv(csv_path)

    # Optional: clear existing records
    db.query(Ticket).delete()
    db.commit()

    inserted_count = 0

    for _, row in df.iterrows():
        category, confidence = categorize_ticket(str(row["message"]))
        sentiment_score, frustration_level = analyze_sentiment(
            str(row["message"])
        )
        summary = summarize_ticket(str(row["message"]))
        suggested_response = generate_response(
            category, str(row["message"])
        )

        ticket = Ticket(
            ticket_id=row["ticket_id"],
            timestamp=pd.to_datetime(row["timestamp"]),
            customer_id=row["customer_id"],
            channel=row["channel"],
            message=row["message"],
            agent_reply=row.get("agent_reply"),
            product=row.get("product"),
            order_value=float(row.get("order_value", 0)),
            customer_country=row.get("customer_country"),
            resolution_status=row.get("resolution_status"),
            category=category,
            confidence=confidence,
            sentiment_score=sentiment_score,
            frustration_level=frustration_level,
            summary=summary,
            suggested_response=suggested_response,
        )

        db.add(ticket)
        inserted_count += 1

    db.commit()
    return inserted_count