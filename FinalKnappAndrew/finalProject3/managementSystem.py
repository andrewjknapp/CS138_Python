# managementSystem.py
import os


class ManagementSystem():
    def __init__(self):
        self.run()

    def run(self):
        print("Welcome to the Miracosta Employee Directory")

        shouldPromptAgain = True
        while shouldPromptAgain:
            action = self.menu()

            shouldPromptAgain = self.dispatch(action)

    def menu(self):
        numChoices = 7
        print("Menu")
        print("\
             1: View All Employees\n\
             2: Add Employee\n\
             3: Remove Employee\n\
             4: Save Changes\n\
             5: Load other Employee Database\n\
             6: Calcuate Pay for All Employees\n\
             7: Exit"
            )
        choice = int(input("Please choose an action (enter the number) "))

        if not 1 <= choice <= numChoices:
            print("Please choose a valid action")
            self.clear()
            self.menu()

        return choice

    def dispatch(self, action):
        if action == 1:
            self.viewAllEmployees()
        elif action == 2:
            self.addEmployee()
        elif action == 3:
            self.removeEmployee()
        elif action == 4:
            self.saveChanges()
        elif action == 5:
            self.loadEmployees()
        elif action == 6:
            self.calculatePay()
        else:
            self.exit()
            return False

        return True

    def viewAllEmployees(self):
        print("View All Employees")
    
    def addEmployee(self):
        print("Add Employee")
    
    def removeEmployee(self):
        print("Remove Employee")
    
    def saveChanges(self):
        print("Save Changes")
    
    def loadEmployees(self):
        print("Load Employees")
    
    def calculatePay(self):
        print("Calculate Pay")
    
    def exit(self):
        print("Goodbye")

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

