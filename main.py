from code1.classes import connection, route, station, load_data
from random import randrange
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

exit()




# set first station randomly
current_station = station_objects[randrange(len(station_objects))]

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
