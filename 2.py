#!/usr/bin/env python3

"""Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i."""

import unittest


def product_array_n2(number_list):
    result = []
    for index, _ in enumerate(number_list):
        final_value = 0
        for item in number_list:
            if number_list[index] == item:
                continue
            if final_value == 0:
                final_value = item
            else:
                final_value = final_value * item
        result.append(final_value)

    return result


def product_array_n(number_list):
    result = []
    total = 0
    for item in number_list:
        if total == 0:
            total = item
        else:
            total = total * item

    for item in number_list:
        result.append(int(total / item))

    return result


class Test(unittest.TestCase):
    test_1 = [[1, 2, 3, 4, 5], [120, 60, 40, 30, 24]]
    test_2 = [[1, 2], [2, 1]]

    def test(self):
        result = product_array_n2(self.test_1[0])
        self.assertEqual(result, self.test_1[1])

        result = product_array_n2(self.test_2[0])
        self.assertEqual(result, self.test_2[1])

        result = product_array_n(self.test_1[0])
        self.assertEqual(result, self.test_1[1])

        result = product_array_n(self.test_2[0])
        self.assertEqual(result, self.test_2[1])


if __name__ == "__main__":
    unittest.main()
