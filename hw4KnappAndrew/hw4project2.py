#! /usr/bin/python
# File Name:     hw4project1.py
# Programmer:    Andrew Knapp
# Date:          June 16, 2021
#
# Problem Statement: User will click window in two places
# draw line between the points, draw the midpoint, display the slope and length
#
#
# Overall Plan:
# 1. Define constants for screen size
# 2. Define window object
# 3. Listen for two clicks
# 4. Get points from clicks
# 5. Draw line
# 6. Calculate and draw midpoint
# 7. Calculate length
# 8. Calculate slope
# 9. Display slope and length
#
#
# import the necessary python libraries
from graphics import *

def main():
    # Constants for screen size
    HEIGHT = 300
    WIDTH = 400
    TEXT_POINT = Point(WIDTH / 2, HEIGHT - 20)

    # Starting image
    print("Waiting for clicks...")


    # Window Object
    win = GraphWin("Draw an image", WIDTH, HEIGHT)

    t = Text(TEXT_POINT, "Please click two points")
    t.draw(win)

    # Wait for user clicks
    point1 = win.getMouse()
    point2 = win.getMouse()

    # Draw line
    l = Line(point1, point2)
    l.draw(win)

    # Calculate and draw midpoint
    midX = (point1.getX() + point2.getX()) / 2
    midY = (point1.getY() + point2.getY()) / 2
    midpoint = Circle(Point(midX, midY), 3)
    midpoint.setFill("cyan")
    midpoint.draw(win)

    dX = point2.getX() - point1.getX()
    dY = point2.getY() - point1.getY()

    # Calculate Length
    length = (dX**2 + dY**2)**(1/2)

    # Calculate Slope
    slope = - dY / dX

    print("Line Properties")
    print(f"Length: {length:.1f}")
    print(f"Slope: {slope:.1f}")

    t.undraw()
    t = Text(Point(WIDTH / 2, HEIGHT - 20), f"| Length: {length:.1f} | Slope: {slope:.1f} |")
    t.draw(win)

    win.getMouse() 
    win.close()

main()