"""
bound.py 

In this file, you'll find the all calculations made for calculating the amount of 
possible outcomes when considering the state-space and the quality function (K)

Note: the given variables values are either extracted from the dictionary Stations_objects (in main.py)
or the assignment specifications

8/1/2020

"""
import os, csv 
import pandas as pd
import math 

def state_space():
    """ displays and calculates the relevant values to find the state-space to 
        to solve the case problem """

    # number of stations extracted from the Station_objects 
    num_stations = 22 

    # maximum number of operating trains   
    max_routes = 7 

    # maximum train operating time in minutes 
    max_operating_time = 120 

    # the maximum amount of connections at a station which is True for Leiden CS, Zaandam and Amsterdam Sloterdijk
    max_connections = 4 

    df = pd.read_csv('ConnectiesHolland.csv')

    # finds the average amount of time in minutes of connections within Holland
    # avg_distance = df.Time.mean()
    # print(avg_distance)

    # finds the minimum amount of time of connections within Holland
    min_distance = df.Time.min()
    print(min_distance)

    # calculates the max. amount of stops of one route assuming the shortest distance 
    max_stops = max_operating_time / min_distance
    print(max_stops)

    # """" We assume the State-space lower bound is equal to zero """"

    # calculates the State-space upper bound (worst-case)
    print("="*50)
    UB = ((num_stations * max_connections**max_stops)**max_routes)
    print(UB)

def quality():
    """ displays and calculates the relevant values to find the highest quality score 
        in order to indicate whether a our solution is efficient and is near the maximum quality score """
    
    max_quality_score = 10000 
    
    # the sum of the distance between all connections of Holland in minutes 
    sum_distance = 381 

    # calculates the minumum amount of routes taking in account the time constraint 
    min_routes = math.ceil(sum_distance/ max_operating_time)
    print(min_routes)

    # fraction value if all connection have been passed by route(s)   
    p_max = 1

    # calculates the quality function best-case scenario 
    Best_K_Score = ((p_max * max_quality_score) - (min_routes * 100 + sum_distance))
    print(Best_K_Score)

if __name__ == "__main__":

    state_space()
    quality()