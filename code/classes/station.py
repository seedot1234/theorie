"""
station.py

@author Heuristic Heroes
@version
"""

from connection import Connection

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
        self.connections = []
        self.rail_head = False

    def add_connection:
        pass

    def set_rail_head(self):
        if len(self.connections) == 1:
            self.rail_head = True