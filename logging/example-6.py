import logging
import sys  

logging.basicConfig(filename="object-appformat.log", 
            level=logging.DEBUG,
            filemode="w",
            format="{name}:{asctime}:{lineno}:{message}",
            datefmt="%d-%b-%y %H:%M:%S",
            style="{")  # %d for date, %b for month, %y for year, %H:%M:%S for hour, minute and second respectively

# Here we are creating a logging object called logger. Wr can also specify the name inside the args parenthesis
logger = logging.getLogger("self-made")
logger.setLevel(10)
logger.info("Here is the information")
logger.error("Error goes here")