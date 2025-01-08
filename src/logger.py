import datetime
import logging
import os
from config.config import LOG_LEVEL, MY_LOGGER_NAME, LOGGER_FOLDER

class LoggerAdapter:
    def __init__(self):
        self.create_log_folder()
        current_time = datetime.datetime.now()
        log_file = current_time.strftime(LOGGER_FOLDER + "/log_%Y%m%d%H%M%S.log")
        logging.basicConfig(filename=log_file, level=LOG_LEVEL)
        self.logger = logging.getLogger(MY_LOGGER_NAME)

    def create_log_folder(self):
        if not os.path.exists(LOGGER_FOLDER):
            os.makedirs(LOGGER_FOLDER)

    def log_info(self, message):
        message = self._format_log_message(message)
        self.logger.info(message)

    def log_warning(self, message):
        message = self._format_log_message(message)
        self.logger.warning(message)

    def log_error(self, message):
        message = self._format_log_message(message)
        self.logger.error(message)

    def log_critical(self, message):
        message = self._format_log_message(message)
        self.logger.critical(message)

    def log_debug(self, message):
        message = self._format_log_message(message)
        self.logger.debug(message)

    def _format_log_message(self, message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")  # Hour:Minute:Second.Millisecond
        return f"[{timestamp}] {message}"
    
logger = LoggerAdapter()