import math
import random


# class to generate a data set in a circumference shape
class CircleGenerator:

    # Constructor, receives the circumference parameters
    def __init__(self, center_x=0, center_y=0, radius=1):
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y

    # function that returns the point of the circumference positioned at the given angle
    def generate_point(self, angle):
        x = math.cos(angle) * self.radius + self.center_x
        y = math.sin(angle) * self.radius + self.center_y
        return x, y

    # function that returns a random collection of points in circumference
    def generate_sample(self, sample):
        for i in range(0, sample):
            current_angle = random.uniform(0, 360)
            radians = math.radians(current_angle)
            yield self.generate_point(radians)

    # function that return a collection of points in the circumference of the same distance between them
    def generate_sample_equidistant(self, sample):
        angle_increment = 360/sample
        for i in range(0, sample):
            current_angle = angle_increment*i
            radians = math.radians(current_angle)
            yield self.generate_point(radians)