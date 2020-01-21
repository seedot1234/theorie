"""
hill.py

Uses the interative Hill Climbing algorithm in order to remove the first connection 
from the route to improve the K score. 

@author Heuristic Heroes (Sarah-Jane)
@version 1

"""
import copy 

from code1.classes.station import Station
from code1.classes.connection import Connection
from code1.classes.solution import Solution
from code1.classes.route import Route
from code1.classes.pcalc import Pcalc

def hillclimb_first(connection_objects, station_objects, solution):
  
    # picks a valid random start state (taken from random_p.py)
    state = solution 
                    
    # makes a copy of the current state 
    copy_state = copy.deepcopy(solution) 

    # sets the old quality value 
    old_K = copy_state.set_K()
    lining = []
    i = 0 

    # saves the improved* lining before small alteration
    imp_lining = copy.deepcopy(copy_state.lining)
    
    # iterates over every route and connection within that route from the original solution
    for i, route in enumerate(copy_state.lining):  
            
        # saves the improved* route before small alteration
        imp_route = imp_lining[i]
                
        # resets boolean that checks whether to move to the next route 
        next = False 
                     
        # continues making alterations until  K doesn't improve or the route is empty 
        while next is False: 

            # deletes the first connection from the route
            del imp_route[0]
        
            # calculates the new P 
            temp = Pcalc(imp_lining, connection_objects)
            p = temp.set_p()

            # calculates the new solution after the alteration
            diff_solution = Solution(imp_lining, p) 
                    
            # calculates the new K value 
            new_K = diff_solution.set_K()
                                    
            # removes the route from the lining if empty
            if len(route.visited_connections) == 0:
                print(f"Route {route.number} Is Empty")
                next = True                 

            elif new_K > old_K:
                route = imp_route # doesn't work ???
                old_K = new_K
                
            # if the alteration decreases K, declines the improvement and move to the next route 
            elif new_K <= old_K: 
                new_K = old_K
                lining.append(route)
                # copy_state.lining = imp_lining # doesnt work ???
                next = True  

        for route in lining:            
            if len(route.visited_connections) == 0:
                lining.remove(route)

    
       
        

        
                
