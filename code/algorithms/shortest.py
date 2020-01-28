"""
shortest.py

Picks the first station of a route randomly.
Then goes to the shortest unused connection.
If all connections of a station have been used already,
pick a connection randomly.

@author Heuristic Heroes
@version

"""
from code.classes.station import Station
from code.classes.route import Route
from code.classes.solution import Solution
from random import randrange
import random  

# makes new routes randomly until all connections have been used
def shortest(station_objects, len_connections, route_maximum, time_maximum, requested_p):
    while True:

        p = 0
        visited_connections = []
        total_time = 0

        # makes a list of the solution that matches the requirements 
        lining = []

        # make 'route_maximum' routes at max
        for total_routes in range(route_maximum):

            # picks a random station to the begin the route from
            current_station = station_objects[randrange(len(station_objects))]
            
            # starts new route
            route = Route(total_routes, current_station)

            # add route to lining
            lining.append(route)

            # keeps on adding stations until maximum time has been reached 
            while True:
                
                # when all connections have been used, end the algorithm
                if p >= requested_p:
                    solution = Solution(lining, 1)
                    return solution

                # make a list of all unused connections of this station
                unused_connections = []
                for connection in current_station.connections:
                    if current_station.connections[connection] not in visited_connections:
                        unused_connections.append(connection)

                # if there are unused connections, find the shortest connection
                if len(unused_connections) > 0:
                    
                    # sets a shortest connection/distance variable 
                    shortest = None
                    for connection in unused_connections:
                        # connection = current_station.connections[connection]
                        if shortest is None:
                                shortest = connection

                        else:
                            if current_station.connections[connection].time < current_station.connections[shortest].time:
                                shortest = connection
                    new_station = shortest
               
                # if there are no unused connections, pick a random connection
                else:
                    new_station = random.choice(list(current_station.connections.keys()))

                # find the corresponding connection
                link = current_station.connections[new_station]

                # finds the time for the new station 
                time = link.time
                
                # stops adding stations until the total time would exceed the maximum time
                if time + route.total_time > time_maximum:
                    total_time += route.total_time
                    break

                # add the new connection to the route
                route.add_connection2(link, time)

                # add the station to the route
                route.add_station(new_station)

                # update visited connections:
                if link not in visited_connections:
                    visited_connections.append(link)
                
                # calculate p
                p = len(visited_connections) / len_connections

                # set this new station as the current station
                current_station = new_station
