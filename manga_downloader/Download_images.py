import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import shutil
from colorama import Fore, Style

red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
reset = Style.RESET_ALL


def download_images(name, url, folder_path, num):
    temp_folder = folder_path + "tempfolder/"
    extracted_part = url.split("/downloads/")[-1]
    url = f"https://w15.mangafreak.net/Read1_{extracted_part}"

    # print(f"{green}Downloading: {blue}{name} {num}, {red}this is going to take a second{reset}")

    # Make a request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all img tags
        img_tags = soup.find_all('img')

        # Create the save folder if it doesn't exist
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)

        # Download each image
        for img_tag in img_tags:
            img_url = urljoin(url, img_tag['src'])
            img_name = os.path.join(temp_folder, os.path.basename(img_url))

            # Download the image
            img_data = requests.get(img_url).content
            if img_name.lower().endswith('.jpg'):
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_data)

        # deletes file if saved
        if os.path.exists(f"{folder_path}{name} {num}.cbz"):
            os.remove(f"{folder_path}{name} {num}.cbz")

        # makes zip
        shutil.make_archive(f"{folder_path}{name} {num}", 'zip', f"{temp_folder}")
        shutil.rmtree(temp_folder)

        # renames the file
        os.rename(f"{folder_path}{name} {num}.zip", f"{folder_path}{name} {num}.cbz")

        # print(f"{red}Zipped: {blue}{name} {num}.cbz{reset}")

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")