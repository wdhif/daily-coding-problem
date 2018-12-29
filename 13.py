#!/usr/bin/env python3

"""Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters."""

import unittest


def len_distinct_characters(string, k):
    results = []

    for original_index, original_letter in enumerate(string):
        result = 1
        roster = [original_letter]
        for tested_index, tested_letter in enumerate(string):
            if original_index == tested_index:
                continue

            if original_letter == tested_letter:
                result = result + 1
            elif original_letter != tested_letter and len(roster) < k:
                roster.append(tested_letter)
                result = result + 1

        results.append(result)

    return max(results)


class Test(unittest.TestCase):
    test_0 = ['abcba', 2, 3]
    test_1 = ['abcba', 5, 5]
    test_2 = ['aaa', 1, 3]

    def test(self):
        result = len_distinct_characters(self.test_0[0], self.test_0[1])
        self.assertEqual(result, self.test_0[2])

        result = len_distinct_characters(self.test_1[0], self.test_1[1])
        self.assertEqual(result, self.test_1[2])

        result = len_distinct_characters(self.test_2[0], self.test_2[1])
        self.assertEqual(result, self.test_2[2])


if __name__ == '__main__':
    unittest.main()
