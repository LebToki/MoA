# View MoA Chatbot Logs
# This script displays the latest log entries

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "MoA Chatbot - Log Viewer" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$logFile = "logs\moa_app.log"

if (Test-Path $logFile) {
    Write-Host "Latest log entries:" -ForegroundColor Green
    Write-Host "----------------------------------------" -ForegroundColor Gray
    
    # Show last 50 lines
    Get-Content $logFile -Tail 50 | ForEach-Object {
        if ($_ -match "ERROR") {
            Write-Host $_ -ForegroundColor Red
        } elseif ($_ -match "WARNING") {
            Write-Host $_ -ForegroundColor Yellow
        } elseif ($_ -match "INFO") {
            Write-Host $_ -ForegroundColor Cyan
        } else {
            Write-Host $_
        }
    }
    
    Write-Host ""
    Write-Host "Full log file: $((Get-Item $logFile).FullName)" -ForegroundColor Gray
    Write-Host "File size: $([math]::Round((Get-Item $logFile).Length / 1KB, 2)) KB" -ForegroundColor Gray
} else {
    Write-Host "No log file found. Logs will be created when the application runs." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan

