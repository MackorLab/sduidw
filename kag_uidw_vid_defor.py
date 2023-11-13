import subprocess
commands = [

    #ControlNet - Deforum
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/TemporalNet%20/diff_control_sd15_temporalnet_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/models/ControlNet -o diff_control_sd15_temporalnet_fp16.safetensors",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/TemporalNet%20/diffusion_pytorch_model.fp16.yaml -d /kaggle/working/stable-diffusion-webui/models/ControlNet -o diffusion_pytorch_model.fp16.yaml",
    #adapter-models
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter-plus-face_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-plus-face_sd15.pth",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter-plus_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-plus_sd15.pth",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter_sd15.pth",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter_sd15_light.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter_sd15_light.pth", 
    
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
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11u_sd15_tile_fp16.safetensors -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11u_sd15_tile_fp16.safetensors",

    #models
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/Models-coll/resolve/main/models/realcartoon3d_v10.safetensors -d /kaggle/working/stable-diffusion-webui/models/Stable-diffusion -o realcartoon3d_v10.safetensors",
     #VAE
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors -d /kaggle/working/stable-diffusion-webui/models/VAE -o vae-ft-mse-840000-ema-pruned.safetensors",
   



     
    


    
]
for command in commands:
    subprocess.run(command, shell=True)
