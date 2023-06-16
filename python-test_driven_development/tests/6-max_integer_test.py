#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
""" Unittest for function max_integer([..]) """


class TestMaxInteger(unittest.TestCase):
    """ Test cases """
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 2, 1]), 3)
        self.assertEqual(max_integer([3, 3, 3,]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1, 2, 1 + 2]), 1 + 2)
        self.assertEqual(max_integer([[6, 5, 4], [3, 2, 1]]), [6, 5, 4])
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 4, float('inf')]), float('inf'))
        with self.assertRaises(TypeError):
            max_integer([1, 2, "si"])
            max_integer([1, 2, 3], [4, 5, 6])
            max_integer()
            max_integer("Hola")
            max_integer([1, 4, tuple(4, 5)])
            max_integer([1, 4, [5, 6]])


if __name__ == '__main__':
    unittest.main()
