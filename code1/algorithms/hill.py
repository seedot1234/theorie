"""
hill.py

Uses the interative Hill Climbing algorithm 

@author Heuristic Heroes (Sarah-Jane)
@version 1

"""
import math 
import random 

from code1.classes.station import Station
from code1.classes.connection import Connection

# the path intails the sequence of connections 
# path = 

def state(connection_objects, station_objects): 
   
    for i in station_objects:
        print(f""i.lat)
    print("="*50) 
    path = random.sample(station_objects, len(station_objects))
    for i in path:
        print(i)

    
    # print(len(connection_objects))
    # print("="*80)
    # path = random.sample(station_objects, len(station_objects))
    # for i in path:
    #     print(i)
    # print(len(test))
    # return 


# calculates the geometric distance between two stations using the Pythagorean formula
# distance = math.sqrt((lat_a - lat_b)**2 + (lon_a-lon_b)**2)
# print(distance)
