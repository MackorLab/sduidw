import subprocess
commands = [
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/DmitrMakeev/DiamonSD-Adapter/resolve/main/ip-adapter-plus-face_sd15.pth -d /kaggle/working/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o ip-adapter-plus-face_sd15.pth
",
   
]
for command in commands:
    subprocess.run(command, shell=True)
