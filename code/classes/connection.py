"""
connection.py

In this class connection objects are made. 

@author Heuristic Heroes
@version 28-1-2020
"""

class Connection(object):
    """ 
    In this class, the connections between stations are made. 
    A connection consists of two stations and a distance in time.  
    """

    def __init__(self, station_a, station_b, time):
        """ Constructor of the Connection class. """

        self.station_a = station_a
        self.station_b = station_b
        self.time = time

    def __str__(self):
        return f"{self.station_a} - {self.station_b}"      