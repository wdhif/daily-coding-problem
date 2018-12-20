#!/usr/bin/env python3

"""cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4."""

import unittest


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(pair):
    def first(a, b):
        return a

    return pair(first)


def cdr(pair):
    def last(a, b):
        return b

    return pair(last)


class Test(unittest.TestCase):
    test_1 = [[3, 4], 3, 4]

    def test(self):
        result = car(cons(self.test_1[0][0], self.test_1[0][1]))
        self.assertEqual(result, self.test_1[1])

        result = cdr(cons(self.test_1[0][0], self.test_1[0][1]))
        self.assertEqual(result, self.test_1[2])


if __name__ == "__main__":
    unittest.main()
