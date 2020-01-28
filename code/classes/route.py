"""
route.py

This class creates route objects

@author Heuristic Heroes
@version 28-1-2020
"""
<<<<<<< HEAD

from code.classes.connection import Connection
=======
from code1.classes.connection import Connection
>>>>>>> 6fe9d996dff9bc452b83a8828d20085ab84a4eca

class Route(object):
    """
    This class modifies routes by adding, inserting stations and connections. 
    This class can also delete connections.
    """

    def __init__(self, route_nr, current_station):

        self.number = route_nr
        self.total_time = 0 
        self.stations = [current_station]
        self.all_connections = [] 

    def add_station(self, station):
        """
        Add station to the route.
        """

        self.stations.append(station)
    
    def add_connection(self, link, time): 
        """
        Add a connection to the route with link. 
        Update total time.
        """

        self.all_connections.append(link)
        self.total_time += time

    def insert_station(self, station, index):
        """
        Insert a station to the station list given an index number.
        """

        self.stations.insert(index, station)

    def insert_connection(self, link, time, index):
        """
        Insert a connection to the connection list given an index number.
        """

        self.all_connections.insert(index, link)
        self.total_time += time

    def delete_connection(self, link, index):
        """
        Delete a given connection from the connection list.
        Update total time.
        """

        del self.all_connections[index]
        self.total_time -= link.time

    def __str__(self):
        return f"train{self.number} ({self.total_time}): {self.stations}"
