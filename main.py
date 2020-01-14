"""
main.py

Calls all functions in the repository 'theorie'

10/1/20

"""
from code1.classes import connection, route, station, load_data
from code1.classes.route import Route
from code1.algorithms.random import random_solution
from code1.algorithms.railhead import railhead
from code1.algorithms.shortest import shortest
from code1.algorithms.unused import unused
from random import randrange
import random
import csv, io, os

from results.random_vis import visualise


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

# creates test
coordinates_csv = os.path.join("data", "StationsNationaal.csv")
coordinates_objects = visualise.coordinates(coordinates_csv)

# adds connections to stations
connections_list = []
load_data.add_station_connection(station_objects, connection_objects)
exit()
# set railhead stations
for station in station_objects:
    station.set_rail_head()


# voer hier een algoritme uit
solution = random_solution(station_objects, connection_objects, 20, 180)
for line in solution:
    print(line)
total_time = 0
for route in solution:
    total_time += route.total_time
print(total_time)

exit()

# print("="*80)
# visualise.test_vis()