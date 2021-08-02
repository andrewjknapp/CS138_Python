# salary.py

from employee import Employee

class Salary(Employee):
    def __init__(self, first, last, id, monthly_salary, num_months_worked):
        Employee.__init__(self, first, last, id)
        self.monthly_salary = monthly_salary
        self.num_months_worked = num_months_worked

    def add_num_classes(self, num_new_classes):
        self.classes_taught += num_new_classes

    def set_pay_per_class(self, salary):
        self.monthly_salary = salary

    def calculate_pay(self):
        return self.monthly_salary * self.classes_taught