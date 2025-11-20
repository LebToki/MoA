@echo off
REM MoA Chatbot - Update Script for Windows
REM Checks for and applies updates from git repository

echo MoA Chatbot - Self-Update Utility
echo ===================================
echo.

python update.py --check

if %ERRORLEVEL% EQU 0 (
    echo.
    set /p UPDATE="Do you want to update now? (Y/N): "
    if /i "%UPDATE%"=="Y" (
        echo.
        python update.py --update
    )
) else (
    echo.
    echo Update check failed. Make sure you're in a git repository.
    pause
)

