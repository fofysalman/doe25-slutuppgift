from datetime import datetime

def now_str():
    """Return the current datetime as a filename-safe string."""
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


class Logger:
    """Simple file logger used by the monitoring application."""
    def __init__(self):
        """Create a logfile name that includes a current time string so
        each run gets its own file (helps with debugging and preserves history).
        """
        self.filename = f"log_{now_str()}.log"

    def log(self, message: str):
        """Append a timestamped message to the logfile."""

        # Create a timestamp and write the log line.
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        timestamped_message = f"{timestamp} {message}\n"
        with open(self.filename, 'a', encoding='utf-8') as f:  # Open file in append (a) mode
            f.write(timestamped_message)
