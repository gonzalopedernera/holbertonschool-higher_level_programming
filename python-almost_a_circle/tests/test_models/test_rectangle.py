#!/usr/bin/python3
"""Import modules for testing"""


import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys
"""Class for rectangle testing"""


class TestRectangle(unittest.TestCase):

    def test_rectangle_width(self):
        """Test for init width"""
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.width, 1)

    def test_rectangle_height(self):
        """Test for init height"""
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.height, 2)

    def test_rectangle_x(self):
        """Test for init x"""
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.x, 3)

    def test_rectangle_x_zero(self):
        """Test for init x no value"""
        obj = Rectangle(1, 2)
        self.assertEqual(obj.x, 0)

    def test_rectangle_y(self):
        """Test for init y"""
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.y, 4)

    def test_rectangle_y_zero(self):
        """Test for init y no value"""
        obj = Rectangle(1, 2)
        self.assertEqual(obj.y, 0)

    def test_rectangle_id(self):
        """Test for init id"""
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.id, 5)

    def test_rectangle_id_none(self):
        """Test for init id no value"""
        obj = Rectangle(1, 2)
        self.assertEqual(obj.id, 3)

    def test_rectangle_typeerror(self):
        """Test for init TypeError"""
        with self.assertRaises(TypeError):
            obj = Rectangle("test", 2, 3, 4, 5)
            obj = Rectangle(1, "test", 3, 4, 5)
            obj = Rectangle(1, 2, "test", 4, 5)
            obj = Rectangle(1, 2, 3, "test", 5)

    def test_rectangle_no_args(self):
        """Test for init no args"""
        with self.assertRaises(TypeError):
            obj = Rectangle()

    def test_rectangle_many_args(self):
        """Test for init too many args"""
        with self.assertRaises(TypeError):
            obj = Rectangle(1, 2, 3, 4, 5, 6)

    def test_rectangle_valueerror(self):
        """Test for init ValueError"""
        with self.assertRaises(ValueError):
            obj = Rectangle(-1, 2, 3, 4, 5)
            obj = Rectangle(1, -2, 3, 4, 5)
            obj = Rectangle(1, 2, -3, 4, 5)
            obj = Rectangle(1, 2, 3, -4, 5)
            obj = Rectangle(0, 2, 3, 4, 5)
            obj = Rectangle(1, 0, 3, 4, 5)

    def test_rectangle_width_setter(self):
        """Test for width setter"""
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.width = 2
        self.assertEqual(obj.width, 2)

    def test_rectangle_width_setter_typeerror(self):
        """Test for width setter TypeError"""
        obj = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            obj.width = "Si"

    def test_rectangle_width_setter_valueerror(self):
        """Test for width setter ValueError"""
        obj = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(ValueError):
            obj.width = -1
            obj.width = 0

    def test_rectangle_width_getter(self):
        """Test for width getter"""
        obj = Rectangle(1, 2, 3, 4, 5)
        width = obj.width
        self.assertEqual(width, 1)

    def test_rectangle_height_setter(self):
        """Test for height setter"""
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.height = 3
        self.assertEqual(obj.height, 3)

    def test_rectangle_height_setter_typerror(self):
        """Test for height setter TypeError"""
        obj = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            obj.height = "Si"

    def test_rectangle_height_setter_valueerror(self):
        """Test for height setter ValueError"""
        obj = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(ValueError):
            obj.height = -1
            obj.height = 0

    def test_rectangle_height_getter(self):
        """Test for height getter"""
        obj = Rectangle(1, 2, 3, 4, 5)
        height = obj.height
        self.assertEqual(height, 2)

    def test_rectangle_area(self):
        """Test for area method"""
        obj = Rectangle(2, 2, 3, 4, 5)
        self.assertEqual(obj.area(), 4)

    def test_area_errors(self):
        """Test for area method errors"""
        obj = Rectangle(2, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            obj.area(1)

    def test_rectangle_display(self):
        """Test display method"""
        obj = Rectangle(3, 2, 0, 0, 5)
        save_op = StringIO()
        sys.stdout = save_op

        obj.display()
        print_op = save_op.getvalue().strip()
        sys.stdout = sys.__stdout__

        self.assertEqual(print_op, "###\n###")

    def test_rectangle_displat_position(self):
        """Test display method with x > 0 and y > 0"""
        obj = Rectangle(3, 2, 2, 2, 5)
        save_op = StringIO()
        sys.stdout = save_op

        obj.display()
        print_op = save_op.getvalue().strip()
        sys.stdout = sys.__stdout__

        self.assertEqual(print_op, "###\n  ###")

    def test_display_many_args(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            obj.display(12)

    def test_rectangle_print(self):
        """Test for __str__ method"""
        obj = Rectangle(1, 2, 3, 4, 5)
        save_op = StringIO()
        sys.stdout = save_op

        print(obj)
        print_op = save_op.getvalue().strip()
        sys.stdout = sys.__stdout__

        self.assertEqual(print_op, "[Rectangle] (5) 3/4 - 1/2")

    def test_update_full(self):
        """Test for update method"""
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.update(10, 2, 4, 6, 8)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 8)

    def test_update_some(self):
        """Test for update method with some args"""
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.update(10, 2, 4)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_update_full_kwargs(self):
        """Test for update method with kwargs"""
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.update(id=10, width=2, height=4, x=6, y=8)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 8)

    def test_update_kwargs_mixed(self):
        """Test for update method with kwargs and mixed args"""
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.update(y=8, id=10, height=4, x=6, width=2)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 8)

    def test_update_kwargs_some(self):
        """Test for update method with kwargs and some args"""
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.update(id=10, width=2, height=4)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_update_empty(self):
        """Test for update method with no args"""
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.update()
        self.assertEqual(obj.id, 5)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_dict(self):
        """Test for to_dictionary method"""
        obj = Rectangle(1, 2, 3, 4, 5)
        obj_dict = obj.to_dictionary()
        self.assertEqual(
                obj_dict,
                {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
                )

    def test_dict_error(self):
        """Test for to_dictionary method errors"""
        obj = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            obj_dict = obj.to_dictionary(1)


if __name__ == '__main__':
    unittest.main()
