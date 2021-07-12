
#! /usr/bin/python
# File Name:     hw9project1.py
# Programmer:    Andrew Knapp
# Date:          Jun 22, 2021
#
#
# Problem Statement: 
#
#
# Overall Plan:
# 1.
#
#
# import the necessary python libraries
from components.button import Button
from graphics import *

# Converts a number representing inches into
# a string formatted as feet and inches
def inchesToFeetAndInches(height):
    feet = height // 12
    inches = height % 12
    return f"{feet:.0f}'{inches:.0f}\""

def calculateHeight(heightMother, heightFather, gender):
    gender = gender.lower()

    # Calculate height based on correct formula for specified gender
    if (gender == "male"):
        height = ((heightMother * 13/12) + heightFather ) / 2
    else:
        height = ((heightFather * 12/13) + heightMother ) / 2

    return inchesToFeetAndInches(height)


def main():
    WIDTH = 600
    CENTER_X = WIDTH / 2
    HEIGHT = 600
    CURR_Y = 0
    SPACING = 50

    def next_y(type=True): 
        nonlocal CURR_Y
        if type:
            CURR_Y += SPACING
        else:
            CURR_Y += SPACING / 2
        return CURR_Y

    win = GraphWin("Height Calculator", WIDTH, HEIGHT)

    Text(Point(CENTER_X, next_y()), "Child Height Predictor").draw(win)

    Text(Point(CENTER_X, next_y()), "Enter The Mother's height in inches").draw(win)
    motherHeightEntry = Entry(Point(CENTER_X, next_y(False)), 20).draw(win)

    Text(Point(CENTER_X, next_y()), "Enter The Father's height in inches").draw(win)
    fatherHeightEntry = Entry(Point(CENTER_X, next_y(False)), 20).draw(win)

    Text(Point(CENTER_X, next_y()), "Please select the child's biological gender").draw(win)
    femaleButton = Button(win, Point(CENTER_X, next_y()), 100, 50, "Female")
    femaleButton.activate()
    maleButton = Button(win, Point(CENTER_X, next_y()), 100, 50, "Male")
    maleButton.activate()
    Text(Point(CENTER_X, next_y()), "Gender Selection").draw(win)
    genderSelection = Text(Point(CENTER_X, next_y(False)), "Female")
    genderSelection.draw(win)

    submitButton = Button(win, Point(CENTER_X, next_y()), 100, 50, "Calculate")
    submitButton.activate()

    heightLabel = Text(Point(CENTER_X, next_y()), "Calculated Height")
    calculatedHeight = Text(Point(CENTER_X, next_y(False)), "5'")

    try:
        while True:
            point = win.getMouse()

            if maleButton.clicked(point):
                genderSelection.setText("Male")
            elif femaleButton.clicked(point):
                genderSelection.setText("Female")
            elif submitButton.clicked(point):
                try:
                    try:
                        m_height = eval(motherHeightEntry.getText())
                        if m_height < 0:
                            raise ValueError()
                    except:
                        motherHeightEntry.setText("Enter positive Integer")
                        raise ValueError()
                    try:
                        f_height = eval(fatherHeightEntry.getText())
                        if f_height < 0:
                            raise ValueError()
                    except:
                        fatherHeightEntry.setText("Enter positive Integer")
                        raise ValueError()

                    gender = genderSelection.getText()
                    height = calculateHeight(m_height, f_height, gender)

                    calculatedHeight.setText(height)
                    heightLabel.undraw()
                    heightLabel.draw(win)
                    calculatedHeight.undraw()
                    calculatedHeight.draw(win)
                except:
                    print("Invalid number input")
    except:
        win.close()

main()

