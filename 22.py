#!/usr/bin/env python3

"""
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
If there is more than one possible reconstruction, return any of them.
If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""

import unittest

def separate_string(dictionary, string):
    result = []

    current_word = ''
    for letter in string:
        current_word += letter
        if current_word in dictionary:
            result.append(current_word)
            current_word = ''

    return result


class Test(unittest.TestCase):
    test_0 = [['quick', 'brown', 'the', 'fox'], 'thequickbrownfox']
    test_1 = [['bed', 'bath', 'bedbath', 'and', 'beyond'], 'bedbathandbeyond']

    def test(self):

        result = separate_string(self.test_0[0], self.test_0[1])
        self.assertEqual(result, ['the', 'quick', 'brown', 'fox'])

        result = separate_string(self.test_1[0], self.test_1[1])
        self.assertEqual(result, ['bed', 'bath', 'and', 'beyond'])


if __name__ == '__main__':
    unittest.main()
