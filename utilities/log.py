import inspect
import logging
import os


class LogGen:

    @staticmethod
    def getLogger():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(os.path.abspath(os.getcwd())+"\\logs\\" +'logging.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(level=logging.DEBUG)
        return logger