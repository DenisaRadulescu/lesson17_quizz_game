import logging

import coloredlogs

logger = logging.getLogger(__name__)
# logging.basicConfig(filename="quizz_log.log",filemode="w", format='%(asctime)s| %(filename)s| %(levelname)s| %(message)s',level=logging.DEBUG)

logging.basicConfig(filename="quizz_log.log",filemode="w", format='%(asctime)s| %(filename)s| %(levelname)s| %(message)s',level=logging.DEBUG)
coloredlogs.install(level='DEBUG', logger=logger)

if __name__ == '__main__':
    logger.debug("Aici e un debug00")
    logger.info("Aici e un info print")  # will not print anything
    logger.warning("Aici este un warning")
    logger.error("Aici este un error")


