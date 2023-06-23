#!/usr/bin/python3
"""New class student"""


class Student:

    """Intialization for a new Student object
    Args:
        first_name: first name of Student
        last_name: last name of Student
        age: age of student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """Retrieves a dictionary representation of a Student instance"""
    def to_json(self):
        return vars(self)
