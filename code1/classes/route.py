"""
route.py

@author Heuristic Heroes
@version
"""
from code1.classes.connection import Connection

class Route(object):
    """The Route object creates routes by chaining Connections together."""

    def __init__(self, route_nr, first_station):
        """
        Constructor of the Route class.
        Parameters: number.
        """
        # route properties
        self.number = route_nr
        self.total_time = 0 
        self.stations = [first_station]
        self.all_connections = [] 

    def add_station(self, station):
        """
        Adds a station to the route and updates the total time accordingly.
        Paramaters: station (station object), connection (connection object).
        """
        self.stations.append(station)
    
    def add_connection2(self, link, time): 
        """
        Adds a connection to the route.
        Parameters: link, time.
        """

        self.all_connections.append(link)
        self.total_time += time


    def insert_station(self, station, index):
        """
        Inserts a station to the station list,
        given an index number.
        Parameters: station, index.
        """

        self.stations.insert(index, station)


    def insert_connection(self, link, time, index):
        """
        Inserts a connection to the connection list,
        given an index number.
        Parameters: link, time, index.
        """

        self.all_connections.insert(index, link)
        self.total_time += time


    def delete_connection(self, link):
        """
        Deletes a given connection from the connection list.
        Parameters: link.
        """

        self.all_connections.remove(link)
        self.total_time -= link.time

    def __str__(self):
        return f"train{self.number} ({self.total_time}): {self.stations}"


