"""
unused.py

Picks the first station of a route randomly.
Looks up all unused connections for that station.
Picks a random station out of this list and goes there next.
When all connections are used, pick the next station randomly
out of all connections

@author Heuristic Heroes
@version

"""
from code.classes.station import Station
from code.classes.route import Route
from code.classes.solution import Solution
from random import randrange
import random  

# makes new routes randomly until all connections have been used
def unused(station_objects, len_connections, route_maximum, time_maximum, requested_p):
    while True:

        visited_connections = []
        total_time = 0
        p = 0

        # makes a list of the solution that matches the requirements 
        lining = []

        # make 'route_maximum' routes at max
        for route_nr in range(route_maximum):

            # picks a random station to the begin the route from
            current_station = station_objects[randrange(len(station_objects))]
            
            # starts new route 
            route = Route(route_nr, current_station)

            # add route to lining
            lining.append(route)

            # keeps on adding stations until maximum time has been reached 
            while True:
                
                # p equals or is larger than 0.8, return the lining and thus end the algorithm
                if p >= requested_p:
                    solution = Solution(lining, p)
                    return solution

                # make a list of all unused connections of this station
                unused_connections = []
                for connection in current_station.connections:
                    if current_station.connections[connection] not in visited_connections:
                        unused_connections.append(connection)


                # if there are unused connections, pick one randomly
                if len(unused_connections) > 0:
                    new_station = random.choice(unused_connections)
                    link = new_station 
                # if there are no unused connections, pick a random connection
                else:
                    new_station = random.choice(list(current_station.connections.keys()))

                link = current_station.connections[new_station]

                # finds the time for the new station 
                time = link.time
                
                # stops adding stations until the total time would exceed the maximum time
                if time + route.total_time > time_maximum:
                    total_time += route.total_time
                    break
                
                # add a new connection to the route
                route.add_connection2(link, time)

                # add new station to the route
                route.add_station(new_station)

                if link not in visited_connections:
                    visited_connections.append(link)    

                # calculates p
                p = len(visited_connections) / len_connections
                
                # set this new station as the current station
                current_station = new_station