"""
Skript Name:    beispiel_abgabelayout_python.py
python Version: 3.12
Author:         Matthias Deitermann
Matrikelnummer: 00000
Datum:          06.11.2025
Übungsblatt:    0
"""

import math


# example functions
def my_function_name():
    """Einfaches print Beispiel."""
    print("This function is done.")


def my_for_loop_function(number_of_runs=3):
    """Einfaches for-loop Beispiel."""
    for i in range(number_of_runs):
        print(f"Running loop {i}.")


def my_while_loop_function(random_number):
    """Einfaches while-loop Beispiel"""
    while random_number > 0:
        print(f"Reducing your number by pi. Currently at: {random_number}")
        random_number -= math.pi


def my_return_function(a):
    """Simple return example"""
    return a
