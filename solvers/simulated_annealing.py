import random
import math
from enum import Enum
import queue


class StoppingCriterion(Enum):
    ITERATIONS = 1  # stop when makes a number of iterations
    TEMPERATURE = 2  # stop when reach a min temperature
    SAME_RESULTS = 3  # stop when last results are the same


class SimulatedAnnealing:

    def __init__(self):
        self.max_iterations = 1000  # max iteration for ITERATION stopping criterion
        self.init_temperature = 1000  # initial temperature
        self.min_temperature = 0.001  # min temperature for TEMPERATURE stopping criterion
        self.temperature_cooling_factor = 0.999  # cooling factor
        self.last_results_size = 1000  # number of last result checked for SAME_RESULTS stopping criterion
        self.stopping_criterion = StoppingCriterion.SAME_RESULTS  # stopping criterion

    def run(self, nodes, distances):

        # start with random solution
        best_solution = list(range(0, len(nodes)))
        random.shuffle(best_solution)

        last_results = queue.Queue(self.last_results_size)
        temperature = self.init_temperature
        iteration = 0
        continue_iterating = True
        while continue_iterating:
            # cool temperature
            temperature *= self.temperature_cooling_factor
            # generate new solution
            new_solution = self._select_neighbour(best_solution[:])
            # check if we take the new solution
            if self._probability_function(best_solution, new_solution, distances, temperature) >= random.uniform(0, 1):
                best_solution = new_solution
            iteration += 1
            # store the solution of this iteration
            if last_results.full():
                last_results.get()
            last_results.put(best_solution)
            # check stopping criterion
            continue_iterating = self.check_stopping_criterion(iteration, temperature, last_results)
        return best_solution

    def _select_neighbour(self, solution):
        # select positions to swap randomly
        pos1 = random.randrange(len(solution) - 1)
        pos2 = random.randrange(len(solution) - 1)
        # pos2 = pos1+1
        # if pos2 == len(solution):
        #     pos2 = 0
        # swap positions
        solution[pos1], solution[pos2] = solution[pos2], solution[pos1]
        return solution

    def _probability_function(self, best_solution, new_solution, distances, temperature):
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

    def check_stopping_criterion(self, iteration, temperature, last_results):
        if self.stopping_criterion is StoppingCriterion.ITERATIONS:
            return iteration < self.max_iterations
        if self.stopping_criterion is StoppingCriterion.TEMPERATURE:
            return temperature > self.min_temperature
        if self.stopping_criterion is StoppingCriterion.SAME_RESULTS:
            # check if any result in te queue is different
            count_elements = 1
            continue_result = False
            last_results_aux = queue.Queue(self.last_results_size)
            result1 = last_results.get()
            last_results_aux.put(result1)
            while not last_results.empty():
                count_elements += 1
                result2 = last_results.get()
                last_results_aux.put(result2)
                if result1 != result2:
                    continue_result = True
                result1 = result2
            # if there are not enough elements, continue iterating
            if count_elements < self.last_results_size:
                continue_result = True
            # fill the queue again
            while not last_results_aux.empty():
                last_results.put(last_results_aux.get())
            return continue_result
