"""
longest.py

Picks the first station of a route randomly.
Then goes to the longest unused connection.
If all connections of a station have been used already,
pick a connection randomly.

@author Heuristic Heroes
@version

"""
from code1.classes.station import Station
from code1.classes.route import Route
from code1.classes.solution import Solution
from random import randrange
import random  

# makes new routes randomly until all connections have been used
def longest(station_objects, connection_objects, route_maximum, time_maximum):
    while True:

        visited_connections = []
        total_time = 0

        # makes a list of the solution that matches the requirements 
        lining = []

        # make 'route_maximum' routes at max
        for route_nr in range(route_maximum):

            # picks a random station to the begin the route from
            current_station = station_objects[randrange(len(station_objects))]
            
            # starts new route | SJ: WAT DOET DIT? 
            route = Route(route_nr , current_station)

            # add route to lining
            lining.append(route)

            # keeps on adding stations until maximum time has been reached 
            while True:
                
                # when all connections have been used, end the algorithm
                if len(connection_objects) == len(visited_connections):
                    solution = Solution(lining, 1)
                    return solution
                    # return lining

                # make a list of all unused connections of this station
                unused_connections = []

                for connection in connection_objects:
                    if connection not in visited_connections:
                        unused_connections.append(connection)

                # if there are unused connections, find the shortest connection
                if len(unused_connections) > 0:
                    
                    # sets a shortest connection/distance variable 
                    longest = None
                    for connection in unused_connections:
                        if longest is None:
                                longest = connection
                        else:
                            if connection.time > longest.time:
                                longest = connection
                    new_connection = longest
               
                # if there are no unused connections, pick a random connection
                else:
                    new_connection = random.choice(list(current_station.connections.keys()))

                link = connection

                # finds the time for the new station 
                time = connection.time
                
                # stops adding stations until the total time would exceed the maximum time
                if time + route.total_time > time_maximum:
                    total_time += route.total_time
                    break
                
                # add a new station to the route
                route.add_connection2(link, time)

                if link not in visited_connections:
                    visited_connections.append(link)

                current_station = new_connection