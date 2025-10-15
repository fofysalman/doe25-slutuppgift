from datetime import datetime
from utils import now_str

class Logger:
    def __init__(self):
        self.filename = f"log_{now_str()}.log"
    