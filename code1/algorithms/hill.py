"""
hill.py
Uses the interative Hill Climbing algorithm 
@author Heuristic Heroes (Sarah-Jane)
@version 1
"""
import copy 
import random
from code1.classes.station import Station
from code1.classes.connection import Connection
from code1.classes.solution import Solution
from code1.classes.route import Route
from code1.classes.pcalc import Pcalc

class Hillclimber(object):
  
    def __init__ (self, len_connections, station_objects, solution):

        self.state = copy.deepcopy(solution)  # makes a copy of the current state 
    
        # sets the old quality value 
        self.K = self.state.set_K(len_connections)
        self.lining = []
        self.len_connections = len_connections

    def pick_random_route(self, potential_solution):
        
        # select the route of which the first station must be deleted
        route = random.choice(potential_solution.lining)

        for connection in route.all_connections:
            print(connection)
        print()
        return route

    def delete_first_connection(self, route):
        
        selected = route.all_connections[0]
        print("deleted:", selected)
        print()
        route.delete_connection(selected)

    def check_solution(self, potential_solution):
        """calculates new and old K, compares these and accepts new when it's better."""

        old_k = self.K
        new_k = potential_solution.set_K(self.len_connections)
        print("oude", old_k)
        print("nieuwe", new_k)

        # accept the new state when K is higher
        if new_k > old_k:
            self.state = potential_solution
            self.K = new_k
            print("accepted\n")
        else:
            print("not accepted\n")
        print()
        
    def run(self, iterations, action):
        for iteration in range(iterations):

            # Create a copy of the graph to simulate the change
            potential_solution = copy.deepcopy(self.state)

            # pick the route to alter
            random_route = self.pick_random_route(potential_solution)

            # perform action (delete first)
            action(random_route)
            # self.delete_first_connection(random_route)

            # check solution and take it when it's better
            self.check_solution(potential_solution)

    # # saves the improved* lining before small alteration
    # imp_lining = copy.deepcopy(copy_state.lining)
    
    # # saves the improved* route before small alteration
    # # imp_route = imp_lining[i] # ik kan deze niet in for-loop doen anders worden route en imp-route aan elkaar gelijk??
    
    # # iterates over every route and connection within that route from the original solution
    # for i, route in enumerate(copy_state.lining):  
            
    #     # saves the improved* route before small alteration
    #     imp_route = imp_lining[i]
                
    #     # resets boolean that checks whether to move to the next route 
    #     next = False 
                      
    #     # continues making alterations until  K doesn't improve or the route is empty 
    #     while next is False: 

    #         # deletes the first connection from the route     
    #         deleted_time = imp_route.all_connections[0].time
    #         del imp_route.all_connections[0]

    #         # calculates the old P 
    #         oldP = Pcalc(copy_state.lining, len_connections)
    #         oldPP = oldP.set_p()

    #         # calculates the new P 
    #         temp = Pcalc(imp_lining, len_connections)
    #         p = temp.set_p()

    #         # calculates the new solution after the alteration
    #         diff_solution = Solution(imp_lining, p) 


    #         diff_solution.min -= deleted_time

    #         # calculates the new K value 
    #         new_K = diff_solution.set_K()

    #         # removes the route from the lining if empty
    #         if len(route.all_connections) == 0:
    #             next = True                

    #         else:
    #             if new_K <= old_K:
    #                 lining.append(route)
    #                 # copy_state.lining = imp_lining # doesnt work ???
    #                 next = True

    #             else:
    #                 # if the alteration decreases K, declines the improvement and move to the next route 
    #                 del route.all_connections[0]
    #                 old_K = new_K

    #     for route in lining:            
    #         if len(route.all_connections) == 0:
    #             lining.remove(route)