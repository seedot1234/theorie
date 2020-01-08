"""
connection.py

@author Heuristic Heroes
@version
"""

import station

class Connection(object):
    """ Creates connections between the stations. """

    def __init__(self, station_a, station_b, time):
        """ Constructor of the Connection class. """

        self.station_a = station_a
        self.station_b = station_b
        self.time = time
        self.visited = False 

    def set_visited(self):
        self.visitd = True