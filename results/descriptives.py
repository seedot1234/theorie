import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# from code1.algorithms.random_p import random_solution_p
from code1.algorithms.random_k import random_solution_k
from code1.algorithms.greedy_lookahead import greedy_lookahead
from code1.algorithms.trim import trim
from code1.algorithms.railhead import railhead
from code1.algorithms.shortest import shortest
from code1.algorithms.longest import longest
from code1.algorithms.unused import unused
from code1.algorithms.greedy_lookahead import greedy_lookahead
from code1.algorithms.hill import Hillclimber



def descriptive(len_connections, station_objects, algorithm, iterations, requested_p):
    
    # write to results.csv
    with open('results.csv', 'w', newline='') as csv_file:
        
        # K = kwaliteit
        fieldnames = ['K', 'P', 'MIN', 'R']

        # write csv file into dictionary
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for i in range (iterations):
            solution = algorithm(station_objects, len_connections, 20, 180, requested_p)     

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


def boxplot(problem, algorithm):
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
    axes.set_title(f'Kwaliteit lijnvoering: {problem}')

    # sets boxplot labels to corresponding algorithm
    axes.set_xticklabels([f'{str(algorithm)}'])
       
    # show or save the plot
    plt.show()



def histogram(problem, algorithm):
    """ Creates a histogram of algorithm """

    # load csv in dataframe
    results = pd.read_csv('results.csv')

    # create histogram with K from results dataframe
    results.K.plot.hist(grid=True, rwidth=0.9) 

    # sets labels and title
    plt.xlabel('Kwaliteit')
    plt.ylabel('Frequentie')
    plt.title(f'Kwaliteit lijnvoering: {problem} - {str(algorithm)}')

    # show plot
    plt.show()
    # plt.savefig("out.png")

# print('max: ', max(results.K))
# print('min: ', min(results.K))
# print('avg: ', np.mean(results.K))
# gemiddelde k, gemiddelde min, gemiddelde p, gemiddelde,t 