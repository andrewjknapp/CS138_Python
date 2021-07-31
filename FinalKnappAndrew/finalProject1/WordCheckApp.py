# atmApp.py
from graphics import *
from dashboard import Dashboard

class Word_Check_App:

    def __init__(self):
        """
        Creates the Spell Check App
        This app starts on the dashboard
        """
        self.win = GraphWin("Spell Check", 600, 400)

        self.page = Dashboard(self)

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
