"""
Example code to capture IO from
"""

import util


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

    @classmethod
    def class_method_without_decorator(cls):
        """
        Class method
        """
        print("This is a class method without decorator.")
        print("Class attribute:", cls)

    def __repr__(self):
        return util.format_repr(self.__class__.__qualname__)


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


def sum_v5(*args, **kwargs):
    """
    sum numbers

    Args:
        args: numbers to sum
    """

    running_sum = ""

    for elem in args:
        running_sum += "0" + str(elem)

    for elem in kwargs.items():
        running_sum += str(elem[0]) + str(elem[1])

    return running_sum


def do_nothing_v1():
    """
    Does nothing; there to test edge case

    Returns:
        None

    """
    return None


def do_something_v1():
    """
    Does something; there to test edge case

    Returns:
        None

    """
    return 1


def do_something_v2(addend, addend_2=100):
    """
    Does something; there to test edge case

    Returns:
        None

    """
    return addend + addend_2


def main():
    """
    The Driver Code
    """
    sum_v3({1: "one", 2: "two", 3: "three"})
    sum_v4({1, 2, 3, 4, 5, 6.6, -7.7})

    sum_v2([1.2, 2, 3.4, 5.5, 3, -1.1])
    sum_v2({1.2, 2, 3.4, 5.5, 3, -1.1})

    add(2, 5)
    add(2, 3)
    multiply(4, 5)

    # Function calls with functions as parameters
    apply_operation(add, 200, 300)
    apply_operation(multiply, 4000, 5000)

    foo_baz(2)

    obj = MyClass()
    obj.my_method(5)

    sum_v5(1, 2, 3, 4, 5, 6, key=100, keykey=200, keykeykey=300)
    do_nothing_v1()
    do_something_v1()
    do_something_v2(1)
    do_something_v2(1, -1)

    apply_operation(add, 200, 300)


if __name__ == "__main__":
    main()
