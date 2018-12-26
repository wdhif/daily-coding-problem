#!/usr/bin/env python3

"""Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative."""

import unittest


def largest_sum_non_adjacent(array):
    taken = [False] * len(array)
    result = 0
    maximum = max(array)
    for _ in range(maximum, 0, -1):
        for index, item in enumerate(array):
            if item == maximum:
                if index == 0:
                    if taken[index + 1] is not True:
                        print('adding {0}'.format(item))
                        result = result + item
                        taken[index] = True
                elif index == len(array) - 1:
                    if taken[index - 1] is not True:
                        print('adding {0}'.format(item))
                        result = result + item
                        taken[index] = True
                else:
                    if taken[index + 1] is not True and taken[index - 1] is not True:
                        print('adding {0}'.format(item))
                        result = result + item
                        taken[index] = True

        maximum = maximum - 1
    return result


class Test(unittest.TestCase):
    test_0 = [[2, 4, 6, 2, 5], 13]
    test_1 = [[5, 1, 1, 5], 10]

    def test(self):
        result = largest_sum_non_adjacent(self.test_0[0])
        self.assertEqual(result, self.test_0[1])

        result = largest_sum_non_adjacent(self.test_1[0])
        self.assertEqual(result, self.test_1[1])


if __name__ == '__main__':
    unittest.main()
