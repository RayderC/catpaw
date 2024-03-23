import os
from time import sleep
import requests
import manga_downloader.Download_images
from colorama import Fore, Style

red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
reset = Style.RESET_ALL

download_list = []

def download_file(name, url, folder_path, num, file_size, response):
    download_list.append(f'{name} {num}.cbz')

    for attempt in range(5):
        try:
            # print(f"{red}Downloading: {blue}{name} {num} {green}Size: {blue}{round(file_size / 1000)}{green}KB{reset}")

            if file_size >= 64:
                response.raise_for_status()
                with open(folder_path + f'{name} {num}.cbz', 'wb') as f:
                    f.write(response.content)

                print(f"{blue}Download complete: {red}'{name} {num}.cbz'{blue} saved to {green}'{folder_path}' {blue}Size: {red}{round(file_size / 1024)}{blue}KB.{reset}")
                break
            else:
                break

        except requests.exceptions.RequestException as e:
            os.remove(folder_path + f'{name} {num}.cbz')
            # print(f"{green}Attempt {attempt + 1} failed: {reset}{e}")
            if attempt >= 4:
                manga_downloader.Download_images.download_images(name, url, folder_path, num)
                break
            sleep(1)
