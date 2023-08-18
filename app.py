#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:30:27 2023

@author: kevinrojer
"""


from src.game.gameManager import GameManager
import src.tools.display as display




def main():
    # initialize the game manager & map
    gameManager = GameManager()
    gameManager.initialize_map()
    
    while (True):
        display.show_main_menu()
        
        choice = input("Please, make a selection: ")

        if (choice == "1"):
            gameManager.select_target()
            continue
        elif (choice == "2"):
            gameManager.update_map()
            continue
        elif (choice == "3"):
            gameManager.exit_game()
            break
        else:
            display.show_invalid_main_menu()
            continue
        
        
    # Print a good by message
    display.show_exit_message()
        

if __name__ == "__main__":
    main()