
#! /usr/bin/python
# File Name:     hw10project2.py
# Programmer:    Andrew Knapp
# Date:          Jul 12, 2021
#
#
# Problem Statement: Create a program to display a playing card. Allow the user to 
# specify the card displayed
#
#
# Overall Plan:
# 1. Create window, entry and button objects
# 2. Define a card class containing links to each suit image
# 3. Listen for clicks on the See Card button
# 4. When clicked set the card's number and suit with what was entered in the Entries
#
#
# import the necessary python libraries
from components.card import Card
from graphics import *
from components.button import Button
import os


def main():

    # os.path.join(os.path.dirname(__file__), 'file.name')
    print(os.path.dirname(__file__))
    # Constants
    WIDTH = 350
    CENTER_X = WIDTH / 2
    HEIGHT = 550

    # Create window object
    win = GraphWin("Height Calculator", WIDTH, HEIGHT)

    # Display Entries and buttons
    Text(Point(CENTER_X, 30), "Choose suit").draw(win)
    suitEntry = Entry(Point(CENTER_X, 60), 10)
    suitEntry.draw(win)

    Text(Point(CENTER_X, 90), "Choose Number").draw(win)
    numEntry = Entry(Point(CENTER_X, 120), 10)
    numEntry.draw(win)

    cardButton = Button(win, Point(CENTER_X, 160), 75, 25, "See Card")
    cardButton.activate()

    # Display card
    card = Card(win, Point(CENTER_X, 350), "hearts", 5)

    # Listen for clicks on the See Card button and update the card
    try:
        while True:
            point = win.getMouse()

            if cardButton.clicked(point):
                card.setCard(suitEntry.getText(), numEntry.getText())
    except:
        win.close()

main()

