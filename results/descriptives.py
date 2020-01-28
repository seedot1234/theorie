"""
descriptives.py
Creates descriptive graphs such as boxplots, histograms and linecharts.
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from code1.algorithms.annealing import SimulatedAnnealing
from code1.algorithms.greedy_lookahead import greedy_lookahead
from code1.algorithms.greedy_lookahead_test import greedy_lookahead_test
from code1.algorithms.hill import Hillclimber
from code1.algorithms.longest import longest
from code1.algorithms.railhead import railhead
from code1.algorithms.random_p import random_solution_p
from code1.algorithms.shortest import shortest
from code1.algorithms.trim import trim
from code1.algorithms.unused import unused


def descriptive(len_connections, station_objects, connection_objects):
    """

    """
    # write to results.csv
    with open('results.csv', 'w', newline='') as csv_file:
        # K = kwaliteit
        fieldnames = [
            'Random', 'RandomHill', 'RandomSim', 
            'Lookahead', 'LookaheadHill', 'LookaheadSim', 
            'Shortest', 'ShortestHill', 'ShortestSim',
            'Unused', 'UnusedHill', 'UnusedSim'
        ]

        # write csv file into dictionary
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        route_maximum = 20
        time_maximum = 180

        for i in range(3):
            solution0 = random_solution_p(station_objects, len_connections, route_maximum, time_maximum)     
            # trimmed_solution0 = trim(solution0, connection_objects)
            # hill0 = Hillclimber(len_connections, station_objects, trimmed_solution0)
            # answer0 = hill0.run(1000) 
            # # simanneal0 = SimulatedAnnealing(len_connections, station_objects, solution0, temperature=35)
            # # answer00 = simanneal0.run(1000)

            # solution1 = greedy_lookahead_test(station_objects, len_connections, route_maximum, time_maximum)
            # # trimmed_solution1 = trim(solution1, connection_objects)
            # # hill1 = Hillclimber(len_connections, station_objects, trimmed_solution1)    
            # # answer1 = hill1.run(1000)
        
            # solution2 = shortest(station_objects, len_connections, route_maximum, time_maximum) 
            # # trimmed_solution2 = trim(solution2, connection_objects)
            # # hill2 = Hillclimber(len_connections, station_objects, trimmed_solution2)
            # # answer2 = hill2.run(1000)

            # solution3 = unused(station_objects, len_connections, route_maximum, time_maximum)
            # trimmed_solution3 = trim(solution5, connection_objects)
            # hill = Hillclimber(len_connections, station_objects, trimmed_solution3)
            # answer3 = hill3.run(1000)

            print(i)
            writer.writerow({
                'K0': round(solution0.set_K(len_connections), 2),# , 'KH0': answer0.K, 'KH00': answer00
                # 'K1': round(solution1.set_K(len_connections), 2), #, 'KH1': answer1.K,
                # 'K2': round(solution2.set_K(len_connections), 2), #, 'KH2': answer2.K,
                # 'K5': round(solution3.set_K(len_connections), 2), #, 'KH3': answer5.K                
            })
            
def boxplot():
    """ Creates boxplots of all algorithms """

    # load csv in dataframe
    results = pd.read_csv('results.csv')

    # create plot
    fig, axes = plt.subplots(1, 1) # (row, col)

    # put solution results in a list
    data = [ results.K0, results.K1, results.K2, results.K5
        # results.K0, results.KH0, results.K1, results.KH1, results.K2, results.KH2, results.K5, results.KH5
    ] 

    # puts data in boxplot function
    axes.boxplot(data)

    # sets plot title
    axes.set_title('Kwaliteit lijnvoering')

    # sets boxplot labels to corresponding algorithm
    axes.set_xticklabels(['Random'
        # 'Random', 'Random Hill', 'Lookahead', 'Lookahead Hill', 'Shortest', 'Shortest Hill', 'Unused', 'Unused Hill'
    ])
    print('avg: ', np.mean(results.K0))


    # show or save the plot
    plt.show()

def histogram():
    """ Creates a histogram of algorithm """

    # load csv in dataframe
    results = pd.read_csv('results.csv')

    # create histogram with K from results dataframe
    results.K2.plot.hist(grid=True, rwidth=0.9) 

    # sets labels and title
    plt.xlabel('Kwaliteit')
    plt.ylabel('Frequentie')
    plt.title('Kwaliteit lijnvoering')

    # print('max: ', max(results.K1))
    # print('min: ', min(results.K1))
    
    # show plot
    plt.show()
    # plt.savefig("out.png")



def linechart():
    """ Creates a linechart of algorithm """

    # load csv in dataframe
    results = pd.read_csv('results.csv')

    # create histogram with K from results dataframe
    results.K0.plot() 

    # sets labels and title
    plt.xlabel('Kwaliteit')
    plt.ylabel('Frequentie')
    plt.title('Kwaliteit lijnvoering: random')

    # show plot
    plt.show()

