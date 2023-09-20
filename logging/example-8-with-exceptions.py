import logging

logging.basicConfig(filename="exception-log.log", filemode="a", level=10, format="{name} {asctime} {lineno}:{message}", datefmt="%d-%b-%Y %H:%M:%S", 
                    style="{")

# Here, we're adding an exception handling block to log exceptions/error type occurring in the program.
try:
    age = int(input("Enter your age:"))
except Exception as e:
    logging.error(e)

# This block will log the entire error message
try:
    age = int(input("Enter your age:"))
except Exception as e:
    logging.error("Exception details:",exc_info=True)

