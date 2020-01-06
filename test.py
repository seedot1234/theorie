import csv, io


connections = []

csv_path = 'C:/Users/Seedot1234/Documents/Stuff/UvA/Minor_Programmeren/Opdrachten/theorie/ConnectiesHolland.csv'
f = open(csv_path)
reader = csv.reader(f, delimiter = ",")
for row in reader:
    connections.append(row)


current_station = 'Den Helder'
route1 = [current_station]
used_connections = []
total_time = 0
for connection in connections:
    if current_station in connection and connection not in used_connections:
        if connection[0] == current_station:
            route1.append(connection[1])
        else:
            route1.append(connection[0])

        used_connections.append(connection)
        total_time += int(connection[-1])
        break
print(total_time)
print(route1)

status = True

while status == True:
    current_station = route1[-1]
    for connection in connections:
        if current_station in connection and connection not in used_connections:
            if total_time + int(connection[-1]) > 120:
                status = False
                break
            elif connection[0] == current_station:
                route1.append(connection[1])
            else:
                route1.append(connection[0])
            used_connections.append(connection)
            total_time += int(connection[-1])
            break
    print(total_time)
    print(route1)

print("nieuwe route?")
route2 = []
status = True
current_station = 'Amsterdam Zuid'
route2 = [current_station]
used_connections = []
total_time = 0
for connection in connections:
    if current_station in connection and connection not in used_connections:
        if connection[0] == current_station:
            route2.append(connection[1])
        else:
            route2.append(connection[0])

        used_connections.append(connection)
        total_time += int(connection[-1])
        break
print(total_time)
print(route2)


while status == True:
    current_station = route2[-1]
    for connection in connections:
        if current_station in connection and connection not in used_connections:
            if total_time + int(connection[-1]) > 120:
                status = False
                break
            elif connection[0] == current_station:
                route2.append(connection[1])
            else:
                route2.append(connection[0])
            used_connections.append(connection)
            total_time += int(connection[-1])
            break
    print(total_time)
    print(route2)

# current_station = 'Amsterdam Centraal'
# possible_next_stations = []

# for connection in connections:
#     if current_station in connection:
#         possible_next_stations.append(connection)
