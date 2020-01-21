"""
solution.py

@author Heuristic Heroes
@version 1 
"""
# from .connection import Connection

class Solution(object):
    """The Solution object (..) """

    def __init__(self, lining, p):
                
        # makes the solution properties
        self.lining = lining
        self.K = None
        self.p = p
        self.min = 0 

        for route in self.lining: 
            self.min += route.total_time
        
    def set_K(self, len_connections):
       
        self.set_p(len_connections)

        self.set_min()

        max_quality_score = 10000 

        self.K = round(((self.p * max_quality_score) - (len(self.lining) * 100 + self.min)))
        return self.K

    def set_p(self, len_connections):
        self.visited_connections = []

        # loops over every route in the lining 
        for route in self.lining: 
            for connection in route.all_connections: 
                # checks what connections have been visited               
                if connection not in self.visited_connections:
                   self.visited_connections.append(connection)

        # calculates p   
        self.p = len(self.visited_connections) / len_connections
        print("p = ", self.p)

        return self.p
  
    def set_min(self):

        self.min = 0
        for route in self.lining:
            self.min += route.total_time
        print("min = ", self.min)




