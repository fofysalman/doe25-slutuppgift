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
        """Main function to run the monitoring application."""
        while True:
            print_main_menu()
