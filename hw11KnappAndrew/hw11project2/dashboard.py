# dashboard.py
from graphics import *
from page import Page
from button import Button

class Dashboard(Page):

    def initializeState(self):
        """Initializes any page specific variables"""

        self.userInfo = self.parent.getDBData()[self.parent.loggedInUser]


    def defineElements(self):
        """Defines the elements that will appear on the page and adds them to the elements list"""

        self.createElement("title", Text(Point(self.center, 30), "Dashboard"))

        self.createElement("userName", Text(Point(self.center, 60), f"Hello {self.userInfo['username']}"))

        self.createElement("checkingAmount", Text(Point(self.center, 90), f"Checking Balance: ${self.userInfo['checkingAccount']}"))

        self.createElement("savingsAmount", Text(Point(self.center, 120), f"Savings Balance: ${self.userInfo['savingsAccount']}"))

        self.createElement("logoutButton", Button(self.parent.win, Point(self.center, 200), 60, 25, "Logout", True))


    def defineClickActions(self):
        """Defines what should happen when a button is clicked on the page"""

        self.clickActions.append({"button": self.logoutButton, "action": self.handleLogout})


    def handleLogout(self):
        """Logs out the user"""
        self.parent.logout()

