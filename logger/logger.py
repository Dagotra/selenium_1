import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from logger.logger_config import LoggerConfig


class Logger:
    if not os.path.isdir(LoggerConfig.LOGS_DIR_NAME):
        os.makedirs(LoggerConfig.LOGS_DIR_NAME)
    __logger = logging.getLogger(LoggerConfig.LOGGER_NAME)
    __logger.setLevel(LoggerConfig.LOGS_LEVEL)
    __handler_1 = RotatingFileHandler(LoggerConfig.LOGS_FILE_NAME,
                                      maxBytes=LoggerConfig.MAX_BYTES,
                                      backupCount= LoggerConfig.BACKUP_COUNT,
                                      encoding='UTF-8'
                                      )
    __handler_2 = logging.StreamHandler(sys.stdout)
    __formatter = logging.Formatter(LoggerConfig.FORMAT)
    __handler_1.setFormatter(__formatter)
    __handler_2.setFormatter(__formatter)
    __logger.addHandler(__handler_1)
    __logger.addHandler(__handler_2)

    @staticmethod
    def set_level(level) -> None:
        Logger.__logger.setLevel(level)

    @staticmethod
    def info(message) -> None:
        Logger.__logger.info(msg=message)

    @staticmethod
    def error(message) -> None:
        Logger.__logger.error(msg=message)

    @staticmethod
    def debug(message) -> None:
        Logger.__logger.debug(msg=message)