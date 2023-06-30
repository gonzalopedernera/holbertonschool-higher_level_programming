#!/usr/bin/python3
import unittest
from models.square import Square
from io import StringIO
import sys

class TestSquare(unittest.TestCase):

    def test_square_init(self):
        obj = Square(2, 3, 4, 5)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 2)
    
    def test_square_x(self):
        obj = Square(2, 3, 4, 5)
        self.assertEqual(obj.x, 3)

    def test_square_x_zero(self):
        obj = Square(2)
        self.assertEqual(obj.x, 0)

    def test_square_y(self):
        obj = Square(2, 3, 4, 5)
        self.assertEqual(obj.y, 4)

    def test_square_y_zero(self):
        obj = Square(2)
        self.assertEqual(obj.y, 0)

    def test_square_id(self):
        obj = Square(2, 3, 4, 5)
        self.assertEqual(obj.id, 5)
    
    def test_square_id_none(self):
        obj = Square(2)
        self.assertEqual(obj.id, 6)

    def test_square_typeerror(self):
        with self.assertRaises(TypeError):
            obj = Square("test", 3, 4, 5)
            obj = Square(2, "test", 4, 5)
            obj = Square(2, 3, "test", 5)

    def test_square_no_args(self):
        with self.assertRaises(TypeError):
            obj = Square()

    def test_square_many_args(self):
        with self.assertRaises(TypeError):
            obj = Square(1, 2, 3, 4, 5)

    def test_square_valueerror(self):
        with self.assertRaises(ValueError):
            obj = Square(-2, 3, 4, 5)
            obj = Square(2, -3, 4, 5)
            obj = Square(2, 3, -4, 5)
            obj = Square(0, 3, 4, 5)
    
    def test_square_size_setter(self):
        obj = Square(2, 3, 4, 5)
        obj.size = 1
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)

    def test_square_size_getter(self):
        obj = Square(2, 3, 4, 5)
        size = obj.size
        self.assertEqual(size, 2)

    def test_square_area(self):
        obj = Square(2, 3, 4, 5)
        self.assertEqual(obj.area(), 4)

    def test_square_area_error(self):
        obj = Square(2, 3, 4, 5)
        with self.assertRaises(TypeError):
            obj.area(1)

    def test_square_print(self):
        obj = Square(2, 3, 4, 5)
        save_op = StringIO()
        sys.stdout = save_op

        print(obj)
        print_op = save_op.getvalue().strip()
        sys.stdout = sys.__stdout__

        self.assertEqual(print_op, "[Square] (5) 3/4 - 2")

    def test_square_update(self):
        obj = Square(2, 3, 4, 5)
        obj.update(10, 4, 6, 8)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 8)

    def test_square_update_some(self):
        obj = Square(2, 3, 4, 5)
        obj.update(10, 4)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_square_update_kwargs(self):
        obj = Square(2, 3, 4, 5)
        obj.update(id=10, size=4, x=6, y=8)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 8)

    def test_square_update_kwargs_mixed(self):
        obj = Square(2, 3, 4, 5)
        obj.update(x=6, id=10, y=8, size=4)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 8)

    def test_square_update_kwargs_some(self):
        obj = Square(2, 3, 4, 5)
        obj.update(id=10, size=4)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 4)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_dict(self):
        obj = Square(2, 3, 4, 5)
        obj_dict = obj.to_dictionary()
        self.assertEqual(obj_dict, {'id': 5, 'size': 2, 'x': 3, 'y': 4})

    def test_dict_error(self):
        obj = Square(2, 3, 4, 5)
        with self.assertRaises(TypeError):
            obj_dict = obj.to_dictionary(1)
if __name__ == '__main__':
    unittest.main()
