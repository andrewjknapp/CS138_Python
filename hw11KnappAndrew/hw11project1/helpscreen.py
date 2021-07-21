# pokerapp.py

from graphics import *

class HelpScreen:

    def __init__(self):
        self.pointValues = [
            "Five of a Kind: 30 Points",
            "Straight: 20 Points",
            "Four of a Kind: 15 Points",
            "Full House: 15 Points",
            "Three of a Kind: 8 Points",
            "Two Pairs: 5 Points",
        ]

    def show(self):
        # Create Window
        self.win = GraphWin("Dice Poker", 300, 300)
        self.win.setBackground("green3")

        # Create Banner
        banner = Text(Point(150,30), "Help Screen")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)

        self.displayValues()

    def displayValues(self):
        yPosition = 100
        for score in self.pointValues:
            Text(Point(150, yPosition), score).draw(self.win)

            yPosition += 25

    def hide(self):
        self.win.close()

    def isOpen(self):
        try:
            return self.win.isOpen()
        except AttributeError:
            return False

    
