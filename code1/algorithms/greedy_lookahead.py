"""
greedy_lookahead.py

greedy lookahead algorithm that bases itself on the highest K score.
Looks ahead 1 extra step than a normal greedy;
looks at all possible childs from the starting point and then calculates
the K score for all options.

@author Heuristic Heroes
@version
"""

from code1.classes.station import Station
from code1.classes.route import Route
from code1.classes.solution import Solution
from random import randrange
import random


def greedy_lookahead(station_objects, connection_objects, route_maximum, time_maximum):

    while True:

        visited_connections = []
        p_per_connection = 1 / len(connection_objects)
        lining = []
        p = 0

        # make 'route_maximum' routes at max
        for route_nr in range(route_maximum):

            status = False
            while status == False:

                # kies een beginstation
                current_station = station_objects[randrange(len(station_objects))]

                # loop over connecties van dit station
                for station in current_station.connections:
                    for item in connection_objects:
                        if (item.station_a == current_station and item.station_b == station) or (item.station_a == station and item.station_b == current_station):
                            if item not in visited_connections:
                                status = True
            
            # starts new route
            route = Route(route_nr, current_station)

            # add route to lining
            lining.append(route)

            # keeps on adding stations until maximum time has been reached 
            while True:
            
                # p equals or is larger than 0.8, return the lining and thus end the algorithm
                if p >= 1:
                    solution = Solution(lining, p)
                    return solution
                
                # # when all connections are used, return the lining and thus end the algorithm
                # if len(connection_objects) == len(visited_connections):
                #     solution = Solution(lining, 1)
                #     return solution
            
                options = {}

                for connection in current_station.connections:

                    for child_connection in connection.connections:

                        for child2_connection in child_connection.connections:

                            option = [current_station]
                            option.append(connection)
                            option.append(child_connection)
                            option.append(child2_connection)

                            # find the connection that was added
                            future_connections = []

                            for item in connection_objects:
                                if (item.station_a == current_station and item.station_b == connection) or (item.station_a == connection and item.station_b == current_station):
                                    
                                    # add this connection to the future connections
                                    future_connections.append(item)

                            # find the connection that was added
                            for item in connection_objects:
                                if (item.station_a == connection and item.station_b == child_connection) or (item.station_a == child_connection and item.station_b == connection):
                                   
                                    # add this connection to the future connections
                                    future_connections.append(item)

                            # find the connection that was added
                            for item in connection_objects:
                                if (item.station_a == child_connection and item.station_b == child2_connection) or (item.station_a == child2_connection and item.station_b == child_connection):
                                   
                                    # add this connection to the future connections
                                    future_connections.append(item)


                            options[tuple(option)] = tuple(future_connections)

                possible_k = {}
                
                # bekijk alle opties
                for option in options:
                    
                    min = 0
                    p_upgrade = 0
                    k = 0

                    # per optie, bekijk iedere connectie
                    for possible_connect in options[option]:

                        # haal de tijd uit de connectie en bereken de totale tijd
                        min += possible_connect.time

                        # kijk of de connecties al bereden zijn, zo niet verhoog p
                        if possible_connect not in visited_connections:
                            p_upgrade += p_per_connection
                    
                        # bereken de k van deze optie
                        k = 10000 * p_upgrade - min
                        possible_k[option] = k

                # zoek de optie met de hoogste k
                best = None
                for possibility in possible_k:
                    if best is None:
                        best = possibility
                    else:
                        if possible_k[possibility] > possible_k[best]:
                            best = possibility
                
                # when the best option doesn't improve the score, stop adding connections to this route
                if possible_k[best] <= 0 :
                    break
                
                # when it does improve the score, define the new station
                new_station = best[1]

                # finds the connection
                link = current_station.connections[new_station]

                # finds the time for the new station
                time = int(current_station.connections[new_station].time)  
                
                # stops adding stations until the total time would exceed the maximum time
                if time + route.total_time > time_maximum:
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

                current_station = new_station