#!/usr/bin/env python3

"""
Given a array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock once.
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""

import unittest


def find_max_profit(stocks):
    min_value = None
    max_value = None
    max_profit = 0

    for buy_price in stocks:
        # Initialization pass
        if min_value is None and max_value is None:
            min_value = buy_price
            max_value = buy_price
            continue

        if buy_price < min_value:  # Possibly lower buy price
            min_value = buy_price
            max_value = buy_price  # Reset the max sell price
        elif buy_price - min_value > max_profit:  # Possibly higher maximum profit
            max_value = buy_price
            max_profit = max(buy_price - min_value, max_profit)

    return max_profit


class Test(unittest.TestCase):
    test_0 = [[9, 11, 8, 5, 7, 10], 5]
    test_1 = [[9, 10, 100, 8, 5, 7, 10], 91]
    test_2 = [[10, 9, 8, 7, 3, 0], 0]

    def test(self):
        self.assertEqual(find_max_profit(self.test_0[0]), self.test_0[1])
        self.assertEqual(find_max_profit(self.test_1[0]), self.test_1[1])
        self.assertEqual(find_max_profit(self.test_2[0]), self.test_2[1])


if __name__ == '__main__':
    unittest.main()
