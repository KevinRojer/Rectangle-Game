#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:30:27 2023

@author: kevinrojer
"""


from src.maps.GameMap import GameMap


def showMenu():
    print()
    print(" "*10 + "Menu" + " "*10)
    print("-"*25)
    print("1. Play Game")
    print("2. Change Map")
    print("3. Exit Game")
    print()


def main():
    # initialize the game map
    gameMap = GameMap()
    gameMap.initializeMap()
    
    while (True):
        showMenu()
        
        choice = input("Please, select your choice: ")

        if (choice == "1"):
            print("\nyou chose number 1.\n")
            continue
        elif (choice == "2"):
            gameMap.changeMap()
            continue
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