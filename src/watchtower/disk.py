from platform import system
from psutil import disk_partitions, disk_usage, disk_io_counters
from time import sleep

def disk_stats():
    stats = {}

    disks_start = disk_io_counters(perdisk=True)
    sleep(.99)
    disks_end = disk_io_counters(perdisk=True)

    for disk in disk_partitions(all=False):
        usage = disk_usage(disk.mountpoint)

        if system() == "Linux":
            device = disk.device.split("/")[-1]
            mountpoint = disk.mountpoint
        elif system() == "Freebsd":
            print "Not Implemented"
        elif system() == "Windows":
            if disk.fstype != "NTFS":
                continue
            device = drive.device.strip(":\\")
            mountpoint = drive.mountpoint.strip(":\\")
        else:
            print "Not Implemented"

        stats.update({device: { "mountpoint": mountpoint,
            "fstype": disk.fstype,
            "free": bytes2megabytes(usage.free),
            "used": bytes2megabytes(usage.used),
            "size": bytes2megabytes(usage.total),
            "percent": usage.percent }})

    return stats

def mapPhysicalDisk(disk, valid_mount_points):
    c = wmi.WMI()
    mountpoint = ''
    mountpoints = []
    for physical_disk in c.Win32_DiskDrive():
        if disk.upper() in physical_disk.DeviceID:
            for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
                for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                    mountpoints.append(logical_disk.Caption)
    for value in mountpoints:
        if value in valid_mount_points:
            mountpoint = value
    return mountpoint.strip(":")

def bytes2megabytes(n):
    return ((n / 1024) / 1024)

'''

def disk_stats(disk, disk_start, disk_end):
    read_bytes = str(disk_end.read_bytes - disk_start.read_bytes)
    write_bytes = str(disk_end.write_bytes - disk_start.write_bytes)
    read_count = str(disk_end.read_count - disk_start.read_count)
    write_count = str(disk_end.write_count - disk_start.write_count)
    return disk + "=" + read_bytes + "B/s," + write_bytes + "B/s," + read_count + "IO/s," + write_count + "IO/s," + read_time + "ms," + write_time + "ms;"



    if platform.system() == "Windows":
        disks = psutil.disk_partitions(all=False)
        for disk in disks:
            if disk.fstype != "NTFS":
                disks.remove(disk)
        mountpoints = []
        for disk in disks:
            mountpoints.append(disk.mountpoint.strip("\\"))
        invalid_disks = []
        for disk in disks_start:
            if MapPhysicalDisk(disk, mountpoints) != '':
                disks_start[MapPhysicalDisk(disk, mountpoints)] = disks_start.pop(disk)
                disks_end[MapPhysicalDisk(disk, mountpoints)] = disks_end.pop(disk)
            else:
                invalid_disks.append(disk)
        for device in invalid_disks:
            disks_start.pop(device)
            disks_end.pop(device)

'''
