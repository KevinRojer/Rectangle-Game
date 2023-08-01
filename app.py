#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:30:27 2023

@author: kevinrojer
"""

from src.point import Point
from src.rectangle import Rectangle


def initializeMap():
    
    while (True):
        # Display the options
        print(" "*5 + "Initialize Map" + " "*5)
        print("-"*25)
        print()
        
        width = input("Please, choose the width: ")
        try:
            # Validate the input
            width = int(width)
        except ValueError:
            print("\nInvalid input. Please, try agian.\n")
            continue
            
        height = input("Please, choose the height: ")
        
        try:
            # Validate the input
            height = int(height)
        except ValueError:
            print("\nInvalid input. Please, try again.\n")
            continue
            
        # Initialize the grid
        gameMap = Rectangle(width, height)
        
        x = input("Please, select an origin x-coordinate: ")
        try:
            # Validate input
            xVal = int(x)
        except ValueError:
            print("\nInvalid input. Please, try again.\n")
            continue
            
        y = input("Now, select the y-coordinate: ")
        try:
            # validate input
            yVal = int(y)           
        except ValueError:
            print("\nInvalid input. Please, try again.\n")
            continue
        
        # Initialize the map
        gameMap = gameMap.createMap(xVal, yVal)
        break
        
    print("\nMap initialized.\n")
    
    return gameMap


def showMenu():
    print(" "*10 + "Menu" + " "*10)
    print("-"*25)
    print("1. Play Game")
    print("2. Change Map")
    print("3. Exit Game")
    print()


def main():
    # start default game
    gameMap = initializeMap()
    
    while (True):
        showMenu()
        
        choice = input("Please, select your choice: ")

        if (choice == "1"):
            print("\nyou chose number 1.\n")
        elif (choice == "2"):
            print("\nYou chose number 2.\n")
        elif (choice == "3"):
            print("\nExiting game...")
            break
        else:
            print("\nInvalid input. Please, choose a number between 1 and 3.\n")
            continue
        
    # Print a good by message
    print("Thanks for playing. Bye, bye!")
        

if __name__ == "__main__":
    main()