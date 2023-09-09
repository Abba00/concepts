import logging

logging.basicConfig(filename='logger/employee.log', 
                    level=logging.INFO,
                    format='%(levelname)s:%(message)s')

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        
        logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
emp_1 = Employee('Abba', 'Ali-Concern')
emp_2 = Employee('Jesse', 'Pinkman')
emp_3 = Employee('Gerard', 'Sullivan')
emp_4 = Employee('Dominik', 'Szoboszlai')