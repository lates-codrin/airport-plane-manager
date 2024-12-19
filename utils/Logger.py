import sys
from datetime import datetime

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("utils/log.txt", "a+", buffering=1)
    
    @staticmethod
    def isBlank(myString):
        return not (myString and myString.strip())
    def write(self, message):
        if not self.isBlank(message):
            self.terminal.write(message + "\n")
            self.log.write(f"[LOG - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]   " + message + "\n")  
    def flush(self):
        self.log.flush()
sys.stdout = Logger()