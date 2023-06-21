"""
The person class
"""


class Person:
    """
    Represents a person
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        """
        Produce a short intro.
        """
        return f"Hi, my name is {self.name} and I am {self.age} years old."

    def __repr__(self):
        return f"[name': {self.name} 'age': {self.age}]"
