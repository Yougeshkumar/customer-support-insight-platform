from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.ticket import Ticket
from app.pipeline.pipeline import process_csv

router = APIRouter()


@router.post("/api/upload")
def upload_dataset(db: Session = Depends(get_db)):
    csv_path = Path("../data/customer_support_tickets.csv")
    if not csv_path.exists():
        csv_path = Path("data/customer_support_tickets.csv")

    inserted = process_csv(str(csv_path), db)

    return {
        "message": "Dataset processed successfully",
        "tickets_inserted": inserted,
    }


@router.get("/api/insights/overview")
def get_overview(db: Session = Depends(get_db)):
    total_tickets = db.query(Ticket).count()

    avg_sentiment = (
        db.query(func.avg(Ticket.sentiment_score)).scalar() or 0
    )

    revenue_at_risk = (
        db.query(func.sum(Ticket.order_value))
        .filter(
            Ticket.resolution_status != "Resolved",
            Ticket.sentiment_score < 0,
        )
        .scalar()
        or 0
    )

    top_issue_row = (
        db.query(Ticket.category, func.count(Ticket.id).label("count"))
        .group_by(Ticket.category)
        .order_by(func.count(Ticket.id).desc())
        .first()
    )

    top_issue = top_issue_row.category if top_issue_row else None

    high_frustration_count = (
        db.query(Ticket)
        .filter(Ticket.frustration_level == "High")
        .count()
    )

    return {
        "total_tickets": total_tickets,
        "avg_sentiment": round(float(avg_sentiment), 3),
        "revenue_at_risk": round(float(revenue_at_risk), 2),
        "top_issue": top_issue,
        "high_frustration_count": high_frustration_count,
    }


@router.get("/api/insights/top-issues")
def get_top_issues(db: Session = Depends(get_db)):
    rows = (
        db.query(
            Ticket.category,
            func.count(Ticket.id).label("count")
        )
        .group_by(Ticket.category)
        .order_by(func.count(Ticket.id).desc())
        .all()
    )

    return [
        {"category": row.category, "count": row.count}
        for row in rows
    ]


@router.get("/api/insights/revenue-impact")
def get_revenue_impact(db: Session = Depends(get_db)):
    rows = (
        db.query(
            Ticket.category,
            func.sum(Ticket.order_value).label("revenue")
        )
        .filter(
            Ticket.resolution_status != "Resolved",
            Ticket.sentiment_score < 0,
        )
        .group_by(Ticket.category)
        .order_by(func.sum(Ticket.order_value).desc())
        .all()
    )

    return [
        {
            "category": row.category,
            "revenue": round(float(row.revenue or 0), 2),
        }
        for row in rows
    ]


@router.get("/api/tickets")
def get_tickets(
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
):
    tickets = (
        db.query(Ticket)
        .offset(skip)
        .limit(limit)
        .all()
    )

    return tickets


@router.get("/api/tickets/{ticket_id}")
def get_ticket(ticket_id: str, db: Session = Depends(get_db)):
    ticket = (
        db.query(Ticket)
        .filter(Ticket.ticket_id == ticket_id)
        .first()
    )

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return ticket