from cryptography.fernet import Fernet
from colorama import Fore
import os
import time
import pyperclip
import sys

sys.stdout.write("\x1b]2;Cryptor | Decrypt\x07")

print(Fore.GREEN + open("./Art/art.txt", "r").read())

try:
    DecryptKey = open("./Tools/Secret.txt", "r").read()
    DecryptKey = Fernet(DecryptKey)
except:
    print("""Your secret file has not available""")

EncryptedMessage = pyperclip.paste().encode()

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