# Imports
from cryptography.fernet import Fernet
from colorama import Fore
import os
import time
import pyperclip
import sys

print(Fore.GREEN + open("./Art/art.txt", "r").read())

sys.stdout.write("\x1b]2;Cryptor | Decrypt\x07")

# Get Secret
try:
    DecryptKey = open("./Tools/Secret.txt", "r").read()
    DecryptKey = Fernet(DecryptKey)
except:
    print("""Your secret file has not available""")

EncryptedMessage = input(f"""{Fore.LIGHTGREEN_EX}What would you like to decrypt?
{Fore.WHITE}""").encode('utf-8')

# Decryption
try:
    DecryptedMessage = DecryptKey.decrypt(EncryptedMessage)
    print("")
    print(Fore.LIGHTGREEN_EX + DecryptedMessage.decode())
except:
    print("Decryption Failed")
finally:
    print("""
    
    """)
    input(f"""{Fore.LIGHTBLACK_EX}Press Enter to Continue...""")
    os.system('python ./Start.py')