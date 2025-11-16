import subprocess

def get_changed_files():
    result = subprocess.run(["git", "status", "--short"], capture_output=True, text=True)
    if result.returncode != 0:
        print("Git командасын орындау кезінде қате пайда болды.")
        return

    print("Өзгерген файлдар:")
    lines = result.stdout.strip().split("\n")
    for line in lines:
        if line:
            print(line)

if __name__ == "_main_":
    get_changed_files()