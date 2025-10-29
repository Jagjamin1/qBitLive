# Version 0.3
# AUTHOR: Jagjamin

import qbittorrentapi
import time
import os

def clear_screen():
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')

conn_info = dict(
    host="localhost",
    port=8080,
    username="admin",
    password="adminadmin",
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
        eta=eta+torrent.eta




    def format_bytes(size):
        # 2**10 = 1024
        power = 2**10
        n = 0
        power_labels = {0 : '', 1: 'kilo', 2: 'mega', 3: 'giga', 4: 'tera'}
        while size > power:
            size /= power
            n += 1
        return str(size) + " " + power_labels[n]+'bytes'
    if tc==0:
        tc=1

    print("total size ",format_bytes(totalsize))
    print("Remaining = ",(format_bytes(remaining)))
    print("Average DL Speed = ",(speed/tc))
    print("Average ETA = ",(eta/tc))

    time.sleep(1)
    clear_screen()