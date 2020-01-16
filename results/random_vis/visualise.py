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
from bokeh.models import HoverTool, ColumnDataSource, GMapOptions, GeoJSONDataSource
from bokeh.plotting import figure, gmap

from code1.algorithms.random import random_solution
from code1.algorithms.random_p import random_solution_p

from bokeh.plotting import figure, show, output_file
from bokeh.tile_providers import get_provider, Vendors

def coordinates(coordinates_csv, solution):

    output_file("visualise.html")

    # read csv file with pandas to abstract tabel
    reader = pd.read_csv('data/StationsNationaal.csv')
    source = ColumnDataSource(data=reader)

    # coordinates of Utrecht, because that's sort of the middle of the Netherlands
    map_options = GMapOptions(lat=52.0907374, lng=5.1214201, map_type="roadmap", zoom=7)

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
    colors = ["maroon", "brown", "olive", "red", "pink", "beige", "yellow", "orange", "lime", "green", "sienna", "cyan", "teal", "navy", "blue", "purple", "lavender", "magenta", "black", "grey"]

    # add lines
    for i, j, k in zip(station_lon, station_lat, colors):
        p.line(i, j, line_width=2, color=k)
    show(p)


# =====================
    # # box = ((reader.longitude.min(), reader.longitude.max(),      
    # #         reader.latitude.min(), reader.latitude.max())

    # # add plot
    # p = figure(title="Visualisatie", x_axis_label="Longitude/Lengtegraad", y_axis_label="Latitude/Breedtegraad", match_aspect=True)
    
    # # render scatterplot
    # p.scatter(x='lon', y='lat', legend_label="Stations", line_width=4, source=source)

    # # add hovertool for station name
    # p.add_tools(HoverTool(tooltips=[('Station', '@Station')]))

    # # x = reader.lon y = reader.lat
    # # for i in connection_objects:
    # #     print(i)

    # # add lines
    # # p.multi_line(xs='lon', ys='lat', source=source, color="red", line_width=2)
    # # p.line(test.Station_A, test.Station_B, line_width=2, color="green")
    # # p.line([reader.lon, reader.lat], line_width=2, color='green')

    # # for line in solution:
    # #     # print(line)
    # #     testline.append(line)
    # #     for station in line.stations:
    # #         # print(station)
    # #         if 'Alkmaar' in reader.Station:
    # #             print("y")
    # # print(reader)
    
            
    # print("="*80)
    # for i in testline:
    #     print(i)

    # show(p)
