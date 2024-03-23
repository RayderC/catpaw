import os
import manga_downloader.Download_file
import requests
from colorama import Fore, Style

red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
reset = Style.RESET_ALL


def does_file_exitst(folder_path, name, link):
    num = 1

    while True:
        file_to_download = folder_path + name + " " + str(num) + ".cbz"

        if os.path.exists(file_to_download):
            if os.path.getsize(file_to_download) <= 64:
                os.remove(file_to_download)
                print(f"{red}Redownloading: {blue}{name} {str(num)}.cbz{reset}")

        if not os.path.exists(file_to_download):
            url = link + str(num)
            response = requests.get(url, stream=True)
            file_size = int(response.headers.get("Content-length", 0))

            if file_size >= 64:
                manga_downloader.Download_file.download_file(name, url, folder_path, num, file_size, response)
                num = num + 1
            else:
                break
        else:
            num = num + 1


def create_directory(path):
    # Check if the directory already exists
    if not os.path.exists(path):
        try:
            # Create the directory
            os.makedirs(path)
            print(f"{red}Directory created: '{green}{path}'{red}")
        except OSError as e:
            print(f"{red}Error creating directory '{path}': {e}{reset}")