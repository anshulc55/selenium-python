import logging

class logClass:

    def info(self, msg):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.info(msg)

    def error(self, msg):
        logger = logging.getLogger()
        logger.setLevel(logging.ERROR)
        logger.error(msg)


    def debug(self, msg):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.debug(msg)

    def fatal(self, msg):
        logger = logging.getLogger()
        logger.setLevel(logging.FATAL)
        logger.fatal(msg)

    def critical(self, msg):
        logger = logging.getLogger()
        logger.setLevel(logging.CRITICAL)
        logger.critical(msg)