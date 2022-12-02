import logging
from logging.handlers import RotatingFileHandler
from logging import LogRecord
from app.core.config import settings


class Format(logging.Formatter):
    asctime = "%(asctime)s"
    name = "[%(name)s]"
    levelname = "[%(levelname)-4s]"
    message = "%(message)s"
    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    green = "\x1b[32m"
    formats = {}

    def format(self, record):
        log_fmt = self.formats.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class ConsoleFormat(Format):
    def __init__(self):
        self.formats = {
            logging.DEBUG: f"{self.asctime} {self.grey} {self.name} {self.levelname} {self.reset} {self.message}",
            logging.INFO: f"{self.asctime} {self.green} {self.name} {self.levelname} {self.reset} {self.message}",
            logging.WARNING: f"{self.asctime} {self.yellow} {self.name} {self.levelname} {self.message} {self.reset}",
            logging.ERROR: f"{self.asctime} {self.red} {self.name} {self.levelname} {self.message} {self.reset}",
            logging.CRITICAL: f"{self.asctime} {self.bold_red} {self.name} {self.levelname} {self.message} {self.reset}",
        }


class FileFormat(Format):
    def __init__(self):
        self.formats = {
            logging.DEBUG: f"{self.asctime} {self.name} {self.levelname}  {self.message}",
            logging.INFO: f"{self.asctime}  {self.name} {self.levelname}  {self.message}",
            logging.WARNING: f"{self.asctime} {self.name} {self.levelname} {self.message} ",
            logging.ERROR: f"{self.asctime} {self.name} {self.levelname} {self.message} ",
            logging.CRITICAL: f"{self.asctime}  {self.name} {self.levelname} {self.message} ",
        }


def filter_error_messages(record: LogRecord):
    if record.levelno > 30:
        return False
    return True


def get_logger(name: str) -> logging.Logger:
    logging_level = logging.DEBUG if settings.DEBUGGER else logging.INFO

    logger = logging.getLogger(name)
    logger.setLevel(logging_level)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(ConsoleFormat())
    stream_handler.setLevel(logging_level)
    logger.addHandler(stream_handler)

    info_handler = RotatingFileHandler(
        f"app/logs/{name}.log",
        mode=settings.LOGGING_MODE,
        maxBytes=settings.LOGGING_MAX_BYTES,
        backupCount=settings.LOGGING_BACKUP_COUNT,
    )
    info_handler.setFormatter(FileFormat())
    info_handler.setLevel(logging_level)
    info_handler.addFilter(filter_error_messages)

    logger.addHandler(info_handler)

    error_handler = RotatingFileHandler(
        f"app/logs/{name}.error.log",
        mode=settings.LOGGING_MODE,
        maxBytes=settings.LOGGING_MAX_BYTES,
        backupCount=settings.LOGGING_BACKUP_COUNT,
    )
    error_handler.setFormatter(FileFormat())
    error_handler.setLevel(logging.ERROR)
    logger.addHandler(error_handler)
    return logger
