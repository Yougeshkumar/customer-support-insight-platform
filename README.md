# AI-Powered Customer Support Insight Platform

An AI-powered analytics platform that transforms raw customer support conversations into actionable business intelligence.

The system automatically:
- Categorizes customer complaints
- Detects sentiment and frustration levels
- Identifies recurring issue trends
- Estimates revenue at risk
- Generates suggested support responses
- Visualizes insights in an interactive dashboard

---

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
📂 Project Structure
customer-support-insight-platform/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models/
│   │   ├── pipeline/
│   │   ├── schemas/
│   │   └── services/
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
📊 Dashboard Overview

The dashboard includes:

KPI Cards
Total Tickets
Average Sentiment
Revenue at Risk
High Frustration Count
Visualizations
Top Issues Bar Chart
Revenue Impact Pie Chart
Ticket Analytics
Recent Tickets Table
🧠 Business Insights Generated

Examples of insights produced by the platform:

Delivery Delay complaints increased significantly.
Refund requests represent the highest revenue at risk.
Damaged Product complaints show the highest frustration scores.
Payment failures disproportionately affect high-value orders.
⚙️ Local Setup
1. Clone the Repository
git clone https://github.com/Yougeshkumar/customer-support-insight-platform.git
cd customer-support-insight-platform
2. Generate the Synthetic Dataset
pip install pandas
python generate_dataset.py
3. Run the Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

Backend URLs:

API: http://127.0.0.1:8000
Swagger Docs: http://127.0.0.1:8000/docs
4. Run the Frontend
cd frontend
npm install
npm run dev

Frontend URL:

Dashboard: http://localhost:5173
5. Load the Dataset
Open Swagger Docs: http://127.0.0.1:8000/docs
Execute POST /api/upload

This processes all 10,000 tickets and stores them in SQLite.

▶️ How to Use the Application
Start the backend server.
Start the frontend server.
Run POST /api/upload from Swagger Docs.
Open the dashboard.
Explore KPIs, charts, and ticket data.
🧪 Running Tests
cd backend
pytest

Expected output:

3 passed
🐳 Docker Support

Run the entire application using Docker:

docker compose up --build
📡 API Endpoints
Endpoint	Description
POST /api/upload	Process dataset and store analyzed tickets
GET /api/insights/overview	KPI overview metrics
GET /api/insights/top-issues	Issue frequency counts
GET /api/insights/revenue-impact	Revenue at risk by issue category
GET /api/tickets	Paginated list of tickets
GET /api/tickets/{ticket_id}	Detailed ticket analysis
GET /health	Health check
🛠️ Technology Stack
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
📈 Resume Highlights
Built an AI-powered customer support analytics platform processing 10,000+ support tickets.
Developed FastAPI APIs for categorization, sentiment analysis, and revenue-at-risk estimation.
Designed a React dashboard with KPI cards, charts, and ticket drill-down.
Implemented automated testing with pytest and CI/CD with GitHub Actions.
🎤 Interview Summary

This project demonstrates:

AI/ML engineering
Data pipeline design
Backend API development
Frontend dashboard development
Automated testing
CI/CD
Deployment readiness
👤 Author

Yougesh Kumar

GitHub: https://github.com/Yougeshkumar
LinkedIn: https://linkedin.com/in/yougeshkumar22
give full in markdown formta
AI-Powered Customer Support Insight Platform

An AI-powered analytics platform that transforms raw customer support conversations into actionable business intelligence.

The system automatically:

Categorizes customer complaints
Detects sentiment and frustration levels
Identifies recurring issue trends
Estimates revenue at risk
Generates suggested support responses
Visualizes insights in an interactive dashboard
🚀 Features
AI/ML Features
Ticket categorization using rule-based NLP
Sentiment analysis using TextBlob
Frustration level detection
Ticket summarization
Suggested response generation
Revenue-at-risk estimation
Backend
FastAPI REST API
SQLAlchemy ORM
SQLite database
Swagger API documentation
Frontend
React + TypeScript
Tailwind CSS
Recharts visualizations
KPI cards, charts, and ticket table
Engineering
Synthetic dataset generation (10,000 tickets)
Automated tests with pytest
GitHub Actions CI/CD
Docker and Docker Compose support
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
│   │   └── test_api.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── pytest.ini
│
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
│
├── data/
│   └── customer_support_tickets.csv
│
├── docs/
│   ├── architecture.md
│   ├── business_insights.md
│   ├── demo_script.md
│   └── design_document.md
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── docker-compose.yml
├── generate_dataset.py
└── README.md
📊 Dashboard Overview

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
🧠 Business Insights Generated

Examples of insights produced by the platform:

Delivery Delay complaints increased significantly.
Refund requests represent the highest revenue at risk.
Damaged Product complaints show the highest frustration scores.
Payment failures disproportionately affect high-value orders.
⚙️ Local Setup
1. Clone the Repository
git clone https://github.com/Yougeshkumar/customer-support-insight-platform.git
cd customer-support-insight-platform
2. Generate the Synthetic Dataset
pip install pandas
python generate_dataset.py
3. Run the Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

Backend URLs:

API: http://127.0.0.1:8000
Swagger Docs: http://127.0.0.1:8000/docs
4. Run the Frontend
cd frontend
npm install
npm run dev

Frontend URL:

Dashboard: http://localhost:5173
5. Load the Dataset
Open Swagger Docs: http://127.0.0.1:8000/docs
Execute POST /api/upload

This processes all 10,000 tickets and stores them in SQLite.

▶️ How to Use the Application
Start the backend server.
Start the frontend server.
Run POST /api/upload from Swagger Docs.
Open the dashboard.
Explore KPIs, charts, and ticket data.
🧪 Running Tests
cd backend
pytest

Expected output:

3 passed
🐳 Docker Support

Run the full application with Docker:

docker compose up --build
📡 API Endpoints
Endpoint	Description
POST /api/upload	Process dataset and store analyzed tickets
GET /api/insights/overview	KPI overview metrics
GET /api/insights/top-issues	Issue frequency counts
GET /api/insights/revenue-impact	Revenue at risk by issue category
GET /api/tickets	Paginated list of tickets
GET /api/tickets/{ticket_id}	Detailed ticket analysis
GET /health	Health check
🛠️ Technology Stack
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
📈 Resume Highlights
Built an AI-powered customer support analytics platform processing 10,000+ support tickets.
Developed FastAPI APIs for categorization, sentiment analysis, and revenue-at-risk estimation.
Designed a React dashboard with KPI cards, charts, and ticket drill-down.
Implemented automated testing with pytest and CI/CD with GitHub Actions.
🎤 Interview Summary

This project demonstrates:

AI/ML engineering
Data pipeline design
Backend API development
Frontend dashboard development
Automated testing
CI/CD
Deployment readiness
👤 Author

Yougesh Kumar

GitHub: https://github.com/Yougeshkumar
LinkedIn: https://linkedin.com/in/yougeshkumar22