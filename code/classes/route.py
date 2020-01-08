"""
route.py

@author Heuristic Heroes
@version
"""

from connection import Connection

def Route(object):
    """The Route object creates routes by chaining Connections together."""

    def __init__(self, number, first_station):
        """
        Constructor of the Route class.
        Parameters: number, first_station.
        """

        # route properties
        self.number = number
        self.first_station = first_station
        self.total_time = 0 
        self.stations = [self.first_station]

    def add_station(self, station, connection):
        """
        Adds a station to the route and updates the total time accordingly.
        Paramaters: station (station object), connection (connection object).
        """

        self.stations.append(station)
        self.total_time += connection.self.time