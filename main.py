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
        while True:
            print_main_menu()
            choice = input("Select an option (1-7): ")

            if choice == '1':
                print("Starting monitoring (no alarms will be triggered)...")
            elif choice == '2':
                print("Listing active monitoring...")
            elif choice == '3':
                print("Creating an alarm...")
            elif choice == '4':
                print("Showing created alarms...")
            elif choice == '5':
                print("Starting monitoring mode (alarms will be triggered)...")
            elif choice == '6':
                print("Removing an alarm...")
            elif choice == '7':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")