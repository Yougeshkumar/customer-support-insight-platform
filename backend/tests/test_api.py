from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_overview():
    response = client.get("/api/insights/overview")
    assert response.status_code == 200
    data = response.json()
    assert "total_tickets" in data
    assert "avg_sentiment" in data