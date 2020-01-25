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

def trim(solution):


    for i in range (len(solution.lining)):

        route = solution.lining[i]
        for j in range(len(route.stations) - 3):
    
            if route.stations[j] == route.stations[j+2] and route.stations[j+1] == route.stations[j+3]:
                del route.stations[j+3]
                del route.stations[j+2]
                return trim(solution)

    # for j in range (len(solution.lining)): 
    #     for i in range(len(solution.lining[j].all_connections)-1): 
            
    #         if solution.lining[j].all_connections[i] == solution.lining[j].all_connections[i + 1]:
    #             del solution.lining[j].all_connections[i]
    #             return trim(solution)
    
    for route in solution.lining:
        if route.total_time == 0:
            solution.lining.remove(route)
            return trim(solution)

    return solution