import random


# class to generate a data set randomly in a given area
class RandomGenerator:

    # Constructor, receives the area parameters
    def __init__(self, max_coordinate_x=1, min_coordinate_x=0, max_coordinate_y=1, min_coordinate_y=0):
        self.max_coordinate_x = max_coordinate_x
        self.min_coordinate_x = min_coordinate_x
        self.max_coordinate_y = max_coordinate_y
        self.min_coordinate_y = min_coordinate_y

    # function that returns a point inside the given area
    def generate_point(self):
        x = random.uniform(self.min_coordinate_x, self.max_coordinate_x)
        y = random.uniform(self.min_coordinate_y, self.max_coordinate_y)
        return x, y

    # function that returns a collection of points inside the given area
    def generate_sample(self, sample):
        for i in range(0, sample):
            yield self.generate_point()
