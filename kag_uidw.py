import subprocess
commands = [

     #adapter-models
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter-plus-face_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-plus-face_sd15.pth",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter-plus-face_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-plus-face_sd15.pth",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter-plus-face_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-plus-face_sd15.pth",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter-plus-face_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-plus-face_sd15.pth", 
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter-plus-face_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-plus-face_sd15.pth",


     #animateDiff-model
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v15_v2.ckpt -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-animatediff/model -o mm_sd_v15_v2.ckpt",



     #modules - models
    
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/v2_lora_PanLeft.ckpt -d /kaggle/working/stable-diffusion-webui/models/Lora/AnimateDiff -o v2_lora_PanLeft.ckpt",

    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/v2_lora_PanRight.ckpt -d /kaggle/working/stable-diffusion-webui/models/Lora/AnimateDiff -o v2_lora_PanRight.ckpt",

    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/v2_lora_RollingAnticlockwise.ckpt -d /kaggle/working/stable-diffusion-webui/models/Lora/AnimateDiff -o v2_lora_RollingAnticlockwise.ckpt",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/v2_lora_RollingClockwise.ckpt -d /kaggle/working/stable-diffusion-webui/models/Lora/AnimateDiff -o v2_lora_RollingClockwise.ckpt",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/v2_lora_TiltDown.ckpt -d /kaggle/working/stable-diffusion-webui/models/Lora/AnimateDiff -o v2_lora_TiltDown.ckpt",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/v2_lora_TiltUp.ckpt -d /kaggle/working/stable-diffusion-webui/models/Lora/AnimateDiff -o v2_lora_TiltUp.ckpt",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/v2_lora_ZoomIn.ckpt -d /kaggle/working/stable-diffusion-webui/models/Lora/AnimateDiff -o v2_lora_ZoomIn.ckpt",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/v2_lora_ZoomOut.ckpt -d /kaggle/working/stable-diffusion-webui/models/Lora/AnimateDiff -o v2_lora_ZoomOut.ckpt",

     
     #models
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/models/realcartoon3d_v10.safetensors -d /kaggle/working/stable-diffusion-webui/models/Stable-diffusion -o realcartoon3d_v10.safetensors",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/models/realcartoonAnime_v6.safetensors -d /kaggle/working/stable-diffusion-webui/models/Stable-diffusion -o realcartoonAnime_v6.safetensors",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/models/realcartoonPixar_v4.safetensors -d /kaggle/working/stable-diffusion-webui/models/Stable-diffusion -o realcartoonPixar_v4.safetensors",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/models/realcartoonRealistic_v9.safetensors -d /kaggle/working/stable-diffusion-webui/models/Stable-diffusion -o realcartoonRealistic_v9.safetensors", 
     #VAE

   "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/stabilityai/sd-vae-ft-ema-original/resolve/main/vae-ft-ema-560000-ema-pruned.ckpt -d /kaggle/working/stable-diffusion-webui/models/VAE -o vae-ft-ema-560000-ema-pruned.ckpt",
   "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.ckpt -d /kaggle/working/stable-diffusion-webui/models/VAE -o vae-ft-mse-840000-ema-pruned.ckpt",



     
     #Lora
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/loras/MandaraArt_v1.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-additional-networks/models/lora -o MandaraArt_v1.safetensors",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://civitai.com/api/download/models/39885 -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-additional-networks/models/lora -o Better_light.safetensors",


    
]
for command in commands:
    subprocess.run(command, shell=True)
