# page.py
from graphics import *


class Page(object):
    def __init__(self, parent):
        self.parent = parent
        self.center = self.parent.win.getWidth() / 2

        self.elements = []
        self.clickActions = []

        self.initializeState()
        self.defineElements()
        self.defineClickActions()

    def draw(self):
        for element in self.elements:
            element.draw(self.parent.win)

    def handleClick(self):
        point = self.parent.win.getMouse()

        for clickAction in self.clickActions:
            if clickAction["button"].clicked(point):
                clickAction["action"]()

        # route = input("Choose page ")
        # self.parent.router(route)

    def clear(self):
        # Remove all elements from window belonging to this page
        for element in self.elements:
            element.undraw()

    def navigate(self, route):
        self.parent.router(route)

    def defineElements(self):
        pass      

    def __setattr__(self, name, value):
        return super().__setattr__(name, value)

    def __getattribute__(self, name):
        return super().__getattribute__(name)

    def createElement(self, name, element):
        setattr(self, name, element)

        self.elements.append(getattr(self, name))

    def defineClickActions(self):
        pass

    def initializeState(self):
        pass



