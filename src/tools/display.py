#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 18:18:35 2023

@author: kevinrojer
"""


def show_main_menu():
    print()
    print(" "*10 + "Menu" + " "*10)
    print("-"*25)
    print("1. Play Game")
    print("2. Change Map")
    print("3. Exit Game")
    print()
    
    
def show_exit_message():
    print("Thanks for playing. Bye, bye!")
    
    
def show_invalid_main_menu():
    print("\nInvalid input. Please, choose a number between 1 and 3.\n")