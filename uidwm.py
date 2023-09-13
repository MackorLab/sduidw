import os
import subprocess
current_dir = os.getcwd()  # Получить текущую директорию
folder_path1 = os.path.join(current_dir, "extensions", "batchlinks-webui")  # Создать путь к новой папке
os.makedirs(folder_path1, exist_ok=True)  # Создать папку
repo_url = "https://github.com/etherealxx/batchlinks-webui.git"
subprocess.run(["git", "clone", repo_url, folder_path1])  # Клонировать репозиторий

current_dir = os.getcwd()  # Получить текущую директорию
folder_path2 = os.path.join(current_dir, "extensions", "sd-webui-depth-lib")  # Создать путь к новой папке
os.makedirs(folder_path2, exist_ok=True)  # Создать папку
repo_url = "https://github.com/jexom/sd-webui-depth-lib.git"
subprocess.run(["git", "clone", repo_url, folder_path2])  # Клонировать репозиторий
