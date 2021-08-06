# hourly.py

from employee import Employee

class Hourly(Employee):
    def __init__(self, first, last, id, hourly_rate, num_hours):
        Employee.__init__(self, first, last, id)
        self.hourly_rate = hourly_rate
        self.hours_worked = num_hours

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

    def toString(self):
        return f"hourly, {self.first_name}, {self.last_name}, {self.id}, {self.hourly_rate}, {self.hours_worked}"