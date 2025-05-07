# Windows Development Environment Setup

## 🚀 Initial Setup

### 1. System Requirements
- Windows 10/11 64-bit
- 8GB RAM minimum (16GB recommended)
- 50GB free disk space
- Administrator access

### 2. Windows Features
```powershell
# Enable Windows Subsystem for Linux (optional)
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

# Enable Virtual Machine Platform
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# Enable Windows Terminal
winget install Microsoft.WindowsTerminal
```

## 📦 Package Manager Setup

### 1. Chocolatey Installation
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

### 2. Scoop Installation
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
```

## 🔧 Development Tools

### 1. Visual Studio Code
```powershell
# Install VS Code
choco install vscode

# Install essential extensions
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension dbaeumer.vscode-eslint
code --install-extension esbenp.prettier-vscode
code --install-extension eamodio.gitlens
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-vscode.powershell
```

### 2. Git Setup
```powershell
# Install Git
choco install git

# Configure Git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global core.autocrlf true
git config --global init.defaultBranch main
```

## 🐍 Python Environment

### 1. Python Installation
```powershell
# Install Python
choco install python --version=3.9.13

# Verify installation
python --version
pip --version

# Upgrade pip
python -m pip install --upgrade pip
```

### 2. Virtual Environment
```powershell
# Install virtualenv
pip install virtualenv

# Create project directory
mkdir content-strategy-agent
cd content-strategy-agent

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\activate

# Install project dependencies
pip install -r requirements.txt
```

## 📱 Node.js Environment

### 1. Node.js Installation
```powershell
# Install Node.js
choco install nodejs

# Verify installation
node --version
npm --version

# Install global packages
npm install -g typescript
npm install -g yarn
npm install -g pnpm
```

### 2. Project Setup
```powershell
# Create frontend directory
mkdir frontend
cd frontend

# Initialize project
npm init -y

# Install dependencies
npm install react react-dom next typescript @types/react @types/node
npm install -D eslint prettier @typescript-eslint/parser @typescript-eslint/eslint-plugin
```

## 🗄️ Database Setup

### 1. PostgreSQL
```powershell
# Install PostgreSQL
choco install postgresql

# Add to PATH
$env:Path += ";C:\Program Files\PostgreSQL\14\bin"

# Create database
createdb content_strategy_agent

# Install pgAdmin
choco install pgadmin4
```

### 2. MongoDB
```powershell
# Install MongoDB
choco install mongodb

# Add to PATH
$env:Path += ";C:\Program Files\MongoDB\Server\5.0\bin"

# Start MongoDB service
net start MongoDB

# Install MongoDB Compass
choco install mongodb-compass
```

## 🔒 Security Setup

### 1. SSL/TLS Configuration
```powershell
# Enable TLS 1.2
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# Install OpenSSL
choco install openssl
```

### 2. Environment Variables
```powershell
# Create .env file
New-Item .env -ItemType File

# Add to .gitignore
Add-Content .gitignore ".env"

# Set environment variables
$env:PYTHONHTTPSVERIFY="1"
$env:NODE_ENV="development"
```

## 🎨 IDE Configuration

### 1. VS Code Settings
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
    "python.terminal.activateEnvironment": true,
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.fixAll.eslint": true
    },
    "files.eol": "\n",
    "terminal.integrated.defaultProfile.windows": "PowerShell"
}
```

### 2. ESLint Configuration
```json
{
    "extends": [
        "eslint:recommended",
        "plugin:@typescript-eslint/recommended"
    ],
    "parser": "@typescript-eslint/parser",
    "plugins": ["@typescript-eslint"],
    "root": true
}
```

## 📝 Git Configuration

### 1. Git Hooks
```powershell
# Install husky
npm install husky --save-dev

# Install lint-staged
npm install lint-staged --save-dev

# Configure pre-commit hooks
npx husky install
npx husky add .husky/pre-commit "npx lint-staged"
```

### 2. Git Ignore
```powershell
# Create .gitignore
New-Item .gitignore -ItemType File

# Add common patterns
Add-Content .gitignore @"
# Python
__pycache__/
*.py[cod]
*$py.class
.venv/
.env

# Node
node_modules/
.next/
dist/
build/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# System
.DS_Store
Thumbs.db
"@
```

## 🚀 Project Structure

### 1. Directory Setup
```powershell
# Create project structure
mkdir backend
mkdir frontend
mkdir docs
mkdir tests
mkdir logs

# Create backend structure
cd backend
mkdir api
mkdir services
mkdir models
mkdir utils
mkdir tests

# Create frontend structure
cd ../frontend
mkdir src
cd src
mkdir components
mkdir pages
mkdir hooks
mkdir store
mkdir services
mkdir utils
mkdir types
mkdir styles
```

### 2. Initial Files
```powershell
# Create backend files
cd ../../backend
New-Item main.py
New-Item requirements.txt
New-Item README.md

# Create frontend files
cd ../frontend
New-Item package.json
New-Item tsconfig.json
New-Item next.config.js
New-Item README.md
```

## 📈 Performance Optimization

### 1. System Configuration
```powershell
# Enable long paths
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1

# Configure npm
npm config set cache C:\npm-cache --global
```

### 2. Development Server
```powershell
# Configure Node.js
$env:NODE_OPTIONS="--max-old-space-size=4096"

# Configure Python
$env:PYTHONOPTIMIZE="1"
```

## 🔍 Verification

### 1. Environment Check
```powershell
# Check Python
python --version
pip --version

# Check Node.js
node --version
npm --version

# Check Git
git --version

# Check databases
psql --version
mongod --version
```

### 2. Project Check
```powershell
# Check backend
cd backend
python -m pytest

# Check frontend
cd ../frontend
npm test
``` 