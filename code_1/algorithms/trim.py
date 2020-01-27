"""
trimming.py

Makes our random even better 
@author Heuristic Heroes
@version 1


"""
import copy 
from code.classes.station import Station
from code.classes.connection import Connection
from code.classes.solution import Solution
from code.classes.route import Route

def trim(solution, connection_objects):


    for i in range (len(solution.lining)):

        route = solution.lining[i]
        for j in range(len(route.stations) - 3):
    
            if route.stations[j] == route.stations[j+2] and route.stations[j+1] == route.stations[j+3]:
                station_1 = route.stations[j+3]
                station_2 = route.stations[j+2]

                # zoek de connectie die bij deze stations hoort
                for connection in connection_objects:
                    if (connection.station_a == station_1 and connection.station_b == station_2) or (connection.station_a == station_2 and connection.station_b == station_1):
                        route.delete_connection(connection)

                # verwijder de stations uit de route
                del route.stations[j+3]
                del route.stations[j+2]
                return trim(solution, connection_objects)
    
    for route in solution.lining:
        if route.total_time == 0:
            solution.lining.remove(route)
            return trim(solution, connection_objects)

    return solution