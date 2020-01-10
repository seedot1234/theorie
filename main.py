""""
main.py 

Calls all functions in the repository 'theorie'

10/1/20

""""
from code1.classes import connection, route, station, load_data
from code1.classes.route import Route
from random import randrange
import random
import csv, io, os

<<<<<<< HEAD
# create station objects from csv
=======
>>>>>>> 05901d2c55a42860b7e9927304a8e5e5f0a02f52
station_csv = os.path.join("data", "ConnectiesHolland.csv")
station_objects = load_data.create_station_list(station_csv)

# create connection objects from csv
connection_csv = os.path.join("data", "ConnectiesHolland.csv")
connection_objects = load_data.create_connection(connection_csv, station_objects)

# add connections to stations
connections_list = []   
load_data.add_station_connection(station_objects, connection_objects)

# make new routes randomly until all connections have been used
def random_solution():
    while True:
        visited_connections = []
        total_time = 0
        for total_routes in range (7):

            # return statement that checks whether all connections have been used yet
            # if len(connection_objects) == len(visited_connections):
            #     print(total_time)
            #     return True

            # set starting station randomly
            current_station = station_objects[randrange(len(station_objects))]

            # start new route
            route = Route(total_routes, current_station)

            # keep adding stations
            while True:
                
                # putting it here makes it shorter..?
                if len(connection_objects) == len(visited_connections):
                    print(total_time)
                    return True

                # pick a random new station out of all connections of the current station
                new_station = random.choice(list(current_station.connections.keys()))
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
            
            print(route)

random_solution()