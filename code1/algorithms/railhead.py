"""
railhead.py

Starts a route with a railhead station.
When all railhead stations are used,
it selects a random station out of non-railhead stations.

@author Heuristic Heroes
@version

"""
from code1.classes.station import Station
from code1.classes.route import Route
from random import randrange
import random   

def railhead(station_objects, connection_objects):
    
    while True: 
        
        visited_connections = []
        total_time = 0
        lining = []
        available_railheads = []
        non_railhead_stations = []

        for station in station_objects:
            if station.rail_head is True:
                available_railheads.append(station)
            non_railhead_stations.append(station)
        
        # make 7 routes maximum
        for total_routes in range (7):

            # when railheads are available, pick one of these as a starting station
            if len(available_railheads) > 0:
                current_station = available_railheads[randrange(len(available_railheads))]
                
                # remove this station from the available railheads
                available_railheads.remove(current_station)
            
            # else pick a random starting station out of the non-railhead stations
            current_station = non_railhead_stations[randrange(len(non_railhead_stations))]

            # start new route
            route = Route(total_routes, current_station)

            # add route to lining
            lining.append(route)

            # keep on adding stations until maximum time has been reached 
            while True:
                
                # when all connections are used, return the lining and thus end the algorithm
                if len(connection_objects) == len(visited_connections):
                    return lining

                # pick a random new station out of all connections of the current station
                new_station = random.choice(list(current_station.connections.keys()))

                
                # find the time for the new station 
                time = int(current_station.connections[new_station])
                
                # stop adding stations until the total time would exceed 120 minutes
                if time + route.total_time > 120:
                    total_time += route.total_time
                    break
                
                # add a new station to the route
                route.add_station(new_station, time)

                # find the connection that was added
                for connection in connection_objects:
                    if (connection.station_a == current_station and connection.station_b == new_station) or (connection.station_a == new_station and connection.station_b == current_station):
                        
                        # if the connection wasn't used before, add it to the visited connections list
                        if connection in visited_connections:
                            break
                        visited_connections.append(connection)
                
                # set this new station as the current station
                current_station = new_station