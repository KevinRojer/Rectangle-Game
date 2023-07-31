#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:30:27 2023

@author: kevinrojer
"""

from src.point import Point
from src.rectangle import Rectangle


def initializeMap():
    print(" "*5 + "Initialize Map" + " "*5)
    print("-"*25)
    print()
    width = input("Please, choose the width: ")
    height = input("Please, choose the height: ")
    
    # Initialize the grid
    gameMap = Rectangle(width, height)
    
    x = input("Please, select an origin (x-coordinate): ")
    y = input("Now, select the y-coordinate: ")
    
    gameMap.createMap(x, y)
    
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
            print("you chose number 1.")
        elif (choice == "2"):
            print("You chose number 2.")
        elif (choice == "3"):
            print("Exiting game...")
            break
        else:
            print("Invalid input. Please, choose a number between 1 and 3.")
            continue
        
    # Print a good by message
    print("Thanks for playing. Bye, bye!")
        

if __name__ == "__main__":
    main()