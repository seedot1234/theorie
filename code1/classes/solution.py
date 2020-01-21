"""
solution.py

@author Heuristic Heroes
@version 1 
"""
# from .connection import Connection

class Solution(object):
    """The Solution object (..) """

    def __init__(self, lining, p):
        """
        (...)
        """
        
        # makes the solution properties
        self.lining = lining 
        self.K = None
        self.p = p

        self.min = 0 

        for route in lining: 
            self.min += route.total_time
        
        self.routes = len(lining)

    def set_K(self):
        """
        (...)
        """
        max_quality_score = 10000 

        self.K = ((self.p * max_quality_score) - (self.routes * 100 + self.min))
        return self.K

    def __str__(self):
        return f"{self.K} {self.lining}"
