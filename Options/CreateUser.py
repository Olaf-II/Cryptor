from cryptography.fernet import Fernet
from colorama import Fore
import os
import time
import sys

sys.stdout.write("\x1b]2;Cryptor | Create Username\x07")

print(Fore.GREEN + open("./Art/art.txt", "r").read())

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

Username = input(f"""{Fore.WHITE}What would you like your username to be?
""")

if(Username != ""):

    if(input("""Are you sure? (This can be changed later on!) (y/n)
    """) == "y"):
        open("./Tools/Username.txt", "w").write(Username)
        os.system('python ./Start.py')
    else:
        clearConsole()
        os.system('python ./Options/CreateUser.py')
else:
    print("Invalid Username")
    time.sleep(3)
    clearConsole()
    os.system('python ./Options/CreateUser.py')