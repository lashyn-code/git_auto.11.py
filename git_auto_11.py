import subprocess
import time
import os

# Репозиторий жолын енгізу
repo_path = input("Репозиторий орналасқан жолды енгізіңіз: ")

if not os.path.exists(repo_path):
    print("Көрсетілген жол жоқ!")
    exit()

os.chdir(repo_path)
print(f"Репозиторий табылды: {repo_path}")

def run_git():
    try:
        subprocess.run(["git", "add", "."], check=True)
        message = input("Commit хабарламасын енгізіңіз: ")
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Барлығы сәтті аяқталды!")
        return True
    except subprocess.CalledProcessError:
        print("Commit немесе Push сәтсіз! 5 секундтан кейін қайтадан әрекет жасаймыз...")
        return False

while not run_git():
    time.sleep(5)