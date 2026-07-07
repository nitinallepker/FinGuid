# 💰 FinGuid

Turn financial goals into actionable plans.

FinGuid is an AI-powered financial planning assistant that helps users explore realistic paths toward achieving their financial goals. Users provide their goal, target amount, timeline, and financial situation, and the AI generates personalized financial insights and recommendations.

---

## 🚀 Live Demo

### Frontend
https://finguid-frontend.vercel.app/

### Backend
https://finguid-backend.onrender.com

---

## 📌 Features

- Goal-based financial planning
- Interactive AI-guided conversation
- Personalized financial analysis
- Simple and intuitive chat interface
- Realistic financial recommendations
- Goal feasibility assessment
- Follow-up financial guidance
- Responsive modern UI
- FastAPI backend
- React frontend

---

## 🛠 Tech Stack

### Frontend
- React
- Vite
- Axios
- React Markdown
- CSS

### Backend
- FastAPI
- Google Gemini 2.5 Flash
- Python
- Uvicorn

### Deployment
- Vercel (Frontend)
- Render (Backend)

---

## 📸 Screenshots

### FinGuid User Interface

![FinGuid UI](UI_image.png)

The chat-based interface guides users through a structured financial planning process by collecting:

- Financial Goal
- Target Amount
- Timeline
- Current Financial Position

The AI then generates personalized financial insights and actionable recommendations.

---

## 🧠 How It Works

### Step 1
User enters a financial goal.

Examples:
- Buy a House
- Buy a Car
- Marriage
- Retirement
- Start a Business

### Step 2
FinGuid asks for the estimated amount required.

### Step 3
FinGuid asks for the desired timeline.

### Step 4
User shares their current financial position including:
- Income
- Savings
- Investments
- Loans
- EMIs

### Step 5
AI analyzes the complete profile and provides:

- Goal feasibility
- Financial observations
- Savings suggestions
- Investment considerations
- Practical strategies
- Next steps

---

## 📂 Project Structure

```text
FinGuid/
│
├── backend/
│   ├── app.py
│   ├── ai.py
│   ├── workflow.py
│   ├── prompts.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatInput.jsx
│   │   │   └── ChatWindow.jsx
│   │   │
│   │   ├── App.jsx
│   │   └── index.css
│   │
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/FinGuid.git

cd FinGuid
```

---

## Backend Setup

### Navigate

```bash
cd backend
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment Variable

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run Backend

```bash
uvicorn app:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

## Frontend Setup

### Navigate

```bash
cd frontend
```

### Install Dependencies

```bash
npm install
```

### Start Frontend

```bash
npm run dev
```

Frontend runs at:

```text
http://localhost:5173
```

---

## API Endpoint

### Chat Endpoint

```http
POST /chat
```

### Request

```json
{
  "message": "Buy a House"
}
```

### Response

```json
{
  "answer": "Great. Approximately how much money will you need to achieve this goal?",
  "question": ""
}
```

---

## Example Workflow

```text
User:
I want to buy a house.

AI:
Approximately how much money will you need?

User:
80 Lakhs

AI:
When do you plan to achieve this goal?

User:
10 years

AI:
Tell me about your income, savings, investments and liabilities.

User:
Monthly income ₹80,000, savings ₹5 lakh.

AI:
[Detailed financial analysis]
```

---

## 🎯 Future Improvements

- Financial calculators
- SIP planning
- Goal tracking dashboard
- Inflation projections
- Multiple financial goals
- Portfolio recommendations
- User authentication
- Conversation history

---

## ⚠ Disclaimer

FinGuid is an educational financial guidance tool and does not provide licensed financial advice. Users should consult qualified financial professionals before making investment or financial decisions.

---

## 👨‍💻 Author

Nitin Anand A

---
