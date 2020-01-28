"""
solution.py

Calculates the K, P and MIN for the lining.

@author Heuristic Heroes
@version 28-1-2020
"""

class Solution(object):
    """The Solution class calculates the K, P and MIN for the given lining """

    def __init__(self, lining, p):
        self.lining = lining
        self.K = 0
        self.p = 0
        self.min = 0

        for route in self.lining: 
            self.min += route.total_time
        
    def set_K(self, len_connections):
        """
        Calculates K, the quality score
        """

        self.set_p(len_connections)

        self.set_min()

        max_quality_score = 10000 

        # given formula to calculate K
        self.K = round(((self.p * max_quality_score) - (len(self.lining) * 100 + self.min)))

        return self.K

    def set_p(self, len_connections):
        """ 
        Recalculates p if the route is changed.
        """

        visited_connections = []
        
        for route in self.lining: 
            for connection in route.all_connections: 

                # check what connections have been visited               
                if connection not in visited_connections:
                    visited_connections.append(connection)

        # calculates p     
        self.p = len(visited_connections) / len_connections

        return self.p
  
    def set_min(self):
        """
        Calculates min: total time of lining.
        """

        self.min = 0
        for route in self.lining:
            self.min += route.total_time
        return self.min

    def __str__(self):
        return f"{self.K} {self.lining}"


