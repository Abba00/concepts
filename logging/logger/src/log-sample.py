import logging #built in python model that returns events in the code

#Logging levels [DEBUG, INFO, WARNING, ERROR, CRITICAL] WARNING is the default log statement with the ones above followed, so these are what the logging module will report unless modified


logging.basicConfig(filename='logger/test.log',    #To create a new file or write to file where logs will be stored
                    level=logging.DEBUG,    #To change the default level
                    format='%(asctime)s:%(levelname)s:%(message)s')     #Format of logging information into the file [{date with time}, {log level e.g warning, debug etc.},{log message/argument}]

#Refer to https://docs.python.org/3/library/logging.html for more logging paramters

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


num_1 = 20
num_2 = 0

try:
    add_result = add(num_1, num_2)
    logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

    sub_result = subtract(num_1, num_2)
    logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

    mul_result = multiply(num_1, num_2)
    logging.debug('mul: {} * {} = {}'.format(num_1, num_2, mul_result))

    div_result = divide(num_1, num_2)
    logging.debug('div: {} / {} = {}'.format(num_1, num_2, div_result))
except Exception as e:
    logging.exception("Exception details:", exc_info=True)

# Instead of printing out output, these results will be appended in the file specified