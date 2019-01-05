#!/usr/bin/env python3

"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

import unittest


def len_distinct_characters(string, k):
    string_array = list(string)
    substrings = []

    for offset in range(0, len(string_array) + 1):
        for length in range(1, len(string_array) + 1):
            if offset + length > len(string_array):
                continue
            substrings.append(string_array[offset:offset + length])

    valid_substrings = []
    for substring in substrings:
        dist_letters = []
        for letter in substring:
            if letter not in dist_letters:
                if len(dist_letters) < k:
                    dist_letters.append(letter)
                else:
                    break
        else:
            valid_substrings.append(substring)

    return max([len(substring) for substring in valid_substrings])


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
