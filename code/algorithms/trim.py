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

                # find the corresponding connection of these two stations
                selected_connection = route.all_connections[j+2]

                # delete this connection twice
                route.delete_connection(selected_connection, j+2)
                route.delete_connection(selected_connection, j+1)


                # delete the stations from the route
                del route.stations[j+3]
                del route.stations[j+2]

                return trim(solution, connection_objects)
    
    for route in solution.lining:
        if route.total_time == 0:
            solution.lining.remove(route)
            return trim(solution, connection_objects)

    return solution