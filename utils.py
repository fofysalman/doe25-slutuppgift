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

def press_any_key_to_continue():
    """Prompt the user to press any key to continue."""
    from readchar import readkey
    print("\nPress any key to return to the main menu...", end='', flush=True)
    readkey() # Wait for a single key press

def is_key_pressed():
    """Check if any key has been pressed. Works on Windows (msvcrt) and POSIX (select + tty/termios)"""
    #Windows
    try:
        import msvcrt
        if msvcrt.kbhit():
            pressed_key = msvcrt.getch()  # Consume the key press
            return True
        return False
    except Exception:
        pass

    # POSIX
    try:
        import termios, sys, select, tty
        file_descriptor = sys.stdin.fileno()
        saved_terminal_settings = termios.tcgetattr(file_descriptor) # hold current terminal settings so we can restore them later after temporariliy changing terminal mode
        try:
            tty.setcbreak(file_descriptor)  # Set terminal to cbreak mode
            if select.select([sys.stdin], [], [], 0)[0]:
                pressed_key = sys.stdin.read(1)  # Consume the key press
                return True
            return False
        finally:
             termios.tcsetattr(file_descriptor, termios.TCSADRAIN, saved_terminal_settings)
    except Exception:
        return False