import logging
logging.basicConfig(filename='test 2.log',level=logging.DEBUG)
logging.debug("this level 10 for Debug")


import logging
logging.basicConfig(filename='test 2.log',level=logging.DEBUG,format="%(levelname)s %(asctime)s %(name)s %(message)s")
logging.debug("this level 10 for Debug")

l=[1,2,3,4,5,6,7,8,9]
for i in l:
    if i == 2:
        logging.info(i)
        logging.warning("this is a warning for the user that we have found 2 in the list")



import logging
logging.basicConfig(filename="test 2.log",level=logging.DEBUG,format="%(levelname)s %(asc time)s %(name)s %(message)s")

l=[1,2,3,4,5,6,]
for i in l:
    if i == 2:
        logging.debug(l)

