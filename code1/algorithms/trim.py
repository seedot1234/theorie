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

    for j in range (len(solution.lining)): 
        for i in range(len(solution.lining[j].all_connections)-1): 
            
            
            if solution.lining[j].all_connections[i] == solution.lining[j].all_connections[i + 1]:
                del solution.lining[j].all_connections[i]
                return trim(solution)
    
    for route in solution.lining:
        if route.total_time == 0:
            solution.lining.remove(route)
            return trim(solution)

    return solution