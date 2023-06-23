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

    """Retrieves a dictionary representation of a Student instance
    Args:
        attrs: list of attributes to return
    """
    def to_json(self, attrs=None):
        if type(attrs) == list:
            attr_list = vars(self)
            var_dict = {}
            for i in attrs:
                if i in attr_list:
                    var_dict[i] = attr_list[i]
            return var_dict

        else:
            return vars(self)
        return vars(self)

    """Replaces all attributes of the Student instance with those in json
    Args:
        json: dict with values to replace
    """
    def reload_from_json(self, json):
        var_dict = vars(self)
        for i, j in json.items():
            if i in var_dict:
                self.__dict__[i] = json[i]
