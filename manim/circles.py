from manimlib import *
import random
import numpy as np


# create a polygon by sorting the randomly generated vectors by the angle in respect to the unit vector (pointing up)
def sort_vector(args):
    angles = []
    for vector in args:
        if vector[0] > 0:
            angles.append((vector, angle(UP, vector)))
        else:
            angles.append((vector, 360 - angle(UP, vector)))

    angles.sort(
        key=lambda tup: tup[1])  # sort the points/vectors by the angle in respect to the unit vector (pointing up)
    vectors = [item[0] for item in angles]  # return only the points/vectors

    return vectors


def angle(a, b):
    return np.arccos(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


class Circles(Scene):
    def construct(self):
        inner = Circle(radius=3)
        outer = Circle(radius=4)

        self.play(ShowCreation(inner))
        self.wait(0.3)
        self.play(ShowCreation(outer))
        self.wait(0.3)
        LR = [LEFT, RIGHT]
        UD = [UP, DOWN]
        args = []

        for i in range(50):
            args.append(random.uniform(0, 1) * random.choice(LR) + random.uniform(0, 1) * random.choice(UD))
        for i in range(len(args)):
            args[i] = random.uniform(3, 4) * args[i] / np.linalg.norm(args[i])

        polygon = Polygon(*sort_vector(args))
        self.play(ShowCreation(polygon))
