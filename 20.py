#!/usr/bin/env python3

"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""

import unittest


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_intersection(starting_nodes):
    seen_nodes = []

    current_node = starting_nodes[0]
    while current_node.next != None:
        seen_nodes.append(current_node)
        current_node = current_node.next

    current_node = starting_nodes[1]
    while current_node.next != None:
        if current_node in seen_nodes:
            return current_node.value
        current_node = current_node.next


class Test(unittest.TestCase):
    def test(self):
        node_10 = Node(10)
        node_8 = Node(8, node_10)
        node_7 = Node(7, node_8)
        node_3 = Node(3, node_7)

        node_1 = Node(1, node_8)
        node_99 = Node(99, node_1)

        starting_nodes = [node_3, node_99]

        self.assertEqual(find_intersection(starting_nodes), 8)


if __name__ == '__main__':
    unittest.main()
