"""
station.py

@author Heuristic Heroes
@version
"""

import csv, io, os

# from .connection import Connection

def create_station_list(csv_file):
    
    f = open(csv_file)
    reader = csv.reader(f, delimiter = ",")

    parsed_stations = []
    stations_objects = []

    # iterates over the csv file 
    for row in reader:
        # checks if station 1 is already in list, if not adds it to the list as object 
        if row[0] not in parsed_stations:
            station_object = Station(row[0])
            stations_objects.append(station_object)
            parsed_stations.append(row[0])
        # checks if station 2 is already in list, if not adds it to the list as object 
        if row[1] not in parsed_stations:
            station_object = Station(row[1])
            stations_objects.append(station_object)
            parsed_stations.append(row[1])


    return stations_objects


class Station(object):
    """The Station class creates stations based on the railmap csv."""

    def __init__(self, name):
        """
        Constructor of the Station class.
        Parameters: name, x_cor, y_cor.
        """

        # station properties
        self.name = name
        # self.x_cor = x_cor
        # self.y_cor = y_cor
        self.connections = {}
        self.rail_head = False

    def add_connection(self, destination, time):
        self.connections[destination] = time

    def set_rail_head(self):
        # of dit moet een functie zijn die True returnt als het een railhead is?
        # misschien is dat handiger in gebruik
        if len(self.connections) == 1:
            self.rail_head = True

    def __str__(self):
        return self.name