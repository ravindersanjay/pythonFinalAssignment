import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler

# timestr = time.strftime("%Y%m%d-%H%M%S")
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "Log" + '.log'


# log_path = "../reports"

def get_logger(logger_name):
    log_path = "../reports"
    Resultdirectory = log_path
    if not os.path.exists(Resultdirectory):
        os.makedirs(Resultdirectory)

    logger = logging.getLogger(logger_name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)  # better to have too much log than not enough

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(FORMATTER)

        file_handler = TimedRotatingFileHandler(filename=log_path + "/" + LOG_FILE, when='midnight')
        file_handler.setFormatter(FORMATTER)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        # with this pattern, it's rarely necessary to propagate the error up to parent
        logger.propagate = False
        # Set up a specific logger with our desired output level

        return logger
