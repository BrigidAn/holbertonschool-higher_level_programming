#!/usr/bin/python3
"""Student class"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary representation of Student

        If attrs is a list of strings, only include those attributes.
        Otherwise, return all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {key: self.__dict__[key]
                    for key in attrs
                    if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        using values from a dictionary
        """
        for key, value in json.items():
            setattr(self, key, value)