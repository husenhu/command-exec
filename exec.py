import os

ans=True

def scroll_lock():
   cmd = "xmodmap -e 'add mod3 = Scroll_Lock'"
   os.system(cmd)

def my_quit_fn():
   raise SystemExit

def youtube_fn():
    url = input('Insert URL: ')
    file_format = input('Format MP3/MP4/MKV/check: ')
    if file_format == 'mp3':
        cmd = "youtube-dl -x --audio-format mp3 " + url
        os.system(cmd)
    elif file_format == 'mp4':
        cmd = "youtube-dl " + url
        os.system(cmd)
    elif file_format == 'mkv':
        cmd = "youtube-dl " + url
        os.system(cmd)
    elif file_format == "check":
        cmd = "youtube-dl -F " + url
        os.system(cmd)
        
        print("Checking Process: Done")
        format_code = input("Insert Format Code (number): ")
        cmd_format_code = "youtube-dl -f " + format_code + " " + url
        os.system(cmd_format_code)
    else:
        print("No command found!")

def invalid():
   print ("INVALID CHOICE!")

print ("Welcome to Manual Launcher")
print ("Created by Husen SAJ")
print ("--------------------------")

menu = {
        "1":("Activated Scroll Lock",scroll_lock),
        "2":("Download Youtube Video", youtube_fn),
        "9":("Quit",my_quit_fn)
       }

for key in sorted(menu.keys()):
     print (key + ":" + menu[key][0])

ans = input("Select Module: ")
menu.get(ans,[None,invalid])[1]()
