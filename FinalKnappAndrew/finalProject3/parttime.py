# parttime.py

from employee import Employee

class PartTime(Employee):
    def __init__(self, first, last, id, classes_taught, pay_per_class):
        Employee.__init__(self, first, last, id)
        self.classes_taught = classes_taught
        self.pay_per_class = pay_per_class

    def add_num_classes(self, num_new_classes):
        self.classes_taught += num_new_classes

    def set_pay_per_class(self, rate):
        self.pay_per_class = rate

    def calculate_pay(self):
        return self.pay_per_class * self.classes_taught