# Windows Troubleshooting Guide

## 🔧 Common Issues and Solutions

### Python Environment Issues

#### 1. Virtual Environment Activation
```powershell
# If you get a security error
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# If you have multiple Python versions
py -3.9 -m venv .venv

# If activation script is not found
# Make sure you're in the correct directory
cd your-project-directory
.\.venv\Scripts\activate
```

#### 2. Package Installation Issues
```powershell
# If pip fails to install packages
python -m pip install --upgrade pip

# If you get SSL errors
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name

# If you get permission errors
# Run PowerShell as Administrator
Start-Process powershell -Verb RunAs
```

#### 3. Native Dependencies
```powershell
# Install Visual C++ Build Tools
# Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/

# Install specific version
pip install --only-binary :all: package-name

# If you get "Microsoft Visual C++ 14.0 is required"
# Install Visual Studio Build Tools with C++ workload
```

### Node.js Issues

#### 1. Native Module Compilation
```powershell
# Install windows-build-tools (as Administrator)
npm install --global --production windows-build-tools

# Configure node-gyp
npm config set msvs_version 2019
npm config set python python3.9

# If you get node-gyp errors
npm install --global node-gyp
```

#### 2. Path Length Issues
```powershell
# Enable long paths in Windows
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1

# Alternative: Use npm config
npm config set cache C:\npm-cache --global
```

#### 3. Permission Issues
```powershell
# Fix npm permissions
npm cache clean --force
npm config set prefix "C:\Users\YourUsername\AppData\Roaming\npm"

# If you get EACCES errors
# Run PowerShell as Administrator
```

### Git Issues

#### 1. Line Ending Problems
```powershell
# Configure Git for Windows
git config --global core.autocrlf true

# Fix existing repositories
git add --renormalize .
git commit -m "Normalize line endings"
```

#### 2. Credential Issues
```powershell
# Configure Git credentials
git config --global credential.helper wincred

# Clear stored credentials
cmdkey /delete:git:https://github.com
```

#### 3. SSL Certificate Issues
```powershell
# Update Git's SSL certificates
git config --global http.sslBackend schannel
```

## 🛠️ Development Environment Setup

### 1. Visual Studio Code Setup

#### Recommended Extensions
```json
{
    "recommendations": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "eamodio.gitlens",
        "ms-azuretools.vscode-docker",
        "ms-vscode.powershell",
        "ms-vscode.vscode-typescript-next"
    ]
}
```

#### Settings
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

### 2. PowerShell Profile Setup

```powershell
# Create PowerShell profile if it doesn't exist
if (!(Test-Path -Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force
}

# Add useful aliases and functions
Add-Content $PROFILE @'
# Python virtual environment activation
function Activate-Venv {
    param([string]$Path = ".venv")
    & "$Path\Scripts\Activate.ps1"
}

# Git shortcuts
function gs { git status }
function ga { git add . }
function gc { git commit -m $args[0] }
function gp { git push }

# Project shortcuts
function Start-Backend {
    cd backend
    uvicorn main:app --reload
}

function Start-Frontend {
    cd frontend
    npm run dev
}
'@
```

### 3. Database Setup

#### PostgreSQL
```powershell
# Install PostgreSQL
# Download from: https://www.postgresql.org/download/windows/

# Add to PATH
$env:Path += ";C:\Program Files\PostgreSQL\14\bin"

# Create database
createdb content_strategy_agent
```

#### MongoDB
```powershell
# Install MongoDB
# Download from: https://www.mongodb.com/try/download/community

# Add to PATH
$env:Path += ";C:\Program Files\MongoDB\Server\5.0\bin"

# Start MongoDB service
net start MongoDB
```

## 📦 Package Management

### 1. Python Package Management
```powershell
# Create requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt

# Update all packages
pip list --outdated
pip install --upgrade -r requirements.txt
```

### 2. Node.js Package Management
```powershell
# Update npm
npm install -g npm@latest

# Clean npm cache
npm cache clean --force

# Update all packages
npm update

# Check for outdated packages
npm outdated
```

## 🔍 Debugging Tools

### 1. Python Debugging
```powershell
# Enable debug logging
$env:PYTHONPATH = "."
$env:DEBUG = "1"

# Run with debugger
python -m pdb your_script.py
```

### 2. Node.js Debugging
```powershell
# Enable debug logging
$env:DEBUG = "*"

# Run with debugger
node --inspect your_script.js
```

### 3. Browser Debugging
- Chrome DevTools
- React Developer Tools
- Redux DevTools
- Network Panel
- Performance Panel

## 📈 Performance Optimization

### 1. System Optimization
```powershell
# Check system resources
Get-Counter '\Processor(_Total)\% Processor Time'
Get-Counter '\Memory\Available MBytes'

# Monitor disk usage
Get-PSDrive C | Select-Object Used,Free
```

### 2. Development Server Optimization
```powershell
# Increase Node.js memory limit
$env:NODE_OPTIONS="--max-old-space-size=4096"

# Enable Python optimization
$env:PYTHONOPTIMIZE="1"
```

## 🔒 Security Best Practices

### 1. Environment Variables
```powershell
# Create .env file
New-Item .env -ItemType File

# Add to .gitignore
Add-Content .gitignore ".env"

# Load environment variables
Get-Content .env | ForEach-Object {
    if ($_ -match '^([^=]+)=(.*)$') {
        $name = $matches[1]
        $value = $matches[2]
        Set-Item -Path "env:$name" -Value $value
    }
}
```

### 2. SSL/TLS Configuration
```powershell
# Enable TLS 1.2
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# Verify SSL certificates
$env:PYTHONHTTPSVERIFY="1"
```

## 🚀 Deployment Preparation

### 1. Build Process
```powershell
# Python build
python setup.py build

# Node.js build
npm run build

# Create distribution
Compress-Archive -Path dist/* -DestinationPath release.zip
```

### 2. Environment Check
```powershell
# Check Python environment
python -c "import sys; print(sys.executable)"
python -c "import sys; print(sys.path)"

# Check Node.js environment
node -v
npm -v

# Check Git configuration
git config --list
``` 