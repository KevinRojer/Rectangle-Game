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
    
    
def show_closing_application_message():
    print("\nExiting application...\n")
    
    
def show_invalid_main_menu():
    print("\nInvalid input. Please, choose a number between 1 and 3.\n")
    
    
def prompt_target_input(dimension):
    return input(f"Please, select your target's {dimension}-coordinate: ")
    
    
def show_invalid_input(error_message):
    print(f"\nInvalid input: {error_message}\n")
    
    
def show_target_missed():
    print("\nTarget missed. Please, try again.\n")
    
    
def show_target_hit():
    print("\nBoom! Target hit!\n")
    
    
def show_input_out_of_map():
    print("\nInput error: Selected target is outside of the map.\n")