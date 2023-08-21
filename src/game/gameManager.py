#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 17:12:39 2023

@author: kevinrojer
"""


import random
from src.maps.GameMap import GameMap
from src.tools.utility import validate_positive_integer_input
from src.dataStructure.point import Point


class GameManager():
    """A class representing that manages the flow and state of the game."""
    
    
    def __init__(self):
        self.num_pieces = 1
        self.map = GameMap()
        self.targets = []
        
        
    def initialize_map(self):

        self.map.initializeMap()
        self._place_targets()
        
        
    def update_map(self):
        
        self.map.changeMap()

        
    def _validate_target(self, point):
        
        return self.map.is_point_on_map(point)
    
    
    def _place_targets(self):
        
        for tg in range(self.num_pieces):
            
            target_x = random.randint(0, self.map.map.width)
            target_y = random.randint(0, self.map.map.height)
            
            target = Point(target_x, target_y)
            self.targets.append(target)
            
            print(f"x: {target_x} ; y: {target_y}")
    
    
    def get_map_dimensions(self):
        self.map.map.getMapSize()
        
        
    def check_for_hits(self, point):
        
        for tg in self.targets:
            if (point.x == tg.x) and (point.y == tg.y):
                print("Success. Target hit!")
            else:
                print("Target missed. Please, try again.")
        
        
    def select_target(self):
        
        x_input = input("Please, select your target's x-coordinate: ")
        x_coordinate = validate_positive_integer_input(x_input)
        
        y_input = input("Please, select your target's y-coordinate: ")
        y_coordinate = validate_positive_integer_input(y_input)
        
        target = Point(x_coordinate, y_coordinate)
        
        if (self._validate_target(target)):
            self.check_for_hits(target)
        else:
            print("Target outside of map")
            
            
    def exit_game(self):
        print("\nExiting game...")
            
            