"""
main.py

Calls all functions in the repository 'theorie'

10/1/20

"""
from code1.classes import connection, route, station, load_data
from code1.classes.route import Route
from random import randrange
import random
import csv, io, os

# creates station objects from csv
station_csv = os.path.join("data", "ConnectiesHolland.csv")
station_objects = load_data.create_station_list(station_csv)

# creates connection objects from csv
connection_csv = os.path.join("data", "ConnectiesHolland.csv")
connection_objects = load_data.create_connection(connection_csv, station_objects)

# adds connections to stations
connections_list = []
load_data.add_station_connection(station_objects, connection_objects)



random_solution()