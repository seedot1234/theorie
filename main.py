"""
main.py
Calls all functions in the repository 'theorie'
10/1/20
"""
import csv, os

from code1.classes import connection, route, station, load_data
from results.visualisation import visualise
from code1.classes.route import Route
from code1.algorithms.random import random_solution
from code1.algorithms.random_p import random_solution_p
from code1.algorithms.greedy_lookahead import greedy_lookahead
from code1.algorithms.trim import trim
from code1.algorithms.railhead import railhead
from code1.algorithms.shortest import shortest
from code1.algorithms.longest import longest
from code1.algorithms.unused import unused
from code1.algorithms.greedy_lookahead import greedy_lookahead
from code1.algorithms.hill import Hillclimber

# nodig?
from results.bound import quality
from results.descriptives import boxplot, histogram
from results.descriptives import descriptive

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
descriptive(len_connections, station_objects, connection_objects)
boxplot()

##################

# creates list of station coordinates VISUALISE
# solution0 = random_solution_p(station_objects, connection_objects, 20, 180)     
# solution1 = greedy_lookahead(station_objects, connection_objects, 20, 180)
# solution2 = shortest(station_objects, connection_objects, 20, 180) 
# solution3 = longest(station_objects, connection_objects, 20, 180)
# solution4 = railhead(station_objects, connection_objects, 20, 180)
# solution5 = unused(station_objects, connection_objects, 20, 180)

# visualise
# coordinates_csv = os.path.join("data", "StationsNationaal.csv")
# coordinates_objects = visualise.coordinates(coordinates_csv, solution1)


# for i in range(100):
#     solution1 = greedy_lookahead(station_objects, connection_objects, 20, 180)
#     print(solution1.set_K(len_connections)) # to print the K

# for i in range (100):
#     for route in solution.lining:
#         total_time += route.total_time
#     total_routes += len(solution.lining)
#     solution = random_solution_p(station_objects, connection_objects, 20, 180)
#     print(i)
#     print('total time: ', route.total_time)

# 1 keer indenten is per stap
# tot_routes = total_routes / 100
# avg_time = total_time / 100
# print("routes aantal: ",tot_routes)
# print("gemiddelde total time: ", avg_time) 
# check bound voor k. van kwaliteit een boxplot maken

# for line in solution:
#     print(line)

# total_time = 0
# for route in solution:
#     total_time += route.total_time
# print(total_time)
 