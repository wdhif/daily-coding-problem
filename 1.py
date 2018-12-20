#!/usr/bin/env python3

"""Given a list of numbers and a number k, return whether any two numbers from the list add up to k."""

import unittest


def adds_up_n2(number_list, k):
    for number in number_list:
        magic_number = k - number
        for number in number_list:
            if number == magic_number:
                return True
    return False


def adds_up_n(number_list, k):
    seen = [False] * (k + 1)
    for number in number_list:
        magic_number = k - number
        if seen[number]:
            return True
        seen[magic_number] = True

    return False


class Test(unittest.TestCase):
    test_1 = [[10, 15, 3, 7], 17]
    test_2 = [[1, 2, 0], 32]

    def test(self):
        result = adds_up_n2(self.test_1[0], self.test_1[1])
        self.assertTrue(result)

        result = adds_up_n2(self.test_2[0], self.test_2[1])
        self.assertFalse(result)

        result = adds_up_n(self.test_1[0], self.test_1[1])
        self.assertTrue(result)

        result = adds_up_n(self.test_2[0], self.test_2[1])
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
