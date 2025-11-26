@echo off
echo Initializing...
python -c "import yt_dlp" 2>nul

if errorlevel 1 (
    echo Installing yt-dlp...
    pip install yt-dlp
)
echo Starting Viper Downloader...
python index.py
pause