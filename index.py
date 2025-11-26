import json
import os
from request import make_download_request


data = {}

def read_settings():
    global data 
    try:
        with open('settings.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {
        "default_download_path":None,
        "download_quality":None,
        "default_media_type":None,
        "always_overwrite_similar_files":None
        }
        with open('settings.json', 'w') as file:
            json.dump(data, file, indent=4)


read_settings()
default_download_path = data.get('default_download_path')
download_quality = data.get('download_quality')
default_media_type = data.get('default_media_type')
always_overwrite_similar_files = data.get('always_overwrite_similar_files')



if not default_download_path or not download_quality or not default_media_type or always_overwrite_similar_files == None:
    print('\n--- Settings Setup ---')
    decision = input("Some settings have not been assigned values. Do you want to use our default values(y) or set your own(n)? y/n ")
    
    if decision.lower() != 'n':
        default_download_path = './downloads'
        download_quality = 3
        default_media_type = 'audio'
        always_overwrite_similar_files = False
        
        data = {
            "default_download_path": default_download_path,
            "download_quality": download_quality,
            "default_media_type": default_media_type,
            "always_overwrite_similar_files": always_overwrite_similar_files
        }
        
        with open('settings.json', 'w') as file:
            json.dump(data, file, indent=4)
        
    else:
        
        if not default_download_path:
            default_download_path = input('Please specify the download path to store downloaded media or press Enter to use the default path (./downloads): ') or './downloads'
        
        if not download_quality:
            try:
                quality_input = input('Please specify a default download quality (1~3) or press Enter to use the default value (i.e. 3): ')
                download_quality = int(quality_input) if quality_input else 3
                if download_quality < 1 or download_quality > 3:
                    print("Quality out of range (1-3), setting to default 3.")
                    download_quality = 3
            except ValueError:
                print("Invalid input, setting quality to default 3.")
                download_quality = 3
                
        if not default_media_type:
            media_input = input("Please specify a default media type to download in. Type 'a' for audio, 'v' for video or 'Enter' for audio as the default: ").lower()
            if media_input == 'v':
                default_media_type = 'video'
            else:
                default_media_type = 'audio'
                
        if always_overwrite_similar_files == None:
            overwrite_input = input("Do you always want to overwrite similar files while downloading? y/n ")
            always_overwrite_similar_files = overwrite_input.lower() == 'y'

        data = {
            "default_download_path":default_download_path,
            "download_quality":download_quality,
            "default_media_type":default_media_type,
            "always_overwrite_similar_files":always_overwrite_similar_files
        }
        
        with open('settings.json', 'w') as file:
            json.dump(data, file, indent=4)


print("""\n
─────╔╗───────── ───────╔═╗╔╗─── ─╔╗──────────────────────╔╗──────
╔═╦═╗╠╣╔═╗╔═╗╔╦╗ ╔══╗╔╦╗║═╣╠╣╔═╗ ╔╝║╔═╗╔╦╦╗╔═╦╗╔╗─╔═╗╔═╗─╔╝║╔═╗╔╦╗
╚╗║╔╝║║║╬║║╩╣║╔╝ ║║║║║║║╠═║║║║═╣ ║╬║║╬║║║║║║║║║║╚╗║╬║║╬╚╗║╬║║╩╣║╔╝
─╚═╝─╚╝║╔╝╚═╝╚╝─ ╚╩╩╝╚═╝╚═╝╚╝╚═╝ ╚═╝╚═╝╚══╝╚╩═╝╚═╝╚═╝╚══╝╚═╝╚═╝╚╝─
───────╚╝─────── ─────────────── ─────────────────────────────────
      
by Áà Män シ
Type '/exit' to exit\n\n
""")

os.makedirs(default_download_path, exist_ok=True)

def start_download():
    song = input('What song do you want to download? ')
    if song == '/exit':
        return
    
    make_download_request(song.lower(), default_download_path, download_quality, default_media_type, always_overwrite_similar_files)
    start_download()

start_download()