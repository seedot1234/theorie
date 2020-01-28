"""
annealing.py

Uses the interative Simulated Annealing algorithm 

@author Heuristic Heroes 
@version 28-1-20

"""
import random
import csv
import numpy as np

from .hillclimber import Hillclimber


class SimulatedAnnealing(Hillclimber):
    """
    The SimulatedAnnealing class makes small alterations to a random route in the solution lining. 
    Each improvement or equivalent solution is kept for the next iteration. 
    Different from HillClimber, this class sometimes accepts solutions
    that give a lower K, depending on the current temperature. 
    
    Most of the functions are similar to those of the HillClimber class, which is why 
    we use that as a parent class. 
    """
  
    def __init__ (self, len_connections, station_objects, solution, max_minutes, temperature):

        # uses the init of the Hillclimber class 
        super().__init__(len_connections, station_objects, solution, max_minutes)
        
        # starting temperature and current temperature 
        self.T0 = temperature
        self.T = temperature
        self.iteration = 0
        
        # save variables to a list 
        self.column1 = []
        self.column2 = []
  
    def update_temperature(self):
        """
        Implements a descending exponential cooling scheme. Temperature becomes 
        zero after all iterations have been passed. 
        """
        self.iteration += 1 
        self.T = self.T0 * 0.9935**self.iteration

    def check_solution(self, potential_solution):
        """
        Calculates new and old K. Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current temperature.
        """
      
        old_k = self.K
        new_k = potential_solution.set_K(self.len_connections)

        # calculate the probability of accepting this solution  
        delta = new_k - old_k
        if delta >= 0: 
            probability = 1
        probability = np.exp(delta / self.T)

        # pull a random number between 0 and 1 and see if we accept the solution
        if random.random() < probability:
            self.column1.append(self.iteration)
            self.column2.append(new_k)
            self.state = potential_solution
            self.K = new_k

        # save progress to a csv file 
        with open('annealing.csv', 'w', newline='') as csv_file:
            fieldnames = ['Iterations', 'K']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for i, j in zip(self.column1, self.column2):
                writer.writerow({'Iterations': i, 'K': j})

        # update the temperature
        self.update_temperature()