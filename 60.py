#!/usr/bin/env python3

"""
Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.
Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.
"""

import unittest


def find_two_subset(multiset):
    total = sum(multiset)
    target = int(total / 2)

    current_total = 0
    for i in multiset:
        current_total += i
        if current_total == target:
            return True

    return False

def find_two_subset_with_sort(multiset):
    multiset.sort()
    for i in range(1, len(multiset) - 1):
        if sum(multiset[:-i]) == sum(multiset[len(multiset) - i:]):
            return True

    return False


class Test(unittest.TestCase):
    test_0 = [15, 5, 20, 10, 35, 15, 10]
    test_1 = [15, 5, 20, 10, 35]
    test_2 = [3, 2, 5]

    def test(self):
        self.assertEqual(find_two_subset(self.test_0), False)
        self.assertEqual(find_two_subset(self.test_1), False)
        self.assertEqual(find_two_subset(self.test_2), True)

        self.assertEqual(find_two_subset_with_sort(self.test_0), True)
        self.assertEqual(find_two_subset_with_sort(self.test_1), False)
        self.assertEqual(find_two_subset_with_sort(self.test_2), True)


if __name__ == '__main__':
    unittest.main()
