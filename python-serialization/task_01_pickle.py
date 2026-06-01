#!/usr/bin/env python3
"""Module for pickling custom objects"""

import pickle


class CustomObject:
    """Custom object that can be serialized and deserialized"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object and save it to a file.
        Returns None if an error occurs.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (pickle.PickleError, OSError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load and return a CustomObject instance from a file.
        Returns None if the file does not exist or is malformed.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError, EOFError, OSError):
            return None