# Import necessary modules and classes
from logger import Logger
from monitor import Monitor, format_status, monitoring_mode
from utils import print_main_menu, press_any_key_to_continue
from alarms import AlarmManager, submenu_configure_alarm, show_configured_alarms
from storage import load_alarms_from_file, save_alarms_to_file

ALARMS_FILE = 'alarms.json'  # Json file to save alarms

def main():
    """Main function to run the monitoring application and handles the menu and logic."""
    logger = Logger() # Create a logger instance/object
    alarm_manager = AlarmManager() # Create an instance/object of AlarmManager
    print('Loading previously saved alarms...')
    loaded_alarms = load_alarms_from_file(ALARMS_FILE) # Load alarms from file
    
    for alarm in loaded_alarms: # Add each loaded alarm to the manager
        alarm_manager.add_alarm(alarm)
    if loaded_alarms:
        print(f'{len(loaded_alarms)} alarms loaded from {ALARMS_FILE}.')
        logger.log('Previously_configured_alarms_loaded')
   
    monitoring_active = False # Flag to track if monitoring is active
    monitor = Monitor() # Create an instance/object of Monitor
    
    while True:
        print_main_menu()
        choice = input("Select an option (1-7): ")
        match choice:
            case '1':
                print("Starting monitoring (no alarms will be triggered)...")
                status = monitor.get_status()
                monitoring_active = True
                format_status(status)
                press_any_key_to_continue()
            case '2':
                print("Listing active monitoring...")
                if monitoring_active:
                    print('Monitoring is ACTIVE (no alarms will be triggered).')
                    status = monitor.get_status()
                    format_status(status)
                else:
                    print('Monitoring is INACTIVE.')
                press_any_key_to_continue()
            case '3':
                print("Creating an alarm...")
                submenu_configure_alarm(alarm_manager, logger, lambda alarms: save_alarms_to_file(alarms, ALARMS_FILE))
            case '4':
                print("Showing created alarms...")
                show_configured_alarms(alarm_manager)
            case '5':
                print("Starting monitoring mode (alarms will be triggered)...")
                monitoring_mode(alarm_manager, logger)
            case '6':
                print("Removing an alarm...")
            case '7':
                print("Exiting the application. Goodbye!")
                break
            case _:
                print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()