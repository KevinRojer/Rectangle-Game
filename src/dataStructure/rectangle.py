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
        
        
    def createMap(self, startX, startY):
        """
        

        Parameters
        ----------
        startX : int
            the smallest x-coordinate.
        startY : int
            the smallest y-coordinate.

        Returns
        -------
        None.

        """
        if (isinstance(startX, int) and isinstance(startY, int)):
            self.lowerLeft = (startX, startY)
            self.upperRight = (startX + self.width, startY + self.height)
        else:
            print("Invalid input for coordinates.")
            
    
    def setWidth(self, width):
        """
        

        Parameters
        ----------
        width : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if (isinstance(width, int) and width > 0):
            self.width = width
        else:
            print("Invalid input. Please, try again.")
        
        
    def setHeight(self, height):
        """
        

        Parameters
        ----------
        height : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if (isinstance(height, int) and height > 0):    
            self.height = height
        else:
            print("Invalid input. Please, try again.")
        
        
    def getMapSize(self):
        """
        

        Returns
        -------
        None.

        """
        print(f"Map size is W {self.width} x H {self.height} grid.")
        
    