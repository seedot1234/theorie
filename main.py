"""
main.py
Main file
Calls functions in the repository 'theorie'
28/1/2020

"""
import random
import csv, io, os
import copy
import pandas as pd 
import matplotlib.pyplot as plt

from code.algorithms.random import random_solution
from code.algorithms.random import random_solution
from code.algorithms.greedy_lookahead import greedy_lookahead
from code.algorithms.trim import trim
from code.algorithms.shortest import shortest
from code.algorithms.unused import unused
from code.classes import connection, route, station, load_data
from code.classes.route import Route
from code.algorithms.hill import Hillclimber
from code.algorithms.annealing import SimulatedAnnealing
from code.classes.solution import Solution
from results.visualisation import visualise
from results.bound import quality
from interface.interface import UI
from os import system, name

from random import randrange
from interface.interface import UI


def clear():
    """Clears the console screen"""

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def ask_problem_set():
    choice = input("Choose what problem set you want to use\nFor options type HELP\n")
    choice_options = ['1', '2', 'HELP']

    while choice.upper() not in choice_options:
        print("That was not a valid command.")
        choice = input("Choose what algorithm you want to use.\nFor options type HELP\n")
    
    if choice.upper() == 'HELP':
        clear()
        print("1 = Holland\n2 = Nederland\n")
        return ask_problem_set()
    
    elif choice == '1':
        problem_set = 'Holland'

    elif choice == '2':
        problem_set = 'Nederland'

    else:
        print("That was not a valid command.")
        choice = input("Choose what algorithm you want to use.\nFor options type HELP\n")

    return problem_set

if __name__ == "__main__":

    clear()

    print("Welcome to RailNL\nPlease refer to the README for instructions as of how to use this program.\n")

    # ask what problem set the user want to use
    problem_set = ask_problem_set()

    # create the corresponding datastructure
    if problem_set == 'Holland':
        interface = UI(os.path.join("data", "StationsHolland.csv"), os.path.join("data", "ConnectiesHolland.csv"), max_routes=7, max_minutes=120)

    elif problem_set == 'Nederland':
        interface = UI(os.path.join("data", "StationsNationaal.csv"), os.path.join("data", "ConnectiesNationaal.csv"), max_routes=20, max_minutes=180)

    # if we get here, something went wrong
    else:
        exit()

    # run the UI
    interface.run()