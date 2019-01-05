#!/usr/bin/env python3

"""
The area of a circle is defined as πr². Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

import unittest
import math
import random


def generate_points(radius):
    x = random.randint(-radius, radius)
    y = random.randint(-radius, radius)

    return x, y


def in_circle(x, y, radius):
    distance = math.sqrt(x ** 2 + y ** 2)
    if distance < radius:
        return True

    return False


def compute_pi():
    points_in_circle = 0
    points_in_square = 0

    radius = 200

    for i in range(250000):
        x, y = generate_points(radius)
        if in_circle(x, y, radius):
            points_in_circle += 1
        points_in_square += 1

    return 4 * (points_in_circle / points_in_square)


class Test(unittest.TestCase):
    def test(self):
        accuracy = (compute_pi() / math.pi) * 100
        self.assertGreater(accuracy, 99)


if __name__ == '__main__':
    unittest.main()
