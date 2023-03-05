#!/usr/bin/python3
"""
Module to define class Student
"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialization
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method that returns json
        """
        return self.__dict__.copy()
