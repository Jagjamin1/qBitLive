# Version 0.7.1
# AUTHOR: Jagjamin

import qbittorrentapi
import time
import os
import datetime
import tabulate

def clear_screen():
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')

defaults = str.lower(input("Use default settings? Y/N\n"))

if defaults == "y":
    conn_info = dict(
        host="localhost",
        port=8080,
        username="admin",
        password="adminadmin",

    )

else:
    print("Leave blank for default")
    username = input("Enter username:\n")
    password = input("Enter password:\n")
    host = input("Enter IP Address:\n")
    port = input("Enter port number:\n")

    if not username:
        username = "admin"
    if not password:
        password = "adminadmin"
    if not port:
        port = 8080
    if not host:
        host = "localhost"


    conn_info = dict(
        host=host,
        port=port,
        username=username,
        password=password,
    )
qbt_client = qbittorrentapi.Client(**conn_info)


while True:
    totalsize = 0
    remaining = 0
    tc = 0
    speed = 0
    eta = 0

    for torrent in qbt_client.torrents_info():
        totalsize=totalsize+torrent.size
        remaining=remaining+torrent.amount_left
        tc+1
        speed=speed+torrent.dlspeed
    for torrent in qbt_client.torrents_info():
        if torrent.state == "downloading":
            eta=eta+torrent.eta


    def format_bytes(size):
        # 2**10 = 1024
        power = 2**10
        n = 0
        power_labels = {0 : '', 1: 'kilo', 2: 'mega', 3: 'giga', 4: 'tera'}
        while size > power:
            size /= power
            n += 1
        return f"{round(size, 2)} {power_labels[n]}bytes"
    if tc==0:
        tc=1
    AveSpeed=speed/tc

    clear_screen()
    print(tabulate.tabulate([[format_bytes(totalsize), format_bytes(remaining), format_bytes(AveSpeed), datetime.timedelta(seconds=eta/tc)]], headers=["Total Size", "Remaining", "Average DL Speed", "Average ETA"], tablefmt="orgtbl"))

    time.sleep(1)
