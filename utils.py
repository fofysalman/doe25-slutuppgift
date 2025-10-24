def percent_input(user_prompt: str):
    """Check user input so it is a number between 1 and 100."""
    entered_percent = input(user_prompt).strip()
    if not entered_percent.isdigit():
        raise ValueError("Input must be a number between 1-100.")
    percent = int(entered_percent)
    if percent < 1 or percent > 100:
        raise ValueError("Input must be between 1-100.")
    return percent

def press_any_key_to_continue():
    """Pause the program so the user can read messages before going back to the menu."""
    from readchar import readkey
    print("\nPress any key to return to the main menu...", end='', flush=True)
    readkey()

def is_key_pressed():
    """Check if any key has been pressed. Works on Windows (msvcrt) and POSIX (select + tty/termios)"""
    #Windows
    try:
        import msvcrt
        if msvcrt.kbhit(): #Check for key press on Windows without stopping the program
            pressed_key = msvcrt.getch()
            return True
        return False
    except Exception:
        pass

    # POSIX
    try:
        import termios, sys, select, tty
        file_descriptor = sys.stdin.fileno()
        saved_terminal_settings = termios.tcgetattr(file_descriptor) # to enable holding current terminal settings so we can restore them later after temporarily changing terminal mode
        try:
            tty.setcbreak(file_descriptor)  # Let Linux/Mac detect key press immediately
            if select.select([sys.stdin], [], [], 0)[0]: # Check if a key is waiting to be read
                pressed_key = sys.stdin.read(1)
                return True
            return False
        finally:
             termios.tcsetattr(file_descriptor, termios.TCSADRAIN, saved_terminal_settings) # Restore terminal so it behaves normally afterwards
    except Exception:
        return False