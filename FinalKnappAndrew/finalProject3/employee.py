# employee.py

class Employee():
    def __init__(self, first, last, id):
        self.first_name = first
        self.last_name = last
        self.id = id

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}"

    def calculate_pay(self):
        pass
