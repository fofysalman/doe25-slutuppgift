from utils import press_any_key_to_continue , percent_input
class Alarm:
    """A class to represent an alarm with type and threshold."""
    def __init__(self, alarm_type: str, threshold: int):
        self.alarm_type = alarm_type
        self.threshold = threshold

    def __str__(self):
        alarm_type_names = {'cpu': 'CPU alarm', 'memory': 'Memory alarm', 'disk': 'Disk alarm'}
        return f"{alarm_type_names.get(self.alarm_type, self.alarm_type)} {self.threshold}%"
    
class AlarmManager:
    """A class to manage multiple alarms."""
    def __init__(self):
        # To enable sorting and manage alarms we keep alarms in a list
        self.alarms = []
    
    def add_alarm(self, alarm: Alarm):
        self.alarms.append(alarm)
    
    def remove_alarm(self, index: int):
        if index < 0 or index >= len(self.alarms):
            raise IndexError("Invalid alarm index.")
        self.alarms.pop(index)
    
    def get_sorted_alarms(self):
        return sorted(self.alarms, key=lambda alarm: (alarm.alarm_type, alarm.threshold))
    
    def get_highest_threshold(self, alarm_type: str):
        thresholds = [alarm.threshold for alarm in self.alarms if alarm.alarm_type == alarm_type]
        return max(thresholds) if thresholds else None

    def get_alarms_by_type(self, alarm_type: str):
        return [alarm for alarm in self.alarms if alarm.alarm_type == alarm_type]

def submenu_configure_alarm(alarm_manager: AlarmManager, logger, save_callback):
    """To enable the user to create a new alarm, a submenu is used."""
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
            threshold = percent_input("Enter threshold percentage (1-100): ")
        except ValueError as value_error:
            print(f"Error: {value_error}")
            continue
        alarm = Alarm(choice_to_alarm_type[choice], threshold)
        alarm_manager.add_alarm(alarm)
        print(f"Alarm for: {alarm.alarm_type} configured to {alarm.threshold}%")
        logger.log(f"{alarm.alarm_type}_Usage_Alarm_Configured_{alarm.threshold}_Percent")
        # To be able to save all alarms after a change, a callback is used, so alarms are not lost when the program closes
        save_callback(alarm_manager.alarms)
        return
    
def show_configured_alarms(alarm_manager: AlarmManager):
    """Displays alarms so the user can verify configurations."""
    sorted_alarms = alarm_manager.get_sorted_alarms()
    if not sorted_alarms:
        print("No alarms configured.")
    else:
        for alarm in sorted_alarms:
            print(str(alarm))
    press_any_key_to_continue()

def remove_alarm_by_index(alarm_manager: AlarmManager, logger, save_callback):
    """Remove an alarm by its index and log the action."""
    if not alarm_manager.alarms:
        print("No alarms to remove.")
        return
    print("Select a configured alarm to remove:")
    for index, alarm in enumerate(alarm_manager.alarms):
        print(f"{index + 1}. {alarm}")
    value = input(f"Choose number (or blank to cancel): ").strip()
    if value == '':
        print("Alarm removal cancelled.")
        return
    if not value.isdigit():
        print("Invalid input. Please enter a valid number.")
        return
    index = int(value) - 1
    try:
        removed_alarm = alarm_manager.alarms[index]
        alarm_manager.remove_alarm(index)
        print(f"Removed alarm: {removed_alarm}")
        logger.log(f"{removed_alarm.alarm_type}_Usage_Alarm_Removed_{removed_alarm.threshold}_Percent")
        save_callback(alarm_manager.alarms)
    except Exception as exception:
        print(f"Error: {exception}")