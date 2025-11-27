@echo off
echo Initializing...
python -c "import yt_dlp" 2>nul

if errorlevel 1 (
    echo Installing yt-dlp...
    pip install yt-dlp
)
REG ADD HKCU\CONSOLE /f /v VirtualTerminalLevel /t REG_DWORD /d 1
echo Starting Viper Music Downloader...
python index.py
pause