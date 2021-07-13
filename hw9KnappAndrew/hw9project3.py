
#! /usr/bin/python
# File Name:     hw9project3.py
# Programmer:    Andrew Knapp
# Date:          Jul 12, 2021
#
#
# Problem Statement: Update project 1 with the circular button
#
#
# Overall Plan:
# 1. import Button component
# 2. Create Text, Entry, and Button elements on the screen
# 3. Define what should happen when each button is clicked
#   - If either gender button is clicked then change value of selected gender
#   - If Calculate button is clicked run step 4
# 4. Validate entered values for mother and father height
# 5. Get selected gender
# 6. Calculate predicted height
# 7. Display predicted height
#
#
# import the necessary python libraries
from hw9project2.cbutton import CButton
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
    # Constants
    WIDTH = 600
    CENTER_X = WIDTH / 2
    HEIGHT = 600
    CURR_Y = 0
    SPACING = 50

    # Used to get the height for each element
    def next_y(type=True): 
        nonlocal CURR_Y
        if type:
            CURR_Y += SPACING
        else:
            CURR_Y += SPACING / 2
        return CURR_Y

    # Create window object
    win = GraphWin("Height Calculator", WIDTH, HEIGHT)

    # DEFINE ELEMENTS FOR SCREEN
    # Heading
    Text(Point(CENTER_X, next_y()), "Child Height Predictor").draw(win)

    # Mother Height Text Entry
    Text(Point(CENTER_X, next_y()), "Enter The Mother's height in inches").draw(win)
    motherHeightEntry = Entry(Point(CENTER_X, next_y(False)), 20).draw(win)

    # Father Height Text Entry
    Text(Point(CENTER_X, next_y()), "Enter The Father's height in inches").draw(win)
    fatherHeightEntry = Entry(Point(CENTER_X, next_y(False)), 20).draw(win)

    # Gender Select Buttons
    Text(Point(CENTER_X, next_y()), "Please select the child's biological gender").draw(win)
    femaleButton = CButton(win, Point(CENTER_X, next_y()), 30, "Female")
    femaleButton.activate()
    next_y(False)
    maleButton = CButton(win, Point(CENTER_X, next_y()), 20, "Male")
    maleButton.activate()

    # Gender Selection
    Text(Point(CENTER_X, next_y()), "Gender Selection").draw(win)
    genderSelection = Text(Point(CENTER_X, next_y(False)), "Female")
    genderSelection.draw(win)

    # Calculate Button
    submitButton = CButton(win, Point(CENTER_X, next_y()), 20, "Calc")
    submitButton.activate()

    # Result of calculation is displayed here
    heightLabel = Text(Point(CENTER_X, next_y()), "Calculated Height")
    calculatedHeight = Text(Point(CENTER_X, next_y(False)), "5'")

    try:
        while True:
            # Gets the point that was clicked
            point = win.getMouse()

            # Checks to see if any button was clicked
            # If male button is clicked set the gender selection to male
            if maleButton.clicked(point):
                genderSelection.setText("Male")
            # If female button is clicked set gender selection to female
            elif femaleButton.clicked(point):
                genderSelection.setText("Female")
            # If Claculate button is clicked Calculate height
            elif submitButton.clicked(point):
                # try/except blocks are in place to ensure valid input into height Entries
                # Valid input consists of positive numbers
                try:
                    # Get parent heights
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

                    # Get selected gender
                    gender = genderSelection.getText()

                    # Calculate height
                    height = calculateHeight(m_height, f_height, gender)

                    # Set text of display for result
                    calculatedHeight.setText(height)

                    # Show results to screen
                    heightLabel.undraw()
                    heightLabel.draw(win)
                    calculatedHeight.undraw()
                    calculatedHeight.draw(win)
                except:
                    print("Invalid number input")
    except:
        win.close()

main()

