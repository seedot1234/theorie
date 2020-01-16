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
from code1.algorithms.random_p import random_solution_p

def coordinates(coordinates_csv, solution):

    output_file("visualise.html")

    # read csv file with pandas to abstract tabel
    reader = pd.read_csv('data/StationsNationaal.csv')
    source = ColumnDataSource(data=reader)

    # print(reader)

    # coordinates of Utrecht, because that's sort of the middle of the Netherlands
    map_options = GMapOptions(lat=52.0907374, lng=5.1214201, map_type="roadmap", zoom=7)

    # gmap function with API key
    p = gmap("AIzaSyAyJoHTODNYyRK2cTAewX4XDu9WHDoaUOI", map_options, title="Visualisatie")

    p.circle(x="lon", y="lat", size=8, fill_color="blue", fill_alpha=0.8, source=source,legend_label="Stations")

    
    # add hovertool for station name
    p.add_tools(HoverTool(tooltips=[('Station', '@Station')]))

    # add lines
    # p.multi_line(xs='lon', ys='lat', source=source, color="red", line_width=2)
    # p.line(x='lon', y='lat', line_width=2, color="green", source=source)

    # solution wordt in main meegegeven aan coordinates objects
    # solution bestaat uit station objecten. 
    station_lat = [] #A
    station_lon = [] #A 

    for line in solution: #line is elke traject : voor elk traject/trein in de oplossing
        route_lat = [] #B
        route_lon = []
        # print(type(line))
        # print(line.stations) # stationsobjecten die in de oplossing zit : print stationsobjecten uit van het traject
        # iterate through every station of every line in the solution 
        
        print('='*8)
        
        for station in line.stations: # voor elk station in het traject
            # put all lat and lons from station in list.
            
            print(station) # = elk traject
            route_lat.append(float(station.lat)) # zet de lat in de lijst > voor elke station_lat moet nog een lijst worden gemaakt. 
            route_lon.append(float(station.lon))
        # break

        station_lat.append(route_lat)
        station_lon.append(route_lon)

    # p.line(x='lon', y='lat', line_width=2, color="green", source=source)
    
    p.line(station_lon, station_lat, line_width=2)
    show( p)


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

    #==============================================================================================

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
