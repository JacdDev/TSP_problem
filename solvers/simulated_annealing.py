import random
import math


class SimulatedAnnealing:

    def __init__(self, max_iterations=1000, init_temperature=0.99, min_temperature=0.001):
        self.max_iterations = max_iterations
        self.init_temperature = init_temperature
        self.min_temperature = min_temperature

    def run(self, nodes, distances):

        # start with random solution
        best_solution = list(range(0, len(nodes)))
        random.shuffle(best_solution)

        temperature = self.init_temperature
        iteration = 0
        while iteration < self.max_iterations and temperature > self.min_temperature:
            # cool temperature
            temperature *= 0.99
            new_solution = self.select_neighbour(best_solution[:])
            if self.probability_function(best_solution, new_solution, distances, temperature) >= random.uniform(0, 1):
                best_solution = new_solution
            iteration += 1
        return best_solution

    def select_neighbour(self, solution):
        # select positions to swap randomly
        pos1 = random.randrange(len(solution) - 1)
        pos2 = random.randrange(len(solution) - 1)
        #pos2 = pos1+1
        #if pos2 == len(solution):
        #    pos2 = 0
        # swap positions
        solution[pos1], solution[pos2] = solution[pos2], solution[pos1]
        return solution

    def probability_function(self, best_solution, new_solution, distances, temperature):
        # calculate the value of best solution
        total_distance_best_solution = 0
        for i, node in enumerate(best_solution):
            if i == len(best_solution) - 1:
                total_distance_best_solution += distances[best_solution[i]][best_solution[0]]
            else:
                total_distance_best_solution += distances[best_solution[i]][best_solution[i + 1]]

        # calculate the value of new solution
        total_distance_new_solution = 0
        for i, node in enumerate(new_solution):
            if i == len(new_solution) - 1:
                total_distance_new_solution += distances[new_solution[i]][new_solution[0]]
            else:
                total_distance_new_solution += distances[new_solution[i]][new_solution[i + 1]]

        if total_distance_best_solution > total_distance_new_solution:
            return 1
        else:
            return math.exp((-1*(total_distance_new_solution-total_distance_best_solution))/temperature)