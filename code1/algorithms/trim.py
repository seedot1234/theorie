"""
trimming.py

Makes our random even better 
@author Heuristic Heroes
@version 1


"""
import copy 
from code1.classes.station import Station
from code1.classes.connection import Connection
from code1.classes.solution import Solution
from code1.classes.route import Route

def trim(solution, connection_objects):


    for i in range (len(solution.lining)):

        route = solution.lining[i]
        for j in range(len(route.stations) - 3):
    
            if route.stations[j] == route.stations[j+2] and route.stations[j+1] == route.stations[j+3]:

                # find the corresponding connection of these two stations
                selected_connection = route.all_connections[j+2]


                for station in route.stations:
                    print(station)
                for connection in route.all_connections:
                    print(connection)

                # delete this connection
                route.delete_connection(selected_connection, j+2)

                # delete the stations from the route
                del route.stations[j+3]
                del route.stations[j+2]
                
                for station in route.stations:
                    print(station)
                for connection in route.all_connections:
                    print(connection)

                return trim(solution, connection_objects)
    
    for route in solution.lining:
        if route.total_time == 0:
            solution.lining.remove(route)
            return trim(solution, connection_objects)

    return solution