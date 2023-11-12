import subprocess
commands = [

    #ControlNet
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/TemporalNet%20/diff_control_sd15_temporalnet_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/models/ControlNet -o diff_control_sd15_temporalnet_fp16.safetensors",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/TemporalNet%20/diffusion_pytorch_model.fp16.yaml -d /kaggle/working/stable-diffusion-webui/models/ControlNet -o diffusion_pytorch_model.fp16.yaml",
    #animateDiff-model
    #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v15_v2.ckpt -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-animatediff/model -o mm_sd_v15_v2.ckpt",



     #modules - models
    
    #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/v2_lora_PanLeft.ckpt -d /kaggle/working/stable-diffusion-webui/models/Lora/AnimateDiff -o v2_lora_PanLeft.ckpt",

    #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/v2_lora_PanRight.ckpt -d /kaggle/working/stable-diffusion-webui/models/Lora/AnimateDiff -o v2_lora_PanRight.ckpt",

    #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/v2_lora_RollingAnticlockwise.ckpt -d /kaggle/working/stable-diffusion-webui/models/Lora/AnimateDiff -o v2_lora_RollingAnticlockwise.ckpt",
    #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/v2_lora_RollingClockwise.ckpt -d /kaggle/working/stable-diffusion-webui/models/Lora/AnimateDiff -o v2_lora_RollingClockwise.ckpt",
    #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/v2_lora_TiltDown.ckpt -d /kaggle/working/stable-diffusion-webui/models/Lora/AnimateDiff -o v2_lora_TiltDown.ckpt",
    #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/v2_lora_TiltUp.ckpt -d /kaggle/working/stable-diffusion-webui/models/Lora/AnimateDiff -o v2_lora_TiltUp.ckpt",
    #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/v2_lora_ZoomIn.ckpt -d /kaggle/working/stable-diffusion-webui/models/Lora/AnimateDiff -o v2_lora_ZoomIn.ckpt",
    #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/v2_lora_ZoomOut.ckpt -d /kaggle/working/stable-diffusion-webui/models/Lora/AnimateDiff -o v2_lora_ZoomOut.ckpt",

     
     #models
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/models/realcartoon3d_v10.safetensors -d /kaggle/working/stable-diffusion-webui/models/Stable-diffusion -o realcartoon3d_v10.safetensors",
    #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/models/realcartoonAnime_v6.safetensors -d /kaggle/working/stable-diffusion-webui/models/Stable-diffusion -o realcartoonAnime_v6.safetensors",
    #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/models/realcartoonPixar_v4.safetensors -d /kaggle/working/stable-diffusion-webui/models/Stable-diffusion -o realcartoonPixar_v4.safetensors",
    #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/models/realcartoonRealistic_v9.safetensors -d /kaggle/working/stable-diffusion-webui/models/Stable-diffusion -o realcartoonRealistic_v9.safetensors", 
     #VAE

   #"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors -d /kaggle/working/stable-diffusion-webui/models/VAE -o vae-ft-mse-840000-ema-pruned.safetensors",
   # "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/hakurei/waifu-diffusion-v1-4/resolve/main/vae/kl-f8-anime2.ckpt -d /kaggle/working/stable-diffusion-webui/models/VAE -o kl-f8-anime2.ckpt",



     
    


    
]
for command in commands:
    subprocess.run(command, shell=True)
