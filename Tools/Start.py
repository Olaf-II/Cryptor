import os
import time
import subprocess
import webbrowser
import sys

sys.stdout.write("\x1b]2;Cryptor | Start\x07")

try:
  from colorama import Fore
  import pyperclip
  import cryptography
except:
  if(input("""Download required Python packages? (y/n)
  """) == "y"):
    subprocess.call([r'setup.bat'])
  else:
    os.close()

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

# Check if first time opened
Username = open("./Tools/Username.txt", "r").read()
if(Username == ""):
  os.system('python ./Options/CreateUser.py')

Secret = open("./Tools/Secret.txt", "r").read()
if(Secret == "aNlZZoZ-B5mk85zG8nylNScbfoovofvWf3ht2IJQhic="):
  if(Username != "admin"):
    os.system('python ./Options/StartCreateKey.py')

clearConsole()

print(Fore.GREEN + open("./Art/art.txt", "r").read())

# Options
Action = input(f"""{Fore.CYAN}What would you like to do?
{Fore.WHITE}1. Encrypt A Message
2. Decrypt A Message
3. Decrypt A Message (clipboard)
4. Create A Group
5. Change Username
6. Set Secret
7. Join Discord Server
{Fore.CYAN}Enter the corresponding number

{Fore.WHITE}""")

if(Action == "1"):
  clearConsole()
  os.system('python ./Options/encrypt.py')
elif(Action == "2"):
  clearConsole()
  os.system('python ./Options/decrypt.py')
elif(Action == "3"):
  clearConsole()
  os.system('python ./Options/clipboardDecrypt.py')
elif(Action == "4"):
  clearConsole()
  os.system('python ./Options/startGroup.py')
elif(Action == "5"):
  clearConsole()
  os.system('python ./Options/createUser.py')
elif(Action == "6"):
  clearConsole()
  os.system('python ./Options/resetSecret.py')
elif(Action == "7"):
  clearConsole()
  webbrowser.open("https://discord.gg/NcdwKWrA5C", new=1)
  os.system('python ./Start.py')
else:
  print("Invalid Option")
  input(f"""{Fore.LIGHTBLACK_EX}Press Enter to Continue...""")
  os.system('python ./Start.py')