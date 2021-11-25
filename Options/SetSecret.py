from cryptography.fernet import Fernet
from colorama import Fore
import time
import os
import sys

sys.stdout.write("\x1b]2;Cryptor | Set Secret\x07")

print(Fore.GREEN + open("./Art/art.txt", "r").read())

NewKey = input("""Input your given secret:
""")

try:
    Fernet(NewKey)
    open("./Tools/Secret.txt", "w").write(NewKey)
    print("Secret has been set!")

    print("""

    """)
    input(f"""{Fore.LIGHTBLACK_EX}Press Enter to Continue...""")
    os.system('python ./Start.py')

except:
    print("""Invalid Key""")
    time.sleep(3)
    os.system('python ./Start.py')