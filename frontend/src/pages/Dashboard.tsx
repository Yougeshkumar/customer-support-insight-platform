import { useEffect, useState } from "react";
import axios from "axios";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
} from "recharts";

const API = "http://127.0.0.1:8000";

const COLORS = [
  "#2563eb",
  "#10b981",
  "#f59e0b",
  "#ef4444",
  "#8b5cf6",
  "#06b6d4",
];

interface Overview {
  total_tickets: number;
  avg_sentiment: number;
  revenue_at_risk: number;
  top_issue: string;
  high_frustration_count: number;
}

interface Issue {
  category: string;
  count?: number;
  revenue?: number;
}

interface Ticket {
  ticket_id: string;
  customer_id: string;
  category: string;
  frustration_level: string;
  sentiment_score: number;
  product: string;
  message: string;
}

export default function Dashboard() {
  const [overview, setOverview] = useState<Overview | null>(null);
  const [topIssues, setTopIssues] = useState<Issue[]>([]);
  const [revenueImpact, setRevenueImpact] = useState<Issue[]>([]);
  const [tickets, setTickets] = useState<Ticket[]>([]);

  useEffect(() => {
    axios.get(`${API}/api/insights/overview`).then((res) => {
      setOverview(res.data);
    });

    axios.get(`${API}/api/insights/top-issues`).then((res) => {
      setTopIssues(res.data.slice(0, 6));
    });

    axios.get(`${API}/api/insights/revenue-impact`).then((res) => {
      setRevenueImpact(res.data.slice(0, 6));
    });

    axios.get(`${API}/api/tickets?limit=10`).then((res) => {
      setTickets(res.data);
    });
  }, []);

  if (!overview) {
    return (
      <div className="p-10 text-center text-xl font-semibold">
        Loading dashboard...
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-100 p-6">
      <h1 className="text-4xl font-bold mb-8">
        AI Customer Support Insight Platform
      </h1>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-10">
        <Card title="Total Tickets" value={overview.total_tickets.toLocaleString()} />
        <Card title="Avg Sentiment" value={overview.avg_sentiment.toFixed(2)} />
        <Card
          title="Revenue at Risk"
          value={`₹${overview.revenue_at_risk.toLocaleString()}`}
        />
        <Card
          title="High Frustration"
          value={overview.high_frustration_count.toLocaleString()}
        />
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-10">
        <Panel title="Top Issues">
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={topIssues}>
              <XAxis dataKey="category" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="count" />
            </BarChart>
          </ResponsiveContainer>
        </Panel>

        <Panel title="Revenue Impact">
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={revenueImpact}
                dataKey="revenue"
                nameKey="category"
                outerRadius={100}
                label
              >
                {revenueImpact.map((_, index) => (
                  <Cell key={index} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </Panel>
      </div>

      {/* Ticket Table */}
      <Panel title="Recent Tickets">
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="border-b">
                <th className="p-3">Ticket ID</th>
                <th className="p-3">Category</th>
                <th className="p-3">Sentiment</th>
                <th className="p-3">Frustration</th>
                <th className="p-3">Product</th>
              </tr>
            </thead>
            <tbody>
              {tickets.map((ticket) => (
                <tr key={ticket.ticket_id} className="border-b hover:bg-slate-50">
                  <td className="p-3 font-medium">{ticket.ticket_id}</td>
                  <td className="p-3">{ticket.category}</td>
                  <td className="p-3">{ticket.sentiment_score}</td>
                  <td className="p-3">{ticket.frustration_level}</td>
                  <td className="p-3">{ticket.product}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Panel>
    </div>
  );
}

function Card({
  title,
  value,
}: {
  title: string;
  value: string | number;
}) {
  return (
    <div className="bg-white rounded-xl shadow p-6">
      <p className="text-gray-500 text-sm">{title}</p>
      <h3 className="text-3xl font-bold mt-2">{value}</h3>
    </div>
  );
}

function Panel({
  title,
  children,
}: {
  title: string;
  children: React.ReactNode;
}) {
  return (
    <div className="bg-white rounded-xl shadow p-6">
      <h2 className="text-2xl font-semibold mb-4">{title}</h2>
      {children}
    </div>
  );
}