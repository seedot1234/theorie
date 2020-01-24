import csv
import pandas as pd
import matplotlib.pyplot as plt

# niet nodig
import numpy as np




def boxplot():
    """ Creates boxplots of all algorithms """

    # load csv in dataframe
    results = pd.read_csv('results.csv')

    # create plot
    fig, axes = plt.subplots(1, 1) # (row, col)

    # puts solution results in a list
    # data = [results.K0, results.KH0, results.K1, results.K2, results.K3, results.K4, results.K5] 
    data = [results.K0, results.KH0, results.K1, results.KH1, results.K2, results.KH2, results.K3, results.KH3, results.K4, results.KH4]

    # puts data in boxplot function
    axes.boxplot(data)
    # sets plot title
    axes.set_title('Kwaliteit lijnvoering')

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
