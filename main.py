"""
main.py

Calls all functions in the repository 'theorie'

10/1/20

"""
from code1.classes import connection, route, station, load_data
from code1.classes.route import Route
from code1.algorithms.random import random_solution
from random import randrange
import random
import csv, io, os

# creates station objects from csv
station_csv = os.path.join("data", "ConnectiesHolland.csv")
station_objects = load_data.create_station_list(station_csv)

# creates connection objects from csv
connection_csv = os.path.join("data", "ConnectiesHolland.csv")
connection_objects = load_data.create_connection(connection_csv, station_objects)

# adds connections to stations
connections_list = []
load_data.add_station_connection(station_objects, connection_objects)

# makes new routes randomly until all connections have been used
def random_solution(station_objects, connection_objects):
    while True:
        visited_connections = []
        total_time = 0
        print("="*100)

        # hier moet een lijst komen die de lijnvoering bijhoudt (lijst van Route objecten)
        for total_routes in range (7):

            # return statement that checks whether all connections have been used yet
            # if len(connection_objects) == len(visited_connections):
            #     print(total_time)
            #     return True

            # picks a random station to the start route with
            current_station = station_objects[randrange(len(station_objects))]
            print(f"Current station: {current_station}")

            # sets a shortest connection/distance variable 
            shortest = None 

            # selection sorting to order the times in ascending order 
            for connection in current_station.connections:
                print(f"Station:{connection.name}, Distance:{current_station.connections[connection]}")
                print("="*100)
            
                # sets the first connection as the shortest value 
                if shortest is None: 
                    shortest = connection
                # checks if the other connection is 
                elif current_station.connections[connection] < current_station.connections[shortest]:
                    shortest = connection 
            print(shortest)
            
            # starts new route
            route = Route(total_routes, current_station)

            # maak dit een gedefineerde while statement met een conditie ipv while True
            # keeps on adding stations until maximum time has been reached 
            while True:
                
                # putting it here makes it shorter..?
                if len(connection_objects) == len(visited_connections):
                    print(total_time)
                    # print hier de lijnvoering
                    return 'Finished'

                # vraag alle connecties op van current station
                connections = list(current_station.connections.keys())
                # print(connections)

                # connecties van station sorteren op tijd 

                # kies station met korste afstand

                # maak dit station het nieuwe station ipv random choice

            #     # picks a random new station out of all connections of the current station
            #     new_station = random.choice(list(current_station.connections.keys()))

                
            #     # finds the time for the new station 
            #     time = int(current_station.connections[new_station])
                
            #     # stops adding stations until the total time would exceed 120 minutes
            #     if time + route.total_time > 120:
            #         total_time += route.total_time

            #         # voeg Route toe aan lijnvoering lijst
            #         break
                
            #     # add a new station to the route
            #     route.add_station(new_station, time)

            #     # find the connection that was added
            #     for connection in connection_objects:
            #         if (connection.station_a == current_station and connection.station_b == new_station) or (connection.station_a == new_station and connection.station_b == current_station):
                        
            #             # if the connection wasn't used before, add it to the visited connections list
            #             if connection in visited_connections:
            #                 break
            #             visited_connections.append(connection)
                
            #     # set this new station as the current station
            #     current_station = new_station
            
            # print(route)

random_solution(station_objects, connection_objects)