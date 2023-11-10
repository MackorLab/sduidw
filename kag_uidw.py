import subprocess
commands = [
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter-plus-face_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-plus-face_sd15.pth",





    
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v15_v2.ckpt -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-animatediff/model -o mm_sd_v15_v2.ckpt",




    
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/v2_lora_PanLeft.ckpt -d /kaggle/working/stable-diffusion-webui/models/Lora/AnimateDiff -o v2_lora_PanLeft.ckpt",


   "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://civitai.com/api/download/models/218017?type=Model&format=SafeTensor&size=pruned&fp=fp16 -d /kaggle/working/stable-diffusion-webui/models/Stable-diffusion -o realcartoon3d_v10.safetensors",



    
]
for command in commands:
    subprocess.run(command, shell=True)
