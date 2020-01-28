"""
station.py

Create station objects

@author Heuristic Heroes
@version 28-1-2020
"""

class Station(object):
    """
    The Station class creates station objects. Saves additional information such as its coordinates.
    """

    def __init__(self, name, lat, lon):
        
        self.name = name

        # latitude
        self.lat = lat 
        #longitude
        self.lon = lon 

        self.connections = {}
        self.rail_head = False

    def add_connection(self, destination, connection):
        """ 
        Dictionary with connections where the given destination is the key and the given connection is the value. 
        """

        self.connections[destination] = connection 

    def set_rail_head(self):
        """
        If a station only has 1 connection, set rail_head boolean to True.
        """

        if len(self.connections) == 1:
            self.rail_head = True

    def __str__(self):
        return f"{self.name}"