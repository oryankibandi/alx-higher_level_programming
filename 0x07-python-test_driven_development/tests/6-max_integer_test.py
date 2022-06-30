#!/usr/bin/python3
"""
This module tests the 6-max_integer module
"""


import unittest


max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):
    """
    This class contains tests for the module
    """

    def test_len(self):
        self.assertEqual(max_integer([]), None)

    def test_no_arg(self):
        self.assertEqual(max_integer(), None)

    def test_pos(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([7, 35, 65, 48]), 65)

    def test_neg(self):
        self.assertEqual(max_integer([-4, -52, -96, -2]). -2)
        self.assertEqual(max_integer([-54, -25, -35, -98]), -25)

    def test_single_elem(self):
        self.assertEqual(max_integer([2]), 2)
