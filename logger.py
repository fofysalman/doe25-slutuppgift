from datetime import datetime

def get_file_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


class Logger:
    def __init__(self):
        self.filename = f"log_{get_file_timestamp()}.log"

    def log(self, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        timestamped_message = f"{timestamp} {message}\n"
        with open(self.filename, 'a', encoding='utf-8') as logfile:
            logfile.write(timestamped_message)
