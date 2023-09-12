
import subprocess
commands = [
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11e_sd15_ip2p.pth -d /content/ui/extensions/sd-webui-controlnet/models -o control_v11e_sd15_ip2p.pth",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11e_sd15_shuffle.pth -d /content/ui/extensions/sd-webui-controlnet/models -o control_v11e_sd15_shuffle.pth"
    # Добавьте дополнительные команды загрузки стилей, если есть
]
for command in commands:
    subprocess.run(command, shell=True)
