"""
load_data.py

@author Heuristic Heroes
@version

one file that loads all data
"""
from code1.classes.station import Station
from code1.classes.connection import Connection
import csv, io, os

def create_station_list_holland(station_csv):
    """ Create list of all stations in csv file. Gets csv file as parameter from main.py """ 

    f = open(station_csv)
    reader = csv.reader(f, delimiter = ",")

    parsed_stations = []
    station_objects = []

    # skips the first line of the csv
    next(reader)

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

def create_station_list_nationaal(station_csv):
    """ Create list of all stations in csv file. Gets csv file as parameter from main.py """ 

    f = open(station_csv)
    reader = csv.reader(f, delimiter = ",")

    station_objects = []

    # skips the first line of the csv
    next(reader)

    # iterates over the csv file 
    for row in reader:

        # create station object from the row. Fill parameters of station function with 0 = station 1 = lat 2 = lon
        station_object = Station(row[0], row[1], row[2])
        station_objects.append(station_object)  
            
    return station_objects

def create_connection(connection_csv, station_objects):
    """ Create list of all connections from csv file """

    f = open(connection_csv)
    reader = csv.reader(f, delimiter = ",")
        
    # create connection objects
    connection_objects = []

    # skips first line of csv
    next(reader)
    
    # loop over all connections
    for row in reader:
        time = float(row[2])

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

def add_station_connection(station_objects, connection_objects):
    """ Adds the connections to a station. All connections from one station. """
    
    # add connections to stations
    for station in station_objects:
        
        # for each station, loop over all connection objects
        for connection in connection_objects:

            # if the station is in the connection object, add its corresponding connected station
            if station == connection.station_a:
                station.add_connection(connection.station_b, connection.time)
            if station == connection.station_b:
                station.add_connection(connection.station_a, connection.time)

