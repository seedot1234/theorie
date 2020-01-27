"""
main.py
Calls all functions in the repository 'theorie'
10/1/20

"""

from code1.classes import connection, route, station, load_data
from results.visualisation import visualise
from code1.classes.route import Route
from code1.algorithms.random import random_solution
from code1.algorithms.random_p import random_solution_p
from code1.algorithms.random_k import random_solution_k
from code1.algorithms.greedy_lookahead import greedy_lookahead
from code1.algorithms.greedy_lookahead_test import greedy_lookahead_test
from code1.algorithms.trim import trim
from code1.algorithms.railhead import railhead
from code1.algorithms.shortest import shortest
from code1.algorithms.longest import longest
from code1.algorithms.unused import unused
from random import randrange
from code1.classes.solution import Solution
from code1.algorithms.hill import Hillclimber
from code1.algorithms.annealing import SimulatedAnnealing
import random
import csv, io, os
import copy
from results.bound import quality
from results.descriptives import boxplot, histogram, linechart
from results.descriptives import descriptive
from interface.interface import UI



print("Welcome to RailNL\nPlease refer to the README for instructions as of how to use this program.")
interface = UI(os.path.join("data", "StationsNationaal.csv"), os.path.join("data", "ConnectiesNationaal.csv"))
interface.run()

# VOOR HOLLAND, DOE DIT:
# creates station objects from csv
# station_csv = os.path.join("data", "ConnectiesHolland.csv")
# station_objects = load_data.create_station_list_nationaal(station_csv)

# # creates connection objects from csv
# connection_csv = os.path.join("data", "TestConnecties.csv")
# connection_objects = load_data.create_connection(connection_csv, station_objects)

# VOOR NATIONAAL, DOE DIT:
station_csv = os.path.join("data", "StationsNationaal.csv")
station_objects = load_data.create_station_list_nationaal(station_csv)

# creates connection objects from csv
connection_csv = os.path.join("data", "ConnectiesNationaal.csv")
connection_objects = load_data.create_connection(connection_csv, station_objects)


# adds connections to stations
connections_list = []
load_data.add_station_connection(station_objects, connection_objects)

# length of connections
len_connections = len(connection_objects)

# get descriptives
descriptive(len_connections, station_objects, connection_objects)
boxplot()
# histogram()
 
# creates list of station coordinates VISUALISE
# solution0 = random_solution_p(station_objects, connection_objects, 20, 180)     
# solution1 = greedy_lookahead(station_objects, connection_objects, 20, 180)
# solution2 = shortest(station_objects, connection_objects, 20, 180) 
# solution3 = longest(station_objects, connection_objects, 20, 180)
# solution4 = railhead(station_objects, connection_objects, 20, 180)
# solution5 = unused(station_objects, connection_objects, 20, 180)

# visualise
# coordinates_csv = os.path.join("data", "StationsNationaal.csv")
# coordinates_objects = visualise.coordinates(coordinates_csv, solution5)

# ########

# trimmed_solution = trim(solution, connection_objects)

# # calls upon the hill climbing algorithm 
# hill = Hillclimber(len_connections, station_objects, solution)
# answer = hill.run(1000)
# print(answer.K - solution.set_K(len_connections))

# solution = unused(station_objects, connection_objects, 20, 180)

print("Setting up Simulated Annealing...")
simanneal = SimulatedAnnealing(len_connections, station_objects, solution, temperature=35)

# # calls upon the hill climbing algorithm 
# hill = Hillclimber(len_connections, station_objects, solution)
# answer = hill.run(1000)
# print(answer.K - solution.set_K(len_connections))

# exit()



# if __name__ == "__main__":
#     print("Welcome to RailNL")
# print("Running Simulated Annealing...")
# simanneal.run(2000)


# print("K  after annealing...")
# print(simanneal.K)


# # load csv in dataframe
# results = pd.read_csv('annealing.csv')

# # create histogram with K from results dataframe
# results.K.plot() 

# # sets labels and title
# plt.xlabel('Number of Iterations x 10')
# plt.ylabel('Kwaliteitsscore (K)')

# # show plot
# plt.show()

# exit()
