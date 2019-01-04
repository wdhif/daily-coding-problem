#!/usr/bin/env python3

"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping).
Find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

import unittest


def compute_minimum_rooms_n2(pairs):
    max_rooms = 0
    for i in pairs:
        rooms = 1
        for j in pairs:
            if j[0] > i[0] and j[0] < i[1]:
                rooms += 1
        max_rooms = max(max_rooms, rooms)
    return max_rooms


def compute_minimum_rooms_nlogn(pairs):
    events = {}
    for pair in pairs:
        if pair[0] in events:
            events[pair[0]] += 1
        else:
            events[pair[0]] = 1
        
        if pair[1] in events:
            events[pair[1]] -= 1
        else:
            events[pair[1]] = -1
    
    max_rooms = 0
    rooms = 0
    for event in sorted(events.items()):
        rooms += event[1]
        max_rooms = max(max_rooms, rooms)

    return max_rooms

class Test(unittest.TestCase):
    test_0 = [[(30, 75), (0, 50), (60, 150)], 2]

    def test(self):
        self.assertEqual(compute_minimum_rooms_n2(self.test_0[0]), self.test_0[1])
        self.assertEqual(compute_minimum_rooms_nlogn(self.test_0[0]), self.test_0[1])


if __name__ == '__main__':
    unittest.main()
