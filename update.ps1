# MoA Chatbot - Update Script for PowerShell
# Checks for and applies updates from git repository

Write-Host "MoA Chatbot - Self-Update Utility" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

# Check for updates
python update.py --check

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    $update = Read-Host "Do you want to update now? (Y/N)"
    if ($update -eq "Y" -or $update -eq "y") {
        Write-Host ""
        python update.py --update
    }
} else {
    Write-Host ""
    Write-Host "Update check failed. Make sure you're in a git repository." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
}

