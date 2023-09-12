import subprocess
command = "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/t2iadapter_style_sd14v1.pth -d /content/ui/extensions/sd-webui-controlnet/models -o t2iadapter_style_sd14v1.pth"
subprocess.run(command, shell=True)
