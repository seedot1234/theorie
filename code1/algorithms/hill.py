"""
hill.py
Uses the interative Hill Climbing algorithm 
@author Heuristic Heroes (Sarah-Jane)
@version 1
"""
import copy 
import random
from code1.classes.station import Station
from code1.classes.connection import Connection
from code1.classes.solution import Solution
from code1.classes.route import Route
from code1.classes.pcalc import Pcalc

class Hillclimber(object):
    """
    The Hillclimber class holds all functionalities to perform a
    hillclimber algorithm on a valid solution.
    """
  
    def __init__ (self, len_connections, station_objects, solution):
        """
        The constructor of the Hillclimber class.
        Parameters: len_connections, station_objects, solution
        """

        self.state = copy.deepcopy(solution)  # makes a copy of the current state 
    
        # sets the old quality value 
        self.K = self.state.set_K(len_connections)
        self.lining = []
        self.len_connections = len_connections

    def pick_random_route(self, potential_solution):
        """
        Picks a random route given a lining.
        Parameters: potential_solution.
        Returns:    route.
        """
        
        # select the route of which the first station must be deleted
        route = random.choice(potential_solution.lining)

        return route

    def pick_random_action(self):
        """
        Picks a random action out of a list of all possible actions
        this hillclimber can perform.
        These actions are:  delete first connection, delete last connection,
                            add first connection, add last connection.
        Returns:    action.
        """

        # all possible actions
        actions = [self.delete_first_connection, self.delete_last_connection, self.add_connection_beginning, self.add_connection_ending]

        # pick a random action
        action = random.choice(actions)
        return action

    def delete_first_connection(self, route):
        """
        Deletes the first connection of a given route.
        Parameters: route.
        """
        
        selected = route.all_connections[0]
        del route.stations[0]
        route.delete_connection(selected)

    def delete_last_connection(self, route):
        """
        Deletes the last connection of a given route.
        Parameters: route.
        """

        selected = route.all_connections[-1]
        route.delete_connection(selected)
        del route.stations[-1]

    def add_connection_beginning(self, route):
        """
        When possible, adds a connection to the beginning
        of a given route.
        Parameters: route.
        """

        current_station = route.stations[0]

        # picks a random new station out of all connections of the current station
        new_station = random.choice(list(current_station.connections.keys()))

        # finds the connection
        link = current_station.connections[new_station]           

        # finds the time for the new station 
        time = current_station.connections[new_station].time
        
        ### HARDCODED. DIT NOG VERANDEREN!!! ###
        # only accept the change if it wouldn't exceed the maximum time
        if time + route.total_time <= 180:
            
            # insert the connection to the front of the connection list
            route.insert_connection(link, time, 0)

            # insert the station to the front of the station list
            route.insert_station(new_station, 0)

    def add_connection_ending(self, route):
        """
        When possible, adds a connection to the end
        of a given route.
        Parameters: route.
        """

        current_station = route.stations[-1]

        # picks a random new station out of all connections of the current station
        new_station = random.choice(list(current_station.connections.keys()))

        # finds the connection
        link = current_station.connections[new_station]           

        # finds the time for the new station 
        time = current_station.connections[new_station].time
        
        ############################################
        ### HARDCODED. DIT NOG VERANDEREN!!! ###
        ############################################
        # only accept the change if it wouldn't exceed the maximum time
        if time + route.total_time <= 180:
            
            # insert the connection to the front of the connection list
            route.insert_connection(link, time, -1)

            # insert the station to the front of the station list
            route.insert_station(new_station, -1)


    def check_solution(self, potential_solution):
        """
        calculates new and old K, compares these and accepts new when it's better.
        Parameters: potential_solution"""

        old_k = self.K
        new_k = potential_solution.set_K(self.len_connections)

        # accept the new state when K is higher
        if new_k > old_k:
            self.state = potential_solution
            self.K = new_k

            # if the action resulted into an empty route, delete this route from the lining
            for route in potential_solution.lining:
                if len(route.all_connections) == 0:
                    potential_solution.lining.remove(route)
        
    def run(self, iterations):
        """
        Runs the hillclimber algorithm given an amout of iterations.
        Parameters: iterations.
        Returns:    improved_solution.
        """
        print(self.state.set_K(self.len_connections))
        for iteration in range(iterations):

            # Create a copy of the graph to simulate the change
            potential_solution = copy.deepcopy(self.state)

            # pick the route to alter
            random_route = self.pick_random_route(potential_solution)

            # pick random action to perform
            random_action = self.pick_random_action()

            # perform action
            random_action(random_route)

            # check solution and take it when it's better
            self.check_solution(potential_solution)

        improved_solution = self.state

        print(improved_solution.set_K(self.len_connections))

        return improved_solution