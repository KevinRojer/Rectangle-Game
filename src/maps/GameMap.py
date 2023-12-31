#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 16:07:04 2023

@author: kevinrojer
"""


from src.dataStructure.rectangle import Rectangle
from src.tools.utility import validate_positive_integer_input


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
            print("\n" + " " * 5 + "Set the Map" + " " * 5)
            print("-" * 25 + "\n")
            
            width_input = input("Please, choose the width: ")
            
            try:
                width = validate_positive_integer_input(width_input)
            except ValueError as e:
                print(f"\nInvalid input: {e}\n")
                continue             
                
            height_input = input("Please, choose the height: ")
            
            try:
                height = validate_positive_integer_input(height_input)
            except ValueError as e:
                print(f"\nInvalid input: {e}\n")
                continue
                
            # Initialize the map
            self.map = Rectangle(width, height)
            self.map.createRectangle()
            break
            
        print("\nMap set.\n")
        
        
    def changeMap(self):
        
        while (True):
            # Display the options
            print("\n" + " " * 5 + "Changing Map" + " " * 5)
            print("-" * 25)
            print("1. Change the whole map")
            print("2. Change the height")
            print("3. Change the width")
            print("4. Back" + "\n")
            
            choice_input = input("Please, choose one of the options: ")
           
            try:
                # Validate the input
                choice = int(choice_input)
            except ValueError:
                print("\nInvalid input. Please, use numbers.\n")
                continue
                
            if (choice == 1):
                self.initializeMap()
                self.map.getRectangleSize()
                break
            
            elif (choice == 2):
                height_input = input("Please, enter the new height: ")
                
                try:
                    # Validate the input
                    height = validate_positive_integer_input(height_input)
                    self.map.setHeight(height)
                    self.map.createRectangle()
                except ValueError as e:
                    print(f"\nInvalid input: {e}\n")
                    continue
                
                
                print("\nChanged the height.")
                self.map.getRectangleSize()
                break
            
            elif (choice == 3):
                width_input = input("Please, enter the new width: ")
                
                try:
                    # Validate the input
                    width = validate_positive_integer_input(width_input)
                    self.map.setWidth(width)
                    self.map.createRectangle()
                except ValueError as e:
                    print(f"\nInvalid input: {e}\n")
                    continue
                
                print("\nChanged the width.")
                self.map.getRectangleSize()
                break
            
            elif (choice == 4):
                break
            else:
                print("Please, choose a relevant number." + "\n")
                continue
            
    
    def is_point_on_map(self, point):
        if (self.map.lowerLeft[0] < point.x < self.map.upperRight[0]) \
            and (self.map.lowerLeft[1] < point.y < self.map.upperRight[1]):
                return True
        else:
            return False