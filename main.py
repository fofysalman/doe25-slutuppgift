from logger import Logger
from monitor import Monitor, format_status, monitoring_mode
from utils import press_any_key_to_continue
from alarms import AlarmManager, submenu_configure_alarm, show_configured_alarms, remove_alarm_by_index
from storage import load_alarms_from_file, save_alarms_to_file

ALARMS_FILE = 'alarms.json'

def print_main_menu():
    print("\n=== Monitor application ===")
    print("1. Start monitoring (collect status, no alarms are triggered)")
    print("2. List active monitoring")
    print("3. Create alarm")
    print("4. Show created alarms")
    print("5. Start monitoring mode (alarms are triggered)")
    print("6. Remove alarm")
    print("7. Exit")

def main():
    logger = Logger()
    alarm_manager = AlarmManager()
    print('Loading previously saved alarms...')
    loaded_alarms = load_alarms_from_file(ALARMS_FILE)
    
    for alarm in loaded_alarms: # To be able to add loaded alarm to manager, otherwise manager would be empty
        alarm_manager.add_alarm(alarm)
    if loaded_alarms:
        print(f'{len(loaded_alarms)} alarms loaded from {ALARMS_FILE}.')
        logger.log('Previously_configured_alarms_loaded')
   
    monitoring_active = False
    monitor = Monitor()
    
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
                remove_alarm_by_index(alarm_manager, logger, lambda alarms: save_alarms_to_file(alarms, ALARMS_FILE))
            case '7':
                print("Exiting the application. Goodbye!")
                break
            case _:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()