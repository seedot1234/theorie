"""
visualise.py

@author Heuristic Heroes
@version

visualise random algorithm
"""
# import pandas as pd
# # import matplotlib.pyplot as plt
# # import numpy as np
# import plotly.express as px
# import csv, io, os

# def coordinates(coordinates_csv):

    # # stations = pd.read_csv('data/TestConnecties.csv')

    # # fig = px.scatter_mapbox(stations, lat="lat", lon="lon", hover_name="Station",
    # #                         color_discrete_sequence=["fuchsia"], zoom=6, height=600)
    # # fig.update_layout(mapbox_style="open-street-map")
    # # fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    # # fig.show()

    # stations = pd.read_csv('data/StationsNationaal.csv')

    # fig = px.scatter_mapbox(stations, lat="lat", lon="lon", hover_name="Station",
    #                         color_discrete_sequence=["fuchsia"], zoom=3, height=300)
    # fig.update_layout(mapbox_style="open-street-map")
    # fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    # fig.show()
    
    # print("sike")
    
    # return 

    # # for loop om marker te plotten en dan een lijn naar de volgende met matplotlib 
    # # visualize traveling salesmen problem


import json
import csv
import pandas as pd

from bokeh.io import show, output_file
from bokeh.models import HoverTool, ColumnDataSource, GMapOptions
from bokeh.plotting import figure, gmap

def coordinates(coordinates_csv):

    output_file("visualise.html")


    # map_options = GMapOptions(lat=30.2861, lng=-97.7394, map_type="roadmap", zoom=11)
    # p = gmap("AIzaSyAyJoHTODNYyRK2cTAewX4XDu9WHDoaUOI", map_options, title="Austin")

    # read csv file with pandas to abstract tabel
    reader = pd.read_csv('data/StationsNationaal.csv')
    source = ColumnDataSource(data=reader)
    print(source)

    # box = ((reader.longitude.min(), reader.longitude.max(),      
    #         reader.latitude.min(), reader.latitude.max())

    # x = longitude (lengtegraad), y = latitude (breedtegraad)
    x = reader.lon
    y = reader.lat

    # add plot
    p = figure(title="Visualisatie", x_axis_label="Longitude/Lengtegraad", y_axis_label="Latitude/Breedtegraad", match_aspect=True)

    # render scatterplot
    # p.circle(x="longitude", y="latitude", legend_label="Stations", line_width=4, source=source)
    p.scatter(x='lon', y='lat', legend_label="Stations", line_width=4, source=source)
    # p.line(x, y, line_width=2)

    stat = reader.Station
    # print(stat)
    p.add_tools(HoverTool(tooltips=[('Station', '@Station')]))
    
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
