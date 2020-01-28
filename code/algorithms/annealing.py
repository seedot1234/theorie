"""
hill.py

Uses the interative Hill Climbing algorithm 
@author Heuristic Heroes (Sarah-Jane)
@version 1
"""
import copy 
import random
import math 
import csv
import numpy as np

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
  
    def __init__ (self, len_connections, station_objects, solution, max_minutes, temperature):

        # uses the init of the Hillclimber class 
        super().__init__(len_connections, station_objects, solution, max_minutes)
        
        # starting temperature and current temperature
        self.iteration = 0
        self.T0 = temperature
        self.T = temperature
        # self.K = K

        self.annealing_list1 = []
        self.annealing_list2 = []
        self.all1 = []
        self.all2 = []

    def update_temperature(self):
        """
        This function implements a *linear* cooling scheme.
        Temperature will become zero after all iterations passed to the run()
        method have passed.

        """
        self.iteration += 1 

        # lineair function 
        # self.T = self.T0 - self.T0 * (self.iteration/self.iterations)
        # self.T = 0.0000001

        # # exponential function:
        # alpha = 0.99
        # self.T = self.T * alpha

        # trying something different: 
        self.T = self.T0 * 0.9935**self.iteration

    def check_solution(self, potential_solution):
        """
        Calculates new and old K, compares these and accepts new when it's better.
        Parameters: potential_solution"""
      
        old_k = self.K
        new_k = potential_solution.set_K(self.len_connections)

        # calculate the probability of accepting this change 
        delta = new_k - old_k

        if delta >= 0: 
            probability = 1
        else:
            # probability = 0 
            probability = np.exp(delta / self.T)

        # # probability = math.exp(delta / self.T)
        # print(self.iteration, "T:",self.T, "old:",old_k, "new:",new_k, "delta", delta,"P", probability)

        self.annealing_list1.append(self.iteration)
        self.annealing_list2.append(self.T)
        # pull a random number between 0 and 1 and see if we accept the graph!
        if random.random() < probability:
            # self.annealing_list1.append(self.T)
            # self.annealing_list2.append(new_k)
            # self.annealing_list1.append(self.iteration)
            # self.annealing_list2.append(new_k)
            self.state = potential_solution
            self.K = new_k
            # print(self.iteration, "T:",self.T, "old:",old_k, "new:",new_k, "delta", delta,"P", probability)


        with open('annealing.csv', 'w', newline='') as csv_file:
            fieldnames = ['Iterations', 'K']

            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for i, j in zip(self.annealing_list1, self.annealing_list2):
                writer.writerow({'Iterations': i, 'K': j})

        # Update the temperature
        self.update_temperature()

