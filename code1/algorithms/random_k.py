"""
random_p.py

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

# makes new routes randomly until all connections have been used
def random_solution_k(station_objects, len_connections, route_maximum, time_maximum):
    
    # while true, reboots the attributes to find a new, valid solution
    while True:
    
        K = 0
        total_time = 0
        lining = []  
        visited_connections = []

        # creates new routes until reached the max. number of routes 
        for route_nr in range(route_maximum):

            # sets starting station using random
            current_station = station_objects[randrange(len(station_objects))]
            
            # makes new route by passing the route number and current station
            route = Route(route_nr, current_station)

            # adds route to lining
            lining.append(route)
          
            # keeps on adding connections until maximum time has been reached 
            while True:
                                
                # p equals or is larger than 0.8, return the lining and thus end the algorithm
                if K >= 4000:
                    print(solution.p)
                    print(K)
                    return solution

                # picks a random new station out of all connections of the current station
                new_station = random.choice(list(current_station.connections.keys()))

                # finds the connection
                link = current_station.connections[new_station]           
                
                # finds the time for the new station 
                time = current_station.connections[new_station].time
                
                # stops adding stations until the total time would exceed the maximum time
                if time + route.total_time > time_maximum:
                    total_time += route.total_time
                    break
                             
                # adds the new connection to the route 
                route.add_connection2(link, time)

                # adds the station to the route
                route.add_station(new_station)

                # calculates what connections have been visited by the routes              
                if link not in visited_connections:
                   visited_connections.append(link)

                # calculates k
                solution = Solution(lining, None)
                K = solution.set_K(len_connections)
                                                                      
                # sets the new station as the current station
                current_station = new_station  
                
                