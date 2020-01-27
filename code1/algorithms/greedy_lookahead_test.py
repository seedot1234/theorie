"""
greedy_lookahead_test.py

greedy lookahead algorithm that bases itself on the highest K score.
Looks ahead 1 extra step than a normal greedy;
looks at all possible childs from the starting point and then calculates
the K score for all options.

@author Heuristic Heroes
@version
"""

<<<<<<< HEAD
from code.classes.station import Station
from code.classes.route import Route
from code.classes.solution import Solution
=======
from code1.classes.station import Station
from code1.classes.route import Route
from code1.classes.solution import Solution
>>>>>>> 74bc6e20a60b0e7cecdf01ac17e0f923a856f8a6
from random import randrange
import random


<<<<<<< HEAD
def greedy_lookahead_test(station_objects, len_connections, route_maximum, time_maximum):
=======
def greedy_lookahead_test(station_objects, connection_objects, route_maximum, time_maximum):
>>>>>>> 74bc6e20a60b0e7cecdf01ac17e0f923a856f8a6

    while True:

        visited_connections = []
<<<<<<< HEAD
        p_per_connection = 1 / len_connections
=======
        p_per_connection = 1 / len(connection_objects)
>>>>>>> 74bc6e20a60b0e7cecdf01ac17e0f923a856f8a6
        lining = []
        p = 0

        # make 'route_maximum' routes at max
        for total_routes in range(route_maximum):

            status = False
            while status == False:

                # kies een beginstation dat nog ongebruikte connecties heeft
                current_station = station_objects[randrange(len(station_objects))]
            
                for connection in current_station.connections:
                    if current_station.connections[connection] not in visited_connections:
                        status = True

            # starts new route
            route = Route(total_routes, current_station)

            # add route to lining
            lining.append(route)

            # keeps on adding stations until maximum time has been reached 
            while True:
            
                # p equals or is larger than x, return the lining and thus end the algorithm
<<<<<<< HEAD
                if p >= 0.9:
=======
                if p >= 1:
>>>>>>> 74bc6e20a60b0e7cecdf01ac17e0f923a856f8a6
                    solution = Solution(lining, p)
                    return solution

            
                options = {}

                # loop over all possibilities for this station
                for connection in current_station.connections:

                    # for each of these options, find all their children
                    for child_connection in connection.connections:
                        
                        option = [current_station]
                        option.append(connection)
                        option.append(child_connection)

                        # find the connection that was added
                        future_connections = []

                        link1 = current_station.connections[connection]
                        link2 = connection.connections[child_connection]
                        future_connections.append(link1)
                        future_connections.append(link2)

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
<<<<<<< HEAD
                p = len(visited_connections) / len_connections
                
=======
                p = len(visited_connections) / len(connection_objects)

>>>>>>> 74bc6e20a60b0e7cecdf01ac17e0f923a856f8a6
                current_station = new_station