# MoA Groq Chatbot - PowerShell Run Script
# This script runs the Flask application on Windows

Write-Host "Starting MoA Groq Chatbot..." -ForegroundColor Green
Write-Host ""

# Check if Python is available
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python version: $pythonVersion" -ForegroundColor Cyan
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.8 or higher" -ForegroundColor Red
    exit 1
}

# Change to the script directory
Set-Location $PSScriptRoot

# Check if .env file exists
if (-not (Test-Path ".env")) {
    Write-Host "WARNING: .env file not found!" -ForegroundColor Yellow
    Write-Host "Please create a .env file with your API keys:" -ForegroundColor Yellow
    Write-Host "  GROQ_API_KEY=your_groq_api_key" -ForegroundColor Yellow
    Write-Host "  OPENAI_API_KEY=your_openai_api_key" -ForegroundColor Yellow
    Write-Host "  DEBUG=0" -ForegroundColor Yellow
    Write-Host ""
}

# Create necessary directories
if (-not (Test-Path "instance")) {
    New-Item -ItemType Directory -Path "instance" | Out-Null
    Write-Host "Created 'instance' directory" -ForegroundColor Green
}

if (-not (Test-Path "uploads")) {
    New-Item -ItemType Directory -Path "uploads" | Out-Null
    Write-Host "Created 'uploads' directory" -ForegroundColor Green
}

# Run the Flask application
Write-Host "Starting Flask server..." -ForegroundColor Cyan
Write-Host "Open your browser and navigate to: http://127.0.0.1:5000/" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Cyan
Write-Host ""

python app.py

