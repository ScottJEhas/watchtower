from platform import system
from psutil import cpu_percent, cpu_times_percent

def cpu_stats():
    stats = {}

    cpus = cpu_percent(interval=1, percpu=True)
    cpus_extended = cpu_times_percent(interval=1)

    for idx, cpu in enumerate(cpus):
        stats.update({"cpu-%s" % idx: cpu})

    if system() == "Windows":
        stats.update({"system": str("%.2f" % cpus_extended.system) , "user": str("%.2f" % cpus_extended.user),
            "idle": str("%.2f" % cpus_extended.idle)})
    else:
        stats.update({"system": str("%.2f" % cpus_extended.system), "user": str("%.2f" % cpus_extended.user),
            "idle": str("%.2f" % cpus_extended.idle), "nice": str("%.2f" % cpus_extended.nice), "iowait": str("%.2f" % cpus_extended.iowait),
            "softirq": str("%.2f" % cpus_extended.softirq), "steal": str("%.2f" % cpus_extended.steal)})

    return stats
