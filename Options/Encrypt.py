# Imports
from cryptography.fernet import Fernet
from colorama import Fore
import os
import time
import pyperclip
import sys

sys.stdout.write("\x1b]2;Cryptor | Encrypt\x07")

print(Fore.GREEN + open("./Art/art.txt", "r").read())

# Get Secret
try:
    EncryptKey = open("./Tools/Secret.txt", "r").read()
    EncryptKey = Fernet(EncryptKey)
except:
    print("""Your secret file has not available""")

# Get Username
try:
    Username = open("./Tools/Username.txt", "r").read()
except:
    print("""Your username has not been set""")

# Get Requested Message
DecryptedMessage = "From " + Username + ": " + input(f"""{Fore.LIGHTGREEN_EX}What would you like to encrypt?
{Fore.WHITE}""")
DecryptedMessage = DecryptedMessage.encode()

# Encryption
try:
    EncryptedMessage = EncryptKey.encrypt(DecryptedMessage)
    print("")
    print(f"{Fore.WHITE}Encrypted Message: {Fore.GREEN}" + EncryptedMessage.decode())
    pyperclip.copy(EncryptedMessage.decode())
    print(f"""{Fore.WHITE}Message successfully copied to clipboard""")
except:
    print("""Invalid String""")
finally:
    print("""

    """)
    input(f"""{Fore.LIGHTBLACK_EX}Press Enter to Continue...""")
    os.system('python ./Start.py')