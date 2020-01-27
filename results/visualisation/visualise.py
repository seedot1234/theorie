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
from bokeh.models import HoverTool, ColumnDataSource, GMapOptions
from bokeh.plotting import figure, show, output_file, gmap

from results.visualisation import style

def coordinates(coordinates_csv, solution):

    # read csv file with pandas to abstract tabel
    reader = pd.read_csv('data/StationsNationaal.csv')
    source = ColumnDataSource(data=reader)

    # coordinates of Utrecht, because that's sort of the middle of the Netherlands
    map_options = GMapOptions(lat=52.0907374, lng=5.1214201, map_type="terrain", zoom=7, styles=style.style_options)

    # gmap function with API key
    p = gmap("AIzaSyAyJoHTODNYyRK2cTAewX4XDu9WHDoaUOI", map_options, title="Visualisatie")

    # add circles for all stations
    p.circle(x="lon", y="lat", size=8, fill_color="blue", fill_alpha=0.8, source=source) #, legend_label="Stations")

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
    with open('stations.csv', 'w', newline='') as csv_file:
        fieldnames = ['station', 'lon', 'lat', 'color']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # for line in solution.lining:
        #     for station in line.stations:
        #         writer.writerow({'station': station})

        for i, j, k in zip(station_lon, station_lat, colors):
            show(p)
            p.line(i, j, line_width=4, line_color=k, line_alpha=0.5)
            writer.writerow({'lon': i, 'lat': j, 'color': k})

    output_file("visualise.html")

    show(p)

    # write to csv for gif
    # with open('stations.csv', 'w', newline='') as csv_file:
    #     fieldnames = ['station']
    #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #     writer.writeheader()

    #     for line in solution.lining:
    #         for station in line.stations:
    #             writer.writerow({'station': station})
