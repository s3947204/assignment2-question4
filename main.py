import numpy as np
from itertools import permutations
from TSPSolver import TSPSolver  # Import the class correctly
import sys
import time
import csv


def generate_symettric_TSP_distance_matrix(num_cities, min_distance=1, max_distance=10):
    distance_matrix = np.zeros((num_cities, num_cities))

    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = np.random.randint(min_distance, max_distance + 1)
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance

    return distance_matrix

solveMethod = sys.argv[1]
num_cities = int(sys.argv[2])

num_cities = num_cities
distance_matrix = generate_symettric_TSP_distance_matrix(num_cities)
TSP_Solver = TSPSolver(distance_matrix);
print("Symmetric Distance Matrix:")
print(distance_matrix)
time_taken = 0;

start_time = time.perf_counter()
if(solveMethod == "brute"):
    start_time = time.perf_counter()
    best_tour_brute, min_distance_brute = TSP_Solver.brute_force_tsp()
    end_time = time.perf_counter()
    time_taken = end_time - start_time
elif(solveMethod == "nearest"):
    start_time = time.perf_counter()
    best_tour, min_distance = TSP_Solver.nearest_neighbor_tsp()
    end_time = time.perf_counter()
    time_taken = end_time - start_time
elif (solveMethod == "greedy"): 
    start_time = time.perf_counter()
    best_tour_greedy, min_distance_greedy = TSP_Solver.greedy_tsp()
    end_time = time.perf_counter()
    time_taken = end_time - start_time

csv_filename = f"{solveMethod}.csv"


with open(csv_filename, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([num_cities, f"{time_taken:.6f}"])