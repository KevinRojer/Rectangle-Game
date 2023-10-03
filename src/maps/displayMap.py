#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 19:02:19 2023

@author: kevinrojer
"""


from src.dataStructure.rectangle import Rectangle


class Map(Rectangle):
    
    
    def __init__(self, name, width, height):
        super.__init__(width, height)
        self.name = name
        
        
    def describeMap(self):
        print(f"Map: {self.name} - W:{self.width} x H:{self.height}.")
    
