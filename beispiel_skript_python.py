#!/usr/bin/env python3
"""
================================================================================
Skript Name:    beispiel_skript_python.py
Author:         Matthias Deitermann
Matrikelnummer: 000000
Mailadresse:    email@hhu.de
Datum:          06.11.2025
Übungsblatt:    1

Beschreibung:
    Beispielskript zu den Programmierübungen in MRT: Bilderzeugung,
    Bildrekonstruktion, Bildverarbeitung

Anwendung:
    python example-python-file.py [arguments]

    Beispiel:
        python script_name.py --input data.csv --output results.txt

Argumente:
    --input, -i     : Input file path (required)
    --output, -o    : Output file path (optional)
    --verbose, -v   : Enable verbose output (flag)

Abhängigkeiten:
    - numpy
    - matplotlib

Notizen:
    Platz für Anmerkungen.
    Dieses Skript dient als Orientierung.

================================================================================
"""
import random
import math


# example functions
def my_function_name():
    """Simple print example."""
    print("This function is done.")


def my_for_loop_function(number_of_runs=3):
    """Simple loop example."""
    for i in range(number_of_runs):
        print(f"Running loop {i}.")


def my_while_loop_function(random_number):
    """Simple while loop example."""
    print(f"You selected number {random_number}. Now reducing it by pi until it reaches zero.")
    while random_number > 0:
        print(f"Reducing your number by pi. Currently at: {random_number}")
        random_number -= math.pi


def my_return_function(a):
    """Simple return example"""
    return a


if __name__ == "__main__":
    # call example functions
    my_function_name()
    my_for_loop_function(5)
    random_number = random.randint(1, 20)
    my_while_loop_function(random_number)
    result = my_return_function(42)
    print(f"The answer to life, the universe and everything is: {result}")