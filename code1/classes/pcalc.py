"""
pcalc.py

Calculates the p-value  

@author Heuristic Heroes
@version 1

"""

class Pcalc(object):
    """The Solution object (..) """

    def __init__(self, lining, len_connections):
                
        self.len_connections = len_connections 
        self.lining = lining
        self.p = None

    def set_p(self):
        print("======================")
        self.visited_connections = []

        # loops over every route in the lining 
        for route in self.lining: 

            for connection in route.all_connections: 

                # checks what connections have been visited               
                if connection not in self.visited_connections:
                   self.visited_connections.append(connection)

        print("lengte visited connections:", len(self.visited_connections))

        # calculates p   
        self.p = len(self.visited_connections) / self.len_connections
               
        return self.p

    def __str__(self):
        return f"{self.p}"
  

   
        


