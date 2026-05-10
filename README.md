# AI-Powered Customer Support Insight Platform

An AI-powered analytics platform that transforms raw customer support conversations into actionable business intelligence.

## 🚀 Features

### AI/ML Features
- Ticket categorization using rule-based NLP
- Sentiment analysis using TextBlob
- Frustration level detection
- Ticket summarization
- Suggested response generation
- Revenue-at-risk estimation

### Backend
- FastAPI REST API
- SQLAlchemy ORM
- SQLite database
- Swagger API documentation

### Frontend
- React + TypeScript
- Tailwind CSS
- Recharts visualizations
- KPI cards, charts, and ticket table

### Engineering
- Synthetic dataset generation (10,000 tickets)
- Automated tests with pytest
- GitHub Actions CI/CD
- Docker and Docker Compose support

---

## 🏗️ Architecture

```mermaid
flowchart LR
    A[CSV Dataset] --> B[FastAPI Upload API]
    B --> C[AI Processing Pipeline]
    C --> D[SQLite Database]
    D --> E[Insights REST APIs]
    E --> F[React Dashboard]
```
## 📂 Project Structure

```

customer-support-insight-platform/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── pipeline/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── database.py
│   │   └── main.py
│   ├── tests/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── pytest.ini
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   └── Dashboard.tsx
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.ts
│   └── Dockerfile
├── data/
│   └── customer_support_tickets.csv
├── docs/
│   ├── architecture.md
│   ├── business_insights.md
│   ├── demo_script.md
│   └── design_document.md
├── .github/
│   └── workflows/
│       └── ci.yml
├── docker-compose.yml
├── generate_dataset.py
└── README.md
```
## 📊 Dashboard Overview
The dashboard includes:

KPI Cards
Total Tickets
Average Sentiment
Revenue at Risk
High Frustration Count
Charts
Top Issues Bar Chart
Revenue Impact Pie Chart
Ticket Analytics
Recent Tickets Table

## 🧠 Business Insights Generated
Delivery Delay complaints increased significantly.
Refund requests represent the highest revenue at risk.
Damaged Product complaints show the highest frustration scores.
Payment failures disproportionately affect high-value orders.
```
## ⚙️ Local Setup

Clone the Repository
git clone https://github.com/Yougeshkumar/customer-support-insight-platform.git
cd customer-support-insight-platform
```
## Generate Dataset
pip install pandas
python generate_dataset.py

## Run Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

Backend URLs:

API: http://127.0.0.1:8000
Swagger Docs: http://127.0.0.1:8000/docs

## Run Frontend
cd frontend
npm install
npm run dev

Frontend URL:

Dashboard: http://localhost:5173

## Load Dataset

Open Swagger Docs and run:

POST /api/upload

## 🧪 Running Tests
cd backend
pytest

## 🐳 Docker Support
docker compose up --build

## 📡 API Endpoints
```
Endpoint	Description
POST /api/upload	Process dataset
GET /api/insights/overview	KPI overview
GET /api/insights/top-issues	Top complaint categories
GET /api/insights/revenue-impact	Revenue at risk by category
GET /api/tickets	List tickets
GET /api/tickets/{ticket_id}	Ticket details
GET /health	Health check
```
## 🛠️ Technology Stack
```
Backend
Python 3.11
FastAPI
SQLAlchemy
SQLite
Pandas
TextBlob
Frontend
React
TypeScript
Tailwind CSS
Recharts
Axios
DevOps
Docker
GitHub Actions
Pytest
```
## 👤 Author
Yougesh Kumar

GitHub: https://github.com/Yougeshkumar
LinkedIn: https://linkedin.com/in/yougeshkumar22
```