"""
visualise.py

@author Heuristic Heroes
@version

visualise random algorithm
"""

import json
import csv
import pandas as pd

from bokeh.io import show, output_file
from bokeh.models import HoverTool, ColumnDataSource, GMapOptions
from bokeh.plotting import figure, gmap

from code1.algorithms.random import random_solution

def coordinates(coordinates_csv): #, solution):

    testline = []
    output_file("visualise.html")

    # read csv file with pandas to abstract tabel
    reader = pd.read_csv('data/StationsNationaal.csv')
    source = ColumnDataSource(data=reader)
    # test = pd.read_csv('data/ConnectiesHolland.csv')

    # coordinates of Utrecht, because that's sort of the middle of the Netherlands
    map_options = GMapOptions(lat=52.0907374, lng=5.1214201, map_type="roadmap", zoom=7)

    # gmap function with API key
    p = gmap("AIzaSyAyJoHTODNYyRK2cTAewX4XDu9WHDoaUOI", map_options, title="Visualisatie")


    stat = reader.Station
    # print(stat)
    p.add_tools(HoverTool(tooltips=[('Station', '@stat')]))
    
    # show(p)

    # AIzaSyAyJoHTODNYyRK2cTAewX4XDu9WHDoaUOI

    # f = open(coordinates_csv)
    # reader = csv.reader(f, delimiter = ",")

    # with open(coordinates_csv, 'r') as coordinates_csv:
    #     data = json.load(coordinates_csv)

    # output_file("kaart.html")

    # for i in range(len(reader['features'])):
    #     data['features'][i]['properties']['Color'] = ['blue', 'red'][i%2]

    # geo_source = GeoJSONDataSource(geojson=json.dumps(data))

    # TOOLTIPS = [
    #     ('Organisation', '@OrganisationName')
    # ]

    # p = figure(background_fill_color="lightgrey", tooltips=TOOLTIPS)
    # p.circle(x='x', y='y', size=15, color='Color', alpha=0.7, source=geo_source)

    # show(p)
