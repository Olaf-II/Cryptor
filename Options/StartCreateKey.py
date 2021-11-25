from cryptography.fernet import Fernet
from colorama import Fore

NewKey = Fernet.generate_key()
open("./Tools/Secret.txt", "w").write(NewKey.decode())