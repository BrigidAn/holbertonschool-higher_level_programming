#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_max_at_end(self):
        """Test when max is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test when max is at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test when max is in the middle"""
        self.assertEqual(max_integer([1, 5, 3, 2]), 5)

    def test_one_negative_number(self):
        """Test list with one negative number"""
        self.assertEqual(max_integer([1, 2, -4, 3]), 3)

    def test_only_negative_numbers(self):
        """Test list with only negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_list_one_element(self):
        """Test list with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))


if __name__ == '__main__':
    unittest.main()