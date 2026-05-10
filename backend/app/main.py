from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.database import Base, engine
from app.models.ticket import Ticket  # noqa: F401

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Customer Support Insight Platform",
    version="1.0.0",
    description="AI-powered analytics platform for customer support tickets.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Customer Support Insight Platform API"}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "customer-support-insight-platform",
    }