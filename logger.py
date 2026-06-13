import logging
from logging.handlers import RotatingFileHandler
import os
from colorama import Fore, Style, init

init(autoreset=True)

#---- Logs folder -----
os.makedirs("logs", exist_ok=True)

#---- Basic-Logger -----
logger = logging.getLogger("Wine_classification_logger")
logger.setLevel(logging.INFO)

#---- Create formatter ----
formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(name)s - %(message)s')

#---- File Handler ----
file_handler = RotatingFileHandler("logs/app.log", encoding="utf-8", maxBytes=1*1024*1024, backupCount=3)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

#---- Console Handler ----
class ColorFormatter(logging.Formatter):

    COLORS = {
        "INFO": Fore.CYAN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "DEBUG": Fore.MAGENTA,
        "SUCCESS": Fore.GREEN  # Custom Level
    }

    def format(self, record):
        color = self.COLORS.get(record.levelname, "")
        message = super().format(record)
        return f"{color}{message}{Style.RESET_ALL}"


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(ColorFormatter("[%(levelname)s] - %(message)s"))

# Add handler to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Custom SUCCESS Level
SUCCESS_LEVEL = 25
logging.addLevelName(SUCCESS_LEVEL, "SUCCESS")

def success(msg):
    logger.log(SUCCESS_LEVEL, msg)

