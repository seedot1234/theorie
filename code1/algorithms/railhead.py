"""
railhead.py

Starts a route with a railhead station.
When all railhead stations are used,
it selects a random station out of non-railhead stations.

@author Heuristic Heroes
@version

"""
import random   

from code1.classes.station import Station
from code1.classes.route import Route
from code1.classes.solution import Solution
from random import randrange

def railhead(station_objects, connection_objects, route_maximum, time_maximum):
    
    # while true, reboots the attributes to find a new, valid solution
    while True: 
        
        p = 0 
        visited_connections = []
        total_time = 0
        lining = []
        available_railheads = []
        non_railhead_stations = []

        # DIT KAN VAST EENVOUDIGER (SJ)
        # checks whether a station is a railhead and adds to list, else adds it to a non-railhead list 
        for station in station_objects:
            if station.rail_head is True:
                available_railheads.append(station)
            non_railhead_stations.append(station)
                
        # make 'route_maximum' routes at max
        for route_nr in range(route_maximum):
            
            # when railheads are available, pick one of these as a starting station
            if len(available_railheads) > 0:
                current_station = available_railheads[randrange(len(available_railheads))]
                
                # remove this station from the available railheads
                available_railheads.remove(current_station)

            else:
                # else pick a random starting station out of the non-railhead stations
                current_station = non_railhead_stations[randrange(len(non_railhead_stations))]

            # start new route
            route = Route(route_nr, current_station)

            # add route to lining
            lining.append(route)

            # keep on adding stations until maximum time has been reached 
            while True:
                                 
                # p equals or is larger than 0.8, return the lining and thus end the algorithm
                if p >= 0.8:
                    solution = Solution(lining, p)
                    for route in lining:
                        print(route)
                    return solution

                # pick a random new station out of all connections of the current station
                new_station = random.choice(list(current_station.connections.keys()))

                # if new station is a railhead, remove it from list
                if new_station.rail_head and new_station in available_railheads:
                    available_railheads.remove(new_station)

                # finds the connection
                link = current_station.connections[new_station]           
                
                # find the time for the new station 
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

                # calculates p
                p = len(visited_connections) / len(connection_objects)
               
                # set this new station as the current station
                current_station = new_station
