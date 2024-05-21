#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestCase(unittest.TestCase):
    """
    test case
    """

    def test_max_at_the_end(self):
        self.assertEqual(max_integer([11, 22, 33]), 33)

    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([33, 22, 11]), 33)

    def test_max_in_the_middle(self):
        self.assertEqual(max_integer([10, 20, 15]), 20)

    def test_one_negative_number_in_the_list(self):
        self.assertEqual(max_integer([12, -1, 8]), 12)

    def test_only_negative_numbers_in_the_list(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_list_of_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_list_is_empty(self):
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
