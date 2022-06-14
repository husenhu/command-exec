import os

ans=True

def clear_screen_fn():
	cmd = "cls"
	os.system(cmd)

def download_youtube_fn():
	url = input("Inser URL: ")
	file_format = input("Format MP3/MP4/MKV/check: ")
	
	if file_format == 'mp3':
		cmd = "com\youtube-dl.exe -x --audio-format mp3 " + url
		os.system(cmd)

		re_enter = "python win32.py"
		os.system(re_enter)
        
	elif file_format == 'mp4':
		cmd = "com\youtube-dl " + url
		os.system(cmd)

		re_enter = "python win32.py"
		os.system(re_enter)

	elif file_format == 'mkv':
		cmd = "com\youtube-dl " + url
		os.system(cmd)

		re_enter = "python win32.py"
		os.system(re_enter)

	elif file_format == "check":
		cmd = "com\youtube-dl -F " + url
		os.system(cmd)
        
		print("Checking Process: Done")
		format_code = input("Insert Format Code (number): ")
		cmd_format_code = "com\youtube-dl -f " + format_code + " " + url
		os.system(cmd_format_code)

	else:
		print("No command found!")
		re_enter = "python win32.py"
		os.system(re_enter)
		
def invalid():
	print ("INVALID CHOICE!")

def my_quit_fn():
	raise SystemExit

clear_screen_fn()
	
print ("Welcome to Launcher for Windows")
print ("Created by Husen SAJ")
print ("---------------------------------")

menu = {
	"1":("Download Youtube Video", download_youtube_fn),
	"9":("quit", my_quit_fn)
}

for key in sorted(menu.keys()):
     print (key + ":" + menu[key][0])

ans = input("Select Module: ")
menu.get(ans,[None,invalid])[1]()