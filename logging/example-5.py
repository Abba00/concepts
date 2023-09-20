from logging import *   # Here we've imported all the entities in the logging module

basicConfig(filename="extended-appformat.log", 
            level=DEBUG,
            filemode="w",
            format="{asctime}:{lineno}:{process}:{message}:{levelname}:{name}",
            datefmt="%d-%b-%y %H:%M:%S",
            style="{")  # %d for date, %b for month, %y for year, %H:%M:%S for hour, minute and second respectively

# In this example were adding process ID, line numnber and date/time attributes
# Also by adding the style attribute, we could modify the way we had to code the format

debug("This is a debug message") 
info("Logging has started") 
warning("Warning message here") 
error("This is the error message") 
critical("Something critical needs attention") 

