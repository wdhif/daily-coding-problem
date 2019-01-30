#!/usr/bin/env python3

"""
Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element

Implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true.
The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true.
The same regular expression on the string "chats" should return false.
"""

import unittest


def match(regex, string):
    asterisk_active = False
    preceding_element = ''
    deactivater = ''

    for index, letter in enumerate(string):
        if asterisk_active:
            if letter == preceding_element:
                continue
            elif letter == deactivater:
                asterisk_active = False
                continue

        if asterisk_active is False and index > len(regex) - 1:
            return False

        if regex[index] == '*':
            if index + 1 < len(regex):
                asterisk_active = True
                deactivater = regex[index + 1]
                preceding_element = string[index - 1]
            else:
                return True
        elif regex[index] == '.':
            continue
        elif letter == regex[index]:
            continue
        else:
            return False

    return True


class Test(unittest.TestCase):
    test_0 = ['ra.', 'ray', True]
    test_1 = ['.*at', 'chats', False]
    test_2 = ['.*', 'chats', True]
    test_3 = ['.*', '', True]

    def test(self):
        self.assertEqual(match(self.test_0[0], self.test_0[1]), self.test_0[2])
        self.assertEqual(match(self.test_1[0], self.test_1[1]), self.test_1[2])
        self.assertEqual(match(self.test_2[0], self.test_2[1]), self.test_2[2])
        self.assertEqual(match(self.test_3[0], self.test_3[1]), self.test_3[2])


if __name__ == '__main__':
    unittest.main()
