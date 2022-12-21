from sys import stdout
from loguru import logger
from utils.constants import *

class MyLogger:
    def __init__(self, log_name = LOG_FILE) -> None:
        self.logger = logger
        self.logger.remove()
        self.logger.add(stdout, level = 'INFO',
            format = '<cyan>{module}.exe</cyan>: '
                     '<level>{message}</level>'
        )
        log_level = 'INFO'
        if DEBUG:
            log_level = 'DEBUG'
        self.logger.add(log_name, level = log_level,
            format = "{time:YYYY.MM.DD HH:mm:ss} - "  # 时间
                     "{thread.name} | "  # 进程名
                     "{module}.{function}:{line} - {level}:\n{message}",
            rotation = '50 MB'
        )


logger = MyLogger().logger