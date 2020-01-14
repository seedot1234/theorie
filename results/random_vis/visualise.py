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
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.plotting import figure

def coordinates(coordinates_csv):

    output_file("visualise.html")

    # read csv file with pandas to abstract tabel
    reader = pd.read_csv('data/StationsNationaal.csv')
    source = ColumnDataSource(data=reader)
    print(source)

    # x = longitude (lengtegraad), y = latitude (breedtegraad)
    x = reader.longitude
    y = reader.latitude

    # add plot
    p = figure(title="Visualisatie", x_axis_label="Longitude/Lengtegraad", y_axis_label="Latitude/Breedtegraad", match_aspect=True)

    # render scatterplot
    # p.circle(x="longitude", y="latitude", legend_label="Stations", line_width=4, source=source)
    p.scatter(x, y, legend_label="Stations", line_width=4)
    # p.line(x, y, line_width=2)

    stat = reader.Station
    # print(stat)
    p.add_tools(HoverTool(tooltips=[('Station', '@stat')]))
    
    show(p)

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