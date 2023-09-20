import logging

logging.basicConfig(level=logging.warning) # This determines the least logging level that can be reported
logging.basicConfig(level=30) # It could also be specified with their level number 

logging.debug("This is a debug message") #10
logging.info("Logging has started") #20
logging.warning("Warning message here") #30
logging.error("This is the error message") #40
logging.critical("Something critical needs attention") #50



