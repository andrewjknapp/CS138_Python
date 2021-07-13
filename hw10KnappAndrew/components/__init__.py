# button.py
from graphics import *

class Card:

    """A Card is a rectangle with a suit and number"""

    def __init__(self, win, center, suit, number):
        """ Creates a rectangular card, eg:
        card = Card(myWin, centerPoint, 'hearts', 5) """ 
        width = 200
        height = 400
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('white')
        self.rect.draw(win)
        self.suit = suit
        self.number = number

    def clicked(self, p):
        "Returns true if p is inside"
        return (self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getNumber(self):
        "Returns the number of this card."
        return self.number

    def getSuit(self):
        "Returns the suit of this card."
        return self.suit


