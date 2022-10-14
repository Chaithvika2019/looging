import logging
logging.basicConfig(filename='test 3.log',level=logging.DEBUG,format = "%(levelname)s %(asctime)s %(name)s %(message)s")

def div (a,b):
    logging.info("the number entered by the user is % s and % s",a,b)
    try:
        logging.info("we are inside the div function")
        d=a/b
        logging.info("division operation complete")
        logging.info("request is % s",d)
        return d
    except :
        print("exception")

div(8,4)
