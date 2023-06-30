#!/usr/bin/python3
"""Import modules for testing"""


import unittest
from models.square import Square
from io import StringIO
import sys
"""Class for unittest"""


class TestSquare(unittest.TestCase):

    def test_square_init(self):
        """Test for square instance initiation"""
        obj = Square(2, 3, 4, 5)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 2)

    def test_square_x(self):
        """Test for square initialization with x > 0"""
        obj = Square(2, 3, 4, 5)
        self.assertEqual(obj.x, 3)

    def test_square_x_zero(self):
        """Test for square init with no x value"""
        obj = Square(2)
        self.assertEqual(obj.x, 0)

    def test_square_y(self):
        """Test for square init with y > 0"""
        obj = Square(2, 3, 4, 5)
        self.assertEqual(obj.y, 4)

    def test_square_y_zero(self):
        """Test for square init with no y value"""
        obj = Square(2)
        self.assertEqual(obj.y, 0)

    def test_square_id(self):
        """Test for square init with id value"""
        obj = Square(2, 3, 4, 5)
        self.assertEqual(obj.id, 5)

    def test_square_id_none(self):
        """Test for square init with no id value"""
        obj = Square(2)
        self.assertEqual(obj.id, 6)

    def test_square_typeerror(self):
        """Test for square init with TypeError"""
        with self.assertRaises(TypeError):
            obj = Square("test", 3, 4, 5)
            obj = Square(2, "test", 4, 5)
            obj = Square(2, 3, "test", 5)

    def test_square_no_args(self):
        """Test for square init with no args"""
        with self.assertRaises(TypeError):
            obj = Square()

    def test_square_many_args(self):
        """Test for square init with too many args"""
        with self.assertRaises(TypeError):
            obj = Square(1, 2, 3, 4, 5)

    def test_square_valueerror(self):
        """Test for square init with ValueError"""
        with self.assertRaises(ValueError):
            obj = Square(-2, 3, 4, 5)
            obj = Square(2, -3, 4, 5)
            obj = Square(2, 3, -4, 5)
            obj = Square(0, 3, 4, 5)

    def test_square_size_setter(self):
        """Test for square size setter"""
        obj = Square(2, 3, 4, 5)
        obj.size = 1
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)

    def test_square_size_setter_typeerror(self):
        """Test for square size setter with TypeError"""
        obj = Square(2, 3, 4, 5)
        with self.assertRaises(TypeError):
            obj.size = "Si"

    def test_square_size_setter_valueerror(self):
        """Test for square size setter with ValueError"""
        obj = Square(2, 3, 4, 5)
        with self.assertRaises(ValueError):
            obj.size = -1
            obj.size = 0

    def test_square_size_getter(self):
        """Test for square size getter"""
        obj = Square(2, 3, 4, 5)
        size = obj.size
        self.assertEqual(size, 2)

    def test_square_area(self):
        """Test for square area method"""
        obj = Square(2, 3, 4, 5)
        self.assertEqual(obj.area(), 4)

    def test_square_area_error(self):
        """Test for square area method errors"""
        obj = Square(2, 3, 4, 5)
        with self.assertRaises(TypeError):
            obj.area(1)

    def test_square_print(self):
        """Test for square __str__ method"""
        obj = Square(2, 3, 4, 5)
        save_op = StringIO()
        sys.stdout = save_op

        print(obj)
        print_op = save_op.getvalue().strip()
        sys.stdout = sys.__stdout__

        self.assertEqual(print_op, "[Square] (5) 3/4 - 2")

    def test_square_update(self):
        """Test for square update method"""
        obj = Square(2, 3, 4, 5)
        obj.update(10, 4, 6, 8)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 8)

    def test_square_update_some(self):
        """Test for square update method with some args"""
        obj = Square(2, 3, 4, 5)
        obj.update(10, 4)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_square_update_kwargs(self):
        """Test for square update method with kwargs"""
        obj = Square(2, 3, 4, 5)
        obj.update(id=10, size=4, x=6, y=8)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 8)

    def test_square_update_kwargs_mixed(self):
        """Test for square update method with kwargs and mixed attributes"""
        obj = Square(2, 3, 4, 5)
        obj.update(x=6, id=10, y=8, size=4)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 8)

    def test_square_update_kwargs_some(self):
        """Test for square update method with kwargs and some attributes"""
        obj = Square(2, 3, 4, 5)
        obj.update(id=10, size=4)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_dict(self):
        """Test for sqaure to_dictionary method"""
        obj = Square(2, 3, 4, 5)
        obj_dict = obj.to_dictionary()
        self.assertEqual(obj_dict, {'id': 5, 'size': 2, 'x': 3, 'y': 4})

    def test_dict_error(self):
        """Test for square to_dictionary method errors"""
        obj = Square(2, 3, 4, 5)
        with self.assertRaises(TypeError):
            obj_dict = obj.to_dictionary(1)


if __name__ == '__main__':
    unittest.main()
