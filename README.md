# 🧠 Content Strategy and Creation Agent

An AI-powered agent designed to assist independent artists and content creators in planning and creating organic Instagram content. Built specifically for Ayumi, combining strategy, creativity, and AI-powered suggestions to enhance the content production process.

## ✨ Core Features

- 📊 Content Strategy Generation
  - Performance-based content ideas
  - Trend analysis and recommendations
  - Strategic theme suggestions

- 🎨 Content Creation Support
  - Optimized scripts and captions
  - Tone of voice consistency
  - Creative experimentation

- 🧠 Smart Learning System
  - Performance-based learning
  - Continuous improvement
  - Data-driven insights

## 🏗️ Technical Architecture

```
Frontend (React + Tailwind)
        ↓
FastAPI (Backend)
        ↓
LangChain (Orchestration)
        ↓
Chroma DB (Vector Memory)
        ↓
OpenAI LLMs
```

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python 3.10+
- **Frontend**: React, TypeScript, Tailwind CSS
- **AI/ML**: OpenAI LLMs, LangChain
- **Database**: ChromaDB (vector store), SQLite
- **Development**: Git, GitHub Actions

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- Git

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd content-strategy-agent
```

2. Set up the backend:
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up the frontend:
```bash
cd frontend
npm install
```

4. Start the development servers:
```bash
# Backend
cd backend
uvicorn main:app --reload

# Frontend
cd frontend
npm run dev
```

## 📚 Documentation

Detailed documentation is available in the `docs/` directory:

- `docs/architecture/` - System architecture and design decisions
- `docs/modules/` - Detailed module documentation
- `docs/development/` - Development guidelines and setup

## 🤝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📝 License

This project is licensed under private use for Ayumi's brand development.

## 🔒 Security & Ethics

- All content requires human review before publishing
- No content is copied verbatim from references
- User data is handled with strict privacy guidelines 