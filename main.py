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

# for i in range(100):
#     solution1 = greedy_lookahead(station_objects, connection_objects, 20, 180)
#     print(solution1.set_K(len_connections)) # to print the K

# DESCRIPTIVES TEST!!
descriptive(len_connections, station_objects, connection_objects)
boxplot()

# # write to results.csv
# with open('results.csv', 'w', newline='') as csv_file:
#     # K = kwaliteit
#     fieldnames = ['K0', 'KH0', 'K1', 'KH1', 'K2', 'KH2', 'K3', 'KH3', 'K4', 'KH4']
#     # write csv file into dictionary
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

#     writer.writeheader()

#     for i in range (1000):
#         solution0 = random_solution_p(station_objects, connection_objects, 20, 180)     
#         trimmed_solution0 = trim(solution0)
#         hill0 = Hillclimber(len_connections, station_objects, trimmed_solution0)
#         answer0 = hill0.run(1000)

#         solution1 = greedy_lookahead(station_objects, connection_objects, 20, 180)
#         trimmed_solution1 = trim(solution1)
#         hill1 = Hillclimber(len_connections, station_objects, trimmed_solution1)
#         answer1 = hill1.run(1000)

#         solution2 = shortest(station_objects, connection_objects, 20, 180) #shortest
#         trimmed_solution2 = trim(solution2)
#         hill2 = Hillclimber(len_connections, station_objects, trimmed_solution2)
#         answer2 = hill2.run(1000)

#         solution3 = longest(station_objects, connection_objects, 20, 180)
#         trimmed_solution3 = trim(solution1)
#         hill3 = Hillclimber(len_connections, station_objects, trimmed_solution3)
#         answer3 = hill3.run(1000)

#         solution4 = railhead(station_objects, connection_objects, 20, 180)
#         trimmed_solution4 = trim(solution1)
#         hill4 = Hillclimber(len_connections, station_objects, trimmed_solution4)
#         answer4 = hill1.run(1000)

#         # solution5 = unused(station_objects, connection_objects, 20, 180)

#         print(i)
#         writer.writerow({'K0': round(solution0.set_K(len_connections), 2), 'KH0': answer0, 
#                             'K1': round(solution1.set_K(len_connections), 2), 'KH1': answer1, 
#                             'K2': round(solution2.set_K(len_connections), 2), 'KH2': answer2, 
#                             'K3': round(solution3.set_K(len_connections), 2), 'KH3': answer3, 
#                             'K4': round(solution4.set_K(len_connections), 2), 'KH4': answer4}) 
#                             #'K5': round(solution5.set_K(len_connections), 2)})

# boxplot()
# histogram()

# creates list of station coordinates VISUALISE
# coordinates_csv = os.path.join("data", "StationsNationaal.csv")
# coordinates_objects = visualise.coordinates(coordinates_csv, solution3)


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
 