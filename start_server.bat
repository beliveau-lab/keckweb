@echo off
REM Keck Microscopy Center Website - Windows Startup Script
REM This batch file starts a local web server for testing the website

echo.
echo ============================================================
echo  Keck Microscopy Center Website Server
echo ============================================================
echo.
echo Starting web server on port 8000...
echo Opening website in your browser...
echo.
echo Press Ctrl+C to stop the server
echo.

python -m http.server 8000

pause
