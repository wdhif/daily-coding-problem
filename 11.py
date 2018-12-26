#!/usr/bin/env python3

"""Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix."""

import unittest


def autocomplete(string, array):
    string_length = len(string)
    result = []
    for _, value in enumerate(array):
        if string == value[0:string_length]:
            result.append(value)
    return result

class Test(unittest.TestCase):
    test_0 = ['de', ['dog', 'deer', 'deal'], ['deer', 'deal']]
    test_1 = [[5, 1, 1, 5], 10]

    def test(self):
        result = autocomplete(self.test_0[0], self.test_0[1])
        self.assertEqual(result, self.test_0[2])


if __name__ == '__main__':
    unittest.main()
