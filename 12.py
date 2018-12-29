#!/usr/bin/env python3

"""There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters."""

import unittest


def staircase(steps):
    steps += 1
    return fibonacci(steps)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


class Test(unittest.TestCase):
    test_0 = [4, 5]
    test_1 = [5, 8]

    def test(self):
        result = staircase(self.test_0[0])
        self.assertEqual(result, self.test_0[1])

        result = staircase(self.test_1[0])
        self.assertEqual(result, self.test_1[1])


if __name__ == '__main__':
    unittest.main()
