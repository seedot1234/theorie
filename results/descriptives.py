import csv
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np


def boxplot():

    results = pd.read_csv('results.csv')
    # results1 = pd.read_csv('results1.csv')

    # MIN = aantal minuten van alle trajecten samen, R = aantal trajecten, P = fractie bereden verbindingen, K = kwaliteit
    
    print('max: ', max(results.K))
    print('min: ', min(results.K))
    print('avg: ', np.mean(results.K))

    # old
    fig, axes = plt.subplots(1, 1) # (1, 1) = (row, col)
    axes.boxplot(results.K)
    # axes.boxplot(data)
    axes.set_title('Kwaliteit lijnvoering: random')


    # plt.savefig("out.png")
    plt.show()

    # basic plot
    # axs[0, 0].boxplot(data)
    # axs[0, 0].set_title('basic plot')

    # plt.boxplot(results.K)
    # plt.set_title("ey")

def histogram():
    results = pd.read_csv('results.csv')

    results.K.plot.hist(grid=True, rwidth=0.9) 
    plt.xlabel('Kwaliteit')
    plt.ylabel('Frequentie')
    plt.title('Kwaliteit lijnvoering: random')
    plt.show()