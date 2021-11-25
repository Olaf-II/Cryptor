from cryptography.fernet import Fernet
open("./Tools/Secret.txt", "w").write(Fernet.generate_key().decode())