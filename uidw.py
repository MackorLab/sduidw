import subprocess
commands = [
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11e_sd15_ip2p.pth -d /content/ui/extensions/sd-webui-controlnet/models -o control_v11e_sd15_ip2p.pth",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11e_sd15_shuffle.pth -d /content/ui/extensions/sd-webui-controlnet/models -o control_v11e_sd15_shuffle.pth",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1e_sd15_tile.pth -d /content/ui/extensions/sd-webui-controlnet/models -o control_v11f1e_sd15_tile.pth",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1p_sd15_depth.pth -d /content/ui/extensions/sd-webui-controlnet/models -o control_v11f1p_sd15_depth.pth",
    
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny.pth -d /content/ui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_canny.pth",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_inpaint.pth -d /content/ui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_inpaint.pth",
    
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart.pth -d /content/ui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_lineart.pth",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_mlsd.pth -d /content/ui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_mlsd.pth",



    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_normalbae.pth -d /content/ui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_normalbae.pth",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose.pth -d /content/ui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_openpose.pth",
    
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_scribble.pth -d /content/ui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_scribble.pth",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_seg.pth -d /content/ui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_seg.pth",
    
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_softedge.pth -d /content/ui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_softedge.pth",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15s2_lineart_anime.pth -d /content/ui/extensions/sd-webui-controlnet/models -o control_v11p_sd15s2_lineart_anime.pth",
]
for command in commands:
    subprocess.run(command, shell=True)

