"""
hill.py

Uses the interative Hill Climbing algorithm 
@author Heuristic Heroes (Sarah-Jane)
@version 1
"""
import copy 
import random
import math 

from .hill import Hillclimber

class SimulatedAnnealing(Hillclimber):
    """
    The SimulatedAnnealing class makes a random to a route from in the lining 
    of the solution. Each improvement or equivalent solution is kept for the next 
    iteration. Different from HillClimber, this class sometimes accepts solutions
    that give a lower K, depending on the current temperature. 
    
    Most of the functions are similar to those of the HillClimber class, which is why 
    we use that as a parent class. 
    """
  
    def __init__ (self, len_connections, station_objects, solution, temperature=1):

        # uses the init of the Hillclimber class 
        super().__init__(len_connections, station_objects, solution)
        
        # starting temperature and current temperature
        self.T0 = temperature
        self.T = temperature

    def update_temperature(self):
        """
        This function implements a *linear* cooling scheme.
        Temperature will become zero after all iterations passed to the run()
        method have passed.

        """
        self.T = self.T - (self.T0 / self.iterations)

    def check_solution(self, potential_solution):
        """
        Calculates new and old K, compares these and accepts new when it's better.
        Parameters: potential_solution"""

        old_k = self.K
        new_k = potential_solution.set_K(self.len_connections)

        # calculate the probability of accepting this change 
        delta = old_k - new_k
        probability = math.exp(-delta / self.T)

        # pull a random number between 0 and 1 and see if we accept the graph!
        if random.random() < probability:
            self.state = potential_solution
            self.k = new_k

        # Update the temperature
        self.update_temperature()