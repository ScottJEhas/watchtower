import Queue
import threading
from time import sleep
from watchtower import disk_stats, cpu_stats, mem_stats, network_stats
import watchtower
import socket

def main():
    while True:

        data = []

        q = Queue.Queue()

        for stats in ['cpu_stats', 'disk_stats', 'mem_stats', "network_stats"]:
            t = threading.Thread(target=q.put(getattr(watchtower, stats)()))
            t.daemon = True
            t.start()
            data.append(q.get())

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 5559))

        s.send(str(data))
        s.close()

        sleep(60)
