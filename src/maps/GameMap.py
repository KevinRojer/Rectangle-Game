#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 16:07:04 2023

@author: kevinrojer
"""


from src.dataStructure.rectangle import Rectangle


class GameMap:
    """ A class representing a game map. """
    
    def __init__(self):
        self.map = None
        
    
    def initializeMap(self):
        """
        Initializes a game map

        Returns
        -------
        None.

        """
        
        while (True):
            # Display the options
            print()
            print(" "*5 + "Set the Map" + " "*5)
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
            self.map = Rectangle(width, height)
            
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
            self.map.createMap(xVal, yVal)
            break
            
        print("\nMap set.\n")
        
        
    def changeMap(self):
        
        while (True):
            # Display the options
            print()
            print(" "*5 + "Changing Map" + " "*5)
            print("-"*25)
            print("1. Change the whole map")
            print("2. Change the height")
            print("3. Change the width")
            print("4. Back")
            print()
            
            choice = input("Please, choose one of the options: ")
            try:
                # Validate the input
                choice = int(choice)
            except ValueError:
                print("\nInvalid input. Please, use numbers.\n")
                continue
                
            if (choice == 1):
                self.initializeMap()
                self.map.getMapSize()
                break
            elif (choice == 2):
                height = input("Please, enter the new height: ")
                try:
                    # Validate the input
                    height = int(height)
                except ValueError:
                    print("\nInvalid input. Please, use a number again.\n")
                    continue
                
                self.map.setHeight(height)
                print("Changed the height.")
                self.map.getMapSize()
                break
            elif (choice == 3):
                width = input("Please, enter the new width: ")
                try:
                    # Validate the input
                    width = int(width)
                except ValueError:
                    print("\nInvalid input. Please, use a number again.\n")
                    continue
                
                self.map.setWidth(width)
                print("Changed the width.")
                self.map.getMapSize()
                break
            elif (choice == 4):
                break
            else:
                print("Please, choose a relevant number.")
                print()
                continue
            
    def pointInMap(self):
        return True
