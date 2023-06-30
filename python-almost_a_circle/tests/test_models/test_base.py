#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestBaseClass(unittest.TestCase):

    def test_base_id_attribute(self):
        obj = Base(None)
        self.assertEqual(obj.id, 1)
        obj = Base(15)
        self.assertEqual(obj.id, 15)
        obj = Base()
        self.assertEqual(obj.id, 2)

    def test_base_json(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        obj_dict = obj.to_dictionary()
        json_dict = Base.to_json_string([obj_dict])
        self.assertEqual(json_dict, '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]')

    def test_base_json_empty(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        obj_dict = obj.to_dictionary()
        with self.assertRaises(TypeError):
            json_dict = Base.to_json_string()

    def test_base_json_none(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        obj_dict = obj.to_dictionary()
        json_dict = Base.to_json_string(None)
        self.assertEqual(json_dict, '[]')

    def test_base_json_many(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        obj_dict = obj.to_dictionary()
        with self.assertRaises(TypeError):
            json_dict = Base.to_json_string([obj_dict], 1)
    
    def test_base_json_file(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([obj])
        with open('Rectangle.json', 'r') as f:
            save_op = StringIO()
            sys.stdout = save_op

            print(f.read())
            print_op = save_op.getvalue().strip()
            sys.stdout = sys.__stdout__

        self.assertEqual(print_op, '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]')

    def test_base_json_file_none(self):
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
        obj = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file([1])
    
    def test_base_from_json(self):
        list_input = [
        {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        ]
        json_list = Rectangle.to_json_string(list_input)
        self.assertEqual(json_list, '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]')

    def test_base_from_json_none(self):
        json_list = Rectangle.to_json_string(None)
        self.assertEqual(json_list, '[]')

    def test_base_from_json_error(self):
        list_input = [
        {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        ]
        with self.assertRaises(TypeError):
            json_list = Rectangle.to_json_string(list_input, 1)
            json_list = Rectangle.to_json_string(1)
            json_list = Rectangle.to_json_string()


            
