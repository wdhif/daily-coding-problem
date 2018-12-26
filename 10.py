#!/usr/bin/env python3

"""Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds."""

import unittest
import time


class JobScheduler(object):
    def __init__(self, function, arguments, delay):
        self.function = function
        self.arguments = arguments
        self.delay = delay / 1000

    def execute(self):
        time.sleep(self.delay)
        result = self.function(self.arguments)

        return result


def job_scheduler(function, delay):
    delay = delay / 1000
    time.sleep(delay)

    return function


class Test(unittest.TestCase):
    test_0 = [[2, 4, 6, 2, 5], 13]
    test_1 = [[5, 1, 1, 5], 10]

    def test(self):
        job_scheduler = JobScheduler(print, 'test', 1000)
        JobScheduler.execute(job_scheduler)


if __name__ == '__main__':
    unittest.main()
