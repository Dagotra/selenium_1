import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from typing import Union
from logger.filters import SecurityMaskingFilter
from logger.logger_config import LoggerConfig


class Logger:
    if not os.path.isdir(LoggerConfig.LOGS_DIR_NAME):
        os.makedirs(LoggerConfig.LOGS_DIR_NAME)
    __logger = logging.getLogger(LoggerConfig.LOGGER_NAME)
    __logger.setLevel(LoggerConfig.LOGS_LEVEL)

    __logger.addFilter(SecurityMaskingFilter())
    __handler1 = RotatingFileHandler(
        LoggerConfig.LOGS_FILE_NAME,
        maxBytes=LoggerConfig.MAX_BYTES,
        backupCount=LoggerConfig.BACKUP_COUNT,
        encoding="utf-8"
    )
    __handler2 = logging.StreamHandler(sys.stdout)
    __formater = logging.Formatter(LoggerConfig.FORMAT)
    __handler1.setFormatter(__formater)
    __handler2.setFormatter(__formater)
    __logger.addHandler(__handler1)
    __logger.addHandler(__handler2)

    @staticmethod
    def set_level(level: Union[str, int]) -> None:
        Logger.__logger.setLevel(level)

    @staticmethod
    def info(message: str) -> None:
        Logger.__logger.info(msg=message)
