"""
visualise.py

@author Heuristic Heroes
@version

visualise algorithm
"""

import json
import csv
import pandas as pd

from bokeh.io import show, output_file
from bokeh.models import HoverTool, ColumnDataSource, GMapOptions, GeoJSONDataSource
from bokeh.plotting import figure, gmap

from code1.algorithms.random import random_solution
from code1.algorithms.random_p import random_solution_p

from bokeh.plotting import figure, show, output_file
from bokeh.tile_providers import get_provider, Vendors

from results.visualisation import style

def coordinates(coordinates_csv, solution):

    output_file("visualise.html")

    # read csv file with pandas to abstract tabel
    reader = pd.read_csv('data/StationsNationaal.csv')
    # reader = pd.read_csv('data/TestConnecties.csv')
    source = ColumnDataSource(data=reader)

    # coordinates of Utrecht, because that's sort of the middle of the Netherlands
    map_options = GMapOptions(lat=52.0907374, lng=5.1214201, map_type="terrain", zoom=7, styles=style.style_options)

    # gmap function with API key
    p = gmap("AIzaSyAyJoHTODNYyRK2cTAewX4XDu9WHDoaUOI", map_options, title="Visualisatie")

    # add circles for all stations
    p.circle(x="lon", y="lat", size=8, fill_color="blue", fill_alpha=0.8, source=source,legend_label="Stations")

    # add hovertool for station name
    p.add_tools(HoverTool(tooltips=[('Station', '@Station')]))

    # create two empty lists to store the smaller lists of coordinates in
    station_lat = [] #A
    station_lon = [] #A 
    
    # for every route in the solution
    for line in solution.lining: 
        # create new lists with the latitudes and longitudes for the routes
        route_lat = [] #B
        route_lon = []

        # for every station in the route
        for station in line.stations: 
            # put all lat and lons from route station in list.
            route_lat.append(float(station.lat)) 
            route_lon.append(float(station.lon))

        # put the smaller coordinates lists for every route in the big list 
        station_lat.append(route_lat)
        station_lon.append(route_lon)

    # list of colors for the lines
    colors = ["maroon", "deeppink", "olive", "red", "pink", "beige", "yellow", "orange", "lime", "green", "sienna", "cyan", "teal", "navy", "blue", "purple", "lavender", "magenta", "black", "dimgrey"]

    # add lines
    for i, j, k in zip(station_lon, station_lat, colors):
        p.line(i, j, line_width=4, color=k, line_alpha=0.5) 
    show(p)


# =====================

    # # add lines
    # # p.multi_line(xs='lon', ys='lat', source=source, color="red", line_width=2)
    # # p.line(test.Station_A, test.Station_B, line_width=2, color="green")
    # # p.line([reader.lon, reader.lat], line_width=2, color='green')

