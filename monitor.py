import psutil

class SystemStatus: # A class to hold system status information
    def __init__(self, cpu_percent, memory_used, memory_total, disk_used, disk_total):
        self.cpu_percent = cpu_percent
        self.memory_used = memory_used
        self.memory_total = memory_total
        self.disk_used = disk_used
        self.disk_total = disk_total