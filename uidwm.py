import os
import subprocess
os.chdir("..")  # Спуститься на один уровень ниже
folder_path = "/content/ui/diamon"
subprocess.run(["mkdir", "-p", f"{folder_path}/extensions/batchlinks-webui"])
repo_url = "https://github.com/etherealxx/batchlinks-webui.git"
subprocess.run(["git", "clone", repo_url, f"{folder_path}/extensions/batchlinks-webui"])


