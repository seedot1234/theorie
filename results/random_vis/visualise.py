"""
visualise.py

@author Heuristic Heroes
@version

visualise random algorithm
"""
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# import csv, io, os

# def test_vis():

#     # read csv file with pandas to abstract tabel
#     reader = pd.read_csv('data/TestConnecties.csv')
    
#     # bounding box: the area defined by two longitudes (lengtegraad) and two latitudes (breedtegraad) that will include all spatial points
#     box = (reader.longitude.min(), reader.longitude.max(),      
#         reader.latitude.min(), reader.latitude.max())

#     # box = reader.columns
#     print(box)
#     print(reader)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def test_vis():

    fig, ax = plt.subplots()

    ax.plot([2.], [3.], 'bo')

    plt.text(  # position text relative to data
        2., 3., 'important point',  # x, y, text,
        ha='center', va='bottom',   # text alignment,
        transform=ax.transData      # coordinate system transformation
    )
    plt.text(  # position text relative to Axes
        1.0, 1.0, 'axes corner',
        ha='right', va='top',
        transform=ax.transAxes
    )
    plt.text(  # position text relative to Figure
        0.0, 1.0, 'figure corner',
        ha='left', va='top',
        transform=fig.transFigure
    )
    plt.text(  # position text absolutely at specific pixel on image
        200, 300, 'pixel (200, 300)',
        ha='center', va='center',
        transform=None
    )

    plt.show()