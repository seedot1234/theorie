"""

interface.py
Calls all functions in the repository 'theorie'
27/01/2020

"""

from code.classes import connection, route, station, load_data
from code.visualisation import visualise
from code.classes.route import Route
from code.algorithms.random import random_solution
from code.algorithms.random_p import random_solution_p
from code.algorithms.random_k import random_solution_k
from code.algorithms.greedy_lookahead import greedy_lookahead
from code.algorithms.greedy_lookahead_test import greedy_lookahead_test
from code.algorithms.trim import trim
from code.algorithms.shortest import shortest
from code.algorithms.unused import unused
from random import randrange
from code.classes.solution import Solution
import random
import csv, io, os
from os import system, name
import copy
from code.visualisation.descriptives import descriptive, boxplot, histogram

class UI(object):

    def __init__(self, station_csv, connection_csv):
        self.station_csv = station_csv
        self.connection_csv = connection_csv
        self.max_routes = 20
        self.max_minutes = 180

    def create_objects(self):
        """
        Creates the datastructure that will be used when running
        the different algorithms.
        """
        
        # create station objects from csv
        self.station_objects = load_data.create_station_list(self.station_csv)
        
        # create connection objects from csv
        self.connection_objects = load_data.create_connection(self.connection_csv, self.station_objects)

        # adds connections to stations
        connections_list = []
        load_data.add_station_connection(self.station_objects, self.connection_objects)

    def ask_algorithm(self):
        """
        Asks the user what algorithm must be performed.
        """

        choice = input("Choose what algorithm you want to use.\nFor options type HELP\n")
        choice_options = ['1', '2', '3', '4', 'HELP']

        while choice.upper() not in choice_options:
            print("That was not a valid command.")
            choice = input("Choose what algorithm you want to use.\nFor options type HELP\n")
        

        if choice.upper() == 'HELP':
            print("1 = random\n2 = shortest\n3 = unused\n4 = greedy lookahead")
            return self.ask_algorithm()
        
        elif choice == '1':
            algorithm = random_solution_p

        elif choice == '2':
            algorithm = shortest

        elif choice == '3':
            algorithm = unused

        elif choice == '4':
            algorithm = greedy_lookahead_test

        return algorithm

    def ask_p(self):
        """
        Ask the user at what p-level the algorithm must stop running.
        Returns:    p.
        """

        while True:
            try:
                p = float(input("What p-level do you want?\n"))
                break
            except ValueError:
                print("It must be a float")
        
        while p <= 0.0 or p > 1:
            return self.ask_p()

        return p

    def ask_iterations(self):
        """
        Asks the user how many times they want their chosen
        algorithm to be performed.
        """

        while True:
            try:
                iterations = int(input("How often do you want to run the algorithm?\nWARNING: with more than 1 iteration, a csv file will be created in /XXX/XXX/XXX\n"))
                break
            except ValueError:
                print("It must be a positive integer")
        
        while iterations <= 0:
            return self.ask_iterations()
        
        return iterations


    def ask_visualisation(self):

        choice = input("Do you want a visualisation (map) of the result?\nIt will open in your browser.\nY / N\n")

        possible_inputs = ['Y', 'YES', 'N', 'NO']

        while choice.upper() not in possible_inputs:
            return self.ask_visualisation()
        
        if choice.upper() == 'Y' or choice.upper() == 'YES':
            visualisation = True
        elif choice.upper() == 'N' or choice.upper() == 'NO':
            visualisation = False
        
        # standard is no visualisation
        else:
            visualisation = False

        return visualisation

    def ask_boxplot(self):
        """Asks user whether they want a boxplot made out of their results."""

        choice = input("Do you want a boxplot made of the results?\nIt will open in a python window and not save unless you say so.\nY / N\n")

        possible_inputs = ['Y', 'YES', 'N', 'NO']

        while choice.upper() not in possible_inputs:
            return self.ask_boxplot()
        
        if choice.upper() == 'Y' or choice.upper() == 'YES':
            boxplot_option = True
        elif choice.upper() == 'N' or choice.upper() == 'NO':
            boxplot_option = False
        
        # standard is no visualisation
        else:
            boxplot_option = False

        return boxplot_option

    def ask_histrogram(self):
        """Asks user whether thay want a histogram made out of their results."""

        choice = input("Do you want a histogram made of the results?\nIt will open in a python window and not save unless you say so.\nY / N\n")

        possible_inputs = ['Y', 'YES', 'N', 'NO']

        while choice.upper() not in possible_inputs:
            return self.ask_histrogram()
        
        if choice.upper() == 'Y' or choice.upper() == 'YES':
            histrogram_option = True
        elif choice.upper() == 'N' or choice.upper() == 'NO':
            histrogram_option = False
        
        # standard is no visualisation
        else:
            histrogram_option = False

        return histrogram_option

    def perform_algorithm_multiple(self, algorithm, iterations, requested_p, boxplot_option, histrogram_option):
        """
        Performs an algorithm for a specified number of times and saves its results to a csv.
        Returns:    statistics.
        """

        statistics = descriptive(len(self.connection_objects), self.station_objects, algorithm, iterations, requested_p)

        if boxplot_option == True:
            boxplot('Nederland', algorithm)

        if histrogram_option == True:
            histogram('Nederland', algorithm)

        return statistics

    def perform_algorithm(self, algorithm, visualisation, requested_p):
        """
        Performs an algorithm one time with a specified p. Shows visualisation.
        Returns:    solution.
        """

        solution = algorithm(self.station_objects, len(self.connection_objects), self.max_routes, self.max_minutes, requested_p)
        solution.set_K(len(self.connection_objects))


        if visualisation == True:
            self.visualise_solution(solution)

        return solution


    def visualise_solution(self, solution):
        """Given a solution, shows a visual representation on a map."""
        
        map = visualise.coordinates(self.station_csv, solution)


    def general_output_info(self, solution):
        """
        Generates the statistics for a given solution.
        Returns: statistics.
        """

        statistics = {}

        statistics['K'] = solution.set_K(len(self.connection_objects))
        statistics['T'] = len(solution.lining)
        statistics['min'] = solution.set_min()
        statistics['p'] = solution.set_p(len(self.connection_objects))

        return statistics

    def run(self):
        """
        Runs the user interface.
        """

        # clear console
        clear()

        # create the datastructure
        self.create_objects()

        # ask user what algorithm they want to use
        algorithm = self.ask_algorithm()

        clear()

        # ask user how many times they want to run the algorithm
        iterations = self.ask_iterations()
        
        clear()

        # ask user what p-level they want their algorithm to have
        requested_p = self.ask_p()

        clear()

        # for 1 iteration
        if iterations == 1:

            # ask user whether they want a visualisation
            visualisation = self.ask_visualisation()
            
            clear()

            # perform the algorithm
            solution = self.perform_algorithm(algorithm, visualisation, requested_p)
            
            # create statistics for the runned algorithm
            statistics = self.general_output_info(solution)
            
            # show results to user
            print("Scores of this algorithm:")
            for stat in statistics:
                print(stat,":", statistics[stat])

        # for more than 1 iteration
        else:

            # ask user whether they want a boxplot made
            boxplot_option = self.ask_boxplot()

            # ask user whether they want a histogram made
            histrogram_option = self.ask_histrogram()

            # perform the algorithm and write its results to a csv
            statistics = self.perform_algorithm_multiple(algorithm, iterations, requested_p, boxplot_option, histrogram_option)
            
            # show results to user
            print("Average scores of this algorithm:")
            for stat in statistics:
                print(stat,":", statistics[stat])

def clear():
    """Clears the console screen"""

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

# greet user
# verwijs voor usage naar readme
# kies het algoritme dat je wil gebruiken
    # 1 = random_p
    # 2 = shortest
    # 3 = unused
    # 4 = greedy lookahead

# hoe vaak wil je het runnen?
    # bij 1:
        # wil je visualisatie / kaart?
        # doe altijd general info
    # bij meer dan 1:
        # wil je statistieken?
            # boxplot?
            # histogram?
            # doe altijd general average info