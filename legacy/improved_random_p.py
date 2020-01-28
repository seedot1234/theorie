"""
improved_random_p.py

Completely random, but stops when P is at least 80%,
instead of 100.

@author Heuristic Heroes
@version

random algorithm
"""
import random

from code1.classes.station import Station
from code1.classes.route import Route
from random import randrange
from code1.classes.solution import Solution


class Random_solution_p(object):
    """
    The Random_solution_p class is a constructive algorithm that finds a solution that meets all constraints. 
    as creating solution with the maximum number of routes and the maximum amount of time per route. 
    
    Our initial idea was to use this class as a parent and use it for the other constructive algorithms such as 
    random, railhead and shortest. Which would reduce duplication. Due to time-constraints we weren't able to do so. 
    """ 

    def __init__(self, station_objects, len_connections, route_maximum, time_maximum):
        
        self.station_objects = station_objects
        self.len_connections = len_connections
        self.route_maximum = route_maximum
        self.time_maximum = time_maximum 
 
    def create_route(self):
        
        # set a starting station using random
        self.current_station = self.station_objects[randrange(len(self.station_objects))]

        # make new route by passing the route number and current station
        route = Route(self.route_nr, self.current_station)

        # add route to lining
        self.lining.append(route)
        return route

    def pick_connection(self, route): 
        
        # pick a random new station out of all connections of the current station
        self.new_station = random.choice(list(self.current_station.connections.keys()))

        # find the connection object 
        self.link = self.current_station.connections[self.new_station]           
        
        # find the time for the connection object  
        self.time = self.link.time

    def check_time(self, route): 

        # stop adding stations until the total time would exceed the maximum time
        if route.total_time + self.time >= self.time_maximum or route.total_time >= self.time_maximum: 
            self.total_time = 0
            return True        
        return False

    def add_connection(self, route): 

        # add the new connection to the route 
        route.add_connection2(self.link, self.time)

        # add the station to the route
        route.add_station(self.new_station)
        self.total_time += self.time
        self.time = 0 

        # check what connections have been visited by the routes              
        if self.link not in self.visited_connections:
            self.visited_connections.append(self.link)

    def calc_p(self): 
        
        self.p = len(self.visited_connections) / 89
        return self.p

    def check_p(self): 

        if self.p >= 0.8:
            self.solution = Solution(self.lining, self.p)
            return True
        return False
        
    def update_station(self):
        
        self.current_station = self.new_station 
        return self.current_station

    def run(self):

        # while true, reboots the attributes to find a new, valid solution            
        self.lining = []
        self.visited_connections = []
        self.total_time = 0 
        self.p = 0 
        self.time = 0

        for self.route_nr in range(self.route_maximum):

            route = self.create_route()
            check_p = self.check_p()

            # keeps on adding connections until maximum time has been reached 
            while self.check_time(route) is False:
                pick_connection = self.pick_connection(route)       
                
                if self.check_time(route) is False: 
                    add_connection = self.add_connection(route)
                    update = self.update_station()
                    calc_p = self.calc_p()
        self.solution = Solution(self.lining, self.p)
        return self.solution