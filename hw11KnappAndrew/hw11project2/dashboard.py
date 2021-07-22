# dashboard.py
from graphics import *
from page import Page
from button import Button

class Dashboard(Page):

    def initializeState(self):
        self.userInfo = self.parent.getDBData()[self.parent.loggedInUser]
        print(self.userInfo)
    
    def defineElements(self):
        self.createElement("title", Text(Point(self.center, 30), "Dashboard"))

        self.createElement("userName", Text(Point(self.center, 60), f"Hello {self.userInfo['username']}"))

        self.createElement("checkingAmount", Text(Point(self.center, 90), f"Checking Balance: ${self.userInfo['checkingAccount']}"))

        self.createElement("savingsAmount", Text(Point(self.center, 120), f"Savings Balance: ${self.userInfo['savingsAccount']}"))

        self.createElement("logoutButton", Button(self.parent.win, Point(self.center, 200), 60, 25, "Logout", True))

    def defineClickActions(self):
        self.clickActions.append({"button": self.logoutButton, "action": self.handleLogout})

    def handleLogout(self):
        self.parent.logout()

