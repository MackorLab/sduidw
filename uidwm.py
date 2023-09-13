import os
import subprocess
current_dir = os.getcwd()  # Получить текущую директорию
folder_path1 = os.path.join(current_dir, "extensions", "batchlinks-webui")  # Создать путь к новой папке
os.makedirs(folder_path1, exist_ok=True)  # Создать папку
repo_url = "https://github.com/etherealxx/batchlinks-webui.git"
subprocess.run(["git", "clone", repo_url, folder_path1])  # Клонировать репозиторий

current_dir = os.getcwd()  # Получить текущую директорию
folder_path2 = os.path.join(current_dir, "extensions", "openpose-editor")  # Создать путь к новой папке
os.makedirs(folder_path2, exist_ok=True)  # Создать папку
repo_url = "https://github.com/fkunn1326/openpose-editor.git"
subprocess.run(["git", "clone", repo_url, folder_path2])  # Клонировать репозиторий


current_dir = os.getcwd()  # Получить текущую директорию
folder_path4 = os.path.join(current_dir, "extensions", "SadTalker")
os.makedirs(folder_path4, exist_ok=True)  # Создать папку

# Клонировать репозиторий
repo_url = "https://github.com/camenduru/SadTalker.git"
subprocess.run(["git", "clone", "-b", "dev", repo_url, folder_path4]) 

# Клонирование дополнительного репозитория
checkpoints_folder = os.path.join(folder_path4, "checkpoints")
os.makedirs(checkpoints_folder, exist_ok=True)
checkpoint_repo_url = "https://huggingface.co/camenduru/SadTalker"
subprocess.run(["git", "clone", checkpoint_repo_url, checkpoints_folder])
