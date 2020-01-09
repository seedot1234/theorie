"""
station.py

@author Heuristic Heroes
@version
"""


# from .connection import Connection

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
        self.connections = {}
        self.rail_head = False

    def add_connection(self, destination, time):
        self.connections[destination] = time

    def set_rail_head(self):
        # of dit moet een functie zijn die True returnt als het een railhead is?
        # misschien is dat handiger in gebruik
        if len(self.connections) == 1:
            self.rail_head = True

    def __str__(self):
        return self.name