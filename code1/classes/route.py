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

    # def add_station(self, station, time):
    #     """
    #     Adds a station to the route and updates the total time accordingly.
    #     Paramaters: station (station object), connection (connection object).
    #     """
    #     self.stations.append(station)
    #     self.total_time += time

    def add_connection2(self, link, time): 

        self.all_connections.append(link)
        self.total_time += time

    def delete_connection(self, link):

        self.all_connections.remove(link)
        self.total_time -= link.time
    
    # def __getitem__(self, connection):
    #     """
    #     method which allows the Route object to support indexing         
    #     """
    #     return self.visited_connections[connection]

   
    # def __delitem__(self, connection):
    #     """
    #     method which allows the Route object to support deleting an element         
    #     """
    #     self.total_time -= self.visited_connections[connection].time
    #     del self.visited_connections[connection]

    def __str__(self):
        return f"train{self.number} ({self.total_time}): {self.stations}"


