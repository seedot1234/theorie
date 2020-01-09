from station import *
from connection import *
from route import *
from random import randrange
import csv, io

f = open('ConnectiesHolland.csv')
reader = csv.reader(f, delimiter = ",")
stations_objects = []
connections_list = []
parsed_stations = []

# iterates over the csv file 
for row in reader:
    # checks if station 1 is already in list, if not adds it to the list as object 
    if row[0] not in parsed_stations:
        station_object = Station(row[0])
        stations_objects.append(station_object)
        parsed_stations.append(row[0])
    # checks if station 2 is already in list, if not adds it to the list as object 
    if row[1] not in parsed_stations:
        station_object = Station(row[1])
        stations_objects.append(station_object)
        parsed_stations.append(row[1])
    # adds the connection to a seperate list 
    connections_list.append(row)

# create connection objects
connection_objects = []

# loop over all connections
for connection in connections_list:
    time = int(connection[-1])

    # loop over all station objects
    for station in stations_objects:

        # if the object is the same as the station in the connection, save it
        if station.name == connection[0]:
            station_a = station
        if station.name == connection[1]:
            station_b = station
    
    # create connection object
    connection_object = Connection(station_a, station_b, time)
    
    # save connection object in a list
    connection_objects.append(connection_object)

# add connections to stations
for station in stations_objects:

    # for each station, loop over all connection objects
    for connection in connection_objects:
        # if station == connection.station_a or station == connection.station_b:
        #     station.add_connection(connection)


        # if the station is in the connection object, add its corresponding connected station
        if station == connection.station_a:
            station.add_connection(connection.station_b, connection.time)
        if station == connection.station_b:
            station.add_connection(connection.station_a, connection.time)

# set first station randomly
current_station = stations_objects[randrange(len(stations_objects))]

# start new route
route = Route(1, current_station)

# 10 stations in one route
for i in range (10):
    print("current station:", current_station.name)

    # pick a random new station out of all connections of the current station
    new_station = current_station.connections[randrange(len(current_station.connections))]

    print(new_station.keys())

    route.add_station(new_station, )
    print("new station:")
    print(new_station.name)
    print()
    
    # set this new station as the current station
    current_station = new_station




# connections = []

# csv_path = 'C:/Users/Seedot1234/Documents/Stuff/UvA/Minor_Programmeren/Opdrachten/theorie/ConnectiesHolland.csv'
# f = open(csv_path)
# reader = csv.reader(f, delimiter = ",")
# for row in reader:
#     connections.append(row)


# current_station = 'Den Helder'
# route1 = [current_station]
# used_connections = []
# total_time = 0
# for connection in connections:
#     if current_station in connection and connection not in used_connections:
#         if connection[0] == current_station:
#             route1.append(connection[1])
#         else:
#             route1.append(connection[0])

#         used_connections.append(connection)
#         total_time += int(connection[-1])
#         break
# print(total_time)
# print(route1)

# status = True

# while status == True:
#     current_station = route1[-1]
#     for connection in connections:
#         if current_station in connection and connection not in used_connections:
#             if total_time + int(connection[-1]) > 120:
#                 status = False
#                 break
#             elif connection[0] == current_station:
#                 route1.append(connection[1])
#             else:
#                 route1.append(connection[0])
#             used_connections.append(connection)
#             total_time += int(connection[-1])
#             break
#     print(total_time)
#     print(route1)

# print("nieuwe route?")
# route2 = []
# status = True
# current_station = 'Amsterdam Zuid'
# route2 = [current_station]
# used_connections = []
# total_time = 0
# for connection in connections:
#     if current_station in connection and connection not in used_connections:
#         if connection[0] == current_station:
#             route2.append(connection[1])
#         else:
#             route2.append(connection[0])

#         used_connections.append(connection)
#         total_time += int(connection[-1])
#         break
# print(total_time)
# print(route2)


# while status == True:
#     current_station = route2[-1]
#     for connection in connections:
#         if current_station in connection and connection not in used_connections:
#             if total_time + int(connection[-1]) > 120:
#                 status = False
#                 break
#             elif connection[0] == current_station:
#                 route2.append(connection[1])
#             else:
#                 route2.append(connection[0])
#             used_connections.append(connection)
#             total_time += int(connection[-1])
#             break
#     print(total_time)
#     print(route2)

# current_station = 'Amsterdam Centraal'
# possible_next_stations = []

# for connection in connections:
#     if current_station in connection:
#         possible_next_stations.append(connection)
