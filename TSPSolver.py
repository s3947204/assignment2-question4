from itertools import permutations
import numpy as np


class TSPSolver: 
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix

    def brute_force_tsp(self):
        num_cities = len(self.distance_matrix)
        min_distance = float('inf')
        best_tour = []

        for tour in permutations(range(num_cities)):
            current_distance = self.calculate_total_distance( tour)
            if current_distance < min_distance:
                min_distance = current_distance
                best_tour = list(tour)

        best_tour.append(0)
        return best_tour, min_distance
    
    def nearest_neighbor_tsp(self):
            num_cities = len(self.distance_matrix)
            tour = [0]
            unvisited_cities = set(range(1, num_cities))

            while unvisited_cities:
                current_city_index = tour[-1]
                current_city_cost_matrix = self.distance_matrix[current_city_index];
                current_cost = np.inf;

                next_city_index = 0

                for i in range(current_city_cost_matrix.shape[0]):
                    if i in unvisited_cities:
                        if current_city_cost_matrix[i] < current_cost:
                            current_cost = current_city_cost_matrix[i]
                            next_city_index = i

                tour.append(next_city_index)
                unvisited_cities.discard(next_city_index)

            tour.append(0)

            return tour, self.calculate_total_distance( tour)
    
    def greedy_tsp(self):
        num_cities = len(self.distance_matrix)
        tour = []
        unvisited_cities = set(range(0, num_cities))
        sorted_cost = self.sort_distance_matrix_with_indices() # [cost, (city1, city2), ... , (cost, (city1, city2))]

        tour.append(sorted_cost[0][1][0])
        tour.append(sorted_cost[0][1][1])
        unvisited_cities.discard(sorted_cost[0][1][0])
        unvisited_cities.discard(sorted_cost[0][1][1])
        sorted_cost.pop(0)

        while len(unvisited_cities) > 1:
            smallest_cost_transition = sorted_cost[0]
            start_node = smallest_cost_transition[1][0]
            end_node = smallest_cost_transition[1][1]
            if(start_node not in tour and end_node not in tour):
                tour.append(start_node)
                tour.append(end_node)
                unvisited_cities.discard(start_node)
                unvisited_cities.discard(end_node)
            sorted_cost.pop(0)

        if(len(unvisited_cities) != 0):
            tour.append(unvisited_cities.pop());
        
        tour.append(tour[0])

        return tour, self.calculate_total_distance( tour)


    
    def calculate_total_distance(self, tour):
        total_distance = 0
        num_cities = len(tour)
        
        for i in range(num_cities):
            total_distance += self.distance_matrix[tour[i], tour[(i + 1) % num_cities]]

        return total_distance

    def sort_distance_matrix_with_indices(self):
        num_cities = self.distance_matrix.shape[0]
        distances_with_indices = []
        for i in range(num_cities):
            for j in range(i + 1, num_cities):
                distance = self.distance_matrix[i][j]
                distances_with_indices.append((distance, (i, j)))
        sorted_distances = sorted(distances_with_indices, key=lambda x: x[0])
        return sorted_distances

