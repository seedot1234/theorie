import csv
import pandas as pd
import matplotlib.pyplot as plt

from code1.algorithms.random_p import random_solution_p
from code1.algorithms.greedy_lookahead import greedy_lookahead
from code1.algorithms.trim import trim
from code1.algorithms.railhead import railhead
from code1.algorithms.shortest import shortest
from code1.algorithms.longest import longest
from code1.algorithms.unused import unused
from code1.algorithms.greedy_lookahead import greedy_lookahead
from code1.algorithms.hill import Hillclimber

# niet nodig
import numpy as np


def descriptive(len_connections, station_objects, connection_objects):
    
    # write to results.csv
    with open('results.csv', 'w', newline='') as csv_file:
        # K = kwaliteit
        fieldnames = ['K0', 'KH0', 'K1', 'KH1', 'K2', 'KH2', 'K3', 'KH3', 'K4', 'KH4']
        # write csv file into dictionary
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for i in range (1000):
            solution0 = random_solution_p(station_objects, connection_objects, 20, 180)     
            trimmed_solution0 = trim(solution0)
            hill0 = Hillclimber(len_connections, station_objects, trimmed_solution0)
            answer0 = hill0.run(1000)

            solution1 = greedy_lookahead(station_objects, connection_objects, 20, 180)
            trimmed_solution1 = trim(solution1)
            hill1 = Hillclimber(len_connections, station_objects, trimmed_solution1)
            answer1 = hill1.run(1000)

            solution2 = shortest(station_objects, connection_objects, 20, 180) #shortest
            trimmed_solution2 = trim(solution2)
            hill2 = Hillclimber(len_connections, station_objects, trimmed_solution2)
            answer2 = hill2.run(1000)

            solution3 = longest(station_objects, connection_objects, 20, 180)
            trimmed_solution3 = trim(solution1)
            hill3 = Hillclimber(len_connections, station_objects, trimmed_solution3)
            answer3 = hill3.run(1000)

            solution4 = railhead(station_objects, connection_objects, 20, 180)
            trimmed_solution4 = trim(solution1)
            hill4 = Hillclimber(len_connections, station_objects, trimmed_solution4)
            answer4 = hill1.run(1000)

            # solution5 = unused(station_objects, connection_objects, 20, 180)

            print(i)
            writer.writerow({'K0': round(solution0.set_K(len_connections), 2), 'KH0': answer0, 
                                'K1': round(solution1.set_K(len_connections), 2), 'KH1': answer1,
                                'K2': round(solution2.set_K(len_connections), 2), 'KH2': answer2, 
                                'K3': round(solution3.set_K(len_connections), 2), 'KH3': answer3, 
                                'K4': round(solution4.set_K(len_connections), 2), 'KH4': answer4}) 
                                #'K5': round(solution5.set_K(len_connections), 2)})


def boxplot():
    """ Creates boxplots of all algorithms """

    # load csv in dataframe
    results = pd.read_csv('results.csv')

    # create plot
    fig, axes = plt.subplots(1, 1) # (row, col)

    # puts solution results in a list
    data = [results.K0, results.KH0, results.K1, results.KH1, results.K2, results.KH2, results.K3, results.KH3, results.K4, results.KH4]

    # puts data in boxplot function
    axes.boxplot(data)

    # sets plot title
    axes.set_title('Kwaliteit lijnvoering: Nederland')

    # sets boxplot labels to corresponding algorithm
    axes.set_xticklabels(['Random', 'Random Hill', 'Greedy Lookahead', 'Lookahead Hill' 'Shortest', 'Shortest Hill', 'Longest', 'Longest Hill', 'Railhead', 'Railhead Hill']) #, 'Unused'])
    # axes.set_xticklabels(['Random', 'iets'])

    # show or save the plot
    plt.show()

def histogram():
    """ Creates a histogram of algorithm """

    # load csv in dataframe
    results = pd.read_csv('results.csv')

    # create histogram with K from results dataframe
    results.K0.plot.hist(grid=True, rwidth=0.9) 

    # sets labels and title
    plt.xlabel('Kwaliteit')
    plt.ylabel('Frequentie')
    plt.title('Kwaliteit lijnvoering: random')

    # show plot
    plt.show()
    # plt.savefig("out.png")




# print('max: ', max(results.K))
# print('min: ', min(results.K))
# print('avg: ', np.mean(results.K))
