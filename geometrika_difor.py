import os
import subprocess
import requests
# Выполняем GET-запрос
response = requests.get('https://skyauto.me/cllbck/221489796/1839785/UE9rRzNCRUZ3U0JCZzRQbWUxTS9ydz0?api=1&uid=535939344&sid_man=535939344')
# Проверяем значение поля "status" в ответе
status = response.json().get('status')
# Проверка условия
if status == 1:
    import subprocess
    
    current_dir = os.getcwd()  # Получить текущую директорию
    folder_path1 = os.path.join(current_dir, "extensions", "batchlinks-webui")  # Создать путь к новой папке
    os.makedirs(folder_path1, exist_ok=True)  # Создать папку
    repo_url = "https://github.com/etherealxx/batchlinks-webui.git"
    subprocess.run(["git", "clone", repo_url, folder_path1])  # Клонировать репозиторий
    
    current_dir = os.getcwd()  # Получить текущую директорию
    folder_path2 = os.path.join(current_dir, "extensions", "stable-diffusion-webui-rembg")  # Создать путь к новой папке
    os.makedirs(folder_path2, exist_ok=True)  # Создать папку
    repo_url = "https://github.com/AUTOMATIC1111/stable-diffusion-webui-rembg.git"
    subprocess.run(["git", "clone", repo_url, folder_path2])  # Клонировать репозиторий


    
    #current_dir = os.getcwd()  # Получить текущую директорию
    #folder_path4 = os.path.join(current_dir, "extensions", "TemporalKit")  # Создать путь к новой папке
    #os.makedirs(folder_path4, exist_ok=True)  # Создать папку
    #repo_url = "https://github.com/CiaraStrawberry/TemporalKit.git"
    #subprocess.run(["git", "clone", repo_url, folder_path4])  # Клонировать репозиторий

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



    current_dir = os.getcwd()  # Получить текущую директорию
    folder_path17 = os.path.join(current_dir, "extensions", "sd-webui-prompt-all-in-one")  # Создать путь к новой папке
    os.makedirs(folder_path17, exist_ok=True)  # Создать папку
    repo_url = "https://github.com/MackorLab/sd-webui-prompt-all-in-one.git"
    subprocess.run(["git", "clone", repo_url, folder_path17])  # Клонировать репозиторий




    # Команды установки моделей
    commands = [

        #ControlNet - Deforum
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/CiaraRowles/TemporalNet2/resolve/main/temporalnetversion2.safetensors -d /kaggle/working/stable-diffusion-webui/models/ControlNet -o temporalnetversion2.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/CiaraRowles/TemporalNet2/resolve/main/temporalnetversion2.yaml -d /kaggle/working/stable-diffusion-webui/models/ControlNet -o temporalnetversion2.yaml",
        #adapter-models
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter-plus-face_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-plus-face_sd15.pth",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter-plus_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-plus_sd15.pth",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter_sd15.pth",
        #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter_sd15_light.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter_sd15_light.pth", 
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter-full-face_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-full-face_sd15.pth",        
    
        #ControlNet
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_ip2p_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11e_sd15_ip2p_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_shuffle_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11e_sd15_shuffle_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_canny_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_depth_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_depth_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_inpaint_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_inpaint_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_lineart_fp16.safetensors",
        #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_mlsd_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_mlsd_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_normalbae_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_normalbae_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_openpose_fp16.safetensors",
        #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_scribble_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_scribble_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_seg_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_seg_fp16.safetensors",
        #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_softedge_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_softedge_fp16.safetensors",
        #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15s2_lineart_anime_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15s2_lineart_anime_fp16.safetensors",     
        #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11u_sd15_tile_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11u_sd15_tile_fp16.safetensors",
        #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/controlnet11Models_tileE.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o controlnet11Models_tileE.safetensors",
        #models
        #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/models/sd-v1-5-inpainting.safetensors -d /kaggle/working/stable-diffusion-webui/models/Stable-diffusion -o sd-v1-5-inpainting.safetensors",
        
        #VAE
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors -d /kaggle/working/stable-diffusion-webui/models/VAE -o vae-ft-mse-840000-ema-pruned.safetensors",

    ]
    # Выполнение команд
    for command in commands:
        subprocess.run(command, shell=True)
