# managementSystem.py
import os
from hourly import Hourly
from parttime import PartTime
from salary import Salary

class ManagementSystem():
    def __init__(self):
        self.employeeInfo = []
        self.DB_Path = os.path.join(os.path.dirname(__file__), 'employee_db.txt')

        self.readDB(self.DB_Path)

        self.run()

    def run(self):
        print("Welcome to the Miracosta Employee Directory")

        shouldPromptAgain = True
        while shouldPromptAgain:
            action = self.menu()

            shouldPromptAgain = self.dispatch(action)
            

    def menu(self):
        numChoices = 7
        print("\
            ~~~~~~~~~ Menu ~~~~~~~~~\n\
             1: View All Employees\n\
             2: Add Employee\n\
             3: Remove Employee\n\
             4: Save Changes\n\
             5: Load other Employee Database\n\
             6: Calcuate Pay for All Employees\n\
             7: Exit"
            )
        try:
            choice = int(input("Please choose an action (enter the number) "))
        except ValueError:
            print("Please choose a valid action")
            return self.menu()
            

        if not 1 <= choice <= numChoices:
            print("Please choose a valid action")
            self.clear()
            return self.menu()

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
        print("id | Name")
        for employee in self.employeeInfo:
            print(str(employee))

        input("Press Enter to continue")

    def addEmployee(self):
        print("Please enter employee information")
        first = input("Please enter first name: ")
        last = input("Please enter last name: ")
        id = input("Please enter id: ")

        invalidType = True
        while invalidType:
            type = int(input("\
Please choose number of employee type\n\
1. Part Time\n\
2. Hourly\n\
3. Salary\n"))
            invalidType = not 1 <= type <= 3

        if type == 1:
            numClassesTaught = input("Please enter number of classes taught: ")
            payPerClass = input("Please enter compensation per course: ")

            self.employeeInfo.append(PartTime(first, last, id, numClassesTaught, payPerClass))

        elif type == 2:
            hourlyRate = input("Please enter hourly rate: ")
            hoursWorked = input("Please enter number of hours worked: ")
            
            self.employeeInfo.append(Hourly(first, last, id, hourlyRate, hoursWorked))

        elif type == 3:
            monthlySalary = input("Please enter monthly salary: ")
            monthsWorked = input("Please enter the number of months worked: ")

            self.employeeInfo.append(Salary(first, last, id, monthlySalary, monthsWorked))
    
    def removeEmployee(self):
        idToRemove = input("Please enter id of employee to remove: ")
        indexToRemove = -1
        
        for i in range(len(self.employeeInfo)):
            if self.employeeInfo[i].id == idToRemove:
                indexToRemove = i
                break
        
        if indexToRemove == -1:
            print(f"No employee found with id {idToRemove}")
            return
        
        del self.employeeInfo[indexToRemove]

        print(f"Employee with id {idToRemove} deleted")
    
    def saveChanges(self):
        print("Saving changes to DB")
        self.writeToDB()
    
    def loadEmployees(self):
        new_DB_Path = input("Please enter path to employee text file: ")

        try:
            self.readDB(new_DB_Path)
        except FileNotFoundError:
            print("Could not find file. Please try again.")

        print(f"Successfully loaded {len(self.employeeInfo)} entries")

    
    def calculatePay(self):
        # ("{:<8} {:<15} {:<10} {:<10}".format()
        "{:<4} | {:<20} | ${:<10}".format("id", "Name", "Wage")
        for employee in self.employeeInfo:
            print("{:<4} | {:<20} | ${:<10}".format(employee.id, f'{employee.first_name} {employee.last_name}', employee.calculate_pay()))

    
    def exit(self):
        print("Goodbye")

    
    # DB Datastructure
    # Each line corresponds to an employee
    # starts with the type of employee
    # continues comma separated as these examples
    # parttime, John, Doe, id, classes_taught, pay_per_class
    # hourly, John, Doe, id, hourly_rate, num_hours
    # salary, John, Doe, id, monthly_salary, num_months_worked
    def readDB(self, fileName):
        self.employeeInfo = []

        try:
            rawEmployeeData = self.readFile(fileName)
        except FileNotFoundError:
            raise FileNotFoundError

        for employeeData in rawEmployeeData:
            type, *data = employeeData.split(', ')
            
            if type == 'parttime':
                employee = Hourly(*data)
            elif type == 'salary':
                employee = Salary(*data)
            elif type == 'hourly':
                employee = Salary(*data)
            else:
                employee = None

            self.employeeInfo.append(employee)
            self.DB_Path = os.path.join(os.path.dirname(__file__), fileName)

    def writeToDB(self):
        dataToWrite = "\n".join([ employee.toString() for employee in self.employeeInfo ])

        self.writeFile(self.DB_Path, dataToWrite)        


    def writeFile(self, fileName, data):
        f = open(fileName, "w")
        f.write(data)
        f.close()

    # Reads given file and returns a list contianing each line
    def readFile(self, fileName):
        try:
            with open(fileName, "r") as f:
                userFile = f.read()
                return userFile.split('\n')
        except FileNotFoundError:
            raise FileNotFoundError

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

