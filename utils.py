def percent_input(user_prompt: str):
    """Prompt the user for a percentage value between 0 and 100."""
    entered_percent = input(user_prompt).strip()
    if not entered_percent.isdigit():
        raise ValueError("Input must be a number between 1-100.")
    percent = int(entered_percent)
    if percent < 1 or percent > 100:
        raise ValueError("Input must be between 1-100.")
    return percent

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