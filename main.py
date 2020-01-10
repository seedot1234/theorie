from code1.classes import connection, route, station, load_data
from code1.classes.route import Route
from random import randrange
import random
import csv, io, os


station_csv = os.path.join("data", "ConnectiesHolland.csv")
station_objects = load_data.create_station_list(station_csv)

connection_csv = os.path.join("data", "ConnectiesHolland.csv")
connection_objects = load_data.create_connection(connection_csv, station_objects)

connections_list = []   

load_data.add_station_connection(station_objects, connection_objects)
for station in station_objects:
    print(station.connections)

for connection in connection_objects:
    print(connection)
# print(len(connection_objects))



# make new routes until all connections have been used


random_solution()