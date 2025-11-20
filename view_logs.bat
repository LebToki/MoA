@echo off
REM View MoA Chatbot Logs
REM This script displays the latest log entries

echo ========================================
echo MoA Chatbot - Log Viewer
echo ========================================
echo.

if exist "logs\moa_app.log" (
    echo Latest log entries:
    echo ----------------------------------------
    powershell -Command "Get-Content 'logs\moa_app.log' -Tail 50"
) else (
    echo No log file found. Logs will be created when the application runs.
)

echo.
echo ========================================
pause

