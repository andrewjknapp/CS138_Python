# loginpage.py
from graphics import *
from page import Page
from button import Button

class LoginPage(Page):

    def defineElements(self):
        """Defines the elements that will appear on the page and adds them to the elements list"""

        self.createElement("title", Text(Point(self.center, 30), "Login Page"))

        self.createElement("userIdLabel", Text(Point(self.center - 50, 60), "User ID"))

        self.createElement("userIdEntry", Entry(Point(self.center + 50, 60), 10))
        self.userIdEntry.setFill("white")

        self.createElement("pinLabel", Text(Point(self.center - 50, 90), "PIN"))

        self.createElement("pinEntry", Entry(Point(self.center + 50, 90), 10))
        self.pinEntry.setFill("white")

        # Creating pin buttons
        pinKeyPoints = [[self.center, 210], [self.center - 30, 120], [self.center, 120], [self.center + 30, 120], [self.center - 30, 150], [self.center, 150], [self.center + 30, 150], [self.center - 30, 180],[self.center, 180], [self.center + 30, 180]]
        for x in range(10):
            self.createElement(f"pin{x}", Button(self.parent.win, Point(*pinKeyPoints[x]), 20, 20, x, True))

        self.createElement("submitButton", Button(self.parent.win, Point(self.center, 250), 50, 25, "Login", True))


    def defineClickActions(self):
        """Defines what should happen when a button is clicked on the page"""
        # Click actions for pin buttons
        for x in range(10):
            self.clickActions.append({"button": self.__getattribute__(f"pin{x}"), "action": self.anonymous([x], self.clickPin)})

        self.clickActions.append({"button": self.submitButton, "action": self.handleLogin})


    def anonymous(self, args, function):
        """Helper function to ensure a new closure is generated with each lambda function"""
        return lambda: function(*args)


    def clickPin(self, number):
        """
        When a numbered button is clicked that number should be appended onto the 
        pin Entry element if that Entry element does not already have four characters
        """
        pinLabelText = self.pinEntry.getText()
        if self.pinIsFull(pinLabelText):
            return

        pinLabelText += str(number)

        self.pinEntry.setText(pinLabelText)


    def pinIsFull(self, pinText):
        """Returns whether or not the pin has reached its capacity"""
        return len(pinText) >= 4


    def handleLogin(self):
        """Validates that the user has entered an id and a pin, then attempts to log them in"""
        idText = self.userIdEntry.getText().strip()
        pinText = self.pinEntry.getText().strip()

        if len(idText) == 0 or not self.pinIsFull(pinText):
            return

        self.parent.login(idText, pinText)
