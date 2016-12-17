from time import sleep
from psutil import net_io_counters
from platform import system
from re import match

def network_stats():
    stats = {}

    net_start = net_io_counters(pernic=True)
    sleep(.99)
    net_end = net_io_counters(pernic=True)

    for key in net_start.keys():
        if system() == "Linux":
            if match(r'([lL]o*)', key):
                continue
        elif system(_) == "Windows":
            if rmatch(r'([lL]oop*)|(.+Pseudo.+)|(6TO4)|(isatap)', key):
                continue

        rx = str(net_end[key].bytes_recv - net_start[key].bytes_recv)
        rxerr = str(net_end[key].errout - net_start[key].errout)
        rxpps = str(net_end[key].packets_recv - net_start[key].packets_recv)
        tx = str(net_end[key].bytes_sent - net_start[key].bytes_sent)
        txerr = str(net_end[key].errin - net_start[key].errin)
        txpps = str(net_end[key].packets_sent - net_start[key].packets_sent)

        stats.update({key: {"rx": rx, "tx": tx, "rxpps": rxpps, "txpps": txpps, "rxerr": rxerr, "txerr": txerr}})

    return stats
