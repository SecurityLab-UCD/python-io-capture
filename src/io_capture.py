"""
PEP-8 Conforming program to capture calls' IO across functions/class methods/inner classes in all
    the files in the 'example_projects' DIR.
"""

import inspect
import json

# List to store all the recorded function calls
calls = []


def dump_records(file_path):
    json.dump(calls, open(file_path, "w"), indent=4)
    calls.clear()


def decorate_module(module):
    """
    Decorate a imported module

    Args:
        module: the module to be decorated
    """

    try:
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
        rnt = func(*args, **kwargs)

        # Create a dictionary to store inputs and outputs
        call_data = {
            "function": func.__qualname__,
            "inputs": process_args(func, *args, **kwargs),
            "output": str(rnt),
        }

        # Store the call data
        calls.append(call_data)

        return rnt

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
        record_arg = None
        # use match-case if wanted
        if isinstance(arg, (list, set)):
            record_arg = str(list(arg))
        elif isinstance(arg, dict):
            record_arg = str(list(zip(arg.keys(), arg.values())))
        else:
            record_arg = str(arg)
        processed[args_names[i]] = str(record_arg)

    return processed
