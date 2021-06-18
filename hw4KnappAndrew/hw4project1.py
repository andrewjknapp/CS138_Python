#! /usr/bin/python
# File Name:     hw4project1.py
# Programmer:    Andrew Knapp
# Date:          June 15, 2021
#
# Problem Statement: Display three graphical objects
#
#
# Overall Plan:
# 1. Define constants for screen size
# 2. Define window object
# 3. Draw circle
# 4. Draw rectangle
# 5. Draw text
# 6. Close window
#
#
# import the necessary python libraries
from graphics import *

def main():
    # Constants for screen size
    HEIGHT = 300
    WIDTH = 400

    # Starting image
    print("Drawing image...")

    # Window Object
    win = GraphWin("My Image", WIDTH, HEIGHT)

    # Circle Object
    c = Circle(Point(WIDTH / 2, HEIGHT / 2), 100)
    c.draw(win)

    # Rectangle Object
    r = Rectangle(Point(100, 100), Point(300, 200))
    r.draw(win)

    # Text object
    t = Text(Point(WIDTH / 2, HEIGHT / 2), "This is my Image")
    t.draw(win)

    win.getMouse() # pause for click in window
    win.close()

main()