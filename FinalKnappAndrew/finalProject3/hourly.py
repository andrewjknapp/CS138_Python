# hourly.py

from employee import Employee

class Hourly(Employee):
    def __init__(self, first, last, id, hourly_rate, num_hours):
        Employee.__init__(self, first, last, id)
        self.hourly_rate = hourly_rate
        self.hours_worked = num_hours

    def add_hours(self, num_hours):
        self.hours_worked += num_hours

    def set_hourly_rate(self, rate):
        self.hourly_rate = rate

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked