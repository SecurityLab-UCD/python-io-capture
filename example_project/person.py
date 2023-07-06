"""
The person class
"""

import util


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
        return util.format_repr(
            self.__class__.__qualname__, name=self.name, age=self.age
        )


class Student(Person):
    def introduce(self):
        return f"{super().introduce()} , and I am a student in UC Davis."
