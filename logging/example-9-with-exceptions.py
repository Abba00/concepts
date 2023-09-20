import logging

logging.basicConfig(filename="exception-log.log", filemode="a", level=10, format="{name} {asctime} {lineno}:{message}", datefmt="%d-%b-%Y %H:%M:%S", 
                    style="{")

class AcessDenied(Exception):
    pass

try:
    age = int(input("Enter your age:"))
    if age<18:
        raise AcessDenied("Access denied!")
    logging.info("A user with age {} has logged in".format(age))
except Exception as e:
    logging.exception("Exception occured:")