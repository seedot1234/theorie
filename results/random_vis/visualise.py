"""
visualise.py

@author Heuristic Heroes
@version

visualise random algorithm
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import csv, io, os

def test_vis():

    # read csv file with pandas to abstract tabel
    reader = pd.read_csv('data/TestConnecties.csv')

    print(reader)

