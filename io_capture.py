"""
Toy / "Hello, World!" program to capture function calls' IO while "conforming" to PEP-8.
"""

import inspect

# List to store all the recorded function calls
calls = []


def record_calls(func):
    """
    Decorator function to record inputs and outputs of a function call.

    Args:
        func: The function to be decorated.

    Returns:
        The wrapper function.
    """

    def wrapper(*args, **kwargs):
        """
        Wrapper function that records the inputs and outputs of a function call.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The output of the wrapperd function.
        """

        # Get the function arguments and their names
        args_names = inspect.getfullargspec(func).args

        # Create a dictionary to store inputs and outputs
        call_data = {
            "function": func.__name__,
            "inputs": dict(zip(args_names, args)),
            "output": None,
        }

        # Call the function and record the output
        call_data["output"] = func(*args, **kwargs)

        # Store the call data
        calls.append(call_data)

        return call_data["output"]

    return wrapper


def apply_decorator_to_all_functions():
    """
    Apply the decorator to all functions in the project.
    """
    global calls  # pylint: disable=C0103, W0603

    calls = []  # Reset the list of recorded calls

    # Get all the global variables
    global_variables = globals()

    # Iterate through all variables and apply the decorator to functions
    for key, value in global_variables.items():
        if inspect.isfunction(value):
            global_variables[key] = record_calls(value)


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


# README: Make sure to include all function definitions prior to applying decorator
# Apply the decorator to all functions in the project
apply_decorator_to_all_functions()

# Perform function calls
add(2, 3)
add(4, 5)
add(6, 7)

foo_baz(10)

# Print the recorded calls
for i, call in enumerate(calls):
    print(f"Call {i+1}:")
    print("Function:", call["function"])
    print("Inputs:", call["inputs"])
    print("Output:", call["output"])
    print()
