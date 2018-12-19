#!/usr/bin/env python3

"""Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well."""

import unittest


def find_missing_int(array):
    seen = [False] * len(array)

    for item in array:
        if item > 0:
            seen[item - 1] = True

    for index, value in enumerate(seen):
        if not value:
            if index + 1 < len(seen):
                if seen[index + 1]:
                    return index + 1
            else:
                return index + 1


class Test(unittest.TestCase):
    test_1 = [[3, 4, -1, 1], 2]
    test_2 = [[1, 2, 0], 3]

    def test(self):
        result = find_missing_int(self.test_1[0])
        self.assertEqual(result, 2)

        result = find_missing_int(self.test_2[0])
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
