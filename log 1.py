
# LEVELS
# DEBUG    = 10
# INFO     = 20
# WARNING  = 30
# ERROR    = 40
# CRITICAL = 50
import logging

logging.basicConfig(filename='test2.log',level=logging.INFO)
logging.info("this is the second part of the logging == 20")
logging.warning("this is the third part of the logging === 30 ")
logging.error("this is the fourth part of the logging ==== 40")
logging.critical("this is the final part of the logging ===== 50")


l=[1,2,3,4,5,6,7,8,7,8,9]
for i in l:
    if i == 2:
        logging.info(l)
        logging.warning("this is the warning for the user that we have found 2 in the list")


l=[1,2,3,4,5,6,7,8,7,8,9]
for i in l:
    if i == 2:
        print(l)
        print("this is a warning for the user  that we have found 2 in the list ")