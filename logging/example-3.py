from logging import *   # Here we've imported all the entities in the logging module

basicConfig(filename="app.log", level=DEBUG,filemode="w") 
# By adding filemode = "w", the log messages we have will overwrite the current messages present in the app.log file.
# By default filemode is set to "a" which is append

debug("This is a debug message") 
info("Logging has started") 
warning("Warning message here") 
error("This is the error message") 
critical("Something critical needs attention") 

