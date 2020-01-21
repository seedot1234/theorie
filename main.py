"""
main.py
Calls all functions in the repository 'theorie'
10/1/20
"""
from code1.classes import connection, route, station, load_data
from results.visualisation import visualise
from results.descriptives import boxplot, histogram
from results.bound import quality
from code1.classes.route import Route
from code1.algorithms.random import random_solution
from code1.algorithms.random_p import random_solution_p
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

# set railhead stations
for station in station_objects:
    station.set_rail_head()


# voer hier een algoritme uit
solution = random_solution_p(station_objects, connection_objects, 20, 180)

len_connections = len(connection_objects)

# calls upon the hill climbing algorithm 
# hill = Hillclimber(len_connections, station_objects, solution)

# actions = {
#     'delete_first': hill.delete_first_connection
# }

# hill.run(10, hill.delete_first_connection)


# creates list of station coordinates
# coordinates_csv = os.path.join("data", "StationsNationaal.csv")
# coordinates_objects = visualise.coordinates(coordinates_csv, solution)

# # voer hier een algoritme uit
# solution = random_solution(station_objects, connection_objects, 7, 120)

# # creates test objects from station with coordinates csv
# coordinates_csv = os.path.join("data", "TestConnecties.csv")
# coordinates_objects = visualise.coordinates(coordinates_csv, solution)

# write to results.csv
with open('results.csv', 'w', newline='') as csv_file:
    # MIN = aantal minuten van alle trajecten samen, R = aantal trajecten, P = fractie bereden verbindingen, K = kwaliteit
    fieldnames = ['result_num', 'K']

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    total_time = 0
    total_routes = 0

    for i in range (50):
        for route in solution.lining:
            total_time += route.total_time
        total_routes += len(solution.lining) # num_routes = len(solution.lining) = mooier?? maar werkt niet??
        solution = random_solution_p(station_objects, connection_objects, 20, 180)
        print(i)
        writer.writerow({'result_num': i, 'K': round(solution.set_K(len_connections), 2)})
        # writer.writerow({'result_num': i, 'MIN': solution.min, 'R': len(solution.lining), 'P': round(solution.p, 2), 'K': round(solution.set_K(), 2)})




boxplot()
# histogram()



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
 
