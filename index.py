import json
import os
import shutil
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
    decision = input("\033[96mSome settings have not been assigned values. Do you want to use our default values(y) or set your own(n)? y/n\033[0m ")
    
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

yellow = '\033[93m'
blue = '\033[94m'
reset = '\033[0m'
print(f"""\n\033[91m
─────╔╗───────── ───────╔═╗╔╗─── ─╔╗──────────────────────╔╗──────
╔═╦═╗╠╣╔═╗╔═╗╔╦╗ ╔══╗╔╦╗║═╣╠╣╔═╗ ╔╝║╔═╗╔╦╦╗╔═╦╗╔╗─╔═╗╔═╗─╔╝║╔═╗╔╦╗
╚╗║╔╝║║║╬║║╩╣║╔╝ ║║║║║║║╠═║║║║═╣ ║╬║║╬║║║║║║║║║║╚╗║╬║║╬╚╗║╬║║╩╣║╔╝
─╚═╝─╚╝║╔╝╚═╝╚╝─ ╚╩╩╝╚═╝╚═╝╚╝╚═╝ ╚═╝╚═╝╚══╝╚╩═╝╚═╝╚═╝╚══╝╚═╝╚═╝╚╝─
───────╚╝─────── ─────────────── ─────────────────────────────────
\033[0m""")
print(f"""
Commands:
      
      \033[93m/exit\033[0m                         -   kill program.
      \033[93m/path\033[0m        \033[96m<directory>\033[0m      -   specify directory.
      \033[93m/quality\033[0m     \033[96m<1~3>\033[0m            -   specify quality.
      \033[93m/media\033[0m       \033[96m<audio/video>\033[0m    -   specify media type.
      \033[93m/overwrite\033[0m   \033[96m<true/false>\033[0m     -   overwrite.

""")
os.makedirs(default_download_path, exist_ok=True)

def start_download():
    song0 = input('What song do you want to download? ')
    song = song0.lower()
    if not song:
        print('\n\033[91mPlease enter a valid query!\033[0m')
        start_download()
    if song.startswith('/'):
        global always_overwrite_similar_files, default_download_path, default_media_type, download_quality
        if song == '/exit':
            exit()
        elif song.startswith('/path'):
            os.makedirs(song0.replace('/path','').strip(), exist_ok=True)
            try:
                for filename in os.listdir(default_download_path):
                    new_path = os.path.join(default_download_path, filename)
                    if os.path.isfile(new_path):
                        shutil.move(new_path, song0.replace('/path','').strip())
                os.rmdir(default_download_path)
                default_download_path = song0.replace('/path','').strip()
            except Exception as e:
                print(f"\n\033[91mAn Error Occurred: {e}\033[0m")
            else:
                print('\n\033[92mUpdated Successfully!\033[0m')
        elif song.startswith('/quality'):
            try:
                if int(song.replace('/quality','')) > 3 or int(song.replace('/quality','')) < 1:
                    print('\n\033[91mOut of range!\033[0m')
                else:
                    download_quality = int(song.replace('/quality',''))
                    print('\n\033[92mUpdated Successfully!\033[0m')
            except ValueError:
                print('\n\033[91mInvalid value!\033[0m')
        elif song.startswith('/media'):
            if song.replace('/media','').strip() == 'a' or song.replace('/media','').strip() == 'audio':
                default_media_type = 'audio'
                print('\n\033[92mUpdated Successfully!\033[0m')
            elif song.replace('/media','').strip() == 'v' or song.replace('/media','').strip() == 'video':
                default_media_type = 'video'
                print('\n\033[92mUpdated Successfully!\033[0m')
            else:
                print('\n\033[91mInvalid media type!\033[0m')
        elif song.startswith('/overwrite'):
            if song.replace('/overwrite','').strip() == 'y' or song.replace('/overwrite','').strip() == 'true':
                always_overwrite_similar_files = True
                print('\n\033[92mUpdated Successfully!\033[0m')
            elif song.replace('/overwrite','').strip() == 'n' or song.replace('/overwrite','').strip() == 'false':
                always_overwrite_similar_files = False
                print('\n\033[92mUpdated Successfully!\033[0m')
            else:
                print('\n\033[91mInvalid value!\033[0m')
        else:
            print('\n\033[91mInvalid command!\033[0m')
            
        data = {
            "default_download_path":default_download_path,
            "download_quality":download_quality,
            "default_media_type":default_media_type,
            "always_overwrite_similar_files":always_overwrite_similar_files
        }
        
        with open('settings.json', 'w') as file:
            json.dump(data, file, indent=4)
        start_download()
    make_download_request(song, default_download_path, download_quality, default_media_type, always_overwrite_similar_files)
    start_download()

start_download()