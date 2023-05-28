from sys import stdout
from loguru import logger
from utils.constants import *

class MyLogger:
    def __init__(self, log_name = LOG_FILE) -> None:
        self.logger = logger
        self.logger.remove()
        self.logger.add(stdout, level = 'INFO',
            format = consoleLogFormat
        )
        log_level = 'INFO'
        if DEBUG:
            log_level = 'DEBUG'
        self.logger.add(log_name, level = log_level,
            format = fileLogFormat, rotation = '50 MB'
        )

logger = MyLogger().logger
