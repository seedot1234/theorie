"""
load_data.py

@author Heuristic Heroes
@version

one file that loads all data
"""
from code1.classes.station import Station
from code1.classes.connection import Connection
import csv, io, os

def create_station_list(station_csv):
    """ Create list of all stations in csv file. Gets csv file as parameter from main.py """ 

    f = open(station_csv)
    reader = csv.reader(f, delimiter = ",")

    parsed_stations = []
    station_objects = []

    # iterates over the csv file 
    for row in reader:
        # checks if station 1 is already in list, if not adds it to the list as object 
        if row[0] not in parsed_stations:
            station_object = Station(row[0])
            station_objects.append(station_object)
            parsed_stations.append(row[0])
        # checks if station 2 is already in list, if not adds it to the list as object 
        if row[1] not in parsed_stations:
            station_object = Station(row[1])
            station_objects.append(station_object)
            parsed_stations.append(row[1])

    return station_objects

def create_connection(connection_csv, station_objects):

    f = open(connection_csv)
    reader = csv.reader(f, delimiter = ",")
        
    # create connection objects
    connection_objects = []

    # loop over all connections
    for row in reader:
        time = int(row[2])

        # loop over all station objects
        for station in station_objects:

            # if the object is the same as the station in the connection, save it
            if station.name == row[0]:
                station_a = station
            if station.name == row[1]:
                station_b = station
        
        # create connection object
        connection_object = Connection(station_a, station_b, time)
        
        # save connection object in a list
        connection_objects.append(connection_object)

    return connection_objects