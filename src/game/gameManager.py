#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 17:12:39 2023

@author: kevinrojer
"""


from src.maps.GameMap import GameMap
from src.tools.utility import validate_positive_integer_input
from src.dataStructure.point import Point


class GameManager():
    """A class representing that manages the flow and state of the game."""
    
    
    def __init__(self):
        self.num_pieces = 1
        self.map = GameMap()
        
        
    def initialize_map(self):

        self.map.initializeMap()
        
        
    def update_map(self):
        
        self.map.changeMap()

        
    def check_for_hits(self, point):
        
        return self.map.is_point_on_map(point)
    
    
    def get_map_dimensions(self):
        self.map.map.getMapSize()
        
        
    def select_target(self):
        
        x_input = input("Please, select your target's x-coordinate: ")
        x_coordinate = validate_positive_integer_input(x_input)
        
        y_input = input("Please, select your target's y-coordinate: ")
        y_coordinate = validate_positive_integer_input(y_input)
        
        target = Point(x_coordinate, y_coordinate)
        
        if (self.check_for_hits(target)):
            print("Target in map")
        else:
            print("Target outside of map")
            
            
    def exit_game(self):
        print("\nExiting game...")
            
            