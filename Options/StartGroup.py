# Imports
from cryptography.fernet import Fernet
from colorama import Fore
import os
import time
import pyperclip
import sys

sys.stdout.write("\x1b]2;Cryptor | Start a Group\x07")

print(Fore.GREEN + open("./Art/art.txt", "r").read())

# Get Secret & Print
try:
    EncryptKey = open("./Tools/Secret.txt", "r").read()
    
    print(f"""{Fore.WHITE}To start a group do the following:
    1. Get your friends to download Encrypter
    2. Select the option 'Set Secret'
    3. Type: {Fore.LIGHTBLUE_EX}""" + EncryptKey + f"""{Fore.WHITE}
    4. Send your encrypted messages to your friends for them to decrypt on their app!""")

    print("""

    """)
    input(f"""{Fore.LIGHTBLACK_EX}Press Enter to Continue...""")

    os.system('python ./Start.py')
except:
    print("""Your secret file was not available""")
    time.sleep(3)