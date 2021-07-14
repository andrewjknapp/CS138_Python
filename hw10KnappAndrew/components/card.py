# button.py
from graphics import *
import os

class Card:

    """A Card is a rectangle with a suit and number"""

    def __init__(self, win, center, suit, number):
        """ Creates a rectangular card, eg:
        card = Card(myWin, centerPoint, 'hearts', 5) """ 

        # Create and display border of card
        width = 200
        height = width * (3/2)
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('white')
        self.rect.draw(win)

        # Save member variables
        self.suit = suit
        self.number = number
        self.center = center
        self.win = win

        # Set and display number label of card
        self.label = Text(Point(self.xmin + 20, self.ymin + 20), number)
        self.label.setSize(20)
        self.label.setFill("red")
        self.label.draw(win)

        # Map of images
        self.imageFiles = {
            "hearts": os.path.join(os.path.dirname(__file__), 'images', 'heart.png'),
            "spades": os.path.join(os.path.dirname(__file__), 'images', 'spade.png'),
            "diamonds": os.path.join(os.path.dirname(__file__), 'images', 'diamond.png'),
            "clubs": os.path.join(os.path.dirname(__file__), 'images', 'club.png')
        }

        # Display suit
        self.suitImage = Image(center, self.imageFiles[suit])
        self.suitImage.draw(win)


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

    def setSuit(self, suit):
        """Set the suit of the card and updates image on card.
            Returns False if suit does not exist"""

        suit = suit.lower()

        if not suit in self.imageFiles:
            return False
        
        self.suit = suit
        self.suitImage.undraw()
        self.suitImage = Image(self.center, self.imageFiles[suit])
        self.suitImage.draw(self.win)

        if suit == "hearts" or suit == "diamonds":
            self.label.setTextColor("red")
        else:
            self.label.setTextColor("black")

    def setNumber(self, number):
        """Set number of card if character is a valid card character
        Returns false if an invalid character is given.
        """
        acceptableCharacters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        if not number in acceptableCharacters:
            return False
        
        self.label.setText(number)

    def setCard(self, suit, number):
        self.setSuit(suit)
        self.setNumber(number)
        
