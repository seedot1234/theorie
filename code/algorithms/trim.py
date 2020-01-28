"""
trim.py

Preprocesses the incoming solution by removing consecutive duplicate 
station pairs from the routes. And deletes routes that don't have any connections. 

@author Heuristic Heroes
@version 28-1-2020
"""
from code.classes.station import Station
from code.classes.connection import Connection
from code.classes.solution import Solution
from code.classes.route import Route


def trim(solution):

    for line in range (len(solution.lining)):
        route = solution.lining[line]

        for station in range(len(route.stations) - 3):
            if route.stations[station] == route.stations[station+2] and route.stations[station+1] == route.stations[station+3]:

                # find the corresponding connection of these two stations
                selected_connection = route.all_connections[station+2]

                # delete this connection twice
                route.delete_connection(selected_connection, station+2)
                route.delete_connection(selected_connection, station+1)

                # delete the stations from the route
                del route.stations[station+3]
                del route.stations[station+2]

                return trim(solution)
    
    for route in solution.lining:
        if route.total_time == 0:
            solution.lining.remove(route)
            return trim(solution)
            
    return solution