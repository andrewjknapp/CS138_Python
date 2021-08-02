# page.py
from graphics import *

class Page(object):

    """
    Page is the parent class to any view in this application.
    When a page is rendered it first initializes its state, 
    then defines its visible elements, and finally defines 
    all click actions. Once these occur the page listens for
    those click acitons and functions accordingly
    """

    def __init__(self, parent):
        """Creates the specified page and invokes the initialize and define methods"""
        self.parent = parent
        self.center = self.parent.win.getWidth() / 2

        self.elements = []
        self.clickActions = []

        self.initializeState()
        self.defineElements()
        self.defineClickActions()


    def draw(self):
        """Draws each of the page's elements onto the screen"""
        for element in self.elements:
            element.draw(self.parent.win)


    def handleClick(self):
        """Waits for mouse click and runs the associated action"""
        try:
            point = self.parent.win.getMouse()
        except GraphicsError as e:
            raise GraphicsError(e)

        for clickAction in self.clickActions:
            if clickAction["button"].clicked(point):
                clickAction["action"]()

        


    def clear(self):
        """Removes each of the page's elements from the screen"""
        for element in self.elements:
            element.undraw()


    def defineElements(self):
        """Can be overridden in child classes to create the visual elements"""
        pass      


    def __setattr__(self, name, value):
        return super().__setattr__(name, value)


    def __getattribute__(self, name):
        return super().__getattribute__(name)

    def createElement(self, name, element):
        """Creates the element and appends to the elements list"""
        setattr(self, name, element)

        self.elements.append(getattr(self, name))

        self.defineStyles(name, element)


    def defineClickActions(self):
        """Can be overridden to define what click actions are present on a given page"""
        pass


    def initializeState(self):
        """Can be overridden to initialize any page specific variables"""
        pass

    def defineStyles(self, name, element):
        """Can be overridden to define styles for any elements on page"""
        pass



