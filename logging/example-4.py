from logging import *   # Here we've imported all the entities in the logging module

basicConfig(filename="appformat.log", 
            level=DEBUG,
            filemode="w",
            format="%(message)s:%(levelname)s:%(name)s") 

# Now we want to format how the output log messages will appear. "%()s" is a place holder for the format with the s at the end indicating a string value. 
# The default format is levelname:logger:message but in our case we'll use logger:levelname:message format

debug("This is a debug message") 
info("Logging has started") 
warning("Warning message here") 
error("This is the error message") 
critical("Something critical needs attention") 

