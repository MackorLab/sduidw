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


# Создание папки и клонирование репозитория для папки "checkpoints"
current_dir = os.getcwd()  # Получить текущую директорию
extensions_path = os.path.join(current_dir, "extensions")  # Путь к папке "extensions"
sadtalker_path = os.path.join(extensions_path, "SadTalker")  # Путь к папке "SadTalker"
os.makedirs(sadtalker_path, exist_ok=True)  # Создать папку "SadTalker"
checkpoints_path = os.path.join(sadtalker_path, "checkpoints")  # Путь к папке "checkpoints"
os.makedirs(checkpoints_path, exist_ok=True)  # Создать папку "checkpoints"
repo_url3 = "https://huggingface.co/datasets/DmatryMakeev/SadTalker"
subprocess.run(["git", "clone", repo_url3, checkpoints_path])  # Клонировать репозиторий


current_dir = os.getcwd()  # Получить текущую директорию
folder_path3 = os.path.join(current_dir, "extensions", "stable-diffusion-webui-rembg")  # Создать путь к новой папке
os.makedirs(folder_path3, exist_ok=True)  # Создать папку
repo_url = "https://github.com/AUTOMATIC1111/stable-diffusion-webui-rembg.git"
subprocess.run(["git", "clone", repo_url, folder_path3])  # Клонировать репозиторий


current_dir = os.getcwd()  # Получить текущую директорию
folder_path4 = os.path.join(current_dir, "extensions", "stable-diffusion-webui-two-shot")  # Создать путь к новой папке
os.makedirs(folder_path4, exist_ok=True)  # Создать папку
repo_url = "https://github.com/ashen-sensored/stable-diffusion-webui-two-shot.git"
subprocess.run(["git", "clone", repo_url, folder_path4])  # Клонировать репозиторий


current_dir = os.getcwd()  # Получить текущую директорию
folder_path5 = os.path.join(current_dir, "extensions", "sd-webui-aspect-ratio-helper")  # Создать путь к новой папке
os.makedirs(folder_path5, exist_ok=True)  # Создать папку
repo_url = "https://github.com/thomasasfk/sd-webui-aspect-ratio-helper.git"
subprocess.run(["git", "clone", repo_url, folder_path5])  # Клонировать репозиторий

current_dir = os.getcwd()  # Получить текущую директорию
folder_path6 = os.path.join(current_dir, "extensions", "asymmetric-tiling-sd-webui")  # Создать путь к новой папке
os.makedirs(folder_path6, exist_ok=True)  # Создать папку
repo_url = "https://github.com/tjm35/asymmetric-tiling-sd-webui.git"
subprocess.run(["git", "clone", repo_url, folder_path6])  # Клонировать репозиторий

current_dir = os.getcwd()  # Получить текущую директорию
folder_path7 = os.path.join(current_dir, "extensions", "posex")  # Создать путь к новой папке
os.makedirs(folder_path7, exist_ok=True)  # Создать папку
repo_url = "https://github.com/hnmr293/posex.git"
subprocess.run(["git", "clone", repo_url, folder_path7])  # Клонировать репозиторий


current_dir = os.getcwd()  # Получить текущую директорию
folder_path7 = os.path.join(current_dir, "extensions", "sd-webui-text2video")  # Создать путь к новой папке
os.makedirs(folder_path7, exist_ok=True)  # Создать папку
repo_url = "https://github.com/kabachuha/sd-webui-text2video.git"
subprocess.run(["git", "clone", repo_url, folder_path7])  # Клонировать репозиторий




