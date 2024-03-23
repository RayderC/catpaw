from colorama import Fore, Style

import db_manager
import manga_downloader.Does_file_exitsts
import manga_downloader.Download_file
import manga_downloader.cmd

wait_time = 3600 * 6

folder_path = "../Manga/"

magenta = Fore.MAGENTA
cyan = Fore.CYAN
red = Fore.RED
reset = Style.RESET_ALL


def download_manga():
    while True:
        manga_names = ["Horimiya"]
        manga_links = ["https://images.mangafreak.net/downloads/Horimiya_"]
        #db_manager.get("manga_downloader/manga.db", "manga", manga_names, 0)
        #db_manager.get("manga_downloader/manga.db", "manga", manga_links, 1)

        for _ in manga_names:
            new_folder_path = folder_path + manga_names[0] + "/"

            manga_downloader.Does_file_exitsts.create_directory(new_folder_path)
            manga_downloader.Does_file_exitsts.does_file_exitst(new_folder_path, manga_names.pop(0), manga_links.pop(0))

        print(f"{cyan}All new files have been downloaded!{reset}")
        print("")

        manga_downloader.cmd.runcmd("chown -R Rayder:www-data /srv/mergerfs/Vault/Vault/")
        manga_downloader.cmd.runcmd("sudo chown -R www-data:www-data /srv/mergerfs/Vault/Vault/nextcloud/")
        manga_downloader.cmd.runcmd("sudo chmod -R g+s /srv/mergerfs/Vault/Vault/nextcloud/")

        for i in manga_downloader.Download_file.download_list:
            print(magenta + i + reset)
        manga_downloader.Download_file.download_list.clear()

        if wait_time / 60 < 60:
            print(f"{red}Restarting in {round(wait_time / 60)} mins.{reset}")
        else:
            print(f"{red}Restarting in {round(wait_time / 60 / 60)} hours.{reset}")

        manga_downloader.cmd.sleepcmd(wait_time)
