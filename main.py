# Import necessary modules and classes


def print_main_menu():
    """Prints the main menu options for the user."""
    print("\n=== Monitor application ===")
    print("1. Start monitoring (collect status, no alarms are triggered)")
    print("2. List active monitoring")
    print("3. Create alarm")
    print("4. Show created alarms")
    print("5. Start monitoring mode (alarms are triggered)")
    print("6. Remove alarm")
    print("7. Exit")

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