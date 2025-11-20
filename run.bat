@echo off
REM MoA Groq Chatbot - Windows Run Script
REM This script runs the Flask application on Windows

echo Starting MoA Groq Chatbot...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

REM Change to the script directory
cd /d "%~dp0"

REM Check if .env file exists
if not exist ".env" (
    echo WARNING: .env file not found!
    echo Please create a .env file with your API keys:
    echo   GROQ_API_KEY=your_groq_api_key
    echo   OPENAI_API_KEY=your_openai_api_key
    echo   DEBUG=0
    echo.
)

REM Create necessary directories
if not exist "instance" mkdir instance
if not exist "uploads" mkdir uploads

REM Run the Flask application
echo Starting Flask server...
echo Open your browser and navigate to: http://127.0.0.1:5000/
echo Press Ctrl+C to stop the server
echo.
python app.py

pause

