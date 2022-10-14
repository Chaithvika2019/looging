import logging
logging.basicConfig(filename='test5.log',level=logging.DEBUG,format="%(levelname)s %(asctime)s %(name)s %(message)s")

logging.debug("this is DEBUG mode =10")
logging.info("this is INFO mode = 20")
logging.warning("this is WARNING mode = 30")
logging.error("this is ERROR mode = 40")
logging.critical("this is CRITICAL mode = 50")

