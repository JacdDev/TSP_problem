from dataset_generators.circle_generator import CircleGenerator
from dataset_generators.random_generator import RandomGenerator
from display import display
import random

sample = 10
#node_list = list(CircleGenerator().generate_sample(50))
node_list = list(CircleGenerator().generate_sample_equidistant(sample))
#node_list = list(RandomGenerator().generate_sample(50))

# create a random solution
solution = list(range(0, sample))
random.shuffle(solution)

display.plot(node_list, solution)
