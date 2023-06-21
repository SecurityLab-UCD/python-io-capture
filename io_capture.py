"""
PEP-8 Conforming program to capture calls' IO across functions/class methods/inner classes in all
    the files in the 'example_projects' DIR.
"""

import glob
import os
import importlib
import inspect

# const defining filename pattern for a prospective target file
FILE_PATTERN = "*.py"
# List to store all the recorded function calls
calls = []


def decorate_directory_modules(target_directory):
    """
    Decorate all modules defined in files in the specified DIR.

    Args:
        target_directory: path to the DIR w/ all the modules
    """

    modules = {}

    for file_path in glob.glob(os.path.join(target_directory, FILE_PATTERN)):
        module_name = os.path.splitext(os.path.basename(file_path))[0]

        modules[module_name] = decorate_module(f"{target_directory}.{module_name}")

    return modules


def decorate_module(module_path):
    """
    Decorate module w/ the given path

    Args:
        module_path: path to the module to decorate
    """

    try:
        module = importlib.import_module(module_path)

        for name, value in inspect.getmembers(
            module,
            predicate=lambda e: inspect.isfunction(e) or inspect.isclass(e),
        ):
            module.__setattr__(name, decorate_object(value))  # pylint: disable=C2801

    except ImportError as exc:
        raise ImportError("Error Importing Module") from exc

    return module


def decorate_object(obj):
    """
    Apply the decorator to the given objects.

    Args:
        objects: A list of objects to decorate.
    """

    if inspect.isfunction(obj):
        return record_calls(obj)
    if inspect.isclass(obj):
        for name, attr in inspect.getmembers(obj):
            if name in ("__repr__", "__str__"):
                continue

            # Instance vs. Class Method
            if inspect.isfunction(attr) or inspect.ismethod(attr):
                setattr(obj, name, record_calls(attr))

            elif inspect.isclass(attr) and not name.startswith("__"):
                decorate_object(attr)

    return obj


def record_calls(func):
    """
    Decorator function to record IO of a function call.

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
            The output of the wrapped function.
        """

        # Create a dictionary to store inputs and outputs
        call_data = {
            "function": func.__qualname__,
            "inputs": process_args(func, *args, **kwargs),
            "output": func(*args, **kwargs),
        }

        # Store the call data
        calls.append(call_data)

        return call_data["output"]

    return wrapper


def process_args(orig_func, *args, **kwargs):
    """
    Flattens composite args (if applicable)
    """

    processed = {}

    # Get the function arguments and their names
    args_names = inspect.getfullargspec(orig_func).args

    # Handle *args and **kwargs
    if not args_names:
        if len(args) > 1:
            processed["*args"] = args
            processed.update(kwargs)
        return processed

    processed: dict = {name: "[OPTIONAL ARG ABSENT]" for name in args_names}

    for i, arg in enumerate(args):
        if isinstance(arg, (list, set)):
            processed[args_names[i]] = list(arg)
        elif isinstance(arg, dict):
            processed[args_names[i]] = list(zip(arg.keys(), arg.values()))
        else:
            processed[args_names[i]] = arg

    return processed
