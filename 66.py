#!/usr/bin/env python3

"""
Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0).
You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
"""

import random
import unittest


def toss_biased():
    return True if random.randint(0, 100) > 25 else False


def toss_unbiased():
    round_1 = None
    round_2 = None
    while round_1 == round_2:
        round_1 = toss_biased()
        round_2 = toss_biased()
    return round_1


class Test(unittest.TestCase):
    def test(self):
        true = 0
        false = 0
        for _ in range(0, 100000):
            if toss_unbiased() == True:
                true += 1
            else:
                false += 1
        self.assertLessEqual(abs(true - false), 1000)


if __name__ == '__main__':
    unittest.main()
