"""
descriptives.py
Creates descriptive graphs such as boxplots, histograms and linecharts.
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from code.algorithms.annealing import SimulatedAnnealing
from code.algorithms.greedy_lookahead import greedy_lookahead
from code.algorithms.hill import Hillclimber
from code.algorithms.random import random_solution
from code.algorithms.shortest import shortest
from code.algorithms.trim import trim
from code.algorithms.unused import unused


def descriptive(len_connections, station_objects, algorithm, iterations, requested_p, max_routes, max_minutes):
    """

    """
    # write to results.csv
    with open('results.csv', 'w', newline='') as csv_file:
        
        # K = kwaliteit
        fieldnames = ['K', 'P', 'MIN', 'R']

        # write csv file into dictionary
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for i in range (iterations):
            solution = algorithm(station_objects, len_connections, max_routes, max_minutes, requested_p)     

            writer.writerow(
                {
                    'K': round(solution.set_K(len_connections), 2),
                    'P': round(solution.set_p(len_connections), 4),
                    'MIN': solution.set_min(),
                    'R': len(solution.lining)
                    }
            )

    results = pd.read_csv('results.csv')

    # create a dictionary with statistic averages
    statistics = {}
    statistics['K'] = np.mean(results.K)
    statistics['R'] = np.mean(results.R)
    statistics['min'] = np.mean(results.MIN)
    statistics['p'] = np.mean(results.P)

    return statistics


def boxplot(algorithm):
    """ Creates boxplots of all algorithms """

    # load csv in dataframe
    results = pd.read_csv('results.csv')

    # create plot
    fig, axes = plt.subplots(1, 1)

    # puts solution results in a list
    data = [results.K]

    # puts data in boxplot function
    axes.boxplot(data)

    # sets plot title
    axes.set_title(f'Kwaliteit lijnvoering')

    # sets boxplot labels to corresponding algorithm
    axes.set_xticklabels([f'{str(algorithm)}'])
       
    # show or save the plot
    plt.show()



def histogram(algorithm):
    """ Creates a histogram of algorithm """

    # load csv in dataframe
    results = pd.read_csv('results.csv')

    # create histogram with K from results dataframe
    results.K.plot.hist(grid=True, rwidth=0.9) 

    # sets labels and title
    plt.xlabel('Kwaliteit')
    plt.ylabel('Frequentie')
    plt.title(f'Kwaliteit lijnvoering: {str(algorithm)}')

    # print('max: ', max(results.K1))
    # print('min: ', min(results.K1))
    
    # show plot
    plt.show()