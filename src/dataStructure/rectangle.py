#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:28:38 2023

@author: kevinrojer
"""


class Rectangle:
    """A class representing a rectangle"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.lowerLeft = None
        self.upperRight = None
        
        
    def createMap(self, startX, startY):
        """
        Create a map using the given coordinates as the lower-left corner

        Parameters
        ----------
        startX : int
            the x-coordinate of the lower left corner.
        startY : int
            the y-coordinate of the lower left corner.

        Returns
        -------
        None.

        """
        if (isinstance(startX, int) and isinstance(startY, int)):
            self.lowerLeft = (startX, startY)
            self.upperRight = (startX + self.width, startY + self.height)
        else:
            raise ValueError("Invalid input for coordinates.")
            
    
    def setWidth(self, width):
        """
        Set the width of the rectangle.

        Parameters
        ----------
        width : int
            The new width of the rectangle.

        """
        if self._validate_positive_integer(width):
            self.width = width
        else:
            raise ValueError("Please, use positive integers for width.")
        
        
    def setHeight(self, height):
        """
        

        Parameters
        ----------
        height : int
            The new height of the rectangle.

        """
        if self._validate_positive_integer(height):
            self.height = height
        else:
            raise ValueError("Please, use positive integers for height.")
            
            
    def _validate_positive_integer(self, value):
        """
        Validate whether a given value is a positive integer.

        Parameters
        ----------
        value : int
            The value to be validated.

        Returns
        -------
        bool
            True if the value is a positive integer. False otherwise.

        """
        if (isinstance(value, int) and value > 0):
            return True
        else:
            return False
        
        
    def getMapSize(self):
        """
        Print the size of the map.

        """
        print(f"Map size is W {self.width} x H {self.height} grid.")
        
    