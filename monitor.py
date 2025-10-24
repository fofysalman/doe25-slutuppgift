import psutil

class SystemStatus:
    """ A class to be able to hold the system status information including CPU, memory, and disk usage."""
    def __init__(self, cpu_percent, memory_used, memory_total, disk_used, disk_total):
        self.cpu_percent = cpu_percent
        self.memory_used = memory_used
        self.memory_total = memory_total
        self.disk_used = disk_used
        self.disk_total = disk_total

class Monitor:
    """A class to monitor and collect system status via psutil library."""
    def get_status(self):
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
    return num_bytes / (1024 ** 3)

def format_status(status):
    """To be able to format and print the system status in a readable way"""
    print(f"CPU usage: {status.cpu_percent:.0f}%")
    print(f"Memory usage: {bytes_to_Gbytes(status.memory_used):.1f} GB out of {bytes_to_Gbytes(status.memory_total):.1f} GB used")
    print(f"Disk usage: {bytes_to_Gbytes(status.disk_used):.1f} GB out of {bytes_to_Gbytes(status.disk_total):.1f} GB used")

def monitoring_mode(alarm_manager, logger):
    logger.log('Monitoring_mode_started')
    print("\nMonitoring mode is active. Press any key to exit and return to the main menu.")
    monitor = Monitor() 

    while True:
        status = monitor.get_status()
        print(f"[Monitoring active] CPU: {status.cpu_percent:.0f}%| Mem {bytes_to_Gbytes(status.memory_used):.1f}GB | Disk {bytes_to_Gbytes(status.disk_used):.1f}GB")

        for alarm_type in ['cpu', 'memory', 'disk']:
            highest_threshold = alarm_manager.get_highest_threshold(alarm_type)
            if highest_threshold is None:
                continue
            current_value = 0
            if alarm_type == 'cpu':
                current_value = status.cpu_percent
            elif alarm_type == 'memory':
                current_value = (status.memory_used / status.memory_total) * 100
            elif alarm_type == 'disk':
                current_value = (status.disk_used / status.disk_total) * 100
            if current_value >= highest_threshold:
                print(f"***WARNING, ALARM ACTIVATED, {alarm_type.upper()} USAGE EXCEEDS THE THRESHOLD OF {highest_threshold}%***")
                logger.log(f"{alarm_type}_UsageAlarm_activated_{highest_threshold}_Percent")
        print('Press any key to exit and return to the main menu...')
        from utils import is_key_pressed
        import time
        for tick in range(30):
            if is_key_pressed():
                logger.log('Monitoring_mode_stopped_by_user')
                print("\nExiting monitoring mode and returning to main menu.")
                return
            time.sleep(0.1)