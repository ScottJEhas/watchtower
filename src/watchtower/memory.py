from platform import system
from psutil import virtual_memory

def mem_stats():
    stats = {}

    memory = virtual_memory()

    stats.update({"total": bytes2megabytes(memory.total),
        "free": bytes2megabytes(memory.free),
        "used": bytes2megabytes(memory.total - memory.used)})

    if system() == "Linux":
        stats.update({"buffers": bytes2megabytes(memory.buffers), "cached": bytes2megabytes(memory.cached)})

    return stats

def bytes2megabytes(n):
    return (n / 1024) / 1024
