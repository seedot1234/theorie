import csv
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np


def boxplot():

    # load csv in dataframe
    results = pd.read_csv('results.csv')
    print(results)

    # MIN = aantal minuten van alle trajecten samen, R = aantal trajecten, P = fractie bereden verbindingen, K = kwaliteit
    
    # print('max: ', max(results.K))
    # print('min: ', min(results.K))
    # print('avg: ', np.mean(results.K))

    fig, axes = plt.subplots(1, 1) # (1, 1) = (row, col)
    # axes.boxplot(results.K1)
    data = [results.K1, results.K2]

    axes.boxplot(data)
    axes.set_title('Kwaliteit lijnvoering: random en shortest')

    # boxplot = df.boxplot(column=['Col1', 'Col2', 'Col3'])    


    # plt.savefig("out.png")
    plt.show()

    # basic plot
    # axs[0, 0].boxplot(data)
    # axs[0, 0].set_title('basic plot')



def histogram():
    results = pd.read_csv('results.csv')

    results.K.plot.hist(grid=True, rwidth=0.9) 
    plt.xlabel('Kwaliteit')
    plt.ylabel('Frequentie')
    plt.title('Kwaliteit lijnvoering: random')
    plt.show()