# NeuroSync AI – Multi-Agent Personal Assistant

NeuroSync AI is a Generative AI-powered Multi-Agent Personal Assistant developed using React, FastAPI, OpenAI APIs, and ChromaDB. The system uses intelligent task routing and specialized AI agents to perform different operations such as research assistance, code support, email generation, and conversational interactions.


## Key Features

- Multi-Agent Architecture
- Research Agent for information assistance
- Coding Agent for programming support
- Email Agent for professional email generation
- Intelligent Coordinator Agent for task routing
- AI Memory Integration using ChromaDB
- Conversational Chat Interface
- OpenAI API Integration
- Modern Dashboard Interface
- Modular Backend Architecture

---

## System Architecture

```
User Interface (React)
          │
          ▼
FastAPI Backend API
          │
          ▼
Coordinator Agent
   ┌────────┼─────────┐
   ▼        ▼         ▼
Research  Coding    Email
 Agent     Agent     Agent
          │
          ▼
      OpenAI API
          │
          ▼
     ChromaDB Memory
```

---

## Technology Stack

### Frontend
- React.js
- CSS
- Axios

### Backend
- Python
- FastAPI

### Generative AI
- OpenAI API
- Prompt Engineering
- Multi-Agent Routing

### Memory Layer
- ChromaDB
- Sentence Transformers

---

## Project Structure

```
neurosync-ai/
│
├── backend/
│   ├── agents/
│   │   ├── coding_agent.py
│   │   ├── email_agent.py
│   │   ├── research_agent.py
│   │   └── coordinator.py
│   │
│   ├── memory/
│   │   └── memory_store.py
│   │
│   ├── services/
│   │   └── openai_service.py
│   │
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── public/
│   └── src/
│
├── screenshots/
│   └── dashboard.png
│
├── README.md
└── .gitignore
```

---

## Installation and Setup

### Clone Repository

```
git clone https://github.com/sukanya-soppihiremath/neurosync-ai.git

cd neurosync-ai
```

---

### Backend Setup

```
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

---

### Frontend Setup

```
cd frontend

npm install

npm start
```

Frontend URL:

```
http://localhost:3000
```

---

## Environment Variables

Create a `.env` file inside backend:

```env
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

Upload only:

```
.env.example
```

Example:

```env
OPENAI_API_KEY=YOUR_KEY
```

---

## Future Enhancements

- Voice Assistant Integration
- LangGraph Workflow Orchestration
- CrewAI Agents
- Retrieval Augmented Generation (RAG)
- Authentication and Authorization
- Task Scheduling System
- Calendar Integration
- Autonomous Agent Workflows
- WhatsApp Integration

---

## Resume Description

Developed **NeuroSync AI**, a Multi-Agent Generative AI Personal Assistant using React, FastAPI, OpenAI APIs, and ChromaDB with intelligent task routing, modular AI agents, conversational interface, and memory integration.

---

## Author

**Sukanya**

Generative AI | Full Stack Development | Multi-Agent Systems
