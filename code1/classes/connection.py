"""
connection.py

@author Heuristic Heroes
@version
"""

class Connection(object):
    """ Creates connections between the stations. """

    def __init__(self, station_a, station_b, time):
        """ Constructor of the Connection class. """

        self.station_a = station_a
        self.station_b = station_b
        self.time = time
        self.visited = False 

    def set_visited(self, connection):
        self.visited = True

    def __str__(self):
        return f"{self.station_a} - {self.station_b}" 


     