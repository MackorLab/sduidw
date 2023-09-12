import os
import subprocess
current_dir = os.getcwd()  # Получить текущую директорию
folder_path = os.path.join(current_dir, "extensions", "batchlinks-webui")  # Создать путь к новой папке
os.makedirs(folder_path, exist_ok=True)  # Создать папку
repo_url = "https://github.com/etherealxx/batchlinks-webui.git"
subprocess.run(["git", "clone", repo_url, folder_path])  # Клонировать репозиторий


