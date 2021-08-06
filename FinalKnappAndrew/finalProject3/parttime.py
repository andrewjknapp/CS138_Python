# parttime.py

from employee import Employee

class PartTime(Employee):
    def __init__(self, first, last, id, classes_taught, pay_per_class):
        Employee.__init__(self, first, last, id)
        self.classes_taught = classes_taught
        self.pay_per_class = pay_per_class

    def calculate_pay(self):
        return self.pay_per_class * self.classes_taught

    def toString(self):
        return f"parttime, {self.first_name}, {self.last_name}, {self.id}, {self.classes_taught}, {self.pay_per_class}"