from logging import *   # Here we've imported all the entities in the logging module

basicConfig(filename="app.log", level=DEBUG) # We've specified the output log file name as app.log, so all the log messages will be outputted into this file.

debug("This is a debug message") 
info("Logging has started") 
warning("Warning message here") 
error("This is the error message") 
critical("Something critical needs attention") 

