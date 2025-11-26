import yt_dlp
import os

def make_download_request(query, path, quality, mediatype, overwrite):
    print('Working...')
    quality_map = {
        1: "best[height<=360]/bestvideo[height<=720]+bestaudio/best",
        2: "best[height<=720]/bestvideo[height<=720]+bestaudio/best",
        3: "best"
    }

    if mediatype == 'audio':
        format_selector = 'bestaudio/best'
        outtmpl = f"{path}/%(title)s.m4a"
        postprocessors = []
    else:
        format_selector = quality_map.get(quality, "best")
        outtmpl = f"{path}/%(title)s.%(ext)s"
        postprocessors = []

    ydl_opts = {
        'format': format_selector,
        'outtmpl': outtmpl,
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'ignoreerrors': True,
        'nooverwrites': not overwrite,
        'extractor_args': {
            'youtube': {
                'player_client': ['default']
            }
        }
    }

    if query.startswith('http://') or query.startswith('https://'):
        url = query
    else:
        url = f"ytsearch1:{query}"

    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print('Downloading...')
            ydl.download([url])
            print("Done!")
        except Exception as e:
            print(f"Error: {e}")