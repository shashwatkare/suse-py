import logging
import os


def console_logger():
    # getting dynamic env variables
    log_format = os.environ.get("LOG_FORMAT", "%(asctime)s :: %(levelname)-8s :: %(name)-8s :: %(funcName)-8s (%(lineno)-d) :: %(message)s")
    log_level = os.environ.get("LOGGING_LEVEL", "DEBUG")
    if not log_level.isupper():
        log_level = log_level.upper()

    # create logging formatter
    log_formatter = logging.Formatter(fmt=str(log_format))

    # create console handler
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(level=str(log_level))
    consoleHandler.setFormatter(log_formatter)

    # Add console handler to logger
    logging.basicConfig(level=log_level)
