#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class test(unittest.TestCase):
    """
    test case
    """

    print(max_integer([1, 2, 3, 4]))
    print(max_integer([1, 3, 4, 2]))


if __name__ == '__main__':
    unittest.main()
