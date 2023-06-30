#!/usr/bin/python3
"""Import modules for testing"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys
"""Class for base testing"""


class TestBaseClass(unittest.TestCase):

    def test_base_id_attribute(self):
        """Test for id attribute"""
        obj = Base(None)
        self.assertEqual(obj.id, 1)
        obj = Base(15)
        self.assertEqual(obj.id, 15)
        obj = Base()
        self.assertEqual(obj.id, 2)

    def test_base_json(self):
        """Test for to_json_string method"""
        obj = Rectangle(1, 2, 3, 4, 5)
        obj_dict = obj.to_dictionary()
        json_dict = Base.to_json_string([obj_dict])
        self.assertEqual(
                json_dict,
                '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]'
                )

    def test_base_json_empty(self):
        """Test for to_json_string method with no args"""
        obj = Rectangle(1, 2, 3, 4, 5)
        obj_dict = obj.to_dictionary()
        with self.assertRaises(TypeError):
            json_dict = Base.to_json_string()

    def test_base_json_none(self):
        """Test for to_json string method with None"""
        obj = Rectangle(1, 2, 3, 4, 5)
        obj_dict = obj.to_dictionary()
        json_dict = Base.to_json_string(None)
        self.assertEqual(json_dict, '[]')

    def test_base_json_many(self):
        """Test for to_json_string method with too many arguments"""
        obj = Rectangle(1, 2, 3, 4, 5)
        obj_dict = obj.to_dictionary()
        with self.assertRaises(TypeError):
            json_dict = Base.to_json_string([obj_dict], 1)

    def test_base_json_file(self):
        """Test for save_to_file method"""
        obj = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([obj])
        with open('Rectangle.json', 'r') as f:
            save_op = StringIO()
            sys.stdout = save_op

            print(f.read())
            print_op = save_op.getvalue().strip()
            sys.stdout = sys.__stdout__

        self.assertEqual(
                print_op,
                '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]'
                )

    def test_base_json_file_none(self):
        """Test for save_to_file method with None"""
        obj = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file(None)
        with open('Rectangle.json', 'r') as f:
            save_op = StringIO()
            sys.stdout = save_op

            print(f.read())
            print_op = save_op.getvalue().strip()
            sys.stdout = sys.__stdout__

        self.assertEqual(print_op, '[]')

    def test_base_json_file_error(self):
        """Test for save_to_file method errors"""
        obj = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file([1])

    def test_base_from_json(self):
        """Test for from_json_string method"""
        list_input = [
            {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        ]
        json_list = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list)
        self.assertEqual(
                list_output,
                [{'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}]
                )

    def test_base_from_json_none(self):
        """Test for from_json_string method with None"""
        json_list = Rectangle.from_json_string(None)
        self.assertEqual(json_list, [])

    def test_base_from_json_error(self):
        """Test for from_json_string method errors"""
        list_input = [
            {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        ]
        with self.assertRaises(TypeError):
            json_list = Rectangle.to_json_string(list_input, 1)
            json_list = Rectangle.to_json_string(1)
            json_list = Rectangle.to_json_string()

    def test_base_create_rectangle(self):
        """Test for create method"""
        obj_1 = Rectangle(1, 2, 3, 4, 5)
        obj_1_dict = obj_1.to_dictionary()
        obj_2 = Rectangle.create(**obj_1_dict)
        self.assertEqual(obj_2.id, 5)
        self.assertEqual(obj_2.width, 1)
        self.assertEqual(obj_2.height, 2)
        self.assertEqual(obj_2.x, 3)
        self.assertEqual(obj_2.y, 4)

    def test_base_create_square(self):
        obj_1 = Square(2, 3, 4, 5)
        obj_1_dict = obj_1.to_dictionary()
        obj_2 = Square.create(**obj_1_dict)
        self.assertEqual(obj_2.id, 5)
        self.assertEqual(obj_2.width, 2)
        self.assertEqual(obj_2.height, 2)
        self.assertEqual(obj_2.x, 3)
        self.assertEqual(obj_2.y, 4)

    def test_base_create_error(self):
        """Test for create method errors"""
        with self.assertRaises(TypeError):
            obj = Square.create("Si")
            obj = Rectangle.create("Si")
            obj_1 = Square(2, 3, 4, 5)
            obj_1_dict = obj_1.to_dictionary()
            obj_2 = Square(4, 6, 8, 10)
            obj_2_dict = obj_2.to_dictionary()
            obj = Square.create(**obj_1_dict, **obj_2_dict)


if __name__ == '__main__':
    unittest.main()
