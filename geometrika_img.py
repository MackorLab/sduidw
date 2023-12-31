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

    current_dir = os.getcwd()  # Получить текущую директорию
    folder_path3 = os.path.join(current_dir, "extensions", "stable-diffusion-webui-prompt-travel")  # Создать путь к новой папке
    os.makedirs(folder_path3, exist_ok=True)  # Создать папку
    repo_url = "https://github.com/Kahsolt/stable-diffusion-webui-prompt-travel.git"
    subprocess.run(["git", "clone", repo_url, folder_path3])  # Клонировать репозиторий
    
    #current_dir = os.getcwd()  # Получить текущую директорию
    #folder_path4 = os.path.join(current_dir, "extensions", "multidiffusion-upscaler-for-automatic1111")  # Создать путь к новой папке
    #os.makedirs(folder_path4, exist_ok=True)  # Создать папку
    #repo_url = "https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111.git"
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
    folder_path15 = os.path.join(current_dir, "extensions", "stable-diffusion-webui-dataset-tag-editor")  # Создать путь к новой папке
    os.makedirs(folder_path15, exist_ok=True)  # Создать папку
    repo_url = "https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor.git"
    subprocess.run(["git", "clone", repo_url, folder_path15])  # Клонировать репозиторий

    current_dir = os.getcwd()  # Получить текущую директорию
    folder_path17 = os.path.join(current_dir, "extensions", "sd-webui-prompt-all-in-one")  # Создать путь к новой папке
    os.makedirs(folder_path17, exist_ok=True)  # Создать папку
    repo_url = "https://github.com/MackorLab/sd-webui-prompt-all-in-one.git"
    subprocess.run(["git", "clone", repo_url, folder_path17])  # Клонировать репозиторий

    current_dir = os.getcwd()  # Получить текущую директорию
    folder_path13 = os.path.join(current_dir, "extensions", "adetailer")  # Создать путь к новой папке
    os.makedirs(folder_path13, exist_ok=True)  # Создать папку
    repo_url = "https://github.com/Bing-su/adetailer.git"
    subprocess.run(["git", "clone", repo_url, folder_path13])  # Клонировать репозиторий


    current_dir = os.getcwd()  # Получить текущую директорию
    folder_path14 = os.path.join(current_dir, "extensions", "sd-webui-reactor")  # Создать путь к новой папке
    os.makedirs(folder_path14, exist_ok=True)  # Создать папку
    repo_url = "https://github.com/Gourieff/sd-webui-reactor.git"
    subprocess.run(["git", "clone", repo_url, folder_path14])  # Клонировать репозиторий


    #current_dir = os.getcwd()  # Получить текущую директорию
    #folder_path18 = os.path.join(current_dir, "extensions", "sd-webui-model-converter")  # Создать путь к новой папке
    #os.makedirs(folder_path18, exist_ok=True)  # Создать папку
    #repo_url = "https://github.com/Akegarasu/sd-webui-model-converter.git"
    #subprocess.run(["git", "clone", repo_url, folder_path18])  # Клонировать репозиторий


    #current_dir = os.getcwd()  # Получить текущую директорию
    #folder_path19 = os.path.join(current_dir, "extensions", "sd-webui-train-tools")  # Создать путь к новой папке
    #os.makedirs(folder_path19, exist_ok=True)  # Создать папку
    #repo_url = "https://github.com/liasece/sd-webui-train-tools.git"
    #subprocess.run(["git", "clone", repo_url, folder_path19])  # Клонировать репозиторий

    
    # Команды установки моделей
    commands = [

        #ControlNet - Deforum
        #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/TemporalNet%20/diff_control_sd15_temporalnet_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/models/ControlNet -o diff_control_sd15_temporalnet_fp16.safetensors",
        #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/TemporalNet%20/diffusion_pytorch_model.fp16.yaml -d /kaggle/working/stable-diffusion-webui/models/ControlNet -o diffusion_pytorch_model.fp16.yaml",
        #adapter-models
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter-plus-face_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-plus-face_sd15.pth",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter-plus_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-plus_sd15.pth",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter_sd15.pth",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter_sd15_light.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter_sd15_light.pth", 
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter-full-face_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-full-face_sd15.pth",        
    
        #ControlNet
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_ip2p_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11e_sd15_ip2p_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_shuffle_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11e_sd15_shuffle_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_canny_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_depth_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_depth_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_inpaint_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_inpaint_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_lineart_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_mlsd_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_mlsd_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_normalbae_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_normalbae_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_openpose_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_scribble_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_scribble_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_seg_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_seg_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_softedge_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_softedge_fp16.safetensors",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15s2_lineart_anime_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15s2_lineart_anime_fp16.safetensors",     
        #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11u_sd15_tile_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11u_sd15_tile_fp16.safetensors",
        #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/controlnet11Models_tileE.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o controlnet11Models_tileE.safetensors",
        #models
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/models/sd-v1-5-inpainting.safetensors -d /kaggle/working/stable-diffusion-webui/models/Stable-diffusion -o sd-v1-5-inpainting.safetensors",
        
        #VAE
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors -d /kaggle/working/stable-diffusion-webui/models/VAE -o vae-ft-mse-840000-ema-pruned.safetensors",

        #Script
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/script/0hx51x.py -d /kaggle/working/stable-diffusion-webui/scripts -o 0hx51x.py",



        
    ]
    # Выполнение команд
    for command in commands:
        subprocess.run(command, shell=True)
