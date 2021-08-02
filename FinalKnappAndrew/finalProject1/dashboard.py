# dashboard.py
from graphics import *
from page import Page
from button import Button
import os

class Dashboard(Page):

    def initializeState(self):
        """Initializes any page specific variables"""

        self.defaultDictionaryPath = os.path.join(os.path.dirname(__file__), 'english_win.txt')
        self.filePath = ""


    def defineElements(self):
        """Defines the elements that will appear on the page and adds them to the elements list"""

        self.createElement("title", Text(Point(self.center, 30), "Spell Checker"))

        self.createElement("userFileLabel", Text(Point(self.center - 100, 60), "File to spell check:"))

        self.createElement("userFileEntry", Entry(Point(self.center + 70, 60), 20))

        self.createElement("dictionaryLabel", Text(Point(self.center - 100, 90), "Dictionary:"))

        self.createElement("dictionaryEntry", Entry(Point(self.center + 70, 90), 20))
        self.dictionaryEntry.setText("default")

        self.createElement("checkButton", Button(self.parent.win, Point(self.center, 200), 60, 25, "Check", True))

        self.createElement("misspelledLabel", Text(Point(self.center, 250), ""))
        self.createElement("misspelledText", Text(Point(self.center, 280), ""))

        

    def defineClickActions(self):
        """Defines what should happen when a button is clicked on the page"""

        self.clickActions.append({"button": self.checkButton, "action": self.handleSpellCheck})


    def handleSpellCheck(self):
        """Runs spell check on user entered file"""
        userFile = self.userFileEntry.getText()
        dictionaryFile = self.dictionaryEntry.getText()

        allEntriesFilled = len(userFile) != 0 and len(dictionaryFile) != 0

        if not allEntriesFilled:
            return
        
        if dictionaryFile == "default":
            dictionaryFile = self.defaultDictionaryPath

        # Read dictionary
        dictList = self.readFile(dictionaryFile)

        # Read user file
        userWordList = self.readFile(userFile)

        incorrectlySpelled = []
        # Check if each word from user file is in dictionary
        for word in userWordList:
            if not self.isSpelledCorrectly(word, dictList):
                incorrectlySpelled.append(word)

        print(incorrectlySpelled)

        self.misspelledLabel.setText("Misspelled Words")
        self.misspelledText.setText(", ".join(incorrectlySpelled))
        
        

    def isSpelledCorrectly(self, word, list):
        """Checks if the given word is in a list using binary search"""
        return self.binarySearch(word, list, 0, len(list)) != -1

    def binarySearch(self, target, arr, lowPos, highPos):
        if lowPos > highPos:
            return -1

        midPos = int((highPos + lowPos) / 2)

        if arr[midPos] == target:
            return midPos

        # if target is later in the alphabet than the midpoint
        if arr[midPos].lower() < target.lower():
            return self.binarySearch(target, arr, midPos + 1, highPos) 
        # if target is earlier in the alphabet than midpoint
        if arr[midPos].lower() > target.lower():
            return self.binarySearch(target, arr, lowPos, midPos - 1)


    def readFile(self, fileName):
        """Reads given file and returns a list contianing each word"""
        try:
            with open(fileName, "r") as f:
                userFile = f.read()
                return userFile.split()
        except:
            print("Trouble reading file", fileName)

    def defineStyles(self, name, element):
        """Applies styles specific to element type"""
        if isinstance(element, Entry):
            getattr(self, name).setFill("white")
