#!/usr/bin/env python3

"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""

import unittest


def decode(message):
    memo = [None] * (len(message) + 1) 
    return _decode(message, len(message), memo)


def _decode(message, offset, memo):
    if offset == 0:
        return 1

    starting_index = len(message) - offset
    if message[starting_index] == 0:
        return 0
    
    if memo[offset] is not None:
        return memo[offset]

    result = _decode(message, offset - 1, memo)
    if offset >= 2 and int(message[starting_index:starting_index + 2]) <= 26:
        result += _decode(message, offset - 2, memo)
    
    memo[offset] = result
    return result


class Test(unittest.TestCase):
    test_0 = ['111', 3]

    def test(self):
        print(decode(self.test_0[0]))


if __name__ == "__main__":
    unittest.main()
