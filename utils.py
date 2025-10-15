def percent_input(user_prompt: str)
    """Prompt the user for a percentage value between 0 and 100."""
    entered_percent = input(user_prompt).strip()
    if not entered_percent.isdigit():
        raise ValueError("Input must be a number between 1-100.")
    percent_value = int(entered_percent)
    if percent_value < 1 or percent_value > 100:
        raise ValueError("Input must be between 1-100.")
    return percent_value
