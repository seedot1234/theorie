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
from code1.algorithms.railhead import railhead
from code1.algorithms.shortest import shortest
from code1.algorithms.hill import hillclimb
from code1.algorithms.longest import longest
from code1.algorithms.greedy_lookahead import greedy_lookahead
from code1.algorithms.hill import state
from code1.algorithms.unused import unused
from code1.algorithms.master import master
from random import randrange
import random
import csv, io, os

# VOOR HOLLAND, DOE DIT:
# creates station objects from csv
station_csv = os.path.join("data", "ConnectiesHolland.csv")
station_objects = load_data.create_station_list_holland(station_csv)

# creates connection objects from csv
connection_csv = os.path.join("data", "ConnectiesHolland.csv")
connection_objects = load_data.create_connection(connection_csv, station_objects)

# VOOR NATIONAAL, DOE DIT:
# station_csv = os.path.join("data", "StationsNationaal.csv")
# station_objects = load_data.create_station_list_nationaal(station_csv)

# # creates connection objects from csv
# connection_csv = os.path.join("data", "ConnectiesNationaal.csv")
# connection_objects = load_data.create_connection(connection_csv, station_objects)

# adds connections to stations
connections_list = []
load_data.add_station_connection(station_objects, connection_objects)

# set railhead stations
for station in station_objects:
    station.set_rail_head()
    
# TRANSLATE voer hier een algoritme uit
solution = random_solution_p(station_objects, connection_objects, 20, 180)

# calls upon the hill climbing algorithm 
hillclimb(connection_objects, station_objects, solution)
exit()

# creates list of station coordinates
# coordinates_csv = os.path.join("data", "StationsNationaal.csv")
# coordinates_objects = visualise.coordinates(coordinates_csv, solution)

# # voer hier een algoritme uit
# solution = random_solution(station_objects, connection_objects, 7, 120)

# # creates test objects from station with coordinates csv
# coordinates_csv = os.path.join("data", "TestConnecties.csv")
# coordinates_objects = visualise.coordinates(coordinates_csv, solution)

# voer hier een algoritme uit
# solution = greedy_lookahead(station_objects, connection_objects, 20, 180)
# print(solution)
# for line in solution.lining:
#     print("een trein:")
#     for station in line.stations:
#         print(station)
#     print()
# print(solution.set_K())
# exit()

# creates list of station coordinates
# coordinates_csv = os.path.join("data", "StationsNationaal.csv")
# coordinates_objects = visualise.coordinates(coordinates_csv, solution)


solution = random(station_objects, connection_objects, 7, 120)

# creates list of station coordinates
coordinates_csv = os.path.join("data", "StationsNationaal.csv")
coordinates_objects = visualise.coordinates(coordinates_csv, solution)


# total_time = 0
# total_routes = 0

# for i in range (1000):
#     for route in solution:
#         total_time += route.total_time
#     total_routes += len(solution)
#     solution = random_solution_p(station_objects, connection_objects, 20, 180)
#     print(i)

for i in range (1000):
    for route in solution:
        total_time += route.total_time
    total_routes += len(solution)
    solution = random(station_objects, connection_objects, 7, 120)
    print(i)

# print("routes aantal: ",total_routes/1000)
# print("gemiddelde total time: ", total_time / 1000)

# for line in solution:
#     print(line)
# total_time = 0
# for route in solution:
#     total_time += route.total_time
# print(total_time)
# print(solution)
# print(solution.set_K())

# exit()

# state(connection_objects, station_objects, solution)