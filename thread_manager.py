import manga_downloader.main_manga_downloader

import threading

# Threads (run multiple things at once)
thread_manga_downloader = threading.Thread(target=manga_downloader.main_manga_downloader.download_manga)


def start():
    # Starting up the threads
    thread_manga_downloader.start()
    print("Starting Threads")


def stop():
    # Joining/Stopping Threads
    thread_manga_downloader.join()
    print("Threads Ended")
