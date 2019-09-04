from dataset_generators.circle_generator import CircleGenerator
from dataset_generators.random_generator import RandomGenerator
from display import display
from solvers.simulated_annealing import SimulatedAnnealing, StoppingCriterion
import solvers.reinforcement_learning
import random
import math

# generate data
sample = 20
# node_list = list(CircleGenerator().generate_sample(sample))
node_list = list(CircleGenerator().generate_sample_equidistant(sample))
# node_list = list(RandomGenerator().generate_sample(sample))

# create matrix of distances (euclidean)
distances = []
for idx_origin, node_origin in enumerate(node_list):
    distances.append([])
    for idx_destination, node_destination in enumerate(node_list):
        distances[idx_origin].append(
            math.sqrt(sum([(a - b) ** 2 for a, b in zip(node_origin, node_destination)]))
        )

# run simulated annealing
sa = SimulatedAnnealing()
sa.stopping_criterion = StoppingCriterion.ITERATIONS
sa.max_iterations = 10000
solution = sa.run(node_list, distances)

# display result
display.plot(node_list, solution)
display.print_result(solution, distances)

#solvers.reinforcement_learning.run()
