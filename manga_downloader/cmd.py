import paramiko
import time
from colorama import Fore, Style

green = Fore.GREEN
red = Fore.RED
reset = Style.RESET_ALL

hostname = "192.168.1.117"
port = 24
username = "root"
password = "0817"


def runcmd(command):
    ssh_client = paramiko.SSHClient()

    try:
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname, port, username, password)
        ssh_client.exec_command(command)
        # print(f"{green}Executed: {command}{reset}")



    except paramiko.SSHException as e:
        print(f"{red}Error connecting to SSH server: {e}{reset}")

    finally:
        ssh_client.close()

def sleepcmd(sleeptime):
    time.sleep(sleeptime)