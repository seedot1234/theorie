"""
pcalc.py

Calculates the p-value  

@author Heuristic Heroes
@version 1

"""

class Pcalc(object):
    """The Solution object (..) """

    def __init__(self, lining, connection_objects):
                
        self.connection_objects = connection_objects 
        self.lining = lining
        self.p = None
        self.visited_connections = []
        self.test = 10

    def set_p(self):

        # loops over every route in the lining 
        for route in self.lining: 

            for connection in route: 
                
                # checks what connections have been visited               
                if connection not in self.visited_connections:
                   self.visited_connections.append(connection)
 
        # calculates p   
        self.p = len(self.visited_connections) /  len(self.connection_objects)
               
        return self.p

    def __str__(self):
        return f"{self.p}"
  

   
        


