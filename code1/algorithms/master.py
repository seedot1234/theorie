"""
master.py

Combines the following algorithms:
shortest, railhead

@author Heuristic Heroes
@version

"""
from code1.classes.station import Station
from code1.classes.route import Route
from random import randrange
import random  

# makes new routes randomly until all connections have been used
def master(station_objects, connection_objects, route_maximum, time_maximum):
    while True:

        visited_connections = []
        total_time = 0

        # create available (non)railhead lists
        available_railheads = []
        non_railhead_stations = []
        for station in station_objects:
            if station.rail_head is True:
                available_railheads.append(station)
            else:
                non_railhead_stations.append(station)

        # makes a list of the solution that matches the requirements 
        lining = []

        # make 'route_maximum' routes at max
        for total_routes in range(route_maximum):

            # when railheads are available, pick one of these as a starting station
            if len(available_railheads) > 0:
                current_station = available_railheads[randrange(len(available_railheads))]
                
                # remove this station from the available railheads
                available_railheads.remove(current_station)

            else:
                # else pick a random starting station out of the non-railhead stations
                current_station = non_railhead_stations[randrange(len(non_railhead_stations))]
            
            # starts new route
            route = Route(total_routes, current_station)

            # add route to lining
            lining.append(route)

            # keeps on adding stations until maximum time has been reached 
            while True:
                
                # when all connections have been used, end the algorithm
                if len(connection_objects) == len(visited_connections):
                    return lining

                # make a list of all unused connections of this station
                unused_connections = []
                for connection in current_station.connections:
                    unused_connections.append(connection)
                    for visit in visited_connections:
                        if (visit.station_a == connection and visit.station_b == current_station) or (visit.station_b == connection and visit.station_a == current_station):
                            unused_connections.remove(connection)

                # if there are unused connections, find the shortest connection
                if len(unused_connections) > 0:
                    
                    # sets a shortest connection/distance variable 
                    shortest = None
                    for connection in unused_connections:
                        if shortest is None:
                                shortest = connection
                        else:
                            if current_station.connections[connection] < current_station.connections[shortest]:
                                shortest = connection
                    new_station = shortest
               
                # if there are no unused connections, pick a random connection
                else:
                    new_station = random.choice(list(current_station.connections.keys()))

                # if new station is a railhead, remove it from list
                if new_station.rail_head and new_station in available_railheads:
                    available_railheads.remove(new_station)

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