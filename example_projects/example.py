"""
Example code to capture IO from
"""


# Example function
def add(addend_1, addend_2):
    """
    Function that adds two numbers.

    Args:
        addend_1: The first number.
        addend_2: The second number.

    Returns:
        The sum of the two numbers.
    """
    return addend_1 + addend_2


# Another example function
def foo_baz(number):
    """
    A toy function to have its input and outputs captured.

    Args:
        number: The number to recurse on.

    Returns:
        None.
    """
    if number > 1:
        foo_baz(number - 1)

        # Example class


class Rectangle:
    """
    Represents a rectangle
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Return the area
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter
        """
        return 2 * (self.width + self.height)

    def __repr__(self):
        return f"[width': {self.width} 'height': {self.height}]"

    class NestedClass:
        """
        Example Nested Class
        """

        def __init__(self, data):
            self.data = data

        def process_data(self):
            """
            A toy function
            """

            return len(self.data)

        def process_data_v2(self):
            """
            A toy function
            """

            return len(self.data) + 1


class MyClass:
    """
    Example class to capture method calls.
    """

    def __init__(self):
        pass

    def my_method(self, value):
        """
        Example method to capture inputs and outputs.

        Args:
            value: A value.

        Returns:
            The value squared.
        """
        return value**2

    def my_method_v2(self, value):
        """
        Example method to capture inputs and outputs.

        Args:
            value: A value.

        Returns:
            The value squared.
        """
        return value**3

    @classmethod
    def class_method_without_decorator(cls):
        """
        Class method
        """
        print("This is a class method without decorator.")
        print("Class attribute:", cls)

    def __repr__(self):
        return "[]"


def multiply(num_1, num_2):
    """
    Multiply two numbers

    Args:
        mul_1: The first number to multiply.
        mul_2: The second number to multiply.
    """
    return num_1 * num_2


def apply_operation(operation, arg_1, arg_2):
    """
    A higher order function

    Args:
    arg_1: function argument
    arg_2: function argument
    """
    return operation(arg_1, arg_2)


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


def sum_v2(args):
    """
    sum numbers

    Args:
        args: numbers to sum
    """
    return sum(args)


def sum_v3(dict_arg):
    """
    sum numbers

    Args:
        args: numbers to sum
    """

    running_sum = 0

    for key in dict_arg.keys():
        running_sum += key

    return running_sum


def sum_v4(set_arg):
    """
    sum numbers

    Args:
        args: numbers to sum
    """

    running_sum = 0

    for elem in set_arg:
        running_sum += elem

    return running_sum
