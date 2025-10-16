class Alarm:
    """A class to represent an alarm with type and threshold."""
    def __init__(self, alarm_type: str, threshold: int):
        self.alarm_type = alarm_type
        self.threshold = threshold

    def __str__(self):
        """String representation of the alarm."""
        alarm_type_names = {'cpu': 'CPU alarm', 'memory': 'Memory alarm', 'disk': 'Disk alarm'}
        return f"{alarm_type_names.get(self.alarm_type, self.alarm_type)} {self.threshold}%"
    
class AlarmManager:
    """A class to manage multiple alarms."""
    def __init__(self):
        # Use a list to store alarms
        self.alarms = []
    
    def add_alarm(self, alarm: Alarm):
        """Add a new alarm to the list."""
        self.alarms.append(alarm)
    
    def remove_alarm(self, index: int):
        """Remove an alarm by its index in the list."""
        if index < 0 or index >= len(self.alarms):
            raise IndexError("Invalid alarm index.")
        self.alarms.pop(index)
    
    def get_sorted_alarms(self):
        """Return a list of alarms sorted by type and threshold."""
        return sorted(self.alarms, key=lambda alarm: (alarm.alarm_type, alarm.threshold))
    
    def get_highest_threshold(self, alarm_type: str):
        """Get the highest threshold for a given alarm type."""
        thresholds = [alarm.threshold for alarm in self.alarms if alarm.alarm_type == alarm_type]
        return max(thresholds) if thresholds else None