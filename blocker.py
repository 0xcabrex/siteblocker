#!/bin/python3

import time
import sys
from datetime import datetime as dt
import os
  
# change hosts path according to your OS
hosts_path = "/etc/hosts"
# localhost's IP
redirect = "127.0.0.1"
  
# websites That you want to block
#website_list = ["www.krunker.io", "krunker.io", "www.discord.com", "discord.com", "discord.gg", "www.discord.gg"]
if os.path.isfile("website_list.txt"):
    with open("website_list.txt", "r", encoding='utf-8') as file_handle:
        website_list = file_handle.read().splitlines()
else:
    print("website_list.txt file does not exist, please add websites to block in the file")
    exit(1)

if sys.platform == "win32":
    print("Windows is not supported")
    exit(1)


try:
    open(hosts_path, 'r+')
except PermissionError:
    print("Do not have enough permissions to execute...\nAre you root?")
    exit(0)


def fixer():
    with open(hosts_path, 'r+') as file:
        content=file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)

        # removing hostnmes from host file
        file.truncate()

def blocker():
    with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    # mapping hostnames to your localhost IP address
                    file.write(redirect + " " + website + "\n")

if len(sys.argv) == 2:
    if sys.argv[1].lower() == "fix":
        print("Fixing /etc/hosts...")
        fixer()
        exit(0)
    elif sys.argv[1].lower() == "block":
        print("Blocked")
        blocker()
        exit(0)

  
while True:
  
    # School hours
    if dt(dt.now().year, dt.now().month, dt.now().day,0) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,15):
        print(f"School hours...")
        blocker()

    # After 9 block
    elif dt(dt.now().year, dt.now().month, dt.now().day,20) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,23):
        print("Not allowed hours...")
        blocker()

    # 5 to 9 leased
    else:
        fixer()
        print("Fun hours...")

    try:
        time.sleep(5)
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected")
        fixer()
        exit()