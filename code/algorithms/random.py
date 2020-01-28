
"""
random.py

@author Heuristic Heroes
@version

random algorithm
"""
from code1.classes.station import Station
from code1.classes.route import Route
from random import randrange
import random

# makes new routes randomly until all connections have been used
def random_solution(station_objects, connection_objects, route_maximum, time_maximum):
    while True:
        visited_connections = []
        total_time = 0
        lining = []

        # make 'route_maximum' routes at max
        for total_routes in range(route_maximum):

            # sets starting station randomly
            current_station = station_objects[randrange(len(station_objects))]

            # starts new route
            route = Route(total_routes, current_station)

            # add route to lining
            lining.append(route)

            # keeps on adding stations until maximum time has been reached 
            while True:
                
                # when all connections are used, return the lining and thus end the algorithm
                if len(connection_objects) == len(visited_connections):
                    return lining

                # picks a random new station out of all connections of the current station
                new_station = random.choice(list(current_station.connections.keys()))
                
                # finds the time for the new station 
                time = int(current_station.connections[new_station])
                
                # stops adding stations until the total time would exceed the maximum time
                if time + route.total_time > time_maximum:
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