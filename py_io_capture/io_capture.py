"""
PEP-8 Conforming program to capture calls' IO across functions/class methods/inner classes in all
    the files in the 'example_projects' DIR.
"""

import inspect
import json
from typing import Any
from py_io_capture.report_table import ReportTable, IOVector, ReportTableJSONEncoder
from py_io_capture.common import (
    MAX_REPORT_SIZE,
    MAX_RECURRSION_LIMIT,
    PythonReportError,
)
import sys
import re

calls = ReportTable(max_output_len=MAX_REPORT_SIZE)
instance_tracker: dict[int, tuple(str, list)] = {}  # {id(obj): (class_name, args)}


def dump_records(file_path):
    json.dump(calls, open(file_path, "w"), indent=4, cls=ReportTableJSONEncoder)
    calls.clear()


def decorate_module(module):
    """
    Decorate a imported module

    Args:
        module: the module to be decorated
    """

    if callable(module) or inspect.isfunction(module):
        return record_calls(module)

    instrumented = set()
    for name, value in inspect.getmembers(
        module,
        predicate=lambda e: inspect.isfunction(e) or inspect.isclass(e),
    ):
        module.__setattr__(name, decorate_object(value))  # pylint: disable=C2801
        instrumented.add(name)

    # instrumented functions that are not covered by inspect.getmembers
    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        if callable(attr) and attr_name not in instrumented:
            setattr(module, attr_name, record_calls(attr))
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
            if is_property(name):
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

        try:
            if isinstance(rnt, set):
                rnt_str = set(map(str, rnt))
                for i in range(len(rnt_str)):
                    if is_class_instance(rnt_str[i]):
                        rnt_str[i] = obj2constructor(rnt_str[i])
            else:
                rnt_str = str(rnt)
                if is_class_instance(rnt_str):
                    rnt_str = obj2constructor(rnt)
        except:
            rnt_str = PythonReportError.UNABLE_TO_STRINGIFY

        # some function may not have attribute __qualname__
        # for example, numpy.random.rand
        try:
            func_name = (
                func.__qualname__ if hasattr(func, "__qualname__") else func.__name__
            )
        except AttributeError:
            func_name = str(func)

        if is_property(func_name):
            return rnt

        # store inputs and outputs
        # todo: fix process_args str() recursion error
        inputs = [str(value) for value in process_args(func, *args, **kwargs).values()]
        outputs = [rnt_str]

        # Store the class name and args for class instance initialization
        if "__init__" in func_name:
            class_name = re.match(r"(.*).__init__", func_name).group(1)
            instance_tracker[id(args[0])] = (class_name, inputs[1:])

        # Store the call data
        try:
            file_name = inspect.getfile(func)
        except TypeError:
            file_name = PythonReportError.UNKNOWN_FILE

        # check if any of the input is unexpected class instance
        # todo: find why there are unexpected class instances
        if any(
            val == PythonReportError.UNEXPECTED_CLASS_INSTANCE
            for val in inputs + outputs
        ):
            return rnt

        if "__init__" not in func_name:
            calls.report(
                f"{file_name}?{func_name}", (IOVector(inputs), IOVector(outputs))
            )

        return rnt

    return wrapper


def process_args(orig_func, *args, **kwargs):
    """
    Flattens composite args (if applicable)
    """

    processed = {}

    # Get the function arguments and their names
    # note: inspect.getfullargspec(func).args sometimes give incorrect number of args
    # i.e. len(args_names) != len(args)
    # try:
    #     args_names = inspect.getfullargspec(orig_func).args
    # except TypeError:
    args_names = ["arg" + str(i) for i in range(len(args))]

    # Handle *args and **kwargs
    if not args_names:
        if len(args) > 1:
            processed["*args"] = args
            processed.update(kwargs)
        return processed

    processed: dict = {
        name: PythonReportError.OPTIONAL_ARG_ABSENT for name in args_names
    }
    for i, arg in enumerate(args):
        record_arg = None
        if isinstance(arg, (list, set)):
            record_arg = str(list(arg))
        elif isinstance(arg, dict):
            record_arg = str(list(zip(arg.keys(), arg.values())))
        else:
            # use recursion limit to avoid infinite recursion stackoverflow
            org_recursion_limit = sys.getrecursionlimit()
            sys.setrecursionlimit(MAX_RECURRSION_LIMIT)
            try:
                record_arg = str(arg)
            except RecursionError:
                record_arg = PythonReportError.RECURSION_LIMIT_EXCEEDED
            sys.setrecursionlimit(org_recursion_limit)

        if is_class_instance(record_arg):
            record_arg = obj2constructor(arg)
        processed[args_names[i]] = record_arg

    return processed


def is_property(name):
    whitelist = ["__init__", "__setattr__"]
    return name.startswith("__") and name.endswith("__") and name not in whitelist


def is_class_instance(value: str) -> bool:
    """check if a value is a class instance in Python.
    We consider only a object <class_name object at 0xsome_address> as class instance

    Args:
        value (str): a reported value string

    Returns:
        bool: True if the value is an instance of some class, False otherwise
    """
    pattern = r"<([^}]*) object at 0x([0-9a-fA-F]{12})>"
    match = re.match(pattern, value)
    return bool(match)


def obj2constructor(obj: Any) -> str:
    if id(obj) in instance_tracker:
        class_record = instance_tracker[id(obj)]
        class_name = class_record[0]
        args = class_record[1]
        obj_str = f"{class_name}({', '.join(args)})"
    else:
        obj_str = PythonReportError.UNEXPECTED_CLASS_INSTANCE

    return obj_str
