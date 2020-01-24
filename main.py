"""
main.py
Calls all functions in the repository 'theorie'
10/1/20
"""
from code1.classes import connection, route, station, load_data
from results.random_vis import visualise
from code1.classes.route import Route
from code1.algorithms.random import random_solution
from code1.algorithms.random_p import random_solution_p
from code1.algorithms.greedy_lookahead import greedy_lookahead
from code1.algorithms.trim import trim
from code1.algorithms.railhead import railhead
from code1.algorithms.shortest import shortest
from code1.algorithms.hill import Hillclimber
from code1.algorithms.unused import unused
from code1.algorithms.master import master
from random import randrange
import random
import csv, io, os
import copy

# VOOR HOLLAND, DOE DIT:
# creates station objects from csv
# station_csv = os.path.join("data", "ConnectiesHolland.csv")
# station_objects = load_data.create_station_list_holland(station_csv)

# # creates connection objects from csv
# connection_csv = os.path.join("data", "ConnectiesHolland.csv")
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

# set railhead stations
for station in station_objects:
    station.set_rail_head()




############################################################


len_connections = len(connection_objects)

# voer hier een algoritme uit
for i in range (100):
    solution = greedy_lookahead(station_objects, connection_objects, 20, 180)
    # print(solution.set_K(len_connections))
    trimmed_solution = trim(solution)
    print(trimmed_solution.set_K(len_connections))
    # calls upon the hill climbing algorithm 
    hill = Hillclimber(len_connections, station_objects, trimmed_solution)
    answer = hill.run(1000)

    print(answer.K)
exit()

while answer.set_K(len_connections) < 7040:
    solution = greedy_lookahead(station_objects, connection_objects, 20, 180)
    trimmed_solution = trim(solution)
    hill = Hillclimber(len_connections, station_objects, trimmed_solution)
    answer = hill.run(100)
    print(answer.K)