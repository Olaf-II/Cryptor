import git
import os
import shutil
import time
from colorama import Fore
from git import RemoteProgress

try:   
    git.Repo.clone_from('https://github.com/Olaf-II/Cryptor', './Update', branch='main')

    shutil.rmtree('./Art')
    shutil.rmtree('./Options')
    shutil.rmtree('./Update/Tools')

    os.remove('README.md')
    os.remove('setup.bat')
    os.remove('Start.py')
    os.remove('Update/Update.py')

    input(f"{Fore.GREEN}Update Complete \n{Fore.RED}Drag all contents from the new Update folder into your Cryptor directory.\nAfter you have done this\n{Fore.LIGHTBLACK_EX}Press Enter To Continue")
    os.close()


except:
    print(f"{Fore.RED}Update Failed")