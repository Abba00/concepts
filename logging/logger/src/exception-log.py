import logging

logging.basicConfig(filename="exception_logs", filemode="a", level=10, format="%(process)s:%(levelname)s")

class AccessDenied(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise(AccessDenied("Access Denied"))
    logging.info("A user with age {} has logged in".format(age))
except Exception as e:
    logging.exception("Exception occured")