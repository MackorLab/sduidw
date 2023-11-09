import os
import subprocess

current_dir = os.getcwd()  # Получить текущую директорию
folder_path1 = os.path.join(current_dir, "extensions", "sd-webui-animatediff")  # Создать путь к новой папке
os.makedirs(folder_path1, exist_ok=True)  # Создать папку
repo_url1 = "https://github.com/continue-revolution/sd-webui-animatediff.git"
subprocess.run(["git", "clone", repo_url1, folder_path1])  # Клонировать репозиторий

current_dir = os.getcwd()  # Получить текущую директорию
folder_path2 = os.path.join(current_dir, "extensions", "openpose-editor")  # Создать путь к новой папке
os.makedirs(folder_path2, exist_ok=True)  # Создать папку
repo_url2 = "https://github.com/fkunn1326/openpose-editor.git"
subprocess.run(["git", "clone", repo_url2, folder_path2])  # Клонировать репозиторий





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
folder_path7 = os.path.join(current_dir, "extensions", "posex")  # Создать путь к новой папке
os.makedirs(folder_path7, exist_ok=True)  # Создать папку
repo_url = "https://github.com/hnmr293/posex.git"
subprocess.run(["git", "clone", repo_url, folder_path7])  # Клонировать репозиторий



current_dir = os.getcwd()  # Получить текущую директорию
folder_path8 = os.path.join(current_dir, "extensions", "sd-webui-controlnet")  # Создать путь к новой папке
os.makedirs(folder_path8, exist_ok=True)  # Создать папку
repo_url = "https://dagshub.com/DIAMONIK/controlnet.git"
subprocess.run(["git", "clone", repo_url, folder_path8])  # Клонировать репозиторий


current_dir = os.getcwd()  # Получить текущую директорию
folder_path9 = os.path.join(current_dir, "extensions", "sd-webui-additional-networks")  # Создать путь к новой папке
os.makedirs(folder_path9, exist_ok=True)  # Создать папку
repo_url = "https://dagshub.com/DIAMONIK/networks.git"
subprocess.run(["git", "clone", repo_url, folder_path9])  # Клонировать репозиторий



current_dir = os.getcwd()  # Получить текущую директорию
folder_path10 = os.path.join(current_dir, "extensions", "deforum-for-automatic1111-webui")  # Создать путь к новой папке
os.makedirs(folder_path10, exist_ok=True)  # Создать папку
repo_url = "https://github.com/deforum-art/deforum-for-automatic1111-webui.git"
subprocess.run(["git", "clone", repo_url, folder_path10])  # Клонировать репозиторий



current_dir = os.getcwd()  # Получить текущую директорию
folder_path11 = os.path.join(current_dir, "extensions", "depthmap2mask")  # Создать путь к новой папке
os.makedirs(folder_path11, exist_ok=True)  # Создать папку
repo_url = "https://github.com/Extraltodeus/depthmap2mask.git"
subprocess.run(["git", "clone", repo_url, folder_path11])  # Клонировать репозиторий


#current_dir = os.getcwd()  # Получить текущую директорию
#folder_path12 = os.path.join(current_dir, "extensions", "stable-diffusion-webui-prompt-travel")  # Создать путь к новой папке
#os.makedirs(folder_path12, exist_ok=True)  # Создать папку
#repo_url12 = "https://github.com/s9roll7/animatediff-cli-prompt-travel.git"
#subprocess.run(["git", "clone", repo_url12, folder_path12])  # Клонировать репозиторий


current_dir = os.getcwd()  # Получить текущую директорию
folder_path13 = os.path.join(current_dir, "extensions", "sd-webui-model-converter")  # Создать путь к новой папке
os.makedirs(folder_path13, exist_ok=True)  # Создать папку
repo_url = "https://github.com/Akegarasu/sd-webui-model-converter.git"
subprocess.run(["git", "clone", repo_url, folder_path13])  # Клонировать репозиторий


current_dir = os.getcwd()  # Получить текущую директорию
folder_path14 = os.path.join(current_dir, "extensions", "sd-webui-train-tools")  # Создать путь к новой папке
os.makedirs(folder_path14, exist_ok=True)  # Создать папку
repo_url = "https://github.com/liasece/sd-webui-train-tools.git"
subprocess.run(["git", "clone", repo_url, folder_path14])  # Клонировать репозиторий


current_dir = os.getcwd()  # Получить текущую директорию
folder_path15 = os.path.join(current_dir, "extensions", "stable-diffusion-webui-dataset-tag-editor")  # Создать путь к новой папке
os.makedirs(folder_path15, exist_ok=True)  # Создать папку
repo_url = "https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor.git"
subprocess.run(["git", "clone", repo_url, folder_path15])  # Клонировать репозиторий




