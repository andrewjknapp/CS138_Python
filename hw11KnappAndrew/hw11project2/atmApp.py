# atmApp.py
from graphics import *
from loginpage import LoginPage
from dashboard import Dashboard
import os
import json

class ATM_App:

    def __init__(self):
        """
        Creates the ATM App
        This app starts on the Login Page
        """
        self.win = GraphWin("ATM", 600, 400)
        self.db_path =  os.path.join(os.path.dirname(__file__),"totallySecureDatabase.txt")

        self.loggedInUser = None
        self.page = LoginPage(self)

        self.run()


    def run(self):       
        """
        Draws all the elements from the current page then listens
        for any clicks that occur on the page.
        """ 
        self.page.draw()

        try:
            while True:
                self.page.handleClick()
        except GraphicsError:
            return


    def router(self, route):
        """
        Handles changing the page based on page requested
        """
        if route == "/":
            newPage = LoginPage(self)
        elif route == "/dashboard":
            newPage = Dashboard(self)
        else:
            return

        self.page.clear()
        self.page = newPage
        self.run()


    def login(self, userId, pin):
        """
        Checks to ensure that the userId and pin are valid then logs
        the user in and navigates to the dashboard
        """
        if not self.validateUserLogin(userId, pin):
            return
        
        self.loggedInUser = userId
        self.router("/dashboard")


    def validateUserLogin(self, userId, pin):
        """
        Gets all user data and checks to see if 
        the userId and pin match the database
        """
        data = self.getDBData()

        if userId in data:
            if pin == data[userId]["pin"]:
                return True
        
        return False


    def logout(self):
        """
        Logs out the user and navigates to the login page
        """
        self.loggedInUser = None
        self.router("/")


    def getDBData(self):
        """
        Reads in user data from text file and returns that as a dictionary
        """
        try:
            with open(self.db_path, "r") as f:
                db = f.read() 
        except FileNotFoundError as e:
            print("Trouble connecting to database: " + e)
            return {}

        return json.loads(db)
