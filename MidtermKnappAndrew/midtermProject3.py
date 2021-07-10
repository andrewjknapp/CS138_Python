#! /usr/bin/python
# File Name:     midtermProject3.py
# Programmer:    Andrew Knapp
# Date:          July 9, 2021
#
# Problem Statement: Have the user click to create a draw by
# the numbers picture
#
#
# Overall Plan:
# 1. Define constants for screen size
# 2. Define window object
# 3. Listen for clicks
# 4. Draw point on screen with dot number
# 5. repeat steps 3 and 4
#
#
# import the necessary python libraries
from graphics import *

def main():
    # Constants for screen size
    HEIGHT = 600
    WIDTH = 600
    
    print("Waiting for clicks...")

    # Window Object
    win = GraphWin("Draw an image", WIDTH, HEIGHT)

    dotNum = 0

    try:
        while True:
            dotNum = dotNum + 1

            # Check if maximum number of dots have been added
            if dotNum > 100:
                print("Maximum number of clicks reached")
                break

            # Wait for user to select point
            point = win.getMouse()

            # Get clicked location
            x = (point.getX())
            y = (point.getY())

            # Draw point
            dot = Circle(Point(x, y), 3)
            dot.draw(win)

            # Draw point label
            label = Text(Point(x + 10, y - 10), dotNum)
            label.draw(win)

    except:
        # If the window is closed out with the x or with a keyboard interrupt
        print("Window closed")
    else:
        win.getMouse()
    
    print("Thanks for using the dot picture creator")

    

main()