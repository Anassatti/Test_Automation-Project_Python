import logging
import logging.handlers
import os


class LogGen:
    @staticmethod
    def loggen():
        handler = logging.handlers.WatchedFileHandler(
            os.environ.get("LOGFILE", ".//logs/Framework.log", ))
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.setLevel(os.environ.get("LOGLEVEL", "INFO"))
        logger.addHandler(handler)

        # Setting the threshold of logger to DEBUG
        ## logger.setLevel(logging.INFO)
        return logger
