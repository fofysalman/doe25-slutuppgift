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

    def get_alarms_by_type(self, alarm_type: str):
        """List all alarms of a specific type."""
        return [alarm for alarm in self.alarms if alarm.alarm_type == alarm_type]
def submenu_configure_alarm(alarm_manager: AlarmManager, logger, save_callback):
    """Display submenu for configuring an alarm and return the user's choice."""
    while True:
        print("\n=== Configure Alarm ===")
        print("1. CPU usage alarm")
        print("2. Memory usage alarm")
        print("3. Disk usage alarm")
        print("4. Return to main menu")
        choice = input("Select an option (1-4): ").strip()
        if choice == '4':
            print("Returning to main menu...")
            return 
        choice_to_alarm_type = {'1': 'cpu', '2': 'memory', '3': 'disk'}
        if choice not in choice_to_alarm_type:
            print ("Invalid option. Please try again.")
            continue
        try:
            # Import here to avoid circular dependency
            from utils import percent_input
            lvl = percent_input("Enter threshold percentage (1-100): ")
        except ValueError as value_error:
            print(f"Error: {value_error}")
            continue
        alarm = Alarm(choice_to_alarm_type[choice], lvl)
        alarm_manager.add_alarm(alarm)
        print(f"Alarm for: {alarm.alarm_type} configured to {alarm.threshold}%")
        logger.log(f"{alarm.alarm_type}_Usage alarm_Configured_ {alarm.threshold}_Percent")
        # Persist using provided callback
        save_callback(alarm_manager.alarms)
        return
