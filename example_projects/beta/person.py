"""
The person class
"""

from beta import example
from beta import util


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
