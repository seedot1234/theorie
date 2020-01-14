"""
visualise.py

@author Heuristic Heroes
@version

visualise random algorithm
"""
import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
import plotly.express as px
import csv, io, os

def coordinates(coordinates_csv):

    # stations = pd.read_csv('data/TestConnecties.csv')

    # fig = px.scatter_mapbox(stations, lat="lat", lon="lon", hover_name="Station",
    #                         color_discrete_sequence=["fuchsia"], zoom=6, height=600)
    # fig.update_layout(mapbox_style="open-street-map")
    # fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    # fig.show()

    stations = pd.read_csv('data/StationsNationaal.csv')

    fig = px.scatter_mapbox(stations, lat="lat", lon="lon", hover_name="Station",
                            color_discrete_sequence=["fuchsia"], zoom=3, height=300)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    fig.show()
    
    print("sike")
    
    return 

    # for loop om marker te plotten en dan een lijn naar de volgende met matplotlib 
    # visualize traveling salesmen problem

