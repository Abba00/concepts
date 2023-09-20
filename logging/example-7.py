import logging
import sys

logger = logging.getLogger(sys.argv[0]) 
# This instantiates the object with the file name the log is being called from

logger2 = logging.getLogger(__name__)
# This instantiates the object with the module being executed



logging.basicConfig(filename="object-appformat.log", 
            level=logging.DEBUG,
            filemode="a",
            format="{name}:{asctime}:{lineno}:{process}:{message}:{levelname}",
            datefmt="%d-%b-%y %H:%M:%S",
            style="{")  # %d for date, %b for month, %y for year, %H:%M:%S for hour, minute and second respectively

logger.info("Some information here")
logger2.info("Some information from the second logger object")
