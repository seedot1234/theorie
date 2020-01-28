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


clear()

print("Welcome to RailNL\nPlease refer to the README for instructions as of how to use this program.")
# VRAAG NAAR WELKE MAP ZE WILLEN GEBRUIKEN
interface = UI(os.path.join("data", "StationsNationaal.csv"), os.path.join("data", "ConnectiesNationaal.csv"))
interface.run()

exit()

# VOOR HOLLAND, DOE DIT:
# creates station objects from csv
station_csv = os.path.join("data", "StationsHolland.csv")
station_objects = load_data.create_station_list(station_csv)

# creates connection objects from csv
connection_csv = os.path.join("data", "ConnectiesHolland.csv")
connection_objects = load_data.create_connection(connection_csv, station_objects)

# VOOR NATIONAAL, DOE DIT:
# station_csv = os.path.join("data", "StationsNationaal.csv")
# station_objects = load_data.create_station_list(station_csv)

# # creates connection objects from csv
# connection_csv = os.path.join("data", "ConnectiesNationaal.csv")
# connection_objects = load_data.create_connection(connection_csv, station_objects)


# adds connections to stations
connections_list = []
load_data.add_station_connection(station_objects, connection_objects)

# length of connections
len_connections = len(connection_objects)

# get descriptives
descriptive(len_connections, station_objects, connection_objects)
boxplot()
# histogram()
 
# creates list of station coordinates VISUALISE
# solution0 = random_solution_p(station_objects, connection_objects, 20, 180)     
# solution1 = greedy_lookahead(station_objects, connection_objects, 20, 180)
# solution2 = shortest(station_objects, connection_objects, 20, 180) 
# solution3 = longest(station_objects, connection_objects, 20, 180)
# solution4 = railhead(station_objects, connection_objects, 20, 180)
# solution5 = unused(station_objects, connection_objects, 20, 180)

# visualise
# coordinates_csv = os.path.join("data", "StationsNationaal.csv")
# coordinates_objects = visualise.coordinates(coordinates_csv, solution5)

# ########

# trimmed_solution = trim(solution, connection_objects)

# # calls upon the hill climbing algorithm 
# hill = Hillclimber(len_connections, station_objects, solution)
# answer = hill.run(1000)
# print(answer.K - solution.set_K(len_connections))

# solution = unused(station_objects, connection_objects, 20, 180)

# print("Setting up Simulated Annealing...")
# simanneal = SimulatedAnnealing(len_connections, station_objects, solution, temperature=35)

# # calls upon the hill climbing algorithm 
# hill = Hillclimber(len_connections, station_objects, solution)
# answer = hill.run(1000)
# print(answer.K - solution.set_K(len_connections))

# exit()


# print("Running Simulated Annealing...")
# simanneal.run(2000)


# print("K  after annealing...")
# print(simanneal.K)


# # load csv in dataframe
# results = pd.read_csv('annealing.csv')

solution = unused(station_objects, connection_objects, 20, 180)

# trimmed_solution = trim(solution, connection_objects)

for i in range (250):
# calls upon the hill climbing algorithm 
    solution = unused(station_objects, connection_objects, 20, 180)
    hill = Hillclimber(len_connections, station_objects, solution)
    answer = hill.run(1000)
    print(answer.K - solution.set_K(len_connections))

# solution = unused(station_objects, connection_objects, 20, 180)
