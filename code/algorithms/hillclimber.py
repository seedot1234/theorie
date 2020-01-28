"""
hillclimber.py

Uses the interative Hill Climbing algorithm 

@author Heuristic Heroes 
@version 28-1-20
"""
import copy 
import random

from code.classes.connection import Connection
from code.classes.station import Station
from code.classes.solution import Solution
from code.classes.route import Route


class Hillclimber(object):
    """
    The HillClimber class uses a constructive valid solution that meets all constraints. 
    Then it makes random alterations to a random routes. Alterations consist of: 
    removing the first or last connection, and adding a first or last 
    connection. Each improvement or equivalent solution is kept for the next iteration.
    """
  
    def __init__ (self, len_connections, station_objects, solution, max_minutes):
        """
        The constructor of the Hillclimber class.
        """

        self.len_connections = len_connections
        self.station_objects = station_objects
        self.state = copy.deepcopy(solution)  
        self.K = self.state.set_K(len_connections)
        self.lining = []
        self.max_minutes = max_minutes
       

    def pick_random_route(self, potential_solution):
        """
        Pick and return a random route given a lining.
        """
        route = random.choice(potential_solution.lining)
        return route

    def pick_random_action(self):
        """
        Picks a random action out of a list of all possible action 
        hillclimber can perform.
        """

        actions = [self.delete_first_connection, self.delete_last_connection, self.add_connection_beginning, self.add_connection_ending]
        action = random.choice(actions)
        return action

    def delete_first_connection(self, route, potential_solution):
        """
        Deletes the first station and connection of a given route.
        """
        
        selected = route.all_connections[0]

        # delete the entire route if there is a single connection left 
        if len(route.all_connections) == 1:
            potential_solution.lining.remove(route)
        del route.stations[0]
        route.delete_connection(selected, 0)

    def delete_last_connection(self, route, potential_solution):
        """
        Deletes the last station and connection of a given route.
        """
        
        selected = route.all_connections[-1]

        if len(route.all_connections) == 1:
            potential_solution.lining.remove(route)
        del route.stations[-1]
        route.delete_connection(selected, -1)

    def add_connection_beginning(self, route, potential_solution):
        """
        When possible, adds a connection to the beginning
        of a given route.
        """

        current_station = route.stations[0]

        # pick a random new station out of all connections of the current station
        new_station = random.choice(list(current_station.connections.keys()))

        # find the connection between the two stations 
        link = current_station.connections[new_station]           

        # find the time of the connection 
        time = link.time 
        

        # only accept the change if it wouldn't exceed the maximum time
        if time + route.total_time <= self.max_minutes:
            
            # insert the connection to the front of the connection list
            route.insert_connection(link, time, 0)

            # insert the station to the front of the station list
            route.insert_station(new_station, 0)

    def add_connection_ending(self, route, potential_solution):
        """
        When possible, adds a connection to the end
        of a given route.
        """

        current_station = route.stations[-1]
        new_station = random.choice(list(current_station.connections.keys()))
        link = current_station.connections[new_station]           
        time = link.time 
        

        # only accept the change if it wouldn't exceed the maximum time
        if time + route.total_time <= self.max_minutes:
            
            # insert the connection to the front of the connection list
            route.insert_connection(link, time, -1)

            # insert the station to the front of the station list
            route.insert_station(new_station, -1)


    def check_solution(self, potential_solution):
        """
        calculates new and old K, compares these and accepts new when it's better.
        """

        old_k = self.K
        new_k = potential_solution.set_K(self.len_connections)

        # accept the new state when K is higher
        if new_k > old_k:
            self.state = potential_solution
            self.K = new_k
        
    def run(self, iterations):
        """
        Runs the hillclimber algorithm given an amout of iterations
        and returns the improved solution. 
        """

        self.iterations = iterations 
        
        for iteration in range(self.iterations):
            
            # create a copy of the solution to simulate the change
            potential_solution = copy.deepcopy(self.state)

            random_route = self.pick_random_route(potential_solution)        
            random_action = self.pick_random_action()

            # perform action
            random_action(random_route, potential_solution)
            self.check_solution(potential_solution)

        improved_solution = self.state
        return improved_solution