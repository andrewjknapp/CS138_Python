# salary.py

from employee import Employee

class Salary(Employee):
    def __init__(self, first, last, id, monthly_salary, num_months_worked):
        Employee.__init__(self, first, last, id)
        self.monthly_salary = monthly_salary
        self.num_months_worked = num_months_worked

    def calculate_pay(self):
        return eval(self.monthly_salary) * eval(self.num_months_worked)

    def toString(self):
        return f"salary, {self.first_name}, {self.last_name}, {self.id}, {self.monthly_salary}, {self.num_months_worked}"