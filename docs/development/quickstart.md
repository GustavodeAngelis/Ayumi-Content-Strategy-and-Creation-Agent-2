# Quick Start Guide

## 🚀 Getting Started

### Prerequisites
- Python 3.9+ (Windows)
- Node.js 16+ (Windows)
- Git for Windows
- PowerShell 7+ (recommended)
- Visual Studio Build Tools (for native dependencies)

### Windows-Specific Setup

1. Install Python:
   - Download Python installer from [python.org](https://www.python.org/downloads/windows/)
   - During installation, check "Add Python to PATH"
   - Check "Install for all users" (recommended)

2. Install Node.js:
   - Download Node.js installer from [nodejs.org](https://nodejs.org/)
   - Use the LTS version
   - During installation, check "Automatically install necessary tools"

3. Install Git:
   - Download Git for Windows from [git-scm.com](https://git-scm.com/download/win)
   - Use default settings during installation

4. Install Visual Studio Build Tools:
   - Download from [Visual Studio Downloads](https://visualstudio.microsoft.com/downloads/)
   - Select "Desktop development with C++"
   - This is required for some Python packages with native dependencies

### Initial Setup

1. Clone the repository:
```powershell
# Using PowerShell
git clone https://github.com/your-org/content-strategy-agent.git
cd content-strategy-agent
```

2. Set up the backend:
```powershell
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
Copy-Item .env.example .env
# Edit .env with your configuration
```

3. Set up the frontend:
```powershell
cd frontend
npm install
Copy-Item .env.example .env
# Edit .env with your configuration
```

4. Start the development servers:
```powershell
# Terminal 1 - Backend
cd backend
uvicorn main:app --reload

# Terminal 2 - Frontend
cd frontend
npm run dev
```

## 🔧 Windows-Specific Troubleshooting

### Common Issues and Solutions

1. Python Virtual Environment Issues:
```powershell
# If you get a security error when activating venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# If you have multiple Python versions
py -3.9 -m venv .venv
```

2. Node.js Native Module Issues:
```powershell
# Install windows-build-tools (run as Administrator)
npm install --global --production windows-build-tools

# If you get node-gyp errors
npm config set msvs_version 2019
```

3. Git Line Ending Issues:
```powershell
# Configure Git to handle line endings
git config --global core.autocrlf true
```

4. Path Length Issues:
```powershell
# Enable long paths in Windows
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1
```

### Development Tools for Windows

1. Recommended IDEs:
   - Visual Studio Code with extensions:
     - Python
     - ESLint
     - Prettier
     - GitLens
   - PyCharm Professional

2. Terminal:
   - Windows Terminal
   - PowerShell 7+
   - Git Bash (optional)

3. Database Tools:
   - pgAdmin 4 for PostgreSQL
   - MongoDB Compass

## 📚 Key Documentation

- [Development Guidelines](guidelines.md)
- [API Guidelines](api-guidelines.md)
- [Module Documentation](../modules/)

## 🎯 First Steps

1. Review the project architecture:
   - Backend: FastAPI application
   - Frontend: React/TypeScript application
   - Database: PostgreSQL with ChromaDB for vector storage

2. Understand the core modules:
   - Vector Memory System
   - RAG Pipeline
   - User Interaction Flow
   - Prompt Templates
   - Learning System

3. Set up your development environment:
   - Configure your IDE
   - Set up linting
   - Configure debugging tools

## 🧪 Running Tests

```bash
# Backend tests
pytest

# Frontend tests
cd frontend
npm test
```

## 🔍 Common Tasks

### Creating a New Feature

1. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```

2. Implement your changes following the [Development Guidelines](guidelines.md)

3. Write tests for your changes

4. Create a pull request

### Debugging

1. Backend debugging:
   - Use FastAPI's built-in debugger
   - Check logs in `logs/` directory
   - Use pytest for debugging tests

2. Frontend debugging:
   - Use React Developer Tools
   - Check browser console
   - Use Jest for debugging tests

## 📈 Monitoring

- Backend: Prometheus metrics at `/metrics`
- Frontend: React DevTools
- Logs: Check `logs/` directory

## 🆘 Getting Help

1. Check the documentation first
2. Search existing issues
3. Ask in the team chat
4. Create a new issue if needed

## 🔄 Development Workflow

1. Pull latest changes:
```bash
git pull origin main
```

2. Create feature branch:
```bash
git checkout -b feature/your-feature
```

3. Make changes and commit:
```bash
git add .
git commit -m "feat: your feature description"
```

4. Push changes:
```bash
git push origin feature/your-feature
```

5. Create pull request

## 🎨 Code Style

- Backend: Follow PEP 8
- Frontend: Follow ESLint configuration
- Use pre-commit hooks for automatic formatting

## 🔒 Security

- Never commit sensitive data
- Use environment variables
- Follow security guidelines
- Report security issues privately

## 📝 Documentation

- Update documentation when changing code
- Follow documentation guidelines
- Use clear and concise language
- Include examples where helpful 