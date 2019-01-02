#!/usr/bin/env python3

"""
You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
"""

import unittest


class OrderQueue(object):
    def __init__(self, queue_size):
        self.order_queue = []
        self.queue_size = queue_size

    def record(self, order):
        if len(self.order_queue) >= self.queue_size:
            del self.order_queue[0]

        self.order_queue.append(order)

    def get_last(self, i):
        return self.order_queue[-i:][::-1]


class Test(unittest.TestCase):
    def test(self):
        order_queue = OrderQueue(3)
        order_queue.record(0)
        order_queue.record(1)
        order_queue.record(2)

        self.assertEqual(order_queue.get_last(2), [2, 1])


if __name__ == '__main__':
    unittest.main()
