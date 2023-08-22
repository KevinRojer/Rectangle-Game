#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 17:12:39 2023

@author: kevinrojer
"""


import random
import src.tools.display as display
from src.maps.GameMap import GameMap
from src.tools.utility import validate_positive_integer_input
from src.dataStructure.point import Point



class GameManager():
    """A class representing that manages the flow and state of the game."""
    
    
    def __init__(self):
        self.num_pieces = 1
        self.map = GameMap()
        self.targets = []
        
        
    def start_game(self):

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
            
            # print(f"x: {target_x} ; y: {target_y}")
    
    
    def get_map_dimensions(self):
        self.map.map.getMapSize()
        
        
    def check_for_hits(self, point):
        
        for tg in self.targets:
            if (point.x == tg.x) and (point.y == tg.y):
                display.show_target_hit()
            else:
                display.show_target_missed()
        
        
    def play_game(self):
        
        x_coordinate = self._get_coordinate("x")
        y_coordinate = self._get_coordinate("y")
        
        target = Point(x_coordinate, y_coordinate)
                
        if (self._validate_target(target)):
            self.check_for_hits(target)
        else:
            display.show_input_out_of_map()
                    
                    
    def _get_coordinate(self, dimension):
        
        while True:
            input_str = display.prompt_target_input(dimension)
            try:
                coordinate = validate_positive_integer_input(input_str)
                return coordinate
            except ValueError as e:
                display.show_invalid_input(e)
            
            
    def exit_game(self):
       display.show_closing_application_message()
            
            