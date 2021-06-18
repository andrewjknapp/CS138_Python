#! /usr/bin/python
# File Name:     hw4extraCredit.py
# Programmer:    Andrew Knapp
# Date:          June 17, 2021
#
# Problem Statement: Allow user to draw a house with a series of clicks
#
#
# Overall Plan:
# 1. Define constants for screen size
# 2. Define window object
# 3. Listen for two clicks 
# 4. Draw rectangle using click coordinates
# 5. Listen for one click
# 6. Use coordinate to draw door
# 7. Listen for one click
# 8. Draw window centered on point
# 9. Listen for one click
# 10. Draw roof with peak centered on point
# 11. close window
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
    print("Drawing Image...")


    # Window Object
    win = GraphWin("Create home", WIDTH, HEIGHT)

    ############## Frame of house ##############
    t = Text(TEXT_POINT, "Click the top left corner for your house")
    t.draw(win)

    # Wait for user clicks
    topLeftFrame = win.getMouse()

    t.setText("Click the bottom right corner for your house")
    
    bottomRightFrame = win.getMouse()

    frame = Rectangle(topLeftFrame, bottomRightFrame)
    frame.draw(win)

    ##############     Door      ##############
    t.setText("Click one point within the house to draw the door")

    centerDoorPoint = win.getMouse()

    doorWidth = (bottomRightFrame.getX() - topLeftFrame.getX()) / 5

    topLeftDoor = Point(centerDoorPoint.getX() - (doorWidth / 2), centerDoorPoint.getY())
    bottomRightDoor = Point(centerDoorPoint.getX() + doorWidth / 2, bottomRightFrame.getY())

    door = Rectangle(topLeftDoor, bottomRightDoor)
    door.draw(win)

    ##############    Window     ##############
    t.setText("Click one point within the house to draw window")

    centerWindowPoint = win.getMouse()

    halfWindowWidth = doorWidth / 4

    topLeftWindow = Point(centerWindowPoint.getX() - halfWindowWidth, centerWindowPoint.getY() + halfWindowWidth)
    bottomRightWindow = Point(centerWindowPoint.getX() + halfWindowWidth, centerWindowPoint.getY() - halfWindowWidth)

    window = Rectangle(topLeftWindow, bottomRightWindow)
    window.draw(win)

    ##############     Roof      ##############
    t.setText("Click one point above the house for the roof")

    roofPeakPoint = win.getMouse()

    leftTopRoof = Line(roofPeakPoint, topLeftFrame)
    leftTopRoof.draw(win)

    rightTopRoof = Line(roofPeakPoint, Point(bottomRightFrame.getX(), topLeftFrame.getY()))
    rightTopRoof.draw(win)

    ############# Ending Message ##############
    t.setText("Congrats on building your dream home!")
    

    win.getMouse() 
    win.close()

main()