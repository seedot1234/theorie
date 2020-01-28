"""
load_data.py

Load data to create a list of station objects, connection objects and combines this,
so that each station has its corresponding connections.

@author Heuristic Heroes
@version 28-1-2020
"""
from code.classes.station import Station
from code.classes.connection import Connection
import csv, io, os

def create_station_list(station_csv):
    """ Create list of all stations from csv file. """ 

    # read csv file 
    f = open(station_csv)
    reader = csv.reader(f, delimiter = ",")

    # skip the first line of the csv
    next(reader)

    station_objects = []

    # iterate over every row in the csv file 
    for row in reader:

        # create station object. Fill parameters of station function with station, latitude, longitude
        station_object = Station(row[0], row[1], row[2])
        station_objects.append(station_object)  
    
    return station_objects

def create_connection(connection_csv, station_objects):
    """ Create list of all connections from csv file. """

    f = open(connection_csv)
    reader = csv.reader(f, delimiter = ",")

    next(reader)

    connection_objects = []
    
    for row in reader:
        time = float(row[2])

        # for each row in the csv file, loop over all station_objects
        for station in station_objects:
            
            # if the object from station_object is the same as the station in the connection csv, save it 
            if station.name == row[0]:
                station_a = station
            if station.name == row[1]:
                station_b = station
        
        # create connection object. Fill parameters of connection function with station_a, station_b and the connection time
        connection_object = Connection(station_a, station_b, time)
        connection_objects.append(connection_object)

    return connection_objects

def add_station_connection(station_objects, connection_objects):
    """ Adds the connections to the corresponding station. """
    
    for station in station_objects:
        
        # for each station, loop over all connection objects
        for connection in connection_objects:

            # if the station is the same as the station in connection, add the connection to the station object
            if station == connection.station_a:
                station.add_connection(connection.station_b, connection)
            if station == connection.station_b:
                station.add_connection(connection.station_a, connection)