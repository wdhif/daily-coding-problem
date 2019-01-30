#!/usr/bin/env python3

"""
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

import unittest

OPENING_BRACKETS = {
    '(': ')',
    '{': '}',
    '[': ']'
}
CLOSING_BRACKETS = {
    ')': '(',
    '}': '{',
    ']': '['
}


def check_brackets(string):
    brackets_queue = []
    for index, bracket in enumerate(string):
        if bracket in OPENING_BRACKETS:
            brackets_queue.append(OPENING_BRACKETS[bracket])
            if index == len(string) - 1:
                return False
        elif bracket in CLOSING_BRACKETS:
            if brackets_queue.pop() != bracket:
                return False
            if index == 0:
                return False

    if brackets_queue:
        return False
    return True


class Test(unittest.TestCase):
    test_0 = ['([])[]({})', True]
    test_1 = ['([)]', False]
    test_2 = ['((()', False]
    test_3 = ['', True]

    def test(self):
        self.assertEqual(check_brackets(self.test_0[0]), self.test_0[1])
        self.assertEqual(check_brackets(self.test_1[0]), self.test_1[1])
        self.assertEqual(check_brackets(self.test_2[0]), self.test_2[1])
        self.assertEqual(check_brackets(self.test_3[0]), self.test_3[1])


if __name__ == '__main__':
    unittest.main()
