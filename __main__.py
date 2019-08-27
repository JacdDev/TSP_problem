from matplotlib import pyplot
from dataset_generators.circle_generator import CircleGenerator

li = list(CircleGenerator().generate_sample(100))

xs = [x[0] for x in li]
ys = [x[1] for x in li]

# s = points size
pyplot.scatter(xs, ys, s=2)
pyplot.show()
