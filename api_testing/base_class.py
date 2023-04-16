import inspect
import logging


def get_logger():
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    fil_handler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fil_handler.setFormatter(formatter)
    logger.addHandler(fil_handler)
    logger.setLevel(logging.DEBUG)
    return logger

