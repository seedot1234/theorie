"""
visualise.py

@author Heuristic Heroes
@version 28-01-2020
"""

import json
import csv
import pandas as pd

from bokeh.io import show, output_file
from bokeh.models import HoverTool, ColumnDataSource, GMapOptions
from bokeh.plotting import gmap
from code.visualisation import style


def coordinates(coordinates_csv, solution):

    # read csv file with pandas to abstract tabel
    reader = pd.read_csv('data/StationsNationaal.csv')
    source = ColumnDataSource(data=reader)

    # coordinates of Utrecht, because that's sort of the middle of the Netherlands
    map_options = GMapOptions(lat=52.0907374, lng=5.1214201, map_type="terrain", zoom=7, styles=style.style_options)

    # gmap function with API key
    p = gmap("AIzaSyAyJoHTODNYyRK2cTAewX4XDu9WHDoaUOI", map_options, title="Visualisatie")

    # add circles for all stations
    p.circle(x="lon", y="lat", size=8, fill_color="blue", fill_alpha=0.8, source=source, legend_label="Stations")

    # add hovertool for station name
    p.add_tools(HoverTool(tooltips=[('Station', '@Station')]))

    station_lat = [] 
    station_lon = [] 

    for line in solution.lining: 

        route_lat = [] 
        route_lon = []

        for station in line.stations: 
            route_lat.append(float(station.lat)) 
            route_lon.append(float(station.lon))
            
        station_lat.append(route_lat)
        station_lon.append(route_lon)

    # list of colors for the lines
    colors = [
        "maroon", "deeppink", "olive", "red", "pink", "yellow", "orange", "lime", "green", "sienna", 
        "cyan", "teal", "navy", "blue", "purple", "lavender", "magenta", "black", "dimgrey", "beige"
    ]

    # draw solution lines
    for i, j, k in zip(station_lon, station_lat, colors):
        p.line(i, j, line_width=4, line_color=k, line_alpha=0.5)

    output_file("visualise.html")

    show(p)

