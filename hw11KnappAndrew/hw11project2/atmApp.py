# atmApp.py
from graphics import *
from loginpage import LoginPage
from dashboard import Dashboard
import os
import json

class ATM_App:

    def __init__(self):
        self.win = GraphWin("ATM", 600, 400)
        self.db_path =  os.path.join(os.path.dirname(__file__),"totallySecureDatabase.txt")

        self.loggedInUser = None
        self.page = LoginPage(self)

        self.run()

    def run(self):        
        self.page.draw()

        while True:
            self.page.handleClick()


    def router(self, route):
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
        if not self.validateUserLogin(userId, pin):
            return
        
        self.loggedInUser = userId
        self.router("/dashboard")

    def validateUserLogin(self, userId, pin):
        data = self.getDBData()

        if userId in data:
            if pin == data[userId]["pin"]:
                return True
        
        return False

    def logout(self):
        self.loggedInUser = None
        self.router("/")

    def getDBData(self):
        try:
            with open(self.db_path, "r") as f:
                db = f.read() 
        except FileNotFoundError as e:
            print("Trouble connecting to database: " + e)
            return {}

        return json.loads(db)
