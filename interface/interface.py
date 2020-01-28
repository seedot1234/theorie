"""
interface.py
Creates a user-interface to run the whole program.

@author Heuristic Heroes
@version 28/01/2020

"""

from code.classes import load_data
from code.visualisation import visualise
from code.algorithms.random import random_solution
from code.algorithms.greedy_lookahead import greedy_lookahead
from code.algorithms.trim import trim
from code.algorithms.shortest import shortest
from code.algorithms.unused import unused
from code.algorithms.hillclimber import Hillclimber
from code.algorithms.annealing import SimulatedAnnealing
from os import system, name
from code.visualisation.descriptives import descriptive, boxplot, histogram


class UI(object):

    def __init__(self, station_csv, connection_csv, max_routes, max_minutes):
        self.station_csv = station_csv
        self.connection_csv = connection_csv
        self.max_routes = max_routes
        self.max_minutes = max_minutes

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

        # ask user what algorithm they want to use
        choice = input("Choose what algorithm you want to use.\n1 = Random\n2 = Shortest\n3 = Unused\n4 = Greedy Lookahead\n")
        choice_options = ['1', '2', '3', '4']

        # ensure proper usage
        while choice.upper() not in choice_options:
            print("That was not a valid command.")
            choice = input("Choose what algorithm you want to use.\n1 = Random\n2 = Shortest\n3 = Unused\n4 = Greedy Lookahead\n")
        
        # define the requested algorithm
        if choice == '1':
            algorithm = random_solution

        elif choice == '2':
            algorithm = shortest

        elif choice == '3':
            algorithm = unused

        elif choice == '4':
            algorithm = greedy_lookahead

        return algorithm

    def ask_p(self):
        """
        Ask the user at what p-level the algorithm must stop running.
        Returns:    p.
        """

        # ask user for input, ensure proper usage
        while True:
            try:
                p = float(input("What p-level do you want? It must be a float\n"))
                break
            except ValueError:
                print("It must be a float")
        
        # ensure proper usage
        while p <= 0.0 or p > 1:
            return self.ask_p()

        return p

    def ask_iterations(self):
        """
        Asks the user how many times they want their chosen
        algorithm to be performed.
        """

        # ask user input, ensure proper usage
        while True:
            try:
                iterations = int(input("How often do you want to run the algorithm?\nWARNING: with more than 1 iteration, a csv file called 'results.csv' will be created in the main folder of this project\n"))
                break
            except ValueError:
                print("It must be a positive integer")
        
        # ensure proper usage
        while iterations <= 0:
            return self.ask_iterations()
        
        return iterations


    def ask_visualisation(self):
        """Ask user whether they want a visualisation of their results."""

        # prompt user for input
        choice = input("Do you want a visualisation (map) of the result?\nIt will open in your browser.\nY / N\n")

        # ensure proper usage
        possible_inputs = ['Y', 'YES', 'N', 'NO']
        while choice.upper() not in possible_inputs:
            return self.ask_visualisation()
        
        # process user choice
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

        # prompt user for boxplot input
        choice = input("Do you want a boxplot made of the results?\nIt will open in a python window and not save unless you say so.\nY / N\n")

        # ensure proper usage
        possible_inputs = ['Y', 'YES', 'N', 'NO']
        while choice.upper() not in possible_inputs:
            return self.ask_boxplot()
        
        # process user inpit
        if choice.upper() == 'Y' or choice.upper() == 'YES':
            boxplot_option = True
        elif choice.upper() == 'N' or choice.upper() == 'NO':
            boxplot_option = False
        
        # standard choice is no boxplot
        else:
            boxplot_option = False

        return boxplot_option

    def ask_histrogram(self):
        """Asks user whether thay want a histogram made out of their results."""

        # prompt user for histogram choice
        choice = input("Do you want a histogram made of the results?\nIt will open in a python window and not save unless you say so.\nY / N\n")

        # ensure proper usage
        possible_inputs = ['Y', 'YES', 'N', 'NO']
        while choice.upper() not in possible_inputs:
            return self.ask_histrogram()
        
        # process user prompt
        if choice.upper() == 'Y' or choice.upper() == 'YES':
            histrogram_option = True
        elif choice.upper() == 'N' or choice.upper() == 'NO':
            histrogram_option = False
        
        # standard is no visualisation
        else:
            histrogram_option = False

        return histrogram_option

    def ask_iterative(self):
        """
        Asks user whether they want to perform an iterative algorithm on their results.
        Returns:    iterative.
        """

        # prompt user for iterative algorithm
        choice = input("Do you want to use an iterative algorithm on this result?\nY / N\n")

        # ensure proper usage
        possible_inputs = ['Y', 'YES', 'N', 'NO']
        while choice.upper() not in possible_inputs:
            return self.ask_iterative()
        
        # process user prompt
        if choice.upper() == 'Y' or choice.upper() == 'YES':
            iterative = True
        elif choice.upper() == 'N' or choice.upper() == 'NO':
            iterative = False
        
        # standard is no iterative algorithm
        else:
            iterative = False

        return iterative


    def perform_algorithm_multiple(self, algorithm, iterations, requested_p, boxplot_option, histrogram_option):
        """
        Performs an algorithm for a specified number of times and saves its results to a csv.
        Returns:    statistics.
        """

        # run algorithm multiple times and write its results to a csv
        statistics = descriptive(len(self.connection_objects), self.station_objects, algorithm, iterations, requested_p, self.max_minutes, self.max_routes)

        # when requested, create a boxplot
        if boxplot_option == True:
            boxplot(algorithm)

        # when requested, create a histogram
        if histrogram_option == True:
            histogram(algorithm)

        return statistics

    def perform_algorithm(self, algorithm, visualisation, requested_p):
        """
        Performs an algorithm one time with a specified p. Shows visualisation.
        Returns:    solution.
        """

        # perform the requested algoritm
        solution = algorithm(self.station_objects, len(self.connection_objects), self.max_routes, self.max_minutes, requested_p)
        solution.set_K(len(self.connection_objects))

        # when requested generate visualisation of the results
        if visualisation == True:
            self.visualise_solution(solution)

        return solution

    def perform_iterative_algorithm(self, solution):
        """
        Ask user what iterative algorithm they want to perform, and how many times.
        Then executes that algorithm on the given solution.
        Returns:    statistics.
        """

        # prompt user for iterative algorithm choice
        algorithm_choice = input("What iterative algorithm do you want to perform on the solution?\n1 = Hillclimbing\n2 = Simulated Annealing\n")
       
        # ensure proper usage
        possible_inputs = ['1', '2']
        while algorithm_choice not in possible_inputs:
            return self.perform_iterative_algorithm(solution)
    
        # prompt for amount of iterations and ensure proper usage
        while True:
            try:
                iterations_choice = int(input("How many iterations do you want in the algorithm?\n"))
                break
            except ValueError:
                print("It must be a positive integer")

        # ensure proper usage
        while iterations_choice <= 0:
            return self.perform_iterative_algorithm(solution)

        # preprocess the solution
        trimmed_solution = trim(solution)
        
        # excecute hillclimber
        if algorithm_choice == '1':
        
            hill = Hillclimber(len(self.connection_objects), self.station_objects, trimmed_solution, self.max_minutes)
            
            improved_solution = hill.run(iterations_choice)

        # else execute simulated annealing
        else:
            simulated = SimulatedAnnealing(len(self.connection_objects), self.station_objects, trimmed_solution, self.max_minutes, temperature=35)

            improved_solution = simulated.run(iterations_choice)
        
        return improved_solution

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

            # ask user whether they want iterative improvement
            iterative = self.ask_iterative()

            # perform the algorithm
            solution = self.perform_algorithm(algorithm, visualisation, requested_p)
            
            # create statistics for the runned algorithm
            statistics = self.general_output_info(solution)
            
            # show results to user
            print("Scores of this algorithm:")
            for stat in statistics:
                print(stat,":", statistics[stat])

            # when requested, perform the iterative algorithm of choice
            if iterative == True:

                improved_solution = self.perform_iterative_algorithm(solution)

                # create statistics for the runned iterative algorithm
                statistics = self.general_output_info(improved_solution)
                
                # show results to user
                print("Scores of iterative algorithm:")
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

        # ask user whether they want to perform another algorithm
        again = input("Do you want to run another algorithm on this same problem set?\nFor another problem set, please reboot the program.\nY / N\n")

        # ensure proper usage
        possible_inputs = ['Y', 'YES', 'N', 'NO']
        while again.upper() not in possible_inputs:
            again = input("Do you want to run another algorithm on this same problem set?\nFor another problem set, please reboot the program.\nY / N\n")
        
        # process user choice
        if again.upper() == 'Y' or again.upper() == 'YES':
            self.run()
        elif again.upper() == 'N' or again.upper() == 'NO':
            exit()

def clear():
    """Clears the console screen"""

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')