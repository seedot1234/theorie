"""
main.py
Main file
Calls functions in the repository 'theorie'
28-1-2020
"""


import  os

from code.classes import load_data
from interface.interface import UI
from os import system, name


def clear():
    """Clears the console screen"""

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def ask_problem_set():
    choice = input("Choose what problem set you want to use\n1 = Holland\n2 = Nederland\n")
    choice_options = ['1', '2']

    while choice.upper() not in choice_options:
        print("That was not a valid command.")
        choice = input("Choose what problem set you want to use\n1 = Holland\n2 = Nederland\n")
    
    if choice == '1':
        problem_set = 'Holland'

    elif choice == '2':
        problem_set = 'Nederland'

    else:
        print("That was not a valid command.")
        choice = input("Choose what algorithm you want to use.\n1 = Random\n2 = Shortest\n3 = Unused\n4 = Greedy Lookahead\n")

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

