#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys

class TestRectangle(unittest.TestCase):

    def test_rectangle_width(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.width, 1)

    def test_rectangle_height(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.height, 2)

    def test_rectangle_x(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.x, 3)

    def test_rectangle_x_zero(self):
        obj = Rectangle(1, 2)
        self.assertEqual(obj.x, 0)

    def test_rectangle_y(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.y, 4)

    def test_rectangle_y_zero(self):
        obj = Rectangle(1, 2)
        self.assertEqual(obj.y, 0)

    def test_rectangle_id(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.id, 5)

    def test_rectangle_id_none(self):
        obj = Rectangle(1, 2)
        self.assertEqual(obj.id, 3)

    def test_rectangle_typeerror(self):
        with self.assertRaises(TypeError):
            obj = Rectangle("test", 2, 3, 4, 5)
            obj = Rectangle(1, "test", 3, 4, 5)
            obj = Rectangle(1, 2, "test", 4, 5)
            obj = Rectangle(1, 2, 3, "test", 5)

    def test_rectangle_no_args(self):
        with self.assertRaises(TypeError):
            obj = Rectangle()

    def test_rectangle_many_args(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(1, 2, 3, 4, 5, 6)

    def test_rectangle_valueerror(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(-1, 2, 3, 4, 5)
            obj = Rectangle(1, -2, 3, 4, 5)
            obj = Rectangle(1, 2, -3, 4, 5)
            obj = Rectangle(1, 2, 3, -4, 5)
            obj = Rectangle(0, 2, 3, 4, 5)
            obj = Rectangle(1, 0, 3, 4, 5)
    
    def test_rectangle_width_setter(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.width = 2
        self.assertEqual(obj.width, 2)

    def test_rectangle_width_getter(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        width = obj.width
        self.assertEqual(width, 1)

    def test_rectangle_height_setter(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.height = 3
        self.assertEqual(obj.height, 3)

    def test_rectangle_height_getter(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        height = obj.height
        self.assertEqual(height, 2)
    def test_rectangle_area(self):
        obj = Rectangle(2, 2, 3, 4, 5)
        self.assertEqual(obj.area(), 4)

    def test_area_errors(self):
        obj = Rectangle(2, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            obj.area(1)

    def test_rectangle_print(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        save_op = StringIO()
        sys.stdout = save_op

        print(obj)
        print_op = save_op.getvalue().strip()
        sys.stdout = sys.__stdout__

        self.assertEqual(print_op, "[Rectangle] (5) 3/4 - 1/2")

    def test_update_full(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.update(10, 2, 4, 6, 8)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 8)

    def test_update_some(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.update(10, 2, 4)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_update_full_kwargs(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.update(id=10, width=2, height=4, x=6, y=8)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 8)

    def test_update_kwargs_mixed(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.update(y=8, id=10, height=4, x=6, width=2)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 8)

    def test_update_kwargs_some(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.update(id=10, width=2, height=4)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_update_empty(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.update()
        self.assertEqual(obj.id, 5)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_dict(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        obj_dict = obj.to_dictionary()
        self.assertEqual(obj_dict, {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    def test_dict_error(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            obj_dict = obj.to_dictionary(1)

if __name__ == '__main__':
    unittest.main()
