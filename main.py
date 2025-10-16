# Import necessary modules and classes
from utils import print_main_menu

def main():
    """Main function to run the monitoring application and handles the menu and logic."""
    monitoring_active = False # Flag to track if monitoring is active
    while True:
        print_main_menu()
        choice = input("Select an option (1-7): ")
        match choice:
            case '1':
                print("Starting monitoring (no alarms will be triggered)...")
            case '2':
                print("Listing active monitoring...")
            case '3':
                print("Creating an alarm...")
            case '4':
                print("Showing created alarms...")
            case '5':
                print("Starting monitoring mode (alarms will be triggered)...")
            case '6':
                print("Removing an alarm...")
            case '7':
                print("Exiting the application. Goodbye!")
                break
            case _:
                print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()