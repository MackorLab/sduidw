os.chdir("..")
# Указываем путь к целевой папке 2
folder_path = "/content/ui/extensions"
# Создаем папку с именем репозитория
repo_folder_name = "batchlinks-webui"
subprocess.run(["mkdir", f"{folder_path}/{repo_folder_name}"])
# Клонируем репозиторий в созданную папку
repo_url = "https://github.com/etherealxx/batchlinks-webui.git"
subprocess.run(["git", "clone", repo_url, f"{folder_path}/{repo_folder_name}"])


