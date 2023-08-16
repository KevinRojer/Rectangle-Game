#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 09:22:47 2023

@author: kevinrojer
"""


def validate_positive_integer_input(input_str):
    """
    Validates whether the given input string represents a positive integer.

    Parameters
    ----------
    input_str : string
        A string representing console-based input for width or height.

    Returns
    -------
    int or None
        Returns the positive integer value if input is valid, 
        otherwise return None.

    """
    try:
        dimension = int(input_str)
    except ValueError:
        raise ValueError("Please, use integers.")
    else:
        if dimension < 0:
            raise ValueError("Negative numbers are not allowed for dimensions.")
        return dimension
    