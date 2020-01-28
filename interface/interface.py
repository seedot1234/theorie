"""

interface.py
Calls all functions in the repository 'theorie'
27/01/2020

"""

from code.classes import connection, route, station, load_data
from results.visualisation import visualise
from code.classes.route import Route
from code.algorithms.random import random_solution
from code.algorithms.random_p import random_solution_p
from code.algorithms.random_k import random_solution_k
from code.algorithms.greedy_lookahead import greedy_lookahead
from code.algorithms.greedy_lookahead_test import greedy_lookahead_test
from code.algorithms.trim import trim
from code.algorithms.railhead import railhead
from code.algorithms.shortest import shortest
from code.algorithms.longest import longest
from code.algorithms.unused import unused
from random import randrange
from code.classes.solution import Solution
import random
import csv, io, os
import copy
from results.bound import quality

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
        self.station_objects = load_data.create_station_list_nationaal(self.station_csv)
        
        # create connection objects from csv
        self.connection_objects = load_data.create_connection(self.connection_csv, self.station_objects)

        # adds connections to stations
        connections_list = []
        load_data.add_station_connection(self.station_objects, self.connection_objects)

        # set railhead stations
        for station in self.station_objects:
            station.set_rail_head()

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

    def ask_iterations(self):
        """
        Asks the user how many times they want their chosen
        algorithm to be performed.
        """

        while True:
            try:
                iterations = int(input("How often do you want to run the algorithm?\n"))
                break
            except ValueError:
                print("It must be a positive integer")
        
        while iterations <= 0:
            self.ask_iterations()
        
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

    def perform_algorithm_multiple(self, algorithm, iterations):
        """
        Performs an algorithm for a specified number of times.
        Parameters: algorithm, iterations.
        Returns:    solution.
        """
        for i in range (iterations):

            solution = algorithm(self.station_objects, self.connection_objects, self.max_routes, self.max_minutes)
            solution.set_K(len(self.connection_objects))

        return solution    

    def perform_algorithm(self, algorithm, visualisation):

        solution = algorithm(self.station_objects, self.connection_objects, self.max_routes, self.max_minutes)
        solution.set_K(len(self.connection_objects))


        if visualisation == True:
            map = visualise.coordinates(self.station_csv, solution)

        return solution


    def run(self):

        self.create_objects()
        algorithm = self.ask_algorithm()

        iterations = self.ask_iterations()

        visualisation = self.ask_visualisation()

        if iterations == 1:
            self.perform_algorithm(algorithm, visualisation)

        else:
            self.perform_algorithm_multiple(algorithm, iterations)


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