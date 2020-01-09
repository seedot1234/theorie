from code1.classes import connection, route, station, load_data
from code1.classes.route import Route
from random import randrange
import random
import csv, io, os


station_csv = os.path.join("data", "ConnectiesHolland.csv")
station_objects = load_data.create_station_list(station_csv)

connection_csv = os.path.join("data", "ConnectiesHolland.csv")
connection_objects = load_data.create_connection(connection_csv, station_objects)

connections_list = []   

load_data.add_station_connection(station_objects, connection_objects)
for station in station_objects:
    print(station.connections)

for connection in connection_objects:
    print(connection)
# print(len(connection_objects))



# make new routes until all connections have been used


def functie():
    while True:
        visited_connections = []
        total_time = 0
        for total_routes in range (7):
            if len(connection_objects) == len(visited_connections):
                print(total_time)
                return True

            # set starting station randomly
            current_station = station_objects[randrange(len(station_objects))]

            # start new route
            route = Route(total_routes, current_station)

            # keep adding stations
            while True:
                # retrieve all connected stations to the current station
                
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

functie()