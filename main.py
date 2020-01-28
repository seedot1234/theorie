"""
main.py
Calls all functions in the repository 'theorie'
10/1/20

"""

from code1.classes import connection, route, station, load_data
from results.visualisation import visualise
from code1.classes.route import Route
from code1.algorithms.random import random_solution
from code1.algorithms.random_p import random_solution_p
from code1.algorithms.random_k import random_solution_k
from code1.algorithms.greedy_lookahead import greedy_lookahead
from code1.algorithms.greedy_lookahead_test import greedy_lookahead_test
from code1.algorithms.trim import trim
from code1.algorithms.railhead import railhead
from code1.algorithms.shortest import shortest
from code1.algorithms.longest import longest
from code1.algorithms.unused import unused
from random import randrange
from code1.classes.solution import Solution
from code1.algorithms.hill import Hillclimber
import random
import csv, io, os
import copy
from results.bound import quality
from interface.interface import UI
from os import system, name



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
# station_csv = os.path.join("data", "ConnectiesHolland.csv")
# station_objects = load_data.create_station_list_nationaal(station_csv)

# # creates connection objects from csv
# connection_csv = os.path.join("data", "TestConnecties.csv")
# connection_objects = load_data.create_connection(connection_csv, station_objects)

# VOOR NATIONAAL, DOE DIT:
station_csv = os.path.join("data", "StationsNationaal.csv")
station_objects = load_data.create_station_list_nationaal(station_csv)

# creates connection objects from csv
connection_csv = os.path.join("data", "ConnectiesNationaal.csv")
connection_objects = load_data.create_connection(connection_csv, station_objects)


# adds connections to stations
connections_list = []
load_data.add_station_connection(station_objects, connection_objects)

# length of connections
len_connections = len(connection_objects)

# get descriptives
# descriptive(len_connections, station_objects, connection_objects)
# boxplot()


solution = unused(station_objects, connection_objects, 20, 180)

# trimmed_solution = trim(solution, connection_objects)

for i in range (250):
# calls upon the hill climbing algorithm 
    solution = unused(station_objects, connection_objects, 20, 180)
    hill = Hillclimber(len_connections, station_objects, solution)
    answer = hill.run(1000)
    print(answer.K - solution.set_K(len_connections))

# solution = unused(station_objects, connection_objects, 20, 180)