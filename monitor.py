import psutil

class SystemStatus:
    """ A class to hold the system status information including CPU, memory, and disk usage."""
    def __init__(self, cpu_percent, memory_used, memory_total, disk_used, disk_total):
        self.cpu_percent = cpu_percent
        self.memory_used = memory_used
        self.memory_total = memory_total
        self.disk_used = disk_used
        self.disk_total = disk_total

class Monitor:
    """A class to monitor and collect system status via psutil library."""
    def get_status(self):
        """Fetches the current system status including CPU, memory, and disk usage."""
        cpu_percent = psutil.cpu_percent(interval=0.5)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        return SystemStatus(
            cpu_percent=cpu_percent,
            memory_used=memory.used,
            memory_total=memory.total,
            disk_used=disk.used,
            disk_total=disk.total
        )
def bytes_to_Gbytes(num_bytes):
    """Converts bytes to a human-readable format."""
    return num_bytes / (1024 ** 3)