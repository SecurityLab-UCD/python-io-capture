"""
The person class
"""

from example import example
from example import util


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


def main():
    """
    The Driver Code
    """
    # Function calls with dictionaries
    dictionary = {"name": "Alice", "age": 25}
    example.apply_operation(lambda x, y: Person(**x).introduce(), dictionary, None)

    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)
    person1.introduce()
    person2.introduce()


if __name__ == "__main__":
    main()
