from matplotlib import pyplot
from dataset_generators.circle_generator import CircleGenerator
from dataset_generators.random_generator import RandomGenerator

# li = list(CircleGenerator().generate_sample(50))
li = list(CircleGenerator().generate_sample_equidistant(50))
# li = list(RandomGenerator().generate_sample(50))

xs = [x[0] for x in li]
ys = [x[1] for x in li]

# s = points size
pyplot.scatter(xs, ys, s=3)
pyplot.show()
