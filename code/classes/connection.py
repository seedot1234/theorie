"""
connection.py

@author Heuristic Heroes
@version
"""

from station import Station

class Connection(object):
    """ Creates connections between the stations. """

    def __init__(self, station_a, station_b, time):
        """ Constructor of the Connection class. """

        self.station_a = station_a
        self.station_b = station_b
        self.time
        self.visited = False 

        print(station_a "naar" station_b)