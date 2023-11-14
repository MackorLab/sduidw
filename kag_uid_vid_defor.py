import os
import subprocess


import requests

# Выполняем GET-запрос
response = requests.get('https://skyauto.me/cllbck/221489796/1839785/UE9rRzNCRUZ3U0JCZzRQbWUxTS9ydz0?api=1&uid=535939344&sid_man=535939344')

# Проверяем значение поля "status" в ответе
status = response.json().get('status')

# Проверка условия
if status == 0:
    raise Exception("Условие не выполнилось, блокнот останавливается")



current_dir = os.getcwd()  # Получить текущую директорию
folder_path1 = os.path.join(current_dir, "extensions", "batchlinks-webui")  # Создать путь к новой папке
os.makedirs(folder_path1, exist_ok=True)  # Создать папку
repo_url = "https://github.com/etherealxx/batchlinks-webui.git"
subprocess.run(["git", "clone", repo_url, folder_path1])  # Клонировать репозиторий



current_dir = os.getcwd()  # Получить текущую директорию
folder_path3 = os.path.join(current_dir, "extensions", "stable-diffusion-webui-rembg")  # Создать путь к новой папке
os.makedirs(folder_path3, exist_ok=True)  # Создать папку
repo_url = "https://github.com/AUTOMATIC1111/stable-diffusion-webui-rembg.git"
subprocess.run(["git", "clone", repo_url, folder_path3])  # Клонировать репозиторий


current_dir = os.getcwd()  # Получить текущую директорию
folder_path4 = os.path.join(current_dir, "extensions", "multidiffusion-upscaler-for-automatic1111")  # Создать путь к новой папке
os.makedirs(folder_path4, exist_ok=True)  # Создать папку
repo_url = "https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111.git"
subprocess.run(["git", "clone", repo_url, folder_path4])  # Клонировать репозиторий


current_dir = os.getcwd()  # Получить текущую директорию
folder_path5 = os.path.join(current_dir, "extensions", "sd-webui-aspect-ratio-helper")  # Создать путь к новой папке
os.makedirs(folder_path5, exist_ok=True)  # Создать папку
repo_url = "https://github.com/thomasasfk/sd-webui-aspect-ratio-helper.git"
subprocess.run(["git", "clone", repo_url, folder_path5])  # Клонировать репозиторий







current_dir = os.getcwd()  # Получить текущую директорию
folder_path8 = os.path.join(current_dir, "extensions", "sd-webui-controlnet")  # Создать путь к новой папке
os.makedirs(folder_path8, exist_ok=True)  # Создать папку
repo_url = "https://github.com/Mikubill/sd-webui-controlnet.git"
subprocess.run(["git", "clone", repo_url, folder_path8])  # Клонировать репозиторий





current_dir = os.getcwd()  # Получить текущую директорию
folder_path10 = os.path.join(current_dir, "extensions", "deforum-for-automatic1111-webui")  # Создать путь к новой папке
os.makedirs(folder_path10, exist_ok=True)  # Создать папку
repo_url = "https://github.com/deforum-art/deforum-for-automatic1111-webui.git"
subprocess.run(["git", "clone", repo_url, folder_path10])  # Клонировать репозиторий





#current_dir = os.getcwd()  # Получить текущую директорию
#folder_path12 = os.path.join(current_dir, "extensions", "stable-diffusion-webui-prompt-travel")  # Создать путь к новой папке
#os.makedirs(folder_path12, exist_ok=True)  # Создать папку
#repo_url12 = "https://github.com/Kahsolt/stable-diffusion-webui-prompt-travel.git"
#subprocess.run(["git", "clone", repo_url12, folder_path12])  # Клонировать репозиторий



current_dir = os.getcwd()  # Получить текущую директорию
folder_path15 = os.path.join(current_dir, "extensions", "stable-diffusion-webui-dataset-tag-editor")  # Создать путь к новой папке
os.makedirs(folder_path15, exist_ok=True)  # Создать папку
repo_url = "https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor.git"
subprocess.run(["git", "clone", repo_url, folder_path15])  # Клонировать репозиторий


current_dir = os.getcwd()  # Получить текущую директорию
folder_path17 = os.path.join(current_dir, "extensions", "sd-webui-prompt-all-in-one")  # Создать путь к новой папке
os.makedirs(folder_path17, exist_ok=True)  # Создать папку
repo_url = "https://github.com/Physton/sd-webui-prompt-all-in-one.git"
subprocess.run(["git", "clone", repo_url, folder_path17])  # Клонировать репозиторий





