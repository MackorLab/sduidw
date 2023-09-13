import subprocess
commands = [

    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_inpaint.pth -d /content/ui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_inpaint.pth",
    
    
]
for command in commands:
    subprocess.run(command, shell=True)

